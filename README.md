# Chá de Bebê (Django)

Simple Django app for a baby shower (chá de bebê) page where guests can:

- View a list of available gift suggestions
- Select one or more items
- Submit name + phone
- Store the submission in the database and show a confirmation page

## Tech

- Python + Django 5.2
- SQLite (default)
- `django-phonenumber-field` + `phonenumbers`

## Project layout

- `cha-bebe/manage.py` — Django entrypoint
- `cha-bebe/cha_bebe/` — project settings/urls
- `cha-bebe/app/` — main app (models, views, templates, static)

## Setup (Windows / PowerShell)

From the repository root:

```powershell
cd .\cha-bebe\
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r .\requirements.txt
python .\manage.py migrate
python .\manage.py runserver
```

Open:

- App: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

To create an admin user:

```powershell
python .\manage.py createsuperuser
```

## How it works (high-level)

- `GET /` renders `app/templates/index.html` with active items from the database.
- `POST /` creates a `Usuario` with `nome`, `telefone`, and selected item IDs (`pedidos`), then renders `confirmado.html`.

## Notes

- Default database is SQLite at `cha-bebe/db.sqlite3`.
- The UI text is in Portuguese (`pt-BR`).
