from fastapi import Depends, HTTPException,APIRouter
from sqlalchemy.orm import Session
from .. import models
from ..database import  get_db
from sqlalchemy.exc import NoResultFound

# Create a router instance
router = APIRouter(prefix="", tags=["books"])

# Get all books
@router.get("/books")
def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

# Get book by ID
@router.get("/books/{book_id}")
def get_book(book_id: int, db: Session = Depends(get_db)):
    try:
        return db.query(models.Book).filter(models.Book.id == book_id).one()
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Book not found")

# Create a new book
@router.post("/books")
def create_book(title: str, db: Session = Depends(get_db)):
    new_book = models.Book(title=title)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

# Update a book by ID
@router.put("/books/{book_id}")
def update_book(book_id: int, title: str, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    book.title = title
    db.commit()
    db.refresh(book)
    return book

# Delete a book by ID
@router.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "Book deleted"}
