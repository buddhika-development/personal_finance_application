import psycopg2
import logging
from utils._database_connection import databse_connection
from psycopg2.extensions import connection

logging.basicConfig(level= logging.INFO)
logger = logging.getLogger(__name__)

def transaction_insertion(conn: connection,transaction_type:bool, transaction_amount:float) -> int | None:
    """
    Insert transaction data into transactions table

    Does:
        This function responsible for insert the transaction data into transactions table in database
    
    Args:
        This function requires as first argument it get database_connection:psycopg2.extension.connection 
        as second argument transaction_type as boolean for represent (0)expense and (1)income,
        as third argument required transaction amount from float data type
    
    returns:
        There return the transaction id if process get success, otherwise return none
    """

    query = """
        INSERT INTO transactions(transaction_type, transaction_amount)
        VALUES (%s, %s)
        RETURNING transaction_id
    """

    try:

        with conn.cursor() as cur:
            cur.execute(query, (transaction_type, transaction_amount))
            transaction_id = cur.fetchone()[0]
            conn.commit()
        
        logger.info("Succuessfully insert the transaction details")
        return transaction_id
    except psycopg2.Error as e:
        conn.rollback()
        logger.error(f"Unexpeted error occur in transaction insertion process.. {e}")
    except Exception as e:
        conn.rollback()
        logger.error(f"Something unexpected happen in transaction data insertion process.. {e}")
