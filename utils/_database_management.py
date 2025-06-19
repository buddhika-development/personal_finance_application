import psycopg2
from psycopg2.extensions import connection
import logging

logging.basicConfig(level= logging.INFO)
logger = logging.getLogger(__name__)

def _table_creation_process(conn: connection) -> None:
    """
    reates necessary tables in the database if they do not exist.

    Args:
        conn (psycopg2.extensions.connection): Database connection object.
    """

    _create_transaction_table(conn)
    _create_income_table(conn)
    _create_expense_table(conn)
    _create_income_view(conn)
    _create_expense_view(conn)


def _create_transaction_table(conn:connection) -> None:

    """
    Ceates transaction table in database

    Does:
        If transaction table is not available in the database, create the transacction table in database.
    
    Args:
        Database connection: psyconpg2.extention.connection 
    """

    query = """
        CREATE TABLE IF NOT EXISTS transactions(
            transaction_id SERIAL PRIMARY KEY,
            transaction_date DATE NOT NULL DEFAULT CURRENT_DATE,
            transaction_type BOOLEAN NOT NULL,
            transaction_amount FLOAT NOT NULL
        )
    """

    try:

        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
            
        logger.info("Transaction table creation process successfull....")

    except psycopg2.Error as e:
        conn.rollback()
        logger.error(f"Failed to create transaction table.. {e}")

    except Exception as e:
        conn.rollback()
        logger.error(f"Unexpected error in transaction table creation process.. {e}")



def _create_income_table(conn:connection) -> None:
    """
    Create income table in database

    Does:
        If income table is not available in database create the income table in the database
    
    Args:
        Database connection : psycopg2.extention.connection
    """

    query = """
        CREATE TABLE IF NOT EXISTS income(
            income_id SERIAL PRIMARY KEY,
            transaction_id INT NOT NULL,
            income_source VARCHAR(50) NOT NULL,
            income_additional_note TEXT NOT NULL,
            FOREIGN KEY(transaction_id) REFERENCES transactions(transaction_id) ON DELETE CASCADE
        )
    """

    try:

        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
        
        logger.info("Income table creation process successfull.")
    
    except psycopg2.Error as e:
        conn.rollback()
        logger.error(f"Failed income table creation process.. {e}")

    except Exception as e:
        conn.rollback()
        logger.error(f"Unexpeced error occur in income table creation process.. {e}")



def _create_expense_table(conn: connection):
    """
    Create expense table in database

    Does:
        Create expense tabel if not exists in the database.
    
    Args:
        Database connection: psycopg2.extension.connection
    """

    query = """
        CREATE TABLE IF NOT EXISTS expense(
            expense_id SERIAL PRIMARY KEY,
            transaction_id INT NOT NULL,
            expense_category VARCHAR(50) NOT NULL,
            expense_reason VARCHAR(255) NOT NULL,
            expense_additional_note TEXT NOT NULL,
            FOREIGN KEY(transaction_id) REFERENCES transactions(transaction_id) ON DELETE CASCADE
        )
    """

    try:

        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
        logger.info("Expense table successfully created..")
        
    except psycopg2.Error as e:
        conn.rollback()
        logger.error(f"Expense table creation process occur error : {e}")
        
    except Exception as e:
        conn.rollback()
        logger.error(f"Unexpected error occur in expense table creation.. {e}")



def _create_income_view(conn:connection) -> None:
    """
    Create view for income

    Does:
        Create view to show all the details about income in one place. If already have view it replace or make new view if view already doen't exists
    
    Args:
        Database connection: psycopg2.extension.connection
    """

    query = """
        CREATE OR REPLACE VIEW income_view AS SELECT
            i.income_id,
            t.transaction_id,
            t.transaction_date,
            t.transaction_amount,
            i.income_source,
            i.income_additional_note
        From income i
        JOIN transactions t ON t.transaction_id = i.transaction_id
    """

    try:

        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
        logger.info("Income view successfully created...")
    
    except psycopg2.Error as e:
        conn.rollback()
        logger.error(f"Income view creation process occur unexped happen : {e}")
    except Exception as e:
        conn.rollback()
        logger.error(f"Unexpedcted happen in income view creation process.. {e}")



def _create_expense_view(conn:connection) -> None:
    """
    Create expense view in database

    Does:
        Create or replace the expense view in databse.
        If expense view already exists in database replace that view, other wise create new view related to expense details
    """

    query = """
        CREATE OR REPLACE VIEW expense_view AS
        SELECT
            e.expense_id,
            t.transaction_id,
            t.transaction_date,
            t.transaction_amount,
            e.expense_category,
            e.expense_reason,
            e.expense_additional_note
        FROM expense e
        JOIN transactions t ON t.transaction_id = e.transaction_id
    """

    try:

        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
        logger.info("Expense view successfully created,,")
    except psycopg2.Error as e:
        conn.rollback()
        logger.error(f"Occure error in expence view creation process.. {e}")
    except Exception as e:
        conn.rollback()
        logger.error(f"Something unexpected happen in expense view creation process : {e}")