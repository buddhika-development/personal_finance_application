import psycopg2
import logging
import os
from dotenv import load_dotenv
from psycopg2.extensions import connection
from utils._database_management import _table_creation_process

load_dotenv()

logging.basicConfig(level= logging.INFO)
logger = logging.getLogger(__name__)

def databse_connection() -> connection | None:

    """
    Establish dabase connection with the postgresql database management system through the variables comes from enviorenmental variables

    returns:
        If connection extablish process got success it will return database connection object, otherwise it will return NONE
    """

    try:

        conn = psycopg2.connect(
            host= os.getenv("db_host"),
            port = os.getenv("db_port"),
            database = os.getenv("database"),
            user = os.getenv("db_user"),
            password = os.getenv("db_password")
        )
        
        _table_creation_process(conn)

        logger.info("Database connection succesfully extablished..")
        return conn
    
    except Exception as e:
        logger.error(f"Something went wrong in database conneciton process... {e}")
        return None
