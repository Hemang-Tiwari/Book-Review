from pydantic import BaseModel, Field, ConfigDict
from typing import List
from datetime import datetime

# ---------- REVIEW MODELS ----------
class ReviewBase(BaseModel):
    reviewer: str
    content: str
    rating: int = Field(..., ge=1, le=5)

class ReviewCreate(ReviewBase):
    pass

class ReviewOut(ReviewBase):
    id: int
    created_at: datetime

    # Only this is needed in Pydantic v2
    model_config = ConfigDict(from_attributes=True)

# ---------- BOOK MODELS ----------
class BookBase(BaseModel):
    title: str
    author: str

class BookCreate(BookBase):
    pass

class BookOut(BookBase):
    id: int
    reviews: List[ReviewOut] = []

    model_config = ConfigDict(from_attributes=True)
