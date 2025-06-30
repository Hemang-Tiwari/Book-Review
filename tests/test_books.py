import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, SessionLocal
from app import models

client = TestClient(app)

# ✅ Setup: Run once before all tests
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    db.query(models.Review).delete()
    db.query(models.Book).delete()
    db.commit()
    db.close()

# ✅ Test: Add book
def test_add_book():
    response = client.post("/books/", json={"title": "1984", "author": "George Orwell"})
    assert response.status_code == 201
    assert response.json()["title"] == "1984"

# ✅ Test: Get books (will hit DB first time)
def test_get_books_cache_miss():
    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 1
