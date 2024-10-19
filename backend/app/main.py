from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db
from sqlalchemy.exc import NoResultFound
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Configure CORS
origins = [
    "http://localhost:1234",  # React frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Seed data
@app.on_event("startup")
def seed_data():
    db = next(get_db())
    if db.query(models.Book).count() == 0:
        books = [models.Book(title="Book 1"), models.Book(title="Book 2"), models.Book(title="Book 3")]
        db.add_all(books)
        db.commit()

# Get all books
@app.get("/books")
def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

# Get book by ID
@app.get("/books/{book_id}")
def get_book(book_id: int, db: Session = Depends(get_db)):
    try:
        return db.query(models.Book).filter(models.Book.id == book_id).one()
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Book not found")

# Create a new book
@app.post("/books")
def create_book(title: str, db: Session = Depends(get_db)):
    new_book = models.Book(title=title)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

# Update a book by ID
@app.put("/books/{book_id}")
def update_book(book_id: int, title: str, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    book.title = title
    db.commit()
    db.refresh(book)
    return book

# Delete a book by ID
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "Book deleted"}
