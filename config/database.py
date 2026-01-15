import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=str(os.getenv("DB_HOST")),
        database=str(os.getenv("DB_DATABASE")),
        user=str(os.getenv("DB_USER")),
        password=str(os.getenv("DB_PASSWORD")),
        port=int(os.getenv("DB_PORT"))
    )