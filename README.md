# WTM Library Management System (`library_ms`)

A modular Django-based Library Management System developed as part of the **Women Techmakers (WTM) Bambili × Gwarinpa Mentorship Program 2026**.

This project demonstrates core backend web development concepts, including environment isolation, dependency management with `uv`, modular Django app architecture, custom URL routing, RESTful APIs using Django REST Framework (DRF), OpenAPI documentation with `drf-spectacular`, search filters, and Git version control.

---

## 🛠️ Tech Stack & Environment

- **Language:** Python 3.12+
- **Framework:** Django 5.x
- **API Framework:** Django REST Framework (DRF)
- **API Documentation:** `drf-spectacular` (OpenAPI 3.0 / Swagger UI)
- **Environment & Dependency Manager:** [`uv`](https://github.com/astral-sh/uv)
- **Third-Party Packages:** `django-import-export`, `django-debug-toolbar`
- **Database:** SQLite / PostgreSQL / MySQL
- **Version Control:** Git & GitHub



---

## 🚀 Initial Development Setup & Workflow

If you are setting up the project from scratch, the following workflow was executed:

### 1. Initialize Git & `uv` Project
```bash
# Initialize git and uv project
git init
uv init

# Install Django package
uv add django

# Lock dependencies to requirement_dev.txt
uv pip freeze > requirement_dev.txt
```

### 2. Initialize Django Project
Create the root Django project in the current working directory:
```bash
django-admin startproject library_ms .
```
> **Note:** Adding `.` at the end prevents redundant nested directories (e.g., `library_ms/library_ms/`).

Run the initial development server to verify setup:
```bash
python manage.py runserver
```

---

## 🏗️ Creating and Configuring the `author` App

### 1. Generate Application
```bash
python manage.py startapp author
```

### 2. Register Application in Settings
Register the app in `library_ms/settings.py`:
```python
INSTALLED_APPS = [
    # Built-in Django apps...
    "author",
]
```

---

## 🔗 Routing & Views Setup

### 1. App-Level View (`author/views.py`)
Defined an initial HTTP view function to verify route handling:
```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def author_view(request):
    return HttpResponse(
        "<h2>This is a registered Author Application</h2> "
        "<strong>Yeay our first application in Django under development </strong>"
    )
```

### 2. App-Level URL Configuration (`author/urls.py`)
Created `author/urls.py` to keep routing modular and decoupled from the main project settings:
```python
from django.urls import path
from .views import author_view

urlpatterns = [
    path("display/", author_view),
]
```

### 3. Root URL Integration (`library_ms/urls.py`)
Included `author.urls` into the primary project router:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("author/", include("author.urls")),
]
```
> **Route Access:** `http://127.0.0.1:8000/author/display/`

---

## 📦 Version Control & GitHub Remote Setup

Track files, perform the initial commit, rename the default branch to `main`, and push to GitHub:
```bash
# Stage all project files
git add .

# Create initial commit
git commit -m "feat: initial project setup with uv, django, and author app routing"

# Set primary branch to main
git branch -M main

# Add remote repository link
git remote add origin https://github.com/YOUR_USERNAME/wtm_library.git

# Push changes and set upstream tracking
git push -u origin main
```

### 💡 Fixing Remote URL Misconfigurations
If an incorrect remote repository URL was entered during setup, reset it using:
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/wtm_library.git
```
Verify the active remote configuration:
```bash
git remote -v
```

---

## 📂 Directory Structure

```text
wtm_library/
├── .venv/                   # Virtual environment managed by uv
├── author/                  # Author application module
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py             # Custom app-level routing
│   └── views.py            # Author views
├── library_ms/              # Core Django project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          # Project settings & INSTALLED_APPS
│   ├── urls.py              # Root URL dispatcher
│   └── wsgi.py
├── .gitignore
├── manage.py
├── pyproject.toml           # uv configuration
├── requirement_dev.txt      # Frozen dependencies
└── README.md
```
----
## 📥 Cloning the Repository & Installation

Follow these steps to clone the repository, set up your virtual environment, and install dependencies using `uv`:

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/wtm_library.git
cd wtm_library
```

----

### 2. Create Virtual Environment with `uv`
```bash
# Create a standard virtual environment (.venv)
uv venv

# Activate virtual environment (Windows PowerShell)
.venv\Scripts\activate

# Activate virtual environment (Linux/macOS)
source .venv/bin/activate
```
-----
### 3. Install Dependencies
Install packages directly using `uv` and the provided requirements file:
```bash
# Install dependencies from requirement_dev.txt
uv pip install -r requirement_dev.txt
```

## ⚙️ Creating More Applications for the library management system

### 1. Modular App Structure
Created app modules to separate concerns across the domain models:
```bash

python manage.py startapp book_app
python manage.py startapp genre_app
```

### 2. Application & Template Registration (`library_ms/settings.py`)
Configured global template directory searching using `os.path.join(BASE_DIR, "templates")` and registered custom apps in `INSTALLED_APPS`:

```python
import os

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Custom Apps
    "author",
    "book_app",
    "genre_app",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

---

## 🗄️ Database Models & Admin Registration

### 1. Author Model (`author/models.py`)
```python
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    dob = models.DateField(null=True, blank=True)
    year_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.dob} {self.year_of_death if self.year_of_death else ''}"
```

### 2. Custom Admin Class (`author/admin.py`)
Customized the Django Admin dashboard display layout for `Author` records:

```python
from django.contrib import admin
from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "dob", "year_of_death"]


admin.site.register(Author, AuthorAdmin)
```

### 3. Database Migrations & Superuser
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

## 📝 Forms & Controllers (Views)

### 1. Author ModelForm (`author/forms.py`)
Used Django's `ModelForm` to generate HTML forms mapped directly to the `Author` schema:

```python
from django import forms
from .models import Author


class CreateAuthorEntry(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            "first_name",
            "last_name",
            "dob",
            "year_of_death",
        ]
