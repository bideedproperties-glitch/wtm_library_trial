#fastapi
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","library_ms.settings")
django.setup()
from fastapi import FastAPI, HTTPException,status
from .models import Book
from pydantic import BaseModel
from typing import Optional,List
from datetime import date

#intialize django so FastAPI can access Django models/ORM

#-- Pydantic Schema for Validation
class CreateBook(BaseModel):
    title: str
    isbn: str
    author: int
    genre: List[int] = []
    published_date: Optional[date] = None

app= FastAPI(title="FastAPI Sub-App",version="1.0")

@app.get("/books/")
def all_books_api():
    #you django ORM in Fast
    books_data =[]
    # all_book=list(Book.objects.values("id","title","isbn","author","genre","published_date").order_by("-id"))
    all_book= Book.objects.all().select_related("author").prefetch_related("genre").order_by("-id")
    for book in all_book:
            books_data.append({
                "id":book.id,
                "title":book.title,
                "author":book.author.id,
                "genre":[genre.id for genre in book.genre.all()],
                "published_date":book.published_date
            })
    return ({"source":"FastAPI","books":books_data})

@app.post("/create_book/",status_code=status.HTTP_201_CREATED,summary="Create a new Book")
def create_book_api(book_data: CreateBook):
    create_book = Book.objects.create(
          title=book_data.title,
          isbn=book_data.isbn,
          author=book_data.author,
          published_date=book_data.published_date
     )

     #assign genre,a M2M relationship using set() after the object is saved
    if book_data.genre:
          create_book.genre.set(book_data.genre)

    return {
         "message": "Book created successfully via FastAPI",
         "book":{
                "id":create_book.id,
                "title":create_book.title,
                "author":create_book.author_id,
                "genre":[genre.id for genre in create_book.genre.all()],
                "published_date":create_book.published_date
         }
    }

     