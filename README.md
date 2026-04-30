# 🤖 AI-Powered Transaction Analyzer

## 📌 Overview

This project is a backend system built using Django and Django REST Framework that processes financial transactions from CSV files and automatically categorizes them using an AI model.

It allows users to upload transaction data, stores it efficiently, and provides analytics like category-wise, daily, and monthly summaries.

---

## 🚀 Features

* 📤 Upload transactions via CSV file
* 🤖 Automatic categorization using AI
* ⚡ Optimized bulk database operations
* 📊 Analytics APIs:

  * Category-wise summary
  * Daily spending summary
  * Monthly spending summary
* 🧾 Logging for debugging and monitoring

---

## 🛠️ Tech Stack

* **Backend**: Django, Django REST Framework
* **Database**: PostgreSQL
* **AI/NLP**: Hugging Face Transformers
* **Data Processing**: Pandas

---

## 📂 Project Structure (Simplified)

```
fintech_ai/
│
├── config/                # Django settings & main URLs
├── transactions/          # Core app
│   ├── models.py
│   ├── serializers.py
│   ├── ai_service.py      # AI categorization logic
│   ├── urls.py
│   └── views/
│       ├── upload.py
│       └── analytics.py
│
├── manage.py
└── requirements.txt
```

---

## 🌐 API Endpoints

### 📤 Upload Transactions

**POST**

```
/api/upload/
```

Upload a CSV file containing transactions.

#### Request (Form-Data)

* `file`: CSV file

#### Sample CSV Format

```
description,amount
Uber ride,250
Swiggy food order,450
Amazon shopping,1200
```

#### Response

```json
{
  "message": "Uploaded and categorized successfully",
  "records_processed": 10
}
```

---

### 📊 Category Summary

**GET**

```
/api/analytics/category/
```

#### Response

```json
[
  {"category": "Food", "total": 950},
  {"category": "Transport", "total": 250}
]
```

---

### 📅 Daily Summary

**GET**

```
/api/analytics/daily/
```

#### Response

```json
[
  {"date": "2026-04-30", "total": 1200}
]
```

---

### 📆 Monthly Summary

**GET**

```
/api/analytics/monthly/
```

#### Response

```json
[
  {"month": "2026-04-01", "total": 5000}
]
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd fintech_ai
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

Update `config/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fintech_db',
        'USER': 'fintech_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Run server

```bash
python manage.py runserver
```

---

## 🧪 Testing

You can test APIs using:

* Browser (DRF browsable API)
* Postman

Start with:

```
http://127.0.0.1:8000/api/upload/
```

---

## 📈 Current Status

✅ CSV upload working
✅ AI categorization working
✅ Analytics APIs working
✅ Logging enabled

---

## 🚀 Future Improvements

* Asynchronous processing using Celery
* Frontend dashboard (React)
* Better AI model optimization
* Duplicate detection
* User authentication

---


