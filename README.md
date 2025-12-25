# Full-Stack Bank Application

## About
A simple full-stack banking web app built with Flask. It supports user registration and login, account balances, deposits, transfers, recharges, transaction history, and receipt generation. The app is intended as an educational/demo project and includes scripts for initializing the database and models.

## Tech stack
- Python 3.11+
- Flask, Flask-SQLAlchemy, SQLAlchemy
- PostgreSQL (psycopg2)
- Jinja2 templates, vanilla CSS/JS
- Bcrypt for password hashing

## Project structure
```
Full_Stack_Bank_Application/
├─ config.py                # app configuration (reads .env)
├─ create_db.py             # create DB (if possible) and run db.create_all()
├─ tables.py                # lists DB tables (inspector)
├─ run.py                   # app entrypoint
├─ requirements.txt
├─ .env.example             # sample env vars
├─ .gitignore
├─ README.md
├─ app/
│  ├─ __init__.py
│  ├─ models/
│  │  └─ user/
│  │     ├─ user.py
│  │     └─ transaction.py
│  ├─ routes/
│  │  ├─ root/        # index, login, register, about, contact, services
│  │  └─ user/        # dashboard, deposit, transfer, history, etc.
│  ├─ static/         # css, js, images, fonts
│  └─ templates/      # Jinja templates (root/, user/)
└─ flaskenv/            # virtualenv (not checked into git)
```

> Note: this is a trimmed view — see the repo root for full contents.

## Key features
- User registration and secure authentication
- Account balance management (deposits, transfers, recharges)
- Transaction recording and history with timestamps
- Receipt generation templates
- PostgreSQL backend with environment-configured `DB_URI`
- Auto-create missing tables on startup (configurable via `AUTO_CREATE_TABLES`)

## Quickstart
1. Copy `.env.example` to `.env` and set values (DB_URI, SECRET_KEY).
2. Activate the virtualenv (Windows PowerShell):
   ```powershell
   .\flaskenv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. (Optional) Create DB and tables:
   ```bash
   python create_db.py
   ```
5. Run the app:
   ```bash
   python run.py
   # Open http://127.0.0.1:5000
   ```

## Configuration
Key `.env` variables:
- `DB_URI`: PostgreSQL URI (example: `postgresql+psycopg2://user:pass@host:5432/dbname`)
- `SECRET_KEY`: Flask secret for sessions
- `AUTO_CREATE_TABLES`: `True` to auto-create missing tables on startup
- `DEBUG`: enable debug mode

> Note: Keep `.env` out of source control. Use `.env.example` as a template.

## Database scripts
- `create_db.py`: Tries to create the database (using the maintenance DB) and runs `db.create_all()`.
- `tables.py`: Lists tables in the current database via SQLAlchemy inspector.

## Development notes
- Models specify explicit table names (e.g., `users`) to avoid reserved-name conflicts.
- For production deployments and schema changes, use a migration tool like Alembic/Flask-Migrate.

## Contributing
PRs and issues are welcome. Please avoid committing secrets and large binary files.

## License
MIT (add your own LICENSE file if needed)

---

If you want a different tone or shorter sections, tell me which parts to trim or reword.
