import os
from dotenv import load_dotenv

# Load .env file so environment variables like DB_URI are available
load_dotenv()

class Config:
    """Application configuration.

    Set the `DB_URI` environment variable to your PostgreSQL URI, for example:
    `postgresql+psycopg2://user:password@host:port/database_name`

    If you don't set `DB_URI`, a placeholder default will be used — replace it with
    your real URI in production.
    """
    DEBUG = os.getenv('DEBUG', 'False').lower() in ('1', 'true')
    SECRET_KEY = os.getenv('SECRET_KEY', 'change-me')
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DB_URI',
        'postgresql://user:password@localhost:5432/full_stack_bank_application'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Automatically create tables on app startup when True. Defaults to True.
    # Set AUTO_CREATE_TABLES=False in production if you prefer to manage schema explicitly.
    AUTO_CREATE_TABLES = os.getenv('AUTO_CREATE_TABLES', 'True').lower() in ('1', 'true')

    # Static file cache duration (seconds). Default to 0 in DEBUG to avoid stale assets,
    # and a long cache duration in production.
    SEND_FILE_MAX_AGE_DEFAULT = 0 if DEBUG else 31536000