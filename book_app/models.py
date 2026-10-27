from django.db import models
from author.models import Author
from genre_app.models import Genre
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()
class Book(models.Model):
    Choices = (
        ("av","Available"),
        ("br","Borrowed"),
    )
    title = models.CharField(max_length=200,blank=False,null=False)
    isbn = models.CharField(max_length=40,blank=False,null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name="book")
    genre = models.ManyToManyField(Genre,related_name="book_genre")
    published_date = models.DateField(null=False,blank=False)
    status = models.CharField(max_length=20,choices=Choices,default='av',blank=True,null=True)
    # for admin log audit
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


class BookRequest(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_date_request = models.DateField(blank=False,null=False)
    book_date_return = models.DateField(blank=False,null=False)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id}"