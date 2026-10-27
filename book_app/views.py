from django.shortcuts import render,redirect,get_object_or_404
from .models import Book, BookRequest
from .forms import CreateBookForm, UpdateBookForm, BookRequestForm,ChangeBookStatusForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def display_books(request):
    all_books = Book.objects.all().order_by("-id").select_related("author").prefetch_related("genre")
    query = request.GET.get("q","").title().strip()
    if query:
            all_books=all_books.filter(title__icontains=query)
    grace = Paginator(all_books,6)
    page_number = request.GET.get("franco")
    page_obj =  grace.get_page(page_number)
    if request.method == "POST":
        book_form = CreateBookForm(request.POST)
        if book_form.is_valid():
            create_book =book_form.save(commit=False)
            create_book.save()
            book_form.save_m2m() # for saving genre which is a many to many field
            return redirect("books_app:display_books")

    else:
        book_form = CreateBookForm()
    context = {
        "display_books":page_obj,
        "create_book":book_form,
        "search":query
    }
    return render(request,"book/display_books.html",context)

@login_required
def update_book(request,book_request):
    # get_book = Book.object.get(id=book_request)
    get_book = get_object_or_404(Book,id=book_request)
    if request.method == "POST":
        update_book= UpdateBookForm(request.POST,instance=get_book)
        if update_book.is_valid():
            update_book.save()
            return redirect("books_app:display_books")
    else:
        update_book = UpdateBookForm(instance=get_book)
    context = {
        "update_book":update_book
    }
    return render(request,"book/update_book.html",context)

@login_required
def delete_book(request,book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect("books_app:display_books")


def make_book_request(request):
    user = request.user
    get_related_book_request = BookRequest.objects.filter(customer=user).order_by("-id").select_related("book")
    create_request_form= BookRequestForm()
    if request.method=="POST":
        create_request_form= BookRequestForm(request.POST)
        if create_request_form.is_valid():
            request_form = create_request_form.save(commit=False)
            request_form.customer=user
            book= request_form.book
            print(f"DEBUG: Found book: {book.title}, current status: {book.status}")
            # request_form.book.status=='br'
            if book.status=="av":
                book.status='br'
                book.save(update_fields=["status","updated_at"])
            elif book.status=="br":
                create_request_form.add_error(
                    "This book is not available"
                )
            request_form.save()
            print(f"DEBUG: Book status updated to 'br' and request saved!")
            print(f"DEBUG: Found book: {book.title}, is now what? current status: {book.status}")
            return redirect("books_app:book_request")

    context = {
        "form":create_request_form,
        "book_requested":get_related_book_request
    }
    return render(request,"book_request/book_request.html",context)

    