```

### 2. Views Setup (`author/views.py`)
Implemented views for retrieving author lists and processing form submissions using `POST` request handling and URL redirects:

```python
from django.shortcuts import render, redirect
from .models import Author
from .forms import CreateAuthorEntry


def author_view(request):
    all_author = Author.objects.all().order_by("-id")
    return render(
        request,
        "author/display_author.html",
        {"display_all_author": all_author},
    )


def author_entry(request):
    if request.method == "POST":
        author_form = CreateAuthorEntry(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect("display_authors")
    else:
        author_form = CreateAuthorEntry()

    context = {"create_form": author_form}
    return render(request, "author/create_author.html", context)
```

---

## 🔗 URL Routing Configuration

### 1. App-Level Routing (`author/urls.py`)
```python
from django.urls import path
from .views import author_view, author_entry

urlpatterns = [
    path("display/", author_view, name="display_authors"),
    path("create-author/", author_entry, name="create_author"),
]
```

### 2. Root Project Routing (`library_ms/urls.py`)
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("author/", include("author.urls")),
]
```

---

## 🎨 Templates & Inheritance Architecture

### 1. Master Base Layout (`templates/base/base.html`)
Provides top-level navigation, document setup, and CSS table styling:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        table, th, td {
            border: 1px solid black;
            border-spacing: 0cap;
        }
    </style>
    <title>{{ title }}</title>
</head>
<body>
    <ul style="list-style: none; display: flex;">
        <li style="margin-right: 50px;"><a href="{% url 'create_author' %}">Create Author</a></li>
        <li><a href="{% url 'display_authors' %}">Display Author List</a></li>
    </ul>
    {% block content %}
      
    {% endblock %}
</body>
</html>
```

### 2. Create Author View (`templates/author/create_author.html`)
Extends `base/base.html` and renders the ModelForm with `{% csrf_token %}` protection:

```html
{% extends "base/base.html" %}

{% block content %}
   <form action="" method="post">
        {% csrf_token %}
        {{ create_form.as_p }}
        <button type="submit">Create</button>
    </form>
{% endblock %}
```

### 3. Display Authors View (`templates/author/display_author.html`)
Renders author listings dynamically with fallback conditional logic (`Still Alive` vs. `year_of_death` date):

```html
{% extends "base/base.html" %}

{% block content %}
   <h2>List of Authors</h2>
    <table>
        <tr>
            <th>S/N</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Date of birth</th>
            <th>Year of Death</th>
            <th colspan="2">Options</th>
        </tr>
        {% for author in display_all_author %}
        <tr>
            <td>{{ forloop.counter }}</td>
            <td>{{ author.first_name }}</td>
            <td>{{ author.last_name }}</td>
            <td>{{ author.dob }}</td>

            {% if author.year_of_death %}
              <td>{{ author.year_of_death }}</td>
            {% else %}
              <td>Still Alive</td>
            {% endif %}
            <td><a href="">edit</a></td>
            <td><a href="">delete</a></td>
        </tr>
        {% endfor %}
    </table>
{% endblock %}
```

---

## 📂 Project Directory Layout

```text
wtm_library/
├── .venv/                      # Virtual environment managed by uv
├── author/                     # Author Domain Module
│   ├── admin.py                # AuthorAdmin configuration
│   ├── forms.py                # CreateAuthorEntry ModelForm
│   ├── models.py               # Author database schema
│   ├── urls.py                 # App routing rules
│   └── views.py                # author_view and author_entry handlers
├── book_app/                   # Books Module
├── genre_app/                  # Genres Module
├── library_ms/                 # Core Project Configuration
│   ├── settings.py             # App registration & template DIRS setup
│   └── urls.py                 # Root URL dispatcher
├── templates/                  # Master Templates Folder
│   ├── base/
│   │   └── base.html           # Layout shell with navigation
│   └── author/
│       ├── create_author.html  # Author creation form template
│       └── display_author.html # Author list table template
├── manage.py
├── pyproject.toml              # uv setup file
└── requirement_dev.txt         # Frozen development dependencies
```


---
## 🛠️ Tech Stack & Environment

- **Third-Party Packages:** `django-import-export`
- **Database:** SQLite / PostgreSQL / MySQL
- **Frontend/Templates:** Django Template Language (DTL), HTML5, CSS

---

## 📥 Project Setup
### 1. Activate Virtual Environment with `uv`
```bash
# Create standard virtual environment (.venv)
uv venv

# Activate virtual environment (Windows PowerShell)
.venv\Scripts\activate

# Activate virtual environment (Linux/macOS)
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
uv add django-import-export # To use import and exports
# update the requirements_dev.txt
uv pip install -r requirements_dev.txt
```

---
## ⚙️ Global Configuration & Setup

### 1. Application & Template Registration (`library_ms/settings.py`)
Registered custom apps along with `import_export` in `INSTALLED_APPS`:

```python
import os

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-Party Apps
    "import_export",
    # Custom Apps
    "author",
    "book_app",
    "genre_app",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

### 2. Root URL Configuration (`library_ms/urls.py`)
Registered app routes with namespacing for multi-app routing:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("author/", include("author.urls")),
    path("books/", include("book_app.urls")),
    path("genres/", include("genre_app.urls")),
]
```

---

## 🗄️ Database Models & Admin Registration

### 1. Models Definition

#### Author Model (`author/models.py`)
```python
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    dob = models.DateField(null=True, blank=True)
    year_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        death_status = self.year_of_death if self.year_of_death else ""
        return f"{self.first_name} {self.last_name} {self.dob} {death_status}"
```

#### Genre Model (`genre_app/models.py`)
```python
from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    category = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return f"{self.title}- {self.category}"
```

### 2. Admin Integration with `django-import-export`

#### Author Admin (`author/admin.py`)
```python
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Author


