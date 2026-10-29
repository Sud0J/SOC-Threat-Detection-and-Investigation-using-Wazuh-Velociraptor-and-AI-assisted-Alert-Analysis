
graph TB
    subgraph Internet["☁️ Internet (Linode Cloud)"]
        subgraph Linode["Linode VPS — <WAZUH_SERVER_IP>"]
            subgraph Docker["Docker Containers"]
                WM["🛡️ Wazuh Manager<br/>Port 1514, 1515, 55000"]
                WI["🔍 Wazuh Indexer<br/>OpenSearch — Port 9200"]
                WD["📊 Wazuh Dashboard<br/>Port 443 (HTTPS)"]
            end
            VR["🦖 Velociraptor Server<br/>GUI: 8889 | Frontend: 8000"]
        end
    end

    subgraph LocalNet["🏠 Local Network — 192.168.110.0/24 (VMware)"]
        subgraph Ubuntu["🐧 Ubuntu 24.04 VM — 192.168.110.130"]
            WA1["Wazuh Agent v4.14.4"]
            VRC1["Velociraptor Client"]
        end

        subgraph Kali["🐉 Kali Linux VM — 192.168.110.129"]
            HY["Hydra (Brute-force)"]
        end

        subgraph Win11["🪟 Windows 11 VM — 192.168.110.131"]
            WA2["Wazuh Agent v4.14.4<br/>(Disconnected)"]
        end
    end

    subgraph Dashboard["💻 Host Machine (Windows)"]
        SOC["🤖 SOC Dashboard<br/>Flask + AI (Groq/Llama 3.3)<br/>localhost:5000"]
    end

    WA1 -->|"Logs & Events<br/>Port 1514"| WM
    VRC1 -->|"Forensic Data<br/>Port 8000"| VR
    WA2 -.->|"Disconnected"| WM
    WM -->|"Store Alerts"| WI
    WI -->|"Visualize"| WD
    HY ==>|"🔴 SSH Brute-force<br/>Port 22"| Ubuntu
    SOC -->|"Pull Alerts<br/>Port 9200"| WI
    SOC -->|"Agent Info<br/>Port 55000"| WM
    WM -->|"🚫 Active Response<br/>Auto-block IP"| Ubuntu

    classDef server fill:#1e3a5f,stroke:#3b82f6,color:#e2e8f0
    classDef agent fill:#1a2e1a,stroke:#10b981,color:#e2e8f0
    classDef attacker fill:#3a1a1a,stroke:#ef4444,color:#e2e8f0
    classDef dashboard fill:#2d1a3a,stroke:#8b5cf6,color:#e2e8f0
    classDef disconnected fill:#2a2a2a,stroke:#64748b,color:#94a3b8

    class WM,WI,WD,VR server
    class Ubuntu,WA1,VRC1 agent
    class Kali,HY attacker
    class SOC dashboard
    class Win11,WA2 disconnected

