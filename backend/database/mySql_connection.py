import os
from pathlib import Path
from urllib.parse import quote_plus  # NEW

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load .env from the backend folder
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

DB_HOST = os.getenv("dbhost", "localhost")
DB_PORT = os.getenv("dbport", "3306")
DB_USER = os.getenv("dbuser", "root")

DB_PASSWORD_RAW = os.getenv("dbpassword", "")
DB_PASSWORD = quote_plus(DB_PASSWORD_RAW)  # encode special chars like @

DB_NAME = os.getenv("dbname", "stroke_db")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
db = engine.connect()