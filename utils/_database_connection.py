import os
import psycopg2
from psycopg2.extensions import connection
import logging

# setup basic logging
logging.basicConfig(level= logging.INFO)
logger = logging.getLogger(__name__)

def database_connection() -> connection | None :
    """
    Extablished a connection to the postgreSQL using enviorenment variables

    returns:
        A psycopg2 object if successfull, or None if the connection fails
    """
    
    try:
        conn = psycopg2.connect(
            host = os.getenv("db_host"),
            port = os.getenv("db_port"),
            database = os.getenv("database"),
            user = os.getenv("db_user"),
            password = os.getenv("db_password")
        )
        
        logger.info("Established the database connection successfully.")
        return conn
    
    except Exception as e:
        logger.error(f"Something bad happen while databse conneting process... {e}")
        print(f"Something went wrong in database connection... {e}")