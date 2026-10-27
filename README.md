# FixLog – Repair Services

FixLog is a Django web application for keeping track of device repairs and the parts used to complete them. It is designed for a small repair shop that needs a straightforward way to manage repair tickets, technicians, and inventory in one place.

## What it does

- **Repair tickets:** create and view repair records, check their status, update details, and delete tickets with a confirmation step.
- **Customer ticket lookup:** customers can search for matching repair tickets using the name and phone number supplied with the repair.
- **Technicians:** keep technician information available when assigning work to repair tickets.
- **Inventory:** manage stock items and view individual item details.
- **Parts used:** associate inventory parts with repair tickets so the repair record can show which parts were used.
- **Shared layout:** Django templates use a common base layout and consistent styling across pages.

The project does not use login, registration, or Django User accounts, in line with the Django Basics project requirements.

## Built with

- Python
- Django
- PostgreSQL (recommended for local evaluation)
- Django Template Language
- HTML and CSS

## Getting started

### 1. Get the project

Clone the repository or download the source code, then open a terminal in the project directory.

```bash
git clone <your-public-repository-url>
cd <project-folder>
```

Replace the placeholders above with your repository URL and folder name.

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

On Windows:

```powershell
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

If the project includes a `requirements.txt` file, run:

```bash
pip install -r requirements.txt
```

If it does not, install Django using the version required by the project:

```bash
pip install Django
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open the local address shown in the terminal, usually `http://127.0.0.1:8000/`.

## Using the application

Use the navigation menu to move between the available repair, technician, and inventory pages. Create the required records through the website itself; the application should not depend on preloaded sample data or on using the Django admin to demonstrate its main features.

For a clean evaluation, start with an empty database and create records through the application interface.

## Project structure

The project is organized into Django apps with separate responsibilities:

- `repairs` – repair tickets and related repair workflows.
- `technicians` – technician information.
- `inventory` – inventory items and parts.

The exact files and URL names may vary with the current project version.

## Configuration

The default local setup is intended to use SQLite. If your local settings require environment variables or credentials, document their names and how to set them here before submitting the repository. Do not commit passwords, secret keys, or other private credentials.

## Notes

- Run migrations before starting the application.
- Keep the dependencies file up to date so another person can install the project without guessing which packages are needed.
- Make sure the repository contains the templates, static files, migrations, and other source files required to run the application.

## Repository description

**Short description for GitHub:**

> A Django-based repair service management app for tracking repair tickets, technicians, and inventory, with customer ticket lookup and parts tracking.
