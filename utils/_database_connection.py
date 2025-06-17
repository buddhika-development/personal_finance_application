import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def database_connection():
    print("This is my database connection")