class AuthorAdmin(ImportExportModelAdmin):
    list_display = ["id", "first_name", "last_name", "dob", "year_of_death"]


admin.site.register(Author, AuthorAdmin)
```

#### Genre Admin (`genre_app/admin.py`)
```python
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Genre


@admin.register(Genre)
class GenreAdmin(ImportExportModelAdmin):
    list_display = ["id", "title", "category"]
```

---

## 📝 Forms & Controllers (Views)

### 1. ModelForms Setup

#### Author Forms (`author/forms.py`)
```python
from django import forms
from .models import Author


class CreateAuthorEntry(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "dob", "year_of_death"]


class UpdateAuthorEntry(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "dob", "year_of_death"]
```

#### Genre Form (`genre_app/forms.py`)
```python
from django import forms
from .models import Genre


class CreateGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ["title", "category"]
```

### 2. Views Implementation

#### Author Views (`author/views.py` - Full CRUD)
```python
from django.shortcuts import render, redirect
from .models import Author
from .forms import CreateAuthorEntry, UpdateAuthorEntry


def author_view(request):
    all_author = Author.objects.all().order_by("-id")
    return render(
        request, "author/display_author.html", {"display_all_author": all_author}
    )


def author_entry(request):
    if request.method == "POST":
        author_form = CreateAuthorEntry(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect("display_authors")
    else:
        author_form = CreateAuthorEntry()

    context = {"create_form": author_form}
    return render(request, "author/create_author.html", context)


def update_author(request, author_pk):
    get_unique_author = Author.objects.get(id=author_pk)
    if request.method == "POST":
        update_form = UpdateAuthorEntry(
            request.POST, instance=get_unique_author
        )
        if update_form.is_valid():
            update_form.save()
            return redirect("display_authors")
    else:
        update_form = UpdateAuthorEntry(instance=get_unique_author)

    dictionary = {"update_author": update_form}
    return render(request, "author/update_author.html", dictionary)


def delete_author(request, author_id):
    get_unique_author = Author.objects.get(id=author_id)
    get_unique_author.delete()
    return redirect("display_authors")
```

#### Genre Views (`genre_app/views.py` - Single-Page Form & Listing)
```python
from django.shortcuts import render, redirect
from .models import Genre
from .forms import CreateGenreForm


def display_genre(request):
    all_genre = Genre.objects.all().order_by("-id")
    if request.method == "POST":
        create_genre_form = CreateGenreForm(request.POST)
        if create_genre_form.is_valid():
            create_genre_form.save()
            return redirect("genres:display_genre")
    else:
        create_genre_form = CreateGenreForm()

    franco = {"display_genres": all_genre, "genre_form": create_genre_form}
    return render(request, "Genre/display_genre.html", franco)


def delete_genre(request, pk):
    get_genre = Genre.objects.get(id=pk)
    get_genre.delete()
    return redirect("genres:display_genre")
```

---

## 🔗 App-Level URL Routing

### Author App URLs (`author/urls.py`)
```python
from django.urls import path
from .views import author_view, author_entry, update_author, delete_author

urlpatterns = [
    path("display/", author_view, name="display_authors"),
    path("create-author/", author_entry, name="create_author"),
    path("update-author/<str:author_pk>/", update_author, name="update_author"),
    path("delete-author/<str:author_id>/", delete_author, name="delete_author"),
]
```

### Genre App URLs (`genre_app/urls.py`)
```python
from django.urls import path
from .views import display_genre, delete_genre

app_name = "genres"
urlpatterns = [
    path("display/", display_genre, name="display_genre"),
    path("delete/<int:pk>/", delete_genre, name="delete_genre"),
]
```

---
## 🎨 Templates & Navigation Architecture

### 1. Base Shell with Global Navbar (`templates/base/base.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        table, th, td {
            border: 1px solid black;
            border-spacing: 0cap;
        }
        li {
            margin-right: 50px;
        }
    </style>
    <title>{{ title }}</title>
</head>
<body>
    <ul style="list-style: none; display: flex;">
        <li><a href="{% url 'create_author' %}">Create Author</a></li>
        <li><a href="{% url 'display_authors' %}">Display Author List</a></li>
        <li><a href="{% url 'books_app:display_books' %}">Display Book List</a></li>
        <li><a href="{% url 'genres:display_genre' %}">Display Genre List</a></li>
    </ul>
    {% block content %}
      
    {% endblock %}
</body>
</html>
```

### 2. Author List View (`templates/author/display_author.html`)
Includes age calculation using template filters (`timesince`) and dynamic action URLs:

```html
{% extends "base/base.html" %}

{% block content %}
   <h2>List of Authors</h2>
    <table>
        <tr>
            <th>S/N</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Date of birth</th>
            <th>Year of Death</th>
            <th>Age</th>
            <th colspan="2">Options</th>
        </tr>
        {% for author in display_all_author %}
        <tr>
            <td>{{ forloop.counter }}</td>
            <td>{{ author.first_name }}</td>
            <td>{{ author.last_name }}</td>
            <td>{{ author.dob }}</td>

            {% if author.year_of_death %}
              <td>{{ author.year_of_death }}</td>
            {% else %}
              <td>Still Alive</td>
            {% endif %}
            <td>{{ author.dob|timesince:author.year_of_death }}</td>
            <td><a href="{% url 'update_author' author.id %}">edit</a></td>
            <td><a href="{% url 'delete_author' author.id %}">delete</a></td>
        </tr>
        {% endfor %}
    </table>
{% endblock %}
```

### 3. Combined Genre Form & List View (`templates/Genre/display_genre.html`)
```html
{% extends "base/base.html" %}

{% block content %}
    <h2>List of Books</h2>

    <form action="" method="post">
        {% csrf_token %}
        {{ genre_form.as_p }}
        <button type="submit">Create</button>
    </form>
    <p></p>
    <table>
        <tr>
            <th>S/N</th>
            <th>Title</th>
            <th>Category</th>
            <th colspan="2">Options</th>
        </tr>
        {% for flavia in display_genres %}
        <tr>
            <td>{{ forloop.counter }}</td>
            <td>{{ flavia.title }}</td>
            <td>{{ flavia.category }}</td>
            <td><a href="">edit</a></td>
            <td><a href="{% url 'genres:delete_genre' flavia.id %}">delete</a></td>
        </tr>
        {% endfor %}
    </table>
{% endblock %}
```

---

## 📂 Project Directory Structure

```text
wtm_library/
├── .venv/                      # Virtual environment managed by uv
├── author/                     # Author Domain App
│   ├── admin.py                # AuthorAdmin with ImportExportModelAdmin
│   ├── forms.py                # CreateAuthorEntry & UpdateAuthorEntry
│   ├── models.py               # Author schema
│   ├── urls.py                 # Author CRUD routing
│   └── views.py                # author_view, author_entry, update_author, delete_author
├── book_app/                   # Book Domain App
├── genre_app/                  # Genre Domain App
│   ├── admin.py                # GenreAdmin with ImportExportModelAdmin
│   ├── forms.py                # CreateGenreForm
│   ├── models.py               # Genre schema
│   ├── urls.py                 # Genre app-level routing with namespace
│   └── views.py                # display_genre, delete_genre
├── library_ms/                 # Core Project Configuration
│   ├── settings.py             # App registrations & template configuration
│   └── urls.py                 # Root URL routing dispatcher
├── templates/                  # Global Templates Folder
│   ├── base/
│   │   └── base.html           # Master layout with navigation header
│   ├── author/
│   │   ├── create_author.html
│   │   ├── display_author.html
│   │   └── update_author.html
│   └── Genre/
│   |   └── display_genre.html  # Single-page form & list layout
|   |___book
|        └── display_book.html
├── manage.py
├── pyproject.toml              # uv setup file
└── requirement_dev.txt         # Frozen dependencies
```

# Best Practice

## 1. Create a tuple variable for entries with an exhaustive list instead of an input field  

### **Tuples for Choices & Many-to-Many Relationships**
```python
from django.db import models


class Genre(models.Model):
    # Tuple of choices for explicit select options
    CHOICES = (
        ("Fiction","Fiction"),
        ("Non-Fiction","Non-Fiction"),
        ("Science Fiction","Science Fiction"),
        ("Fantasy","Fantasy"),
        ("Mystery","Mystery"),
        ("Romance","Romance"),
        ("Horror","Horror"),
        ("Thriller","Thriller"),
        ("Biography","Biography"),
        ("History","History"),
        ("Self-Help","Self-Help"),
        ("Academic","Academic/Special"),
    )
    title = models.CharField(max_length=200,blank=False,null=False)
    category = models.CharField(max_length=200,choices=CHOICES,blank=False,null=False)

    def __str__(self):
        return f"{self.title}"
```

---

## 2. Form Validation, Normalization & Custom Widgets (`books/forms.py`), manipulative your frontend in your forms.py

```python
from django import forms
from .models import Book


class CreateBookForm(forms.ModelForm):
    published_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date", "name": "published_date"}
        )
    )

    class Meta:
        model = Book
        fields = ["title", "isbn", "author", "genre", "published_date"]

    # Field-level cleaning: Capitalize input & prevent duplicate entries
    def clean_title(self):
        cleaned_title = self.cleaned_data.get("title")
        proper_title = cleaned_title.title() if raw_title else ""

        if Book.objects.filter(title=proper_title).exists():
            raise forms.ValidationError(
                "This title already exists. Please choose a different title."
            )

        return proper_title


