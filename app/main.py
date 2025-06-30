from fastapi import FastAPI
from .routers import books, reviews


app = FastAPI(
    title="Book Review API",
    description="A small service to manage books and reviews",
    version="1.0.0"
)

app.include_router(books.router)
app.include_router(reviews.router)

@app.get("/")
def root():
    return {"message": "Welcome to Book Review API"}
