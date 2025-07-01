# 📚 Book Review App

A full-stack Book Review web application built with **FastAPI** (backend) and **React + TypeScript + TailwindCSS** (frontend). Users can add books and submit reviews with a clean and modern UI. Backend uses Redis for caching and PostgreSQL/SQLite via SQLAlchemy for data persistence.

---

## 🔧 Features

- ➕ Add new books
- 📝 Submit reviews for existing books
- 🔍 Lazy-load reviews per book
- ⚡ Redis caching for fast response
- 🧪 Swagger/OpenAPI documentation
- 🎨 Styled with TailwindCSS for a responsive UI

---

## 📁 Project Structure

```

book\_review\_api/
├── backend/              # FastAPI backend
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── cache.py
│   └── routers/
│       ├── books.py
│       └── reviews.py
├── database.py
└── .env

book-review-frontend/     # React + TS + Tailwind frontend
├── src/
│   ├── App.tsx
│   ├── main.tsx
│   └── ...
└── public/

````

---

## 🚀 Getting Started

### 🐍 Backend Setup

1. **Create and activate virtualenv:**

```bash
cd backend
python -m venv env
source env/bin/activate  # on Windows use: env\Scripts\activate
````

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run FastAPI server:**

```bash
uvicorn main:app --reload
```

4. Visit Swagger UI at: [http://localhost:8000/docs](http://localhost:8000/docs)

> ⚙️ Optional: Configure `.env` for Redis:
>
> ```env
> USE_FAKE_REDIS=true
> ```

---

### ⚛️ Frontend Setup

1. **Navigate to frontend:**

```bash
cd book-review-frontend
```

2. **Install dependencies:**

```bash
npm install
```

3. **Run the frontend dev server:**

```bash
npm run dev
```

4. Open: [http://localhost:5173](http://localhost:5173)

---

## 🧪 API Docs (Swagger)

FastAPI auto-generates Swagger UI for easy testing:

📍 [http://localhost:8000/docs](http://localhost:8000/docs)

You can test:

* `POST /books` — Add a new book
* `GET /books` — Fetch all books
* `POST /books/{id}/reviews` — Add a review
* `GET /books/{id}/reviews` — Fetch reviews for a book

---

## 🛠 Tech Stack

* **Frontend:** React, TypeScript, TailwindCSS, Vite
* **Backend:** FastAPI, SQLAlchemy, Pydantic, Redis
* **Database:** SQLite (dev) / PostgreSQL (prod-ready)

---

## 📦 Future Improvements

* User login & auth (JWT)
* Like/Dislike reviews
* Pagination & filtering
* GraphQL Subscriptions (for live updates)

---

## 👨‍💻 Author

Hemang Tiwari — [@Hemang-Tiwari](https://github.com/Hemang-Tiwari)

---

## 📃 License

This project is open-source and available under the [MIT License](LICENSE).

````
