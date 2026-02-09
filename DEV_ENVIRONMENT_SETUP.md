# 💻 Development Environment Setup

**Purpose:** Configure your local development environment for Detroit Automation Academy  
**Target Audience:** Developers, DevOps, Technical Staff  
**Last Updated:** February 9, 2026

---

## 🔐 Step 1: Configure Git with Privacy Protection

Before making any commits, configure git to use GitHub's noreply email:

```bash
# Set global user email (noreply to protect privacy)
git config --global user.email "smit4786@users.noreply.github.com"

# Set global user name
git config --global user.name "JustinSmith"

# Verify configuration
git config --global --list | grep user
```

**Output should show:**
```
user.email=smit4786@users.noreply.github.com
user.name=JustinSmith
```

---

## 📁 Step 2: Clone Repository

```bash
git clone https://github.com/smit4786/DetroitAutomationAcademy.git
cd DetroitAutomationAcademy
```

---

## 🐍 Step 3: Set Up Python Environment

### Option A: Using Python venv (Recommended)

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### Option B: Using Conda

```bash
# Create conda environment
conda create -n daa python=3.11

# Activate environment
conda activate daa

# Install dependencies
pip install -r requirements.txt
```

---

## 📦 Step 4: Verify Installation

```bash
# Check Python version
python --version

# Run tests
pytest test_examples.py -v

# Expected output: 32 passed in X.XXs
```

---

## ✅ Step 5: Enable Pre-Commit Hooks

Pre-commit hooks automatically format code and prevent common issues:

```bash
# Install pre-commit
pip install pre-commit

# Install git hooks
pre-commit install

# Test hooks (optional)
pre-commit run --all-files
```

**What happens:** Each `git commit` will automatically run:
- Black formatter (88 char line length)
- Flake8 linter
- Bandit security scan
- YAML/JSON validation
- Trailing whitespace removal
- isort import sorting

---

## 🚀 Step 6: Website Development (docs/)

Files in the `docs/` folder are automatically deployed to GitHub Pages:

```bash
# Edit website files
nano docs/BGC_EVENT_STATUS_DASHBOARD.html

# Commit changes (with correct email)
git add docs/
git commit -m "Update dashboard"

# Push (triggers automatic GitHub Pages deployment)
git push
```

**Automatic deployment:**
- GitHub Actions runs `deploy-pages.yml` workflow
- Website rebuilds in 1-2 minutes
- Changes live at: https://smit4786.github.io/DetroitAutomationAcademy/

---

## 🧪 Step 7: Running Tests

```bash
# Run all tests
pytest test_examples.py -v

# Run specific phase tests
pytest test_examples.py -k "phase1" -v

# Run with coverage report
pytest test_examples.py --cov=phase1 --cov=phase2 --cov=phase3
```

---

## 🔍 Step 8: Code Quality Checks

```bash
# Format code
black .

# Lint code
flake8 .

# Security scan
bandit -r phase1 phase2 phase3 -s B101

# Check imports
isort . --check-only
```

---

## 📝 Step 9: Making Changes

### 1. Create Feature Branch (Optional)
```bash
git checkout -b feature/dashboard-update
```

### 2. Make Changes
```bash
# Edit files
nano docs/BGC_EVENT_STATUS_DASHBOARD.html

# Run tests to verify
pytest
```

### 3. Commit Changes
```bash
# Pre-commit hooks will run automatically
git add .
git commit -m "Update: Dashboard with new metrics"
```

### 4. Push to GitHub
```bash
git push  # or git push origin feature/dashboard-update
```

### 5. GitHub Actions Deploy
GitHub Actions automatically deploys `main` branch to GitHub Pages.

---

## 🛠️ Common Workflow

```bash
# 1. Activate environment
source venv/bin/activate

# 2. Pull latest changes
git pull

# 3. Make changes
nano docs/index.html

# 4. Run tests
pytest

# 5. Format and lint
black . && flake8 .

# 6. Commit and push
git add .
git commit -m "Update documentation"
git push
```

---

## 📚 Project Structure

```
DetroitAutomationAcademy/
├── .github/
│   └── workflows/
│       └── deploy-pages.yml          ← Automated GitHub Pages deployment
├── docs/                             ← Website files (deployed to GitHub Pages)
│   ├── BGC_EVENT_STATUS_DASHBOARD.html
│   ├── INDEX.md
│   └── ...
├── phase1/                           ← Phase 1 curriculum (GPIO)
├── phase2/                           ← Phase 2 curriculum (CAD)
├── phase3/                           ← Phase 3 curriculum (Autonomous)
├── .pre-commit-config.yaml           ← Pre-commit hook configuration
├── requirements.txt                  ← Python dependencies
├── pyproject.toml                    ← Project metadata
├── test_examples.py                  ← Test suite (32 tests)
└── DEPLOYMENT_GUIDE.md               ← Website deployment guide
```

---

## 🚨 Privacy & Security Best Practices

### ✅ DO:
- Use noreply email in git config
- Commit only source code and documentation
- Use `.gitignore` for sensitive files
- Review commit history before pushing
- Use feature branches for experimental work

### ❌ DON'T:
- Commit `.env` files with API keys
- Use personal email addresses in commits
- Push credentials or access tokens
- Hardcode passwords or sensitive data
- Force push to `main` branch without review

---

## 📞 Troubleshooting

### "fatal: not a git repository"
```bash
# Ensure you're in the project directory
cd DetroitAutomationAcademy
git status
```

### "Your branch is ahead of 'origin/main'"
```bash
# Push your commits
git push
```

### "Pre-commit hooks failing"
```bash
# Fix formatting issues
black .

# Then commit again
git add .
git commit -m "Fix formatting"
```

### "Python module not found"
```bash
# Activate virtual environment
source venv/bin/activate

# Install missing packages
pip install -r requirements.txt
```

---

## 📖 Additional Resources

- [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) - Website deployment steps
- [MASTER_DOCUMENT_INDEX.md](MASTER_DOCUMENT_INDEX.md) - Documentation navigation
- [README.md](README.md) - Project overview
- [CTO_TECHNICAL_ROADMAP.md](CTO_TECHNICAL_ROADMAP.md) - Technical roadmap

---

**Setup Complete!** 🎉

You're now ready to:
- Develop curriculum and code
- Deploy website changes automatically
- Run tests and quality checks
- Contribute to the project

**Questions?** Contact the development team or refer to the troubleshooting section above.

