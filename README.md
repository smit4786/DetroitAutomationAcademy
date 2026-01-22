# Detroit Automation Academy: Lab Environment

**Status:** Beta
**Context:** Virtual Lab Infrastructure

## Overview
This repository contains the infrastructure-as-code (IaC) configurations for the Detroit Automation Academy's "Virtual Lab". It provides a standardized development environment for students to practice Python scripting, database management, and CI/CD pipelines without needing complex local installations.

## Features
*   **Docker Compose:** A unified container stack including:
    *   **Python 3.9+**: Pre-installed with course libraries (`pandas`, `requests`, `pytest`).
    *   **PostgreSQL**: For database automation modules.
    *   **Jenkins**: For CI/CD pipeline simulations.
*   **Vagrant:** A full Virtual Machine configuration for students using legacy hardware or incompatible OS versions.
*   **Automation Scripts:** One-click setup scripts for Windows (PowerShell) and macOS/Linux (Bash).

## Prerequisites

### Recommended (Docker)
*   Docker Desktop or OrbStack (macOS)
*   Git

### Legacy Support (Vagrant)
*   VirtualBox
*   Vagrant

## Getting Started

### Option A: Docker (Recommended)

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/smit4786/daa-lab-environment.git
    cd daa-lab-environment
    ```

2.  **Run the setup script:**
    *   **macOS/Linux:**
        ```bash
        ./scripts/setup.sh
        ```
    *   **Windows (PowerShell):**
        ```powershell
        .\scripts\setup.ps1
        ```

3.  **Start the environment:**
    ```bash
    docker-compose up -d
    ```

4.  **Access Services:**
    *   **Jupyter Lab:** `http://localhost:8888`
    *   **Jenkins:** `http://localhost:8080`
    *   **Postgres:** `localhost:5432`

### Option B: Vagrant (Legacy)

Use this option if your computer does not support Docker or virtualization is restricted.

1.  **Initialize the VM:**
    ```bash
    vagrant up
    ```

2.  **SSH into the machine:**
    ```bash
    vagrant ssh
    ```

## Troubleshooting
*   **Windows Volume Mounting:** If you see errors regarding file sharing on Windows, ensure you are running your terminal as Administrator or have enabled file sharing in Docker Desktop settings.
*   **Port Conflicts:** If port 8080 is in use, modify the `docker-compose.yml` to map Jenkins to a different port (e.g., `8081:8080`).

## Contributing
Please submit issues for any environment bugs found during the Beta phase. Pull requests for additional tool configurations are welcome.