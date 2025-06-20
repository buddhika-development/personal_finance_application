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


def income_insertion(conn:connection, transaction_id:int ,income_source:str, income_note:str) -> None:
    """
    Insert income details into database

    Does:
        Insert income details into database with the id of transaction
    
    Args:
        Database connection as conn:psycopg2.extension.connection
        income_source:str
        income_note:str
    """

    query = """
        INSERT INTO income(transaction_id, income_source, income_additional_note)
        VALUES (%s, %s, %s)
    """
    
    try:

        with conn.cursor() as cur:
            cur.execute(query, (transaction_id, income_source, income_note))
            conn.commit()
        logger.info("Successfully insert income details..")
        
    except psycopg2.Error as e:
        conn.rollback()
        logger.error(f"Error occur in income data insertion process.. {e}")
    except Exception as e:
        conn.rollback()
        logger.error(f"Something unexpected happen in income data insertion process,,, {e}")



def expense_insertion(conn:connection, transaction_id:int, expense_category:str, expense_reason:str, expense_note:str) -> None:
    """
    Insert expense details into database

    Does:
        Insert expense details into database with the id of transaction
    
    Args:
        database connection,
        transaction_id,
        expense_category,
        expense_reason,
        expense_note
    """

    query = """
        INSERT INTO expense(transaction_id, expense_category, expense_reason, expense_additional_note)
        VALUES (%s, %s, %s, %s);
    """

    try:
        with conn.cursor() as cur:
            cur.execute(query, (transaction_id, expense_category, expense_reason, expense_note))
            conn.commit()
        logger.info("Successfully insert the expense details...")
        
    except psycopg2.Error as e:
        conn.rollback()
        logger.error(f"Error occur in expense data insertion process... {e}")
    except Exception as e:
        conn.rollback()
        logger.error(f"Something unexpected happe in expense data insertion process.. {e}")



def get_all_income_details(conn:connection):
    """
    Get all details from the income view

    Does:
        Access all the income details from the database, using the income_view
    
    Args:
        Database connection:psycopg2.extension.connection
    """

    query = "SELECT transaction_date,transaction_amount,income_source,income_additional_note FROM income_view;"

    try:
        with conn.cursor() as cur:
            cur.execute(query)
            income_details = cur.fetchall()
        logger.info("Access all the income details from the income_view")
        return income_details
            
    except psycopg2.Error as e:
        logger.error(f"Error occur while income data accessing... {e}")
    except Exception as e:
        logger.error(f"Something unexpected happen while income data loading.. {e}")



def get_all_expense_details(conn:connection):
    """
    Get all details from the expense view

    Does:
        Access all the expense details from the database, using the expense_view
    
    Args:
        Database connection:psycopg2.extension.connection
    """

    query = "SELECT transaction_date,transaction_amount,expense_category,expense_reason,expense_additional_note FROM expense_view;"

    try:
        with conn.cursor() as cur:
            cur.execute(query)
            expense_details = cur.fetchall()
        logger.info("Access all the expense details from the expense_view")
        return expense_details
            
    except psycopg2.Error as e:
        logger.error(f"Error occur while income data accessing... {e}")
    except Exception as e:
        logger.error(f"Something unexpected happen while expense data loading.. {e}")
