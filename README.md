# Notes App (Django CRUD Example)

A minimal Django notes app that demonstrates a simple Create, Read, Update, Delete (CRUD) flow.

This project is a beginner-friendly example and includes a single `notes` app that provides a basic notes listing, a form to create or edit notes, and a confirmation page to delete notes.

---

## Project Overview 

- Framework: Django 5.x (created by `django-admin startproject`) — settings show Django 5.2.8.
- App: `notes` (contains models, views, URLs and templates).
- Database: SQLite (default `db.sqlite3` provided).
- Purpose: Demonstrate CRUD operations for a `Note` model with fields `title`, `content`, and `created_at`.

---

## Features 

- List all notes
- Create new notes
- Update existing notes
- Delete notes (with confirmation page)
- Basic templates using Django template language

---

## Project Structure (important files) 

- `manage.py` - Django's command-line utility.
- `db.sqlite3` - SQLite database file.
- `crudproject/` - Project configuration and settings.
  - `settings.py`
  - `urls.py` - project-level URLs include `notes.urls`.
- `notes/` - Django app for notes functionality.
  - `models.py` - Note model (title, content, created_at).
  - `views.py` - CRUD views: `note_list`, `note_create`, `note_update`, `note_delete`.
  - `urls.py` - URL patterns for notes app (list, create, update, delete).
  - `templates/notes/` - templates: `note_list.html`, `note_form.html`, `note_delete.html`.
  - `migrations/` - migration files. There is at least `0001_initial.py`.

---

## Prerequisites 

- Python 3.11+ (or compatible with Django 5.2.x)
- pip (Python package manager)
- Optional: Git if cloning the repository

---

## Quick Setup (Windows PowerShell) 

Open PowerShell, then run the commands below from the project root (the folder containing `manage.py`).

1) Create and activate a virtual environment:

```powershell
python -m venv .venv
# On Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# If you hit execution policy errors, run (temporary scope):
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process; .\.venv\Scripts\Activate.ps1
```

2) Install Django (The project uses Django 5.2.8 in settings, but you can install another 5.x release compatible with your environment):

```powershell
pip install Django==5.2.8
```

> Tip: If you want a `requirements.txt`, you can run `pip freeze > requirements.txt` after installing packages.

3) Apply migrations (creates the SQLite database if not present) and create a superuser (optional):

```powershell
python manage.py migrate
python manage.py createsuperuser
```

4) Run the development server:

```powershell
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to view the notes list.

To use the admin: http://127.0.0.1:8000/admin/ (use the superuser you created).

---

## URL Endpoints & Usage 

- `/` — Note list (index page showing all notes)
  - Links to create a new note and edit or delete existing notes.
- `/create/` — Create a new note (GET shows form; POST saves the note).
- `/update/<id>/` — Update an existing note (GET shows form; POST saves changes).
- `/delete/<id>/` — Delete a note with a confirmation page (POST deletes it).

Form fields for notes:
- `title` (text input)
- `content` (textarea)

---
