import os
import json
import urllib3

import requests
from groq import Groq
from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv

load_dotenv()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

WAZUH_URL = os.getenv("WAZUH_URL", "https://139.162.62.154")
WAZUH_API_PORT = os.getenv("WAZUH_API_PORT", "55000")
WAZUH_API_USER = os.getenv("WAZUH_USER", "wazuh-wui")
WAZUH_API_PASS = os.getenv("WAZUH_PASS", "wazuh-wui")
INDEXER_URL = os.getenv("INDEXER_URL", "https://139.162.62.154")
INDEXER_PORT = os.getenv("INDEXER_PORT", "9200")
INDEXER_USER = os.getenv("INDEXER_USER", "admin")
INDEXER_PASS = os.getenv("INDEXER_PASS", "SecretPassword")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

WAZUH_API_BASE = f"{WAZUH_URL}:{WAZUH_API_PORT}"
INDEXER_BASE = f"{INDEXER_URL}:{INDEXER_PORT}"


def get_wazuh_token():
    """Authenticate with Wazuh API and return JWT token."""
    try:
        resp = requests.post(
            f"{WAZUH_API_BASE}/security/user/authenticate",
            auth=(WAZUH_API_USER, WAZUH_API_PASS),
            verify=False,
            timeout=10,
        )
        resp.raise_for_status()
        return resp.json()["data"]["token"]
    except Exception as e:
        print(f"Wazuh auth error: {e}")
        return None


def wazuh_api_get(endpoint, params=None):
    """Make authenticated GET request to Wazuh API."""
    token = get_wazuh_token()
    if not token:
        return None
    try:
        resp = requests.get(
            f"{WAZUH_API_BASE}{endpoint}",
            headers={"Authorization": f"Bearer {token}"},
            params=params,
            verify=False,
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"Wazuh API error: {e}")
        return None


def indexer_search(query_body, index="wazuh-alerts-*", size=30):
    """Query the Wazuh Indexer (OpenSearch) for security alerts."""
    try:
        resp = requests.post(
            f"{INDEXER_BASE}/{index}/_search",
            auth=(INDEXER_USER, INDEXER_PASS),
            json={"size": size, **query_body},
            verify=False,
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"Indexer error: {e}")
        return None


def ai_generate(prompt, max_tokens=1024):
    """Generate response using Groq (free, fast LLM inference)."""
    client = Groq(api_key=GROQ_API_KEY)
    chat = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        temperature=0.3,
    )
    return chat.choices[0].message.content


def trim_for_ai(data, max_items=10):
    """Trim data to keep token usage low."""
    if isinstance(data, list):
        return data[:max_items]
    if isinstance(data, dict):
        trimmed = {}
        for key, val in data.items():
            if isinstance(val, list):
                trimmed[key] = val[:max_items]
            else:
                trimmed[key] = val
        return trimmed
    return data


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/alerts")
def get_alerts():
    """Fetch real security alerts from the Wazuh Indexer."""
    limit = request.args.get("limit", 30, type=int)
    level_min = request.args.get("level_min", 3, type=int)

    query = {
        "query": {
            "bool": {
                "must": [
                    {"range": {"rule.level": {"gte": level_min}}},
                    {"range": {"timestamp": {"gte": "now-24h"}}}
                ]
            }
        },
        "sort": [{"timestamp": {"order": "desc"}}],
    }

    result = indexer_search(query, size=limit)

    if result and "hits" in result:
        hits = result["hits"]["hits"]
        alerts = []
        for hit in hits:
            src = hit.get("_source", {})
            alerts.append({
                "timestamp": src.get("timestamp", ""),
                "rule": src.get("rule", {}),
                "agent": src.get("agent", {}),
                "data": src.get("data", {}),
                "location": src.get("location", ""),
                "full_log": src.get("full_log", ""),
            })
        return jsonify({
            "data": {
                "affected_items": alerts,
                "total_affected_items": result["hits"]["total"]["value"],
            }
        })

    # Fallback to manager logs if indexer unavailable
    data = wazuh_api_get("/manager/logs", params={
        "limit": limit,
        "sort": "-timestamp",
    })
    if not data:
        return jsonify({"error": "Could not connect to Wazuh"}), 502
    return jsonify(data)


@app.route("/api/alerts/brute-force")
def get_brute_force_alerts():
    """Fetch specifically brute-force and auth failure alerts."""
    query = {
        "query": {
            "bool": {
                "should": [
                    {"match": {"rule.description": "brute force"}},
                    {"match": {"rule.description": "authentication failed"}},
                    {"match": {"rule.description": "Multiple failed logins"}},
                    {"terms": {"rule.id": ["5763", "5551", "5710", "5503", "5712"]}},
                ],
                "minimum_should_match": 1,
            }
        },
        "sort": [{"timestamp": {"order": "desc"}}],
    }

    result = indexer_search(query, size=20)

    if result and "hits" in result:
        hits = result["hits"]["hits"]
        alerts = [hit.get("_source", {}) for hit in hits]
        return jsonify({
            "data": {
                "affected_items": alerts,
                "total": result["hits"]["total"]["value"],
            }
        })

    return jsonify({"data": {"affected_items": [], "total": 0}})


@app.route("/api/agents")
def get_agents():
    """Fetch agent list from Wazuh API."""
    data = wazuh_api_get("/agents", params={"limit": 50, "sort": "-lastKeepAlive"})
    if not data:
        return jsonify({"error": "Could not connect to Wazuh API"}), 502
    return jsonify(data)


@app.route("/api/agent-summary")
def get_agent_summary():
    """Fetch agent status summary."""
    data = wazuh_api_get("/agents/summary/status")
    if not data:
        return jsonify({"error": "Could not connect to Wazuh API"}), 502
    return jsonify(data)