class UpdateBookForm(forms.ModelForm):
    published_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date", "name": "published_date"}
        )
    )

    class Meta:
        model = Book
        fields = ["title", "isbn", "author", "genre", "published_date"]
```

---

## 3. Views & Query Logic (`books/views.py`)

### **Handling M2M Relationships, CRUD, and Query Methods**
```python
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CreateBookForm, UpdateBookForm
from .models import Book


# View & Create Books (Handling commit=False & save_m2m)
def view_book(request):
    all_books = Book.objects.all().order_by("-published_date")

    if request.method == "POST":
        create_book = CreateBookForm(request.POST)
        if create_book.is_valid():
            # If custom logic is required before committing to DB:
            book_instance = create_book.save(commit=False)
            book_instance.save()  # Save parent record first
            create_book.save_m2m()  # Save Many-to-Many relations (e.g. genre)

            return redirect("books:view_book")
    else:
        create_book = CreateBookForm()

    context = {"all_books": all_books, "create_form": create_book}
    return render(request, "book/display_books.html", context)


# Update Book View
def update_book(request, update_id):
    get_book = get_object_or_404(Book, id=update_id)

    if request.method == "POST":
        update_form = UpdateBookForm(request.POST, instance=get_book)
        if update_form.is_valid():
            update_form.save()
            return redirect("books:view_book")
    else:
        update_form = UpdateBookForm(instance=get_book)

    return render(
        request, "book/update_books.html", {"update_book": update_form}
    )


# Delete Book View
def delete_book(request, delete_id):
    get_book = get_object_or_404(Book, id=delete_id)
    get_book.delete()
    return redirect("books:view_book")
```

---

## 4. Some Interactive Django Shell / CLI ORM Commands (`python manage.py shell`)

```python
from books.models import Book, Genre

# --- READ / QUERY ---
# Fetch all records
all_books = Book.objects.all()

# Order records (Ascending / Descending)
sorted_books = Book.objects.all().order_by("title")
recent_books = Book.objects.all().order_by("-published_date")

# Filter matching records
fiction_books = Book.objects.filter(genre__title="Fiction")

# Fetch single item safely
single_book = Book.objects.get(id=1)

# First or Last item safely
first_book = Book.objects.first()

