# Command Reference

This guide contains the useful commands for installing, running, maintaining, testing, and preparing the portfolio. Run commands from the project root, the folder containing `manage.py`.

**Documentation navigation:** [Project overview](README.md) · [Command reference](command.md) · [Beginner guide](detail.md) · [Complete reference](complete_detail.md)

## Command Categories

- [Environment setup](#environment-setup)
- [Run the project](#run-the-project)
- [Database and migrations](#database-and-migrations)
- [Portfolio content](#portfolio-content)
- [Email delivery](#email-delivery)
- [Validation and testing](#validation-and-testing)
- [Static files](#static-files)
- [Admin and shell](#admin-and-shell)
- [Useful maintenance commands](#useful-maintenance-commands)
- [Commands used during this project](#commands-used-during-this-project)
- [Deployment commands](#deployment-commands)

## Environment Setup

### Create a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
```

Linux or macOS:

```bash
python3 -m venv venv
```

Creates an isolated Python environment in `venv/`, keeping project packages separate from the system Python installation.

### Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Linux or macOS:

```bash
source venv/bin/activate
```

Activates the project environment. Your terminal normally shows `(venv)` when activation succeeds.

### Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Upgrades pip and installs the versions listed in `requirements.txt`.

### Check installed packages

```powershell
python -m pip check
python -m pip list
```

`pip check` reports broken dependency requirements. `pip list` shows installed packages and versions.

## Run the Project

### Start the development server

```powershell
python manage.py runserver
```

Starts Django's development server at `http://127.0.0.1:8000/`.

### Use another port

```powershell
python manage.py runserver 8080
```

Starts the development server at port `8080` when port `8000` is already in use.

### Start on the local network

```powershell
python manage.py runserver 0.0.0.0:8000
```

Makes the development server listen on all network interfaces. This is useful for testing from another device, but it is not a production server.

## Database and Migrations

### Apply migrations

```powershell
python manage.py migrate
```

Creates or updates database tables for Django and the `portfolio` app.

### Create migrations after model changes

```powershell
python manage.py makemigrations
```

Generates migration files from changes in [portfolio/models.py](portfolio/models.py).

### Preview migration changes

```powershell
python manage.py makemigrations --check --dry-run
```

Checks whether model changes need new migration files without creating or modifying files.

### View migration status

```powershell
python manage.py showmigrations
```

Shows which migrations are applied and which are pending.

### Preview pending operations

```powershell
python manage.py migrate --plan
```

Displays the migration operations Django would run.

## Portfolio Content

### Seed starter content

```powershell
python manage.py seed_portfolio
```

Creates or updates the starter skills and projects defined in [seed_portfolio.py](portfolio/management/commands/seed_portfolio.py). It is safe to run repeatedly because records are updated by stable names and slugs.

### Create an administrator

```powershell
python manage.py createsuperuser
```

Creates login credentials for `/admin/`. Use this after migrations have been applied.

## Email Delivery

The contact form saves the visitor's message and sends a thank-you email to the submitted address. In development, Django uses the console backend, so the generated email appears in the terminal instead of being delivered.

For real delivery, configure these environment variables before starting Django:

```text
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-smtp-user
EMAIL_HOST_PASSWORD=your-smtp-password
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False
DEFAULT_FROM_EMAIL=Kaushal Karn <you@example.com>
CONTACT_RECEIVER_EMAIL=kkarn02977@gmail.com
SITE_URL=https://your-domain.example
```

Use your provider's SMTP host, port, credentials, and security requirements. Keep credentials outside source control. If delivery fails, the contact message remains saved and the user sees a warning instead of losing their submission.

## Validation and Testing

### Run Django checks

```powershell
python manage.py check
```

Checks project configuration, URL configuration, models, and application setup.

### Run deployment checks

```powershell
python manage.py check --deploy
```

Checks production security settings such as `DEBUG`, `ALLOWED_HOSTS`, HTTPS, cookies, and HSTS. Resolve every warning before production deployment.

### Run tests

```powershell
python manage.py test
```

Discovers and runs Django tests. Add tests inside the `portfolio` app as the project grows.

### Run a specific app's tests

```powershell
python manage.py test portfolio
```

Runs only tests belonging to the `portfolio` application.

## Static Files

### Collect static files

```powershell
python manage.py collectstatic
```

Copies CSS, JavaScript, images, and other static assets into `STATIC_ROOT`, which is `staticfiles/` in this project.

### Collect without confirmation

```powershell
python manage.py collectstatic --noinput
```

Runs collection in scripts and deployment pipelines without prompting for confirmation.

Do not edit `staticfiles/` directly. Edit files under `static/`, then run `collectstatic` again.

## Admin and Shell

### Open the Django shell

```powershell
python manage.py shell
```

Opens an interactive Python shell with Django configured. Use it to inspect or update database records.

Example:

```python
from portfolio.models import Project, Skill
Project.objects.count()
Skill.objects.filter(category="web")
```

### Open the database shell

```powershell
python manage.py dbshell
```

Opens the configured database client. For this project, that is SQLite, so the SQLite command-line tool must be installed and available on `PATH`.

## Useful Maintenance Commands

### Show all available commands

```powershell
python manage.py help
```

Lists Django's built-in commands and the custom `seed_portfolio` command.

### Show project URL configuration

```powershell
python manage.py show_urls
```

This command is not included in standard Django. Use it only if a URL-listing package is installed. The authoritative route definitions are in [config/urls.py](config/urls.py) and [portfolio/urls.py](portfolio/urls.py).

### Remove Python cache files

PowerShell:

```powershell
Get-ChildItem -Path . -Filter __pycache__ -Recurse -Directory | Remove-Item -Recurse -Force
Get-ChildItem -Path . -Filter *.pyc -Recurse -File | Remove-Item -Force
```

Removes generated Python bytecode. These files are already excluded by `.gitignore` and normally do not need manual cleanup.

## Commands Used During This Project

The following commands were used to install, inspect, build, validate, and document this portfolio. Run them from the project root and activate `venv` first when possible.

### Environment and package commands

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
venv\Scripts\python.exe -m pip install python-dotenv Pillow Daphne Gunicorn
venv\Scripts\python.exe -m pip check
venv\Scripts\python.exe -m pip show Django python-dotenv Pillow daphne gunicorn
```

### Django validation commands

```powershell
venv\Scripts\python.exe manage.py check
venv\Scripts\python.exe manage.py check --deploy
venv\Scripts\python.exe manage.py test
venv\Scripts\python.exe manage.py makemigrations --check --dry-run
venv\Scripts\python.exe manage.py migrate --plan
venv\Scripts\python.exe manage.py collectstatic --noinput
```

### Django runtime and inspection commands

```powershell
venv\Scripts\python.exe manage.py runserver 8000
venv\Scripts\python.exe manage.py shell
venv\Scripts\python.exe manage.py shell -c "..."
venv\Scripts\python.exe manage.py createsuperuser
venv\Scripts\python.exe manage.py seed_portfolio
```

### Environment and asset commands

```powershell
Copy-Item .env.example .env
Get-ChildItem -Force
Get-ChildItem -Recurse -File
Get-Content .gitignore
New-Item -ItemType Directory -Force static\images
Move-Item -Force profile.png static\images\profile-primary.png
Move-Item -Force IMG_20250307_013503.jpg static\images\profile-casual.jpg
Move-Item -Force IMG_20250330_160943.jpg static\images\profile-formal.jpg
```

### Environment cleanup command

The duplicate `.venv` folder was removed because the project already used `venv`:

```powershell
Remove-Item -Recurse -Force .venv
```

### Safe email test command

This uses Django's in-memory backend and does not send real email:

```powershell
venv\Scripts\python.exe manage.py shell -c "from django.core import mail; from django.test.utils import override_settings; from portfolio.models import ContactMessage; from portfolio.views import send_contact_thank_you, send_contact_notification; override = override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend', CONTACT_RECEIVER_EMAIL='kkarn02977@gmail.com'); override.enable(); contact = ContactMessage(name='Test User', email='visitor@example.com', subject='Test', message='Hello'); send_contact_thank_you(contact); send_contact_notification(contact); print([email.to for email in mail.outbox]); override.disable()"
```

Expected recipients:

```text
[['visitor@example.com'], ['kkarn02977@gmail.com']]
```

## Deployment Commands

### Production readiness checks

```powershell
python manage.py check --deploy
python -m pip check
python manage.py makemigrations --check --dry-run
python manage.py test
```

Runs the main configuration, dependency, migration, and test checks before deployment.

### Prepare static assets

```powershell
python manage.py collectstatic --noinput
```

Builds the directory that a production web server should serve as static content.

### Apply production migrations

```powershell
python manage.py migrate --noinput
```

Applies database migrations without interactive confirmation. Run this against the production database only after reviewing the migration plan.

### Start with a WSGI server

The repository provides [config/wsgi.py](config/wsgi.py), but it does not currently include a production WSGI server dependency. After adding and installing one such as Gunicorn, a typical Linux command is:

```bash
gunicorn config.wsgi:application
```

Do not use `runserver` as the production server.

## Command Safety Notes

- Activate the correct virtual environment before running project commands.
- Never commit `.env`, `db.sqlite3`, credentials, or production secrets.
- Back up the database before destructive database operations.
- Do not run `flush` or delete migrations unless you understand the data consequences.
- Set production settings through environment variables instead of hard-coding secrets.

**Continue exploring:** [Project overview](README.md) · [Beginner guide](detail.md) · [Complete reference](complete_detail.md) · [Back to command categories](#command-categories)
