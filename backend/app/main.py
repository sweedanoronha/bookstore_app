from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db
from sqlalchemy.exc import NoResultFound
from fastapi.middleware.cors import CORSMiddleware
from .routes import books

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

# Include the book routes
app.include_router(books.router)

# Seed data
@app.on_event("startup")
def seed_data():
    db = next(get_db())
    if db.query(models.Book).count() == 0:
        books = [models.Book(title="Book 1"), models.Book(title="Book 2"), models.Book(title="Book 3")]
        db.add_all(books)
        db.commit()


# Graceful shutdown
@app.on_event("shutdown")
def shutdown_event():
    print("Shutting down backend gracefully...")