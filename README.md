# DevOps IA 1

## Topic: Trivy – Vulnerability Scanner

### Overview

[Trivy](https://github.com/aquasecurity/trivy) (by Aqua Security) is a simple and comprehensive security scanner for:

* **Container images**
* **File systems**
* **Git repositories**
* **Infrastructure as Code (IaC) configurations**
* **Dependencies** (e.g., npm, pip, etc.)

It helps detect:

* OS package vulnerabilities
* Application dependencies vulnerabilities
* IaC misconfigurations
* Sensitive information (secrets)

Trivy is widely used in DevSecOps pipelines because of its lightweight nature, speed, and ability to integrate with CI/CD tools.

---

### How I Used Trivy in This Project

For this project, I used **Trivy as the alternative tool** for vulnerability scanning.

* Installed Trivy locally.
* Scanned a **Docker image** to detect vulnerabilities in both OS packages and application dependencies.
* Ran a scan on a **project directory** to check for insecure dependencies and misconfigurations.
* Generated detailed scan results that highlighted vulnerabilities (with severity levels like *LOW, MEDIUM, HIGH, CRITICAL*).

This demonstrated how Trivy can be integrated into the DevOps workflow to ensure security checks are automated and efficient.

---

### Key Benefits

* Easy installation and usage with a single command (`trivy image <image_name>`).
* Detects vulnerabilities across different layers (OS + dependencies).
* Supports scanning of IaC files and secrets in code.
* Can be integrated into **CI/CD pipelines** for continuous security.

---