# --- MANY-TO-MANY IN SHELL ---
genre_obj = Genre.objects.get(title="Sci-Fi")
single_book.genre.add(genre_obj)

# --- UPDATE & DELETE ---
single_book.title = "Updated Title"
single_book.save()

single_book.delete()
```

---

## 5. Dynamic URL Routing (`books/urls.py`)

```python
from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.view_book, name="view_book"),
    path("update/<int:update_id>/", views.update_book, name="update_books"),
    path("delete/<int:delete_id>/", views.delete_book, name="delete_books"),
]
```

---

## 6. Templates & Dynamic Tags (`templates/book/display_books.html`), jinja templating form control

### control your forms yourself instead of using the general tags

```html
{% extends "base/base.html" %}

{% block content %}
<h2>Add Books</h2>

<form method="POST">
    {% csrf_token %}
    
    <!-- Rendering Individual Form Fields, Labels, and Errors -->
    <div>
        {{ create_form.title.label_tag }}
        {{ create_form.title }}
        {{ create_form.title.errors }}
    </div>

    <p>
        {{ create_form.isbn.label_tag }}
        {{ create_form.isbn }}
        {{ create_form.isbn.errors }}
    </p>

    <div>
        {{ create_form.author.label_tag }}
        {{ create_form.author }}
        {{ create_form.author.errors }}
    </div>

    <p>
        {{ create_form.genre.label_tag }}
        {{ create_form.genre }}
        {{ create_form.genre.errors }}
    </p>

    <div>
        {{ create_form.published_date.label_tag }}
        {{ create_form.published_date }}
        {{ create_form.published_date.errors }}
    </div>
    
    <button type="submit">Submit</button>
</form>

<h2>Book List</h2>

<table> 
    <thead>
        <tr>
            <th>S/N</th>  
            <th>Title</th>  
            <th>ISBN</th>  
            <th>Author</th>  
            <th>Genre</th>  
            <th>Publication Date</th>
            <th>Age of Book</th>
            <th colspan="2">Actions</th>
        </tr>
    </thead>
    <tbody>
        {% for book in all_books %}
        <tr>
            <td>{{ forloop.counter }}</td>
            <td>{{ book.title }}</td>
            <td>{{ book.isbn }}</td>
            <td>{{ book.author }}</td>
            <td>
                <!-- Many-to-Many Loop Handling with Last Item Formatting -->
                {% for genre in book.genre.all %}
                    {{ genre.title }}{% if not forloop.last %}, {% endif %}
                {% empty %}
                    N/A
                {% endfor %}
            </td>
            <td>{{ book.published_date }}</td>
            <td>{{ book.published_date|timesince }}</td>
            <td><a href="{% url 'books:update_books' book.id %}">Edit</a></td>
            <td><a href="{% url 'books:delete_books' book.id %}">Delete</a></td>
        </tr>
        {% empty %}
        <tr>
            <td colspan="9">No books found in database.</td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}
```
## Django Mentorship Module: Pagination, Authentication & Project Configuration
## 1. Pagination Implementation
### Views (views.py)

```python

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CreateBookForm, CreateGenreForm, UpdateGenreForm
from .models import Genre


@login_required
def display_genre(request):
    all_genre = Genre.objects.all()  #.order_by("-id")
    # paginate = Paginator(object_list, number of rows of your table)
    paginate = Paginator(all_genre, 10)
    page_number = request.GET.get("page")
    page_obj = paginate.get_page(page_number)
    if request.method == "POST":
        create_genre_form = CreateGenreForm(request.POST)
        if create_genre_form.is_valid():
            create_genre_form.save()
            return redirect("genres:display_genre")

    else:
        create_genre_form = CreateGenreForm()

    franco = {
        "display_genres": page_obj,
        "genre_form": create_genre_form,
    }
    return render(request, "Genre/display_genre.html", franco)


def display_books(request):
    all_books = Book.objects.all()

    if request.method == "POST":
        book_form = CreateBookForm(request.POST)
        if book_form.is_valid():
            create_book = book_form.save(commit=False)
            create_book.save()
            book_form.save_m2m()  # for saving genre which is a many to many field
            return redirect("books_app:display_books")

    else:
        book_form = CreateBookForm()
    context = {
        "display_books": all_books,
        "create_book": book_form,
    }
    return render(request, "book/display_books.html", context)


@login_required
def author_view(request):
    # return HttpResponse("<h2>This is a registered Author Application</h2> <strong>Yeay our first application in Django under development </strong>")
    all_author = Author.objects.all().order_by("-id")
    paginate = Paginator(all_author, 10)
    page_number = request.GET.get("pages")
    page_obj = paginate.get_page(page_number)

    raghad = {"page_obj": page_obj}
    return render(
        request, "author/display_author.html", raghad
    )  # {"display_all_author":all_author}

```
## Author List Template (author/display_author.html)

```html
{% extends "base/base.html" %}

{% block content %}
<h2>List of Authors</h2>
<table>
    <tr>
        <th>S/N</th>
        <th>First Name</th>
        <th>Last Name</th>
        <th>Date of birth</th>
        <th>Year of Death</th>
        <th>Age</th>
        <th colspan="2">Options</th>
    </tr>
    {% for author in page_obj %}
    <tr>
        <td>{{page_obj.start_index|add:forloop.counter0}}</td>
        <td>{{author.first_name}}</td>
        <td>{{author.last_name}}</td>
        <td>{{author.dob}}</td>

        {% if author.year_of_death %}
        <td>{{author.year_of_death}}</td>
        {% else %}
        <td>Still Alive</td>
        {% endif %}
        <td>{{author.dob|timesince:author.year_of_death}}</td>
        <td><a href="{% url 'update_author' author.id %}">edit</a></td>
        <td><a href="{% url 'delete_author' author.id %}">delete</a></td>

    </tr>
    {% endfor %}
</table>

