![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![CI/CD](https://img.shields.io/badge/CI/CD-Green?style=flat)
# Nexpenz API  Backend for Personal Finance App

## 🛠 Tech Stack
- **Language:** Python 3 
- **Backend Framework:** Django  
- **API Framework:** Django REST Framework  
- **API Auth:** djangorestframework-api-key  
- **Database:** MySQL, SQLite3  
- **Containerization:** Docker & Docker Compose  
- **CI/CD:** GitHub Actions  
- **OS Tested On:** Linux (Ubuntu recommended)

---

## 🔥 Overview
**Nexpenz API** is a simple, fast, and secure backend API for a personal finance tracking mobile application.  
It powers the Nexpenz Android app, enabling users to track income, expenses, and view financial summaries — without signup or ads.

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

## 🐧 OS Support

| OS      | Status |
|--------|--------|
| Linux  | ✅ Fully supported & recommended |
| macOS  | ✅ Supported |
| Windows| ⚠️ Supported (WSL recommended) |

> **Tested on Linux (Ubuntu). Linux is recommended for production.**

---

## 🔑 API Authentication
This API uses API Key authentication:  
1. Log in to Django Admin  
2. Navigate to **API Keys**  
3. Create a key  
4. Copy it once (shown only once)  

Or go to [Nexpenz API Signup](http://nexpenz.nexapytechnologies.com/api/signup) to generate a key.

---
## 📦 Example API Usage
**GET** `/api/transactions/`  
**Header:** `X-API-KEY: your_api_key_here`  

---

## 📱 Download APK
http://localhost:8000/download_nexpenz



---

## ⚙️ Local Setup (Linux / Windows)
### 1. Clone the repo
git clone https://github.com/nexapytech/Expense-Tracker-app

cd Expense-Tracker-app



### 2. Docker Setup (Recommended)
```bash
docker build -t nexpenz .

docker run -p 8000:8000 nexpenz







