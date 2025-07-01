# 📚 Book Review App

A full-stack web application for managing books and their reviews — built using **FastAPI** (Python backend), **React** (frontend), **SQLite/SQLAlchemy** for data persistence, and optional **Redis** for caching.

---

## 🌐 Features

- 🧾 Add and list books
- ⭐ Submit and view reviews for each book
- 🔍 Fetch reviews dynamically via a button
- ⚡ FastAPI backend with Swagger (OpenAPI) docs
- 🎨 React frontend with styled interface
- 🧠 Optional Redis caching for books list
- 🚀 Easily extendable for GraphQL & Realtime Subscriptions

---

## 🛠 Tech Stack

| Frontend | Backend | Database | Cache    | Docs       |
|----------|---------|----------|----------|------------|
| React    | FastAPI | SQLite   | Redis    | Swagger UI |

---

## 🚀 Getting Started

### 📦 Backend Setup (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

### 💻 Frontend Setup (React)

cd frontend
npm install
npm run dev  # Or `npm start` if using Create React App
Visit the app at: http://localhost:5173

📚 API Documentation
Visit the auto-generated Swagger docs here:
http://localhost:8000/docs



🧪 Running Tests 

cd backend
pytest

🧩 Project Structure


book-review-app/
├── backend/
│   ├── app/
│   │   ├── routers/
│   │   ├── crud.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── main.py
│   └── ...
├── frontend/
│   ├── src/
│   └── App.tsx
└── README.md