<div>
    {% if page_obj.has_previous %}
        <a href="?pages=1">First</a>
        <a href="?pages={{page_obj.previous_page_number}}">Previous</a>
    {% endif %}
</div>
<div>
    {% for yeukai in page_obj.paginator.page_range %}
    <a href="?pages={{yeukai}}">{{yeukai}}</a>
      
    {% endfor %}
</div>
<div>
    {% if page_obj.has_next %}
        <a href="?pages={{page_obj.paginator.num_pages}}">Last</a>
        <a href="?pages={{page_obj.next_page_number}}">Next</a>
    {% endif %}
</div>
{% endblock %}
Genre List Template (Genre/display_genre.html)
HTML
{% extends "base/base.html" %}
{% block content %}
    <h2>List of Genres</h2>

    <form action="" method="post">
        {% csrf_token %}
        {{genre_form.as_p}}
        <button type="submit">Create</button>
    </form>
    <p></p>
    <table>
        <tr>
            <th>S/N</th>
            <th>Title</th>
            <th>Category</th>
            <th colspan="2">Options</th>
        </tr>
        {% for flavia in display_genres %}
        <tr>
            <td>{{display_genres.start_index|add:forloop.counter0}}</td>
            <td>{{flavia.title}}</td>
            <td>{{flavia.category}}</td>
            <td><a href="{% url 'genres:update_genre' flavia.id %}">edit</a></td>
            <td><a href="{% url 'genres:delete_genre' flavia.id %}">delete</a></td>
            
        </tr>
        {% endfor %}
    </table>
    <div>
        {{display_genres.paginator.count}} Total records
    </div>
    <div>
        showing {{display_genres.number}} of {{display_genres.paginator.num_pages}} pages
    </div>
    <div>
        {% for page in display_genres.paginator.page_range %}
          <a href="?page={{page}}">{{page}}</a>
        {% endfor %}
    </div>
    <div>
        {% if display_genres.has_previous %}
          <a href="?page=1">first</a>
          <a href="?page={{display_genres.previous_page_number}}">Previous</a>
        {% endif %}
    </div>
    <div>
        {% if display_genres.has_next %}
          <a href="?page={{display_genres.next_page_number}}">Next</a>
          <a href="?page={{display_genres.paginator.num_pages}}">Last</a>
        {% endif %}
    </div>
{% endblock %}
```
## 2. Accounts Application & Authentication
Views (accounts/views.py)
```Python
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .forms import LoginForm, RegistrationForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home:index")

    if request.method == "POST":
        login_form = LoginForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect("home:index")
    else:
        login_form = LoginForm()

    context = {"login": login_form}
    return render(request, "auth/login.html", context)


def registration_view(request):
    if request.user.is_authenticated:
        return redirect("home:index")
    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            return redirect("accounts:login")
    else:
        registration_form = RegistrationForm()

    grace = {"register": registration_form}
    return render(request, "auth/registration.html", grace)


def logout_view(request):
    logout(request)
    return redirect("accounts:login")
```
### Forms (accounts/forms.py)
```Python
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User_Model = get_user_model()


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User_Model
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]


class LoginForm(AuthenticationForm):
    class Meta:
        model = User_Model
        fields = ["username", "password1"]
User Profile Model (accounts/models.py)
Python
from datetime import date, timedelta
from django.contrib.auth.models import User
from django.db import models
from django.utils import timesince, timezone
```

## accounts.models

```python

