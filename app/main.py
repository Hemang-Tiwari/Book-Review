from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import books, reviews


app = FastAPI(
    title="Book Review API",
    description="A small service to manage books and reviews",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(books.router)
app.include_router(reviews.router)

@app.get("/")
def root():
    return {"message": "Welcome to Book Review API"}
