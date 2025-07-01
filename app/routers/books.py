from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import SessionLocal
from ..cache import get_books_cache, set_books_cache
from fastapi.encoders import jsonable_encoder

router = APIRouter(prefix="/books", tags=["Books"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.BookOut])
def list_books(db: Session = Depends(get_db)):
    cached_books = get_books_cache()
    if cached_books:
        return cached_books

    books = crud.get_all_books(db)
    books_data = jsonable_encoder(books)
    set_books_cache(books_data)
    return books_data

# ✅ UPDATED FOR SWAGGER UI FORM
@router.post("/", response_model=schemas.BookOut, status_code=201)
def add_book(book: schemas.BookCreate = Body(...), db: Session = Depends(get_db)):
    return crud.create_book(db, book)
