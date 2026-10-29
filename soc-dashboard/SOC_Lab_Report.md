# SOC Lab: Wazuh + Velociraptor + AI-Assisted Alert Analysis

**Student Name:** [Your Name]
**Student ID:** [Your Student ID]
**Course:** [Course Name]
**Date:** April 15, 2026

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Project Objectives](#2-project-objectives)
3. [Lab Architecture & Setup](#3-lab-architecture--setup)
4. [Wazuh Server Setup](#4-wazuh-server-setup)
5. [Velociraptor Setup](#5-velociraptor-setup)
6. [Attack Simulation](#6-attack-simulation)
7. [AI-Powered Alert Analysis](#7-ai-powered-alert-analysis)
8. [Results & Findings](#8-results--findings)
9. [Challenges & Lessons Learned](#9-challenges--lessons-learned)
10. [Conclusion & Future Work](#10-conclusion--future-work)
11. [Appendix](#11-appendix)

---

## 1. Introduction

A Security Operations Center (SOC) is the centralized unit within an organization responsible for monitoring, detecting, analyzing, and responding to cybersecurity threats in real-time. SOC teams rely on a combination of technology, processes, and skilled personnel to protect organizational assets from cyberattacks, data breaches, and other security incidents.

In today's increasingly digital landscape, organizations face a growing number of sophisticated cyber threats, ranging from brute-force attacks and malware infections to unauthorized access and data exfiltration. The need for effective, real-time security monitoring has never been more critical. However, many organizations—especially small and mid-sized businesses—lack the resources to build and maintain a fully staffed SOC. This is where automated tools and AI-assisted analysis become invaluable.

This project aims to build a functional SOC lab environment using open-source and freely available tools to simulate a real-world security operations workflow. The lab integrates three core components:

- **Wazuh** — An open-source Security Information and Event Management (SIEM) platform that provides log analysis, intrusion detection, file integrity monitoring, vulnerability detection, and active response capabilities.
- **Velociraptor** — A powerful open-source digital forensics and incident response (DFIR) tool that enables endpoint visibility, artifact collection, and threat hunting across connected systems.
- **AI-Assisted Alert Analysis** — A custom-built web dashboard powered by a large language model (Llama 3.3 70B via Groq) that automatically analyzes Wazuh security alerts and provides human-readable summaries, MITRE ATT&CK mappings, and actionable recommendations.

By combining these tools, this project demonstrates a complete security monitoring pipeline: from attack detection to forensic investigation to AI-powered analysis — all within a controlled lab environment.

---

## 2. Project Objectives

The primary objectives of this project are:

1. **Deploy a SIEM solution (Wazuh)** on a cloud server to centrally collect and analyze security logs from multiple endpoints.

2. **Configure File Integrity Monitoring (FIM)** to detect unauthorized file changes on monitored systems, such as file creation, modification, and deletion.

3. **Implement Active Response** to automatically block malicious IP addresses when brute-force attacks are detected, demonstrating automated incident response capabilities.

4. **Deploy a forensics tool (Velociraptor)** to enable endpoint investigation, artifact collection, and threat hunting on compromised systems.

5. **Simulate real-world cyberattacks** using penetration testing tools (Hydra) to generate authentic security alerts and validate the detection capabilities of the lab.

6. **Build an AI-powered alert analysis dashboard** that pulls live security alerts from Wazuh and uses a large language model to provide automated threat assessment, MITRE ATT&CK technique mapping, and SOC analyst-style recommendations.

7. **Document the entire process** from infrastructure setup to attack simulation to AI analysis, demonstrating a complete SOC workflow.

---

## 3. Lab Architecture & Setup

### 3.1 Architecture Overview

The lab consists of four main components distributed across cloud and local virtual environments:

| Component | Platform | IP Address | Role |
|-----------|----------|------------|------|
| Wazuh Server (Docker) | Linode VPS (Cloud) | <WAZUH_SERVER_IP> | SIEM — log collection, alert generation, active response |
| Velociraptor Server | Linode VPS (Cloud) | <WAZUH_SERVER_IP> | Forensics — endpoint investigation and threat hunting |
| Ubuntu 24.04 VM | VMware (Local) | 192.168.110.130 | Agent/Victim — monitored endpoint with Wazuh agent + Velociraptor client |
| Kali Linux VM | VMware (Local) | 192.168.110.129 | Attacker — runs brute-force attacks using Hydra |
| Windows 11 VM | VMware (Local) | 192.168.110.131 | Registered Wazuh agent (disconnected — insufficient RAM to run simultaneously) |
| SOC Dashboard | Host Machine (Windows) | localhost:5000 | AI analysis dashboard — Flask + Groq/Llama 3.3 |

### 3.2 Network Diagram

The following diagram illustrates the complete lab architecture, showing all components, their connections, data flows, and the attack path:

> **[INSERT SCREENSHOT: Network Diagram — the Mermaid diagram rendered from mermaid.live]**

*Figure 3.1: SOC Lab Network Architecture showing Linode VPS with Wazuh and Velociraptor servers, local VMs (Ubuntu victim, Kali attacker, Windows 11 agent), and the AI-powered SOC Dashboard. The red arrow indicates the SSH brute-force attack path from Kali (192.168.110.129) to Ubuntu (192.168.110.130).*

### 3.3 Linode Cloud Server

The Wazuh server and Velociraptor server are hosted on a Linode VPS (Linode 2 GB plan) located in the SG (Singapore) region. The server runs Docker containers for the Wazuh stack.

> **[INSERT SCREENSHOT: Linode Dashboard — showing wazuh_docker server running with IP <WAZUH_SERVER_IP>]**

*Figure 3.2: Linode Cloud Manager showing the wazuh_docker server instance running with public IP <WAZUH_SERVER_IP> in the Singapore region.*

### 3.4 Docker Containers

The Wazuh stack runs as three Docker containers on the Linode server:

- **single-node_wazuh.manager_1** — Wazuh Manager (ports 1514, 1515, 55000)
- **single-node_wazuh.dashboard_1** — Wazuh Dashboard (port 443)
- **single-node_wazuh.indexer_1** — Wazuh Indexer/OpenSearch (port 9200)

> **[INSERT SCREENSHOT: docker ps output — showing all three containers running]**

*Figure 3.3: Docker containers running on the Linode server. The Wazuh Manager handles agent communication and alert processing, the Indexer stores alert data, and the Dashboard provides the web-based management interface.*

### 3.5 Virtual Machines

All local virtual machines are managed using VMware Workstation. The Ubuntu VM serves as the primary monitored endpoint (victim), the Kali VM acts as the attacker, and the Windows 11 VM is a registered but disconnected agent.

**Ubuntu 24.04 VM (Victim/Agent):**

> **[INSERT SCREENSHOT: Ubuntu VM showing ip a output with IP 192.168.110.130]**

*Figure 3.4: Ubuntu 24.04 VM network configuration showing IP address 192.168.110.130 on the ens33 interface. This machine runs both the Wazuh agent and Velociraptor client.*

**Kali Linux VM (Attacker):**

> **[INSERT SCREENSHOT: Kali VM showing ip a output with IP 192.168.110.129]**

*Figure 3.5: Kali Linux VM network configuration showing IP address 192.168.110.129 on the eth0 interface. Both VMs are on the same 192.168.110.0/24 subnet, enabling direct network communication for attack simulation.*

---

## 4. Wazuh Server Setup

### 4.1 Overview

Wazuh is an open-source security platform that provides unified XDR (Extended Detection and Response) and SIEM capabilities. It was deployed on the Linode VPS using the official `wazuh-docker` repository, which simplifies deployment through Docker Compose.

The Wazuh deployment consists of three core components:
- **Wazuh Manager** — Receives and analyzes data from agents, triggers alerts based on rulesets, and executes active responses.
- **Wazuh Indexer** — Based on OpenSearch, it stores and indexes all alerts and events for searching and analysis.
- **Wazuh Dashboard** — A web-based interface for visualizing alerts, managing agents, and configuring the platform.

### 4.2 Installation Process

The Wazuh stack was deployed using Docker Compose from the official repository:

```bash
# Clone the Wazuh Docker repository
git clone https://github.com/wazuh/wazuh-docker.git -b v4.14.4

# Navigate to the single-node deployment
cd wazuh-docker/single-node

# Generate SSL certificates
docker-compose -f generate-indexer-certs.yml run --rm generator

# Start the Wazuh stack
docker-compose up -d
```

### 4.3 Wazuh Dashboard

After deployment, the Wazuh Dashboard is accessible at `https://<WAZUH_SERVER_IP>`. The dashboard provides a comprehensive overview of the security posture, including agent status, alert severity levels, and quick access to all security modules.

> **[INSERT SCREENSHOT: Wazuh Overview page — showing Agents Summary (Active 1, Disconnected 1), Last 24 Hours Alerts (Medium severity: 37, Low severity: 1,487)]**

*Figure 4.1: Wazuh Dashboard Overview page showing the Agents Summary with 1 active and 1 disconnected agent, and the Last 24 Hours Alerts breakdown by severity level. The dashboard provides quick access to all security modules including Threat Hunting, File Integrity Monitoring, Vulnerability Detection, and MITRE ATT&CK mapping.*

### 4.4 Agent Deployment

Wazuh agents were deployed on the Ubuntu and Windows 11 virtual machines to enable centralized log collection and monitoring. Agents communicate with the Wazuh Manager over port 1514 (event data) and 1515 (agent registration).

The agent deployment process is streamlined through the Wazuh Dashboard:

1. Navigate to **Endpoints** → **Deploy new agent**
2. Select the operating system and architecture
3. Enter the Wazuh Manager IP address (<WAZUH_SERVER_IP>)
4. Copy and run the generated installation commands on the target machine

> **[INSERT SCREENSHOT: Wazuh Deploy New Agent page — showing the installation commands and requirements]**

*Figure 4.2: Wazuh agent deployment page showing the auto-generated installation commands. The process involves downloading the agent package, configuring it with the manager's IP address, and starting the agent service.*

After deployment, agents appear in the Endpoints list with their status, IP address, operating system, and version information:

> **[INSERT SCREENSHOT: Wazuh Endpoints/Agents list — showing Ubuntu_24.04.4_LTS (001, active, 192.168.110.130) and Windows_11 (002, disconnected, 192.168.110.131)]**

*Figure 4.3: Wazuh Endpoints page showing two registered agents. Agent 001 (Ubuntu_24.04.4_LTS) is active and reporting to the manager, while Agent 002 (Windows_11) is disconnected due to the VM being powered off to conserve system resources. Both agents are running Wazuh v4.14.4.*

### 4.5 File Integrity Monitoring (FIM) Configuration

File Integrity Monitoring (FIM) was configured on the Ubuntu agent to detect unauthorized file changes in the `/home` directory. FIM works by creating a baseline of file checksums and then alerting when files are created, modified, or deleted.

The `/home` directory was specifically chosen for FIM monitoring because it is one of the most security-critical locations on a Linux system. This directory contains:

- **User profile and configuration files** (e.g., `.bashrc`, `.profile`) — an attacker could modify these to establish persistence by injecting malicious commands that execute on every login.
- **SSH keys** (`~/.ssh/authorized_keys`) — a compromised system could have unauthorized SSH keys added, granting the attacker persistent backdoor access even after passwords are changed.
- **Personal documents and sensitive data** — any data exfiltration or tampering by an attacker would involve files stored under `/home`.
- **Application configuration files** (`~/.config/`) — malware or attackers may alter application settings to disable security features or redirect data.

In the context of this lab's brute-force attack scenario, monitoring `/home` is especially relevant: if the attacker successfully guesses the password and gains SSH access, FIM would immediately detect any post-compromise file modifications — such as dropping malware, adding SSH keys for persistence, or altering user configurations. This provides a critical second layer of detection beyond the initial brute-force alert.

The FIM configuration is located in the agent's `ossec.conf` file:

> **[INSERT SCREENSHOT: Ubuntu terminal — showing sudo cat /var/ossec/etc/ossec.conf | grep -A5 "syscheck" with the syscheck section showing disabled=no, frequency=60, scan_on_start=yes]**

*Figure 4.4: Wazuh agent syscheck (FIM) configuration on the Ubuntu VM. The scan frequency was set to 60 seconds (reduced from the default 12 hours) for testing purposes, and scan_on_start is enabled to perform an immediate baseline scan when the agent starts.*

Key FIM configuration parameters:
- `<disabled>no</disabled>` — FIM is enabled
- `<frequency>60</frequency>` — Scan every 60 seconds (default: 43200 seconds / 12 hours)
- `<scan_on_start>yes</scan_on_start>` — Perform a baseline scan immediately on agent start
- `<directories realtime="yes" check_all="yes">/home</directories>` — Monitor the `/home` directory in realtime with all integrity checks enabled

### 4.6 Active Response Configuration

Active Response was configured on the Wazuh Manager to automatically block attacker IP addresses when brute-force attacks are detected. When Wazuh rule 5763 (SSH brute-force) triggers, the `firewall-drop` command is executed on the agent to add an iptables DROP rule for the attacker's IP, effectively blocking all further communication for 600 seconds (10 minutes).

The Active Response configuration was added to the Wazuh Manager's `ossec.conf` inside the Docker container:

> **[INSERT SCREENSHOT: Linode console — showing the active-response configuration in ossec.conf with firewall-drop command, location=local, rules_id=5763, timeout=600]**

*Figure 4.5: Wazuh Manager Active Response configuration. When rule 5763 (SSH brute-force attack) is triggered, the firewall-drop command is executed locally on the agent to block the attacker's IP address using iptables for 600 seconds. This demonstrates automated incident response — the system can defend itself without human intervention.*

The Active Response workflow:
1. Attacker launches SSH brute-force attack against the Ubuntu agent
2. Wazuh agent forwards authentication failure logs to the Wazuh Manager
3. Wazuh Manager correlates events and triggers rule 5763 (brute-force detected)
4. Active Response executes `firewall-drop` on the Ubuntu agent
5. The attacker's IP is added to the iptables DROP chain, blocking all traffic
6. After 600 seconds, the IP is automatically unblocked

---

## 5. Velociraptor Setup

### 5.1 Overview

Velociraptor is an open-source digital forensics and incident response (DFIR) tool designed for endpoint visibility and threat hunting. Unlike Wazuh, which provides real-time alerting and passive monitoring, Velociraptor is used for active investigation — allowing SOC analysts to remotely query endpoints, collect forensic artifacts, and hunt for indicators of compromise (IOCs) after a security incident has been detected.

In this lab, Velociraptor serves as the investigation layer: when Wazuh alerts the SOC team to a potential threat (e.g., brute-force attack), the analyst can use Velociraptor to dig deeper into the affected endpoint — checking login history, running processes, network connections, file system changes, and more.

### 5.2 Server Installation

The Velociraptor server binary was downloaded and configured on the Linode VPS:

```bash
# Download the Velociraptor binary
wget https://github.com/Velocidex/velociraptor/releases/download/v0.72/velociraptor-v0.72.0-linux-amd64 -O velociraptor
chmod +x velociraptor

# Run the interactive configuration wizard
./velociraptor config generate -i
```

During the configuration wizard, the following settings were specified:
- **OS:** Linux
- **Datastore directory:** /opt/velociraptor
- **SSL:** Self-Signed
- **Public IP:** <WAZUH_SERVER_IP>
- **Frontend port:** 8000 (client communication)
- **GUI port:** 8889 (web interface)
- **Admin username:** admin

The configuration generated two files:
- `server.config.yaml` — Server configuration (stays on the Linode)
- `client.config.yaml` — Client configuration (deployed to endpoints)

**Important Note:** By default, the Velociraptor GUI binds to `127.0.0.1` (localhost only). To make it accessible remotely, the `bind_address` in the GUI section of `server.config.yaml` was changed to `0.0.0.0`:

```yaml
GUI:
  bind_address: 0.0.0.0
  bind_port: 8889
```

The server was then started in the background:

```bash
nohup ./velociraptor --config server.config.yaml frontend -v > velo.log 2>&1 &
```

### 5.3 Accessing the Velociraptor GUI

After starting the server, the Velociraptor web interface is accessible at `https://<WAZUH_SERVER_IP>:8889`. Since a self-signed SSL certificate is used, the browser displays a certificate warning which can be safely bypassed for this lab environment.

**To take this screenshot:**
1. Open your browser and go to `https://<WAZUH_SERVER_IP>:8889`
2. Click through the certificate warning
3. Log in with the admin credentials you set during configuration
4. You will see the Welcome page with common tasks listed

> **[INSERT SCREENSHOT: Velociraptor Welcome page — showing "Welcome to Velociraptor!" with the dinosaur logo and common tasks list]**

*Figure 5.1: Velociraptor GUI Welcome page after successful login. The interface provides quick access to common tasks including inspecting server state, building offline collectors, writing VQL notebooks, and viewing server configuration.*

### 5.4 Client Deployment on Ubuntu VM

To connect the Ubuntu VM to the Velociraptor server, the client configuration file was transferred and the client binary was installed:

```bash
# On the Ubuntu VM — copy the client config from the Linode server
scp root@<WAZUH_SERVER_IP>:~/client.config.yaml ~/client.config.yaml

# Download the Velociraptor binary
wget https://github.com/Velocidex/velociraptor/releases/download/v0.72/velociraptor-v0.72.0-linux-amd64 -O velociraptor
chmod +x velociraptor

# Start the client in the background
nohup sudo ./velociraptor --config client.config.yaml client -v > velo-client.log 2>&1 &
```

### 5.5 Viewing the Client List

Once the client connects, it appears in the Velociraptor GUI. To view the client list:

1. In the Velociraptor GUI, click the **Search clients** bar at the top left
2. Type `*` (asterisk) or leave it blank and press **Enter**
3. The search results will display all connected clients with their Client ID, Hostname, FQDN, OS Version, and online status (green dot = online)

**Take this screenshot now:**
1. Go to `https://<WAZUH_SERVER_IP>:8889`
2. Click the search bar → type `*` → press Enter
3. You should see your Ubuntu client listed with a green dot

> **[INSERT SCREENSHOT: Velociraptor Client List — showing the Ubuntu client (hostname: sudo, OS: ubuntu24.04) with Client ID and green online status]**

*Figure 5.2: Velociraptor client search results showing one connected client. The Ubuntu VM (hostname: sudo) is online with Client ID C.9a25f3d3816b8d18 running Ubuntu 24.04. The green status indicator confirms active communication between the client and server.*

### 5.6 Collecting Forensic Artifacts

Velociraptor's primary strength is its ability to remotely collect forensic artifacts from endpoints. To demonstrate this capability, several artifact collections were performed on the Ubuntu client.

**To collect an artifact (take screenshots of each step):**

1. **Click on the Ubuntu client** in the client list (click the Client ID link)
2. You will see the client overview page with system information
3. Click the **Collected Artifacts** tab at the top
4. Click the **+ (New Collection)** button
5. In the search box, type `Linux.Sys.LastUserLogin` and select it
6. Click **Launch** to start the collection
7. Wait for the collection to complete (the State column will show a checkmark)
8. Click the **Results** tab to view the collected data

> **[INSERT SCREENSHOT: Velociraptor — New Collection dialog showing Linux.Sys.LastUserLogin selected]**

*Figure 5.3: Creating a new artifact collection in Velociraptor. The Linux.Sys.LastUserLogin artifact retrieves login history from the endpoint, which is particularly useful for investigating the SSH brute-force attack detected by Wazuh. This demonstrates how Velociraptor complements Wazuh — Wazuh alerts on the attack, and Velociraptor investigates the details.*

**Additional artifacts to collect and screenshot for your report:**

| Artifact Name | What It Collects | Why It's Useful |
|---------------|-----------------|-----------------|
| `Linux.Sys.LastUserLogin` | Login history (successful and failed) | Shows brute-force attack evidence |
| `Linux.Sys.Pslist` | Running processes | Identifies suspicious processes |
| `Linux.Network.Netstat` | Active network connections | Shows attacker connections |
| `Linux.Sys.Crontab` | Scheduled tasks | Checks for persistence mechanisms |

**To collect Linux.Sys.Pslist (running processes):**
1. On the client page, click **Collected Artifacts** → **+ New Collection**
2. Search for `Linux.Sys.Pslist` and select it
3. Click **Launch**
4. After completion, click the **Results** tab
5. Screenshot the results showing all running processes

> **[INSERT SCREENSHOT: Velociraptor — Linux.Sys.Pslist results showing running processes on the Ubuntu VM]**

*Figure 5.4: Velociraptor artifact collection results for Linux.Sys.Pslist, showing all running processes on the Ubuntu VM. This information helps SOC analysts identify any suspicious or unauthorized processes that may have been spawned as a result of the detected brute-force attack.*

---

*[Report continues in Sections 6-11: Attack Simulation, AI-Powered Alert Analysis, Results & Findings, Challenges & Lessons Learned, Conclusion & Future Work, and Appendix]*
