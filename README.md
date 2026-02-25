# sandboxPython

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen.svg"/>
  <img src="https://img.shields.io/badge/Updated-2026--02-blue.svg"/>
  <img src="https://img.shields.io/badge/Language-Python-yellow.svg"/>
</p>

<p align="center">
  <i>Python practice sandbox — from isolated scripts to multi-file projects.</i>
</p>

---

## 📑 Table of Contents

- [📌 About](#-about)
- [📁 Project Structure](#-project-structure)
- [✅ Prerequisites](#-prerequisites)
- [🚀 Quick Start](#-quick-start)
- [📖 Usage](#-usage)
- [🧪 Testing](#-testing)

---

## 📌 About

Training repository grouping independent exercises (isolated scripts by theme)
and complete mini-projects (linked files, tests, data).

### Naming Convention

| Pattern | Type | Description |
|---------|------|-------------|
| `<theme>_project/` | **Full project** | Linked files, tests, data — coherent mini-project |
| `<theme>/` | **Category** | Independent scripts grouped by theme |

### Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.12 |
| Tests | pytest |
| DB | SQLite |

---

## 📁 Project Structure

```
sandboxPython/
├── transaction_assure_project/   # [FULL PROJECT] Transactions, insurance, tests
│   ├── transaction.py            # Transaction management
│   ├── assure.py                 # Insurance logic
│   ├── incomes.py                # Revenue calculation
│   ├── test_transaction.py       # pytest tests
│   ├── test_assure.py
│   ├── test_incomes.py
│   └── transaction.txt / assure.db / transaction_report.json
├── debug_exercises/              # [CATEGORY] Find and fix bugs in broken scripts
│   └── ex1.py … ex8.py
├── logs_parsing/                 # [CATEGORY] Parse system logs (nginx, fail2ban, apt)
│   ├── logs.py / nginx.log
│   ├── reportNginxLog.py
│   ├── ipBanned_fail2ban.py
│   └── packagesInstalled.py
├── data_manipulation/            # [CATEGORY] List and string manipulation
│   ├── list_manipulation.py
│   └── strings.py
├── api_exercises/                # [CATEGORY] API calls and data storage
│   ├── testURL.py
│   ├── scanGitRepo.py
│   └── fromGitToSQLite.py
├── Makefile
├── requirements.txt
└── .venv/
```

---

## ✅ Prerequisites

| Requirement | Version |
|-------------|---------|
| Python | >= 3.10 |
| make | any |

---

## 🚀 Quick Start

```bash
# 1. Create venv and install dependencies
make

# 2. Run a script
make run FILE=logs_parsing/logs.py

# 3. Run tests for a project
make test FILE=transaction_assure_project/test_transaction.py
```

> The venv does **not** need to be manually activated — `make run` and `make test`
> call `.venv/bin/python` and `.venv/bin/pytest` directly.

---

## 📖 Usage

### Run a script

```bash
make run FILE=<folder>/<file.py>

# Examples
make run FILE=logs_parsing/reportNginxLog.py
make run FILE=transaction_assure_project/incomes.py
make run FILE=api_exercises/scanGitRepo.py
```

### Interactive session (venv activated)

```bash
make shell
# then run the printed command
source .venv/bin/activate
```

---

## 🧪 Testing

Tests live in `_project/` folders only (complete exercises with linked files).

```bash
make test FILE=transaction_assure_project/test_transaction.py
make test FILE=transaction_assure_project/test_assure.py
make test FILE=transaction_assure_project/test_incomes.py
```

> Category folders (`debug_exercises/`, `logs_parsing/`, etc.) run individually
> via `make run` — no global test suite for isolated scripts.

---

**Last Updated**: 2026-02-25
