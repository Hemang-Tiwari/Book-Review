from sqlalchemy.orm import Session, joinedload
from . import models, schemas
from .cache import set_books_cache  # 👈 Add this import
from .cache import r  # To manually delete key

def get_all_books(db: Session):
    return db.query(models.Book).options(joinedload(models.Book.reviews)).all()


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    # 🧹 Clear cache after adding book
    if r:
        r.delete("books")

    return db_book

def get_reviews_for_book(db: Session, book_id: int):
    return db.query(models.Review).filter(models.Review.book_id == book_id).all()

def add_review_to_book(db: Session, book_id: int, review: schemas.ReviewCreate):
    db_review = models.Review(book_id=book_id, **review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)

    # 🧹 Clear cache after adding review
    if r:
        r.delete("books")

    return db_review