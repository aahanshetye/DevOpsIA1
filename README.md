# DevOps IA 1

## Topic: Trivy – Vulnerability Scanner

### Overview
[Trivy](https://github.com/aquasecurity/trivy) (by Aqua Security) is a simple and comprehensive security scanner for:

- **Container images**
- **File systems**
- **Git repositories**
- **Infrastructure as Code (IaC) configurations**
- **Dependencies** (e.g., npm, pip, etc.)

It helps detect:
- OS package vulnerabilities  
- Application dependencies vulnerabilities  
- IaC misconfigurations  
- Sensitive information (secrets)  

Trivy is widely used in DevSecOps pipelines because of its lightweight nature, speed, and ability to integrate with CI/CD tools.

---

### Project Structure
```
devopsia1/
├─ app/
│  ├─ server.py           # Simple Flask app
│  ├─ requirements.txt    # Flask dependency
│  └─ Dockerfile          # Image definition
├─ .github/workflows/trivy.yml  # GitHub Actions workflow
├─ reports/               # Scan results saved here
├─ 16010122275 Aahan Shetye DevOps IA 1 Report.pdf
└─ README.md
```

---

### How I Used Trivy in This Project
For this project, I used **Trivy as the alternative DevSecOps tool** for vulnerability scanning.

1. **Installed Trivy locally** (via Homebrew on macOS).  
2. Built and ran a **Flask app in Docker** (`python:3.10-slim` base image).  
3. Used Trivy to scan the **Docker image** for vulnerabilities.  
4. Scanned the **project directory** (filesystem) for insecure dependencies.  
5. Generated reports in multiple formats (SARIF, JSON, table).  
6. Integrated scans into a **GitHub Actions workflow** to automate security checks on every push.  
7. Downloaded reports as **workflow artifacts** from GitHub.

---

### Key Commands

**Build and run app locally:**
```bash
cd app
docker build -t devopsia1:local .
docker run --rm -p 8080:8080 devopsia1:local
```

**Trivy image scan:**
```bash
trivy image --severity HIGH,CRITICAL devopsia1:local
```

**Trivy filesystem scan:**
```bash
trivy fs --severity HIGH,CRITICAL .
```

**Save reports:**
```bash
mkdir -p reports
trivy image --format sarif --output reports/trivy-image.sarif devopsia1:local
trivy fs --format table --output reports/trivy-fs.txt .
```

---

### GitHub Actions Integration
- Workflow file: `.github/workflows/trivy.yml`  
- Runs on **push and pull request**.  
- Builds Docker image, runs Trivy scans, and uploads reports as artifacts.  

---

### Key Benefits
- Easy to install and run with one-line commands.  
- Detects vulnerabilities across OS and dependencies.  
- Generates reports in multiple formats for CI/CD integration.  
- Enforces security gates (`--exit-code 1` for HIGH/CRITICAL issues).  
- Fully automated with GitHub Actions.  

---

### Sample Findings
- Flask `1.0.2` → Vulnerable, upgrade to `2.2.5` or `2.3.2`.  
- setuptools `65.5.1` → Vulnerable, upgrade to `70.0.0+`.  
- No HIGH/CRITICAL OS-level vulnerabilities in `python:3.10-slim`.  

---

### Next Steps / Improvements
- Upgrade dependencies and re-run scans to demonstrate remediation.  
- Add secret scanning (`trivy fs --scanners secret`).  
- Extend to IaC scanning (Terraform, Kubernetes manifests).  

