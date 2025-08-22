# Remind-me-later API

A simple Django REST Framework (DRF) API for creating reminders.  

---

## Features
- Create reminders with:
  - Date
  - Time
  - Message
  - Reminder type (SMS / Email)
- Validation rules:
  - Cannot schedule reminders in the past
  - Reminder type must be either SMS or Email
  - Message cannot be empty
- Service Layer pattern for business logic
- Extensible design (future support for Celery/queues to send reminders)
- Admin dashboard integration

---

## Tech Stack
- Python 3.10+
- Django 4.x
- Django REST Framework
- SQLite (default, can switch to Postgres/MySQL)

---

## Setup Instructions
1. Clone the repo:
   ```bash
   git clone https://github.com/sreejayam/remind-me-later.git
   cd remindme
2. Create virtual environment and install dependencies:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   pip install -r requirements.txt
3. Run migrations:
   ```bash
   python manage.py migrate
4. Start the server:
   ```bash
   python manage.py runserver
5. Running Test:

```bash
python manage.py test
   


