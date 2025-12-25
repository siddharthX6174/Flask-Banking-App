from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os

# load environment variables from the .env file
load_dotenv()

# Ensure OS knows about font MIME types (helps some Windows setups and dev servers)
import mimetypes
mimetypes.add_type('font/woff2', '.woff2')
mimetypes.add_type('font/woff', '.woff')

app = Flask(__name__)
app.config.from_object(Config)

# Ensure Flask uses the configured static file cache timeout
app.config.setdefault('SEND_FILE_MAX_AGE_DEFAULT', app.config.get('SEND_FILE_MAX_AGE_DEFAULT'))

# SECRET_KEY and SQLALCHEMY_DATABASE_URI are read from Config (which loads env vars)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)



from app.routes.root import *  
from app.routes.user import *
# Import model classes to ensure they're registered with SQLAlchemy
from app.models.user import User, Transaction

# Optionally auto-create tables on application startup when enabled in config.
if app.config.get('AUTO_CREATE_TABLES', False):
    try:
        with app.app_context():
            db.create_all()
            print('AUTO_CREATE_TABLES is enabled — created missing tables.')
    except Exception as exc:
        # Do not crash the application if table creation fails (e.g., DB missing or permission denied).
        print('AUTO_CREATE_TABLES: failed to create tables (DB may be missing or inaccessible).')
        print('Details:', exc)
        print('If the database does not exist, run: python create_db.py')