class UserProfile(models.Model):
    gender = (
        ("f", "Female"),
        ("m", "Male"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=6, choices=gender, blank=True, null=True
    )
    dob = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    contact = models.CharField(max_length=20, blank=True, null=True)

    def age_func(self):
        self.age = (timezone.now() - self.dob).year()

    def __str__(self):
        return f"{self.user.username}"
```
### App URLs (accounts/urls.py)
```Python
from django.urls import path
from .views import login_view, logout_view, registration_view

app_name = "accounts"
urlpatterns = [
    # path("",home_page,name="index"),
    path("register-page/", registration_view, name="registration"),
    path("login-page/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
```

## Auth Templates
### Login Template (auth/login.html)
```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h2>Login Form</h2>
    <form action="" method="POST">
        {% csrf_token %}
        {{login.as_p}}
        
        <button type="submit">Login</button>
    </form>
    <p>if you dont' have an account</p>
    <a href="{% url 'accounts:registration' %}">register</a>
</body>
</html>
```

## Registration Template (auth/registration.html)
```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h2>Login Form</h2>
    <form action="" method="POST">
        {% csrf_token %}
        {{login.as_p}}
        
        <button type="submit">Login</button>
    </form>
    <p>if you dont' have an account</p>
    <a href="{% url 'accounts:registration' %}">register</a>
</body>
</html>
```
## 3. Project Configuration & Settings
### Settings Configuration (settings.py)
```Python
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Authentication Redirects
LOGIN_REDIRECT_URL = "home:index"
LOGOUT_REDIRECT_URL = "accounts:login"
LOGIN_URL = "accounts:login"

# Static and Media Files Configuration
MEDIA_URL = "/media/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "author",  # Author application registered in the project.settings file telling django project that author application has created
    "home_app",
    "book_app",
    "genre_app",
    "accounts",
    "import_export",  # external library for import and export files
    "debug_toolbar",  # external library for debugging django application
]
```

### Project Root URLs (urls.py)
```Python
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home_app.urls")),
    path("accounts/", include("accounts.urls")),
    path("author/", include("author.urls")),
    path("book/", include("book_app.urls")),
    path("genre/", include("genre_app.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + debug_toolbar_urls()


# Part 2: Continuing the WTM Library Management System Development

This guide picks up directly from your previous setup steps and walks through implementing the **Book Request Workflow**, **Static Assets & HTML Template Integration**, **Django REST Framework (DRF)**, and **OpenAPI/Swagger Documentation**.

---

## 📖 1. Book Request Model, Form, and View Implementation

### A. Book Request Model (`book_app/models.py`)
Add the `BookRequest` model to track book loans, linking customers (users) to books with request and return dates:

```python
class BookRequest(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_date_request = models.DateField(blank=False, null=False)
    book_date_return = models.DateField(blank=False, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id}"
```

### B. Book Request Form & Validation (`book_app/forms.py`)
Create the form to handle book requests, filtering querysets for available books (`status="av"`) and adding cross-field validation for return dates:

```python
class BookRequestForm(forms.ModelForm):
    class Meta:
        model = BookRequest
        fields = ["book", "book_date_request", "book_date_return"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["book"].queryset = Book.objects.filter(status="av")

        self.fields["book"].widget.attrs.update(
            {
                "type": "text",
                "name": "author",
                "required class": "w-full px-4 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:bg-white outline-none transition-all",
            }
        )
        date = ["book_date_request", "book_date_return"]
        for i in date:
            self.fields[i].widget = forms.DateInput(
                {
                    "type": "date",
                    "class": "w-full px-4 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-xl outline-none focus:ring-2 focus:ring-indigo-500",
                }
            )

    def clean(self):
        cleaned_data = super().clean()
        request_date = cleaned_data.get("book_date_request")
        return_date = cleaned_data.get("book_date_return")
        if request_date and return_date:
            if return_date < request_date:
                raise forms.ValidationError(
                    {
                        "book_date_return": (
                            "The return date can not be earlier than the request date"
                        )
                    }
                )
        return cleaned_data
```

### C. Book Request View (`book_app/views.py`)
Implement the view to handle the request logic, update book statuses from available (`av`) to borrowed (`br`), and render the request page:

```python
@login_required
def make_book_request(request):
    user = request.user
    get_related_book_request = BookRequest.objects.filter(customer=user).order_by("-id").select_related("book")
    create_request_form = BookRequestForm()
    if request.method == "POST":
        create_request_form = BookRequestForm(request.POST)
        if create_request_form.is_valid():
            request_form = create_request_form.save(commit=False)
            request_form.customer = user
            book = request_form.book
            print(f"DEBUG: Found book: {book.title}, current status: {book.status}")
            
            if book.status == "av":
                book.status = 'br'
                book.save(update_fields=["status", "updated_at"])
            elif book.status == "br":
                create_request_form.add_error(
                    "book", "This book is not available"
                )
            request_form.save()
            print(f"DEBUG: Book status updated to 'br' and request saved!")
            return redirect("books_app:book_request")

    context = {
        "form": create_request_form,
        "book_requested": get_related_book_request
    }
    return render(request, "book_request/book_request.html", context)
```

---

## 🎨 2. Integrating HTML Templates & Static Assets

Organize your static assets (`css`, `js`, `images`) inside the project root `static/` folder structure, and integrate templates into your Django app.

```text
library_ms/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
└── templates/
    ├── book/
    └── book_request/
```

Load static files in templates using the standard template tag:
```html
{% load static %}
```

---

## 🔌 3. Adding DRF and `drf-yasg` to the Project

### A. Serializer (`book_app/serializers.py`)
Create a serializer for the `Book` model to expose it via REST endpoints:

```python
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title", "isbn", "author", "genre", "published_date"]
```

### B. Serializer View (`book_app/serializer_views.py`)
Create an API view using Django REST Framework decorators:

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from .serializers import BookSerializer
from .models import Book

@login_required
@api_view(["GET"])
def book(request):
    all_book = Book.objects.all()
    if request.method == "GET":
        book_serializer = BookSerializer(all_book, many=True)
        return Response(book_serializer.data, status=status.HTTP_200_OK)
    return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

---

## 🔗 4. URL Configuration for API & Book App

### A. App-Level URL Routing (`book_app/urls.py`)
Include your standard views and the new API endpoint:

```python
from django.urls import path
from .views import display_books, update_book, delete_book, make_book_request
from .serializer_views import book

app_name = "books_app"
urlpatterns = [
    path("display-books/", display_books, name="display_books"),
    path("update-book/<str:book_request>/", update_book, name="update_book"),
    path("delete-book/<str:book_id>/", delete_book, name="delete_book"),
    path("make-a-book-request/", make_book_request, name="book_request"),
    path("book-api/", book, name="book_api"),
]
```

### B. Root Project URL Configuration (`library_ms/urls.py`)
Configure your root URL dispatchers along with `drf-yasg` Swagger and ReDoc documentation:

```python
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Yeukai Library API",
        default_version="v1",
        description="Library OpenAPI for testing",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home_app.urls")),
    path("accounts/", include("accounts.urls")),
    path("author/", include("author.urls")),
    path("book/", include("book_app.urls")),
    path("genre/", include("genre_app.urls")),
    # Swagger and ReDoc API Documentation Endpoints
    path("swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + debug_toolbar_urls()
```

---

## 🚀 Initial Development Setup & Workflow

### 1. Initialize Git & `uv` Project
```bash
# Initialize git and uv project
git init
uv init

# Install Django & DRF packages
uv add django djangorestframework drf-spectacular django-import-export django-debug-toolbar

# Lock dependencies to requirement_dev.txt
uv pip freeze > requirement_dev.txt
```

### 2. Initialize Django Project
Create the root Django project in the current working directory:
```bash
django-admin startproject library_ms .
```

Run the initial development server:
```bash
python manage.py runserver
```

---

## 🏗️ Apps Architecture & Settings Registration

### 1. Modular Application Creation
```bash
python manage.py startapp author
python manage.py startapp book_app
python manage.py startapp genre_app
python manage.py startapp accounts
```

### 2. Settings Configuration (`library_ms/settings.py`)
```python
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # Third-Party Apps
    "rest_framework",
    "drf_spectacular",
    "import_export",
    "debug_toolbar",
    
    # Custom Applications
    "author",
    "book_app",
    "genre_app",
    "accounts",
]

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "WTM Library Management System API",
    "DESCRIPTION": "Interactive OpenAPI 3.0 Documentation for Library Operations",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Authentication Redirects
LOGIN_REDIRECT_URL = "home:index"
LOGOUT_REDIRECT_URL = "accounts:login"
LOGIN_URL = "accounts:login"

# Static and Media Files Configuration
MEDIA_URL = "/media/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

INTERNAL_IPS = [
    "127.0.0.1",
]
```

---

## 🗄️ Database Models & Reverse Relationships (`related_name`)

Configured explicit `related_name` on Foreign Keys and Many-to-Many fields to enable reverse querying from `Author` and `Genre` models back to `Book` directly without relying on default `_set` accessors.

### 1. Author Model (`author/models.py`)
```python
from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    dob = models.DateField(null=True, blank=True)
    year_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        death_status = self.year_of_death if self.year_of_death else ""
        return f"{self.first_name} {self.last_name} {self.dob} {death_status}"
```

### 2. Genre Model (`genre_app/models.py`)
```python
from django.db import models

class Genre(models.Model):
    CHOICES = (
        ("Fiction", "Fiction"),
        ("Non-Fiction", "Non-Fiction"),
        ("Science Fiction", "Science Fiction"),
        ("Fantasy", "Fantasy"),
        ("Mystery", "Mystery"),
        ("Romance", "Romance"),
        ("Horror", "Horror"),
        ("Thriller", "Thriller"),
        ("Biography", "Biography"),
        ("History", "History"),
        ("Self-Help", "Self-Help"),
        ("Academic", "Academic/Special"),
    )
    title = models.CharField(max_length=200, blank=False, null=False)
    category = models.CharField(max_length=200, choices=CHOICES, blank=False, null=False)

    def __str__(self):
        return f"{self.title} - {self.category}"
```

### 3. Book Model with `related_name` (`book_app/models.py`)
```python
from django.db import models
from author.models import Author
from genre_app.models import Genre

class Book(models.Model):
    STATUS_CHOICES = (
        ("av", "Available"),
        ("br", "Borrowed"),
    )
    title = models.CharField(max_length=200, null=False, blank=False)
    isbn = models.CharField(max_length=13, null=False, blank=False)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="books"
    )
    genre = models.ManyToManyField(Genre, related_name="books")
    published_date = models.DateField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default="av")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

* **Reverse Access Usage:**
  * `author.books.all()` fetches all books by an author.
  * `genre.books.all()` fetches all books under a genre.

---

## 🔌 Django REST Framework (DRF) & `drf-spectacular` Integration

### 1. Serializers (`book_app/serializers.py`)
```python
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "isbn", "author", "genre", "published_date", "status"]
```

### 2. Full DRF CRUD API Endpoints (`book_app/serializer_views.py`)
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Book
from .serializers import BookSerializer

@api_view(["GET", "POST"])
def book_list_create_api(request):
    """Retrieve all books or create a new book entry."""
    if request.method == "GET":
        books = Book.objects.all().order_by("-id")
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def book_detail_api(request, pk):
    """Retrieve, Update (PUT/PATCH), or Delete a specific book record by ID."""
    book = get_object_or_404(Book, pk=pk)

    if request.method == "GET":
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        book.delete()
        return Response(
            {"message": f"Book '{book.title}' deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )
```

---

## 🔍 Search Filter Implementation across Views

Implemented normalized search query extraction using `request.GET.get("q", "").title().strip()` across `Book`, `Author`, and `Genre` views:

```python
# genre_app/views.py
@login_required
def display_genre(request):
    all_genre = Genre.objects.all().order_by("-id")
    
    query = request.GET.get("q", "").title().strip()
    if query:
        all_genre = all_genre.filter(title__icontains=query)

    paginate = Paginator(all_genre, 6)
    page_number = request.GET.get("page")
    page_obj = paginate.get_page(page_number)

    if request.method == "POST":
        create_genre_form = CreateGenreForm(request.POST)
        if create_genre_form.is_valid():
            create_genre_form.save()
            return redirect("genres:display_genre")
    else:
        create_genre_form = CreateGenreForm()

    franco = {
        "display_genres": page_obj,
        "genre_form": create_genre_form,
        "search": query,
    }
    return render(request, "Genre/display_genre.html", franco)
```

---

## 🔗 URL Routing & Swagger API Endpoints

### Root URL Dispatcher (`library_ms/urls.py`)
```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("author/", include("author.urls")),
    path("book/", include("book_app.urls")),
    path("genre/", include("genre_app.urls")),
    
    # OpenAPI Schema & Documentation Views
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/docs/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + debug_toolbar_urls()
```

---

## 📂 Project Directory Structure

```text
wtm_library/
├── .venv/                      # Virtual environment managed by uv
├── accounts/                   # Auth & User Profile Domain App
├── author/                     # Author Domain App
│   ├── models.py               # Author schema
│   ├── urls.py                 # Author routing rules
│   └── views.py                # Author views with query searching
├── book_app/                   # Book Domain App
│   ├── models.py               # Book schema with related_name
│   ├── serializers.py          # BookSerializer
│   ├── serializer_views.py     # DRF CRUD endpoints (GET, POST, PUT, PATCH, DELETE)
│   ├── urls.py                 # App & API endpoints routing
│   └── views.py                # Book views & book request handlers
├── genre_app/                  # Genre Domain App
│   ├── models.py               # Genre choices schema
│   ├── urls.py                 # Genre routes with namespace
│   └── views.py                # Genre views with query searching
├── library_ms/                 # Core Project Configuration
│   ├── settings.py             # App registrations & drf-spectacular setup
│   └── urls.py                 # Root URL dispatcher & Swagger endpoints
├── templates/                  # Global Templates Folder
├── manage.py
├── pyproject.toml              # uv configuration file
└── requirement_dev.txt         # Frozen development dependencies
```