@app.route("/api/fim")
def get_fim_events():
    """Fetch FIM (syscheck) events from the indexer."""
    query = {
        "query": {
            "bool": {
                "must": [
                    {"term": {"rule.groups": "syscheck"}},
                    {"range": {"timestamp": {"gte": "now-24h"}}},
                ]
            }
        },
        "sort": [{"timestamp": {"order": "desc"}}],
    }

    result = indexer_search(query, size=20)

    if result and "hits" in result:
        hits = result["hits"]["hits"]
        items = []
        for hit in hits:
            src = hit.get("_source", {})
            syscheck = src.get("syscheck", {})
            items.append({
                "file": syscheck.get("path", src.get("data", {}).get("path", "—")),
                "event": syscheck.get("event", "modified"),
                "date": src.get("timestamp", ""),
                "agent": src.get("agent", {}),
            })
        return jsonify({
            "data": {
                "affected_items": items,
                "total_affected_items": result["hits"]["total"]["value"],
            }
        })

    # Fallback to Wazuh API syscheck
    agent_id = request.args.get("agent_id", "001")
    data = wazuh_api_get(f"/syscheck/{agent_id}", params={
        "limit": 20,
        "sort": "-date",
    })
    if not data:
        return jsonify({"error": "Could not fetch FIM data"}), 502
    return jsonify(data)


@app.route("/api/analyze", methods=["POST"])
def analyze_alerts():
    """Send alerts to AI for analysis — pulls fresh data from indexer."""
    if not GROQ_API_KEY:
        return jsonify({"error": "Groq API key not configured. Set GROQ_API_KEY in .env"}), 400

    # Pull security alerts directly from indexer for analysis
    sec_query = {
        "query": {
            "bool": {
                "must": [
                    {"range": {"rule.level": {"gte": 5}}},
                    {"range": {"timestamp": {"gte": "now-7d"}}},
                ]
            }
        },
        "sort": [{"rule.level": {"order": "desc"}}],
    }
    sec_result = indexer_search(sec_query, size=15)

    # Pull FIM alerts
    fim_query = {
        "query": {
            "bool": {
                "must": [
                    {"term": {"rule.groups": "syscheck"}},
                    {"range": {"timestamp": {"gte": "now-7d"}}},
                ]
            }
        },
        "sort": [{"timestamp": {"order": "desc"}}],
    }
    fim_result = indexer_search(fim_query, size=10)

    alerts = []
    if sec_result and "hits" in sec_result:
        for hit in sec_result["hits"]["hits"]:
            src = hit.get("_source", {})
            alerts.append({
                "timestamp": src.get("timestamp"),
                "rule_id": src.get("rule", {}).get("id"),
                "rule_level": src.get("rule", {}).get("level"),
                "description": src.get("rule", {}).get("description"),
                "groups": src.get("rule", {}).get("groups", []),
                "agent": src.get("agent", {}).get("name"),
                "src_ip": src.get("data", {}).get("srcip", ""),
                "dst_user": src.get("data", {}).get("dstuser", ""),
                "location": src.get("location", ""),
                "full_log": src.get("full_log", "")[:200],
            })

    fim_alerts = []
    if fim_result and "hits" in fim_result:
        for hit in fim_result["hits"]["hits"]:
            src = hit.get("_source", {})
            sc = src.get("syscheck", {})
            fim_alerts.append({
                "timestamp": src.get("timestamp"),
                "path": sc.get("path", ""),
                "event": sc.get("event", ""),
                "agent": src.get("agent", {}).get("name"),
            })

    if not alerts and not fim_alerts:
        # Last resort: use whatever the frontend sent
        body = request.get_json()
        alerts = trim_for_ai(body.get("alerts", []), max_items=10)

    combined = {
        "security_alerts": alerts,
        "file_integrity_events": fim_alerts[:10],
    }
    alerts_text = json.dumps(combined, indent=2, default=str)

    prompt = f"""You are a SOC (Security Operations Center) analyst. Analyze these Wazuh security alerts and provide:

1. **Executive Summary** — A brief overview of the security posture
2. **Critical Findings** — Any high-priority threats or incidents detected
3. **Attack Analysis** — For each type of attack detected:
   - What happened
   - Source/target information
   - MITRE ATT&CK technique (if applicable)
   - Severity assessment
4. **File Integrity** — Any suspicious file changes detected
5. **Recommendations** — Actionable next steps for the SOC team

Format your response in clean markdown. Be specific about IPs, timestamps, and rule IDs.

Here are the alerts:
{alerts_text}"""

    try:
        analysis = ai_generate(prompt)
        return jsonify({"analysis": analysis})
    except Exception as e:
        return jsonify({"error": f"AI analysis error: {str(e)}"}), 500


@app.route("/api/analyze-custom", methods=["POST"])
def analyze_custom():
    """Send a custom question about alerts to AI."""
    if not GROQ_API_KEY:
        return jsonify({"error": "Groq API key not configured"}), 400

    body = request.get_json()
    question = body.get("question", "")
    context = body.get("context", "")

    if not question:
        return jsonify({"error": "No question provided"}), 400

    try:
        context_parsed = json.loads(context) if context else {}
        context = json.dumps(trim_for_ai(context_parsed, max_items=10), indent=2, default=str)
    except (json.JSONDecodeError, TypeError):
        context = context[:3000]

    prompt = f"""You are a SOC analyst assistant. Answer the following question based on the security alert data provided.

Question: {question}

Alert Data:
{context}

Provide a clear, actionable response in markdown format."""

    try:
        response = ai_generate(prompt, max_tokens=1024)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": f"AI analysis error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
