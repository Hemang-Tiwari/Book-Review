from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/books", tags=["Reviews"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{book_id}/reviews", response_model=list[schemas.ReviewOut])
def get_reviews(book_id: int, db: Session = Depends(get_db)):
    return crud.get_reviews_for_book(db, book_id)

# ✅ UPDATED FOR SWAGGER UI FORM
@router.post("/{book_id}/reviews", response_model=schemas.ReviewOut, status_code=201)
def add_review(book_id: int, review: schemas.ReviewCreate = Body(...), db: Session = Depends(get_db)):
    return crud.add_review_to_book(db, book_id, review)
