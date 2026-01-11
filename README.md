# Nexpenz API 💰📊

**Nexpenz API** is a simple, fast, and secure backend API for a personal finance
tracking mobile application.  
It powers the Nexpenz Android app, enabling users to track income, expenses,
and view financial summaries — without signup or ads.

---

## 🚀 Features

- ✅ Add income & expenses instantly
- 📈 Monthly summaries & category-based analytics
- 🧾 Full transaction history
- 🌍 Multi-currency support
- 🔐 API key authentication (no login/signup)
- 🧡 100% free — no ads, no tracking
- 🐳 Docker-ready
- 🧪 CI-tested on Linux

---

## 🛠️ Tech Stack

- **Python 3.11**
- **Django**
- **Django REST Framework**
- **djangorestframework-api-key**
- **SQLite / PostgreSQL**
- **Docker & Docker Compose**
- **GitHub Actions (CI)**

---

## 🐧 OS Support

| OS      | Status |
|--------|--------|
| Linux  | ✅ Fully supported & recommended |
| macOS  | ✅ Supported |
| Windows| ⚠️ Supported (WSL recommended) |

> **Tested on Linux (Ubuntu). Linux is recommended for production.**

---

### API Authentication

This API uses API Key authentication.
- Create API Key
- Log in to Django Admin
- Navigate to API Keys
- Create a key
-Copy it once (shown only once)

or goto nexpenz.nexapytechnologies.com/api/signup  to generate a key

## ⚙️ Local Setup (Linux / Windows)

Follow these steps to run the project locally:




api will be accessible at
http://locahost:8000


##  Example code
GET /api/transactions/
X-API-KEY: your_api_key_here


## 1. DOWNLOAD APK FILE
http://locahost:8000/downoad_nexpenz

### 1. Clone the repo

```bash
git clone https://github.com/nexapytech/Expense-Tracker-app
cd Expense-Tracker-app

### Docker Setup (Recommended)
docker build -t nexpenz .
docker run -p 8000:8000 nexpenz



