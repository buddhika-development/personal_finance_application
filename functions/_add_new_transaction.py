import logging
from utils._database_connection import databse_connection
from utils._database_actions import transaction_insertion, income_insertion, expense_insertion

conn = databse_connection()
logging.basicConfig( level= logging.INFO)
logger = logging.getLogger(__name__)

def add_new_income_transaction_(transaction_type:bool, tranaction_amount:float, income_source:str, income_note:str) -> None:
    """
    Handle the income transaction database store process

    Does:
        This function is responsible for handle the data insertion related to income trasaction process.
        There store data in transaction table and income tables
    
    Args:
        transaction_type -> types of the transaction( true for income and false for expense)
        tansaction_amount:float
        income_source:str
        income_note:str -> is there any special note about the income transaction
    """
    
    transaction_id = transaction_insertion(
        conn= conn,
        transaction_type= transaction_type,
        transaction_amount= tranaction_amount
    )

    income_insertion(conn, transaction_id, income_source, income_note)
    

def add_new_expense_transaction(transaction_type:bool, transaction_amount:float, expense_tag:str, expense_reason:str, expense_note:str) -> None:
    """
    Handle the expense traaction databse store process

    Does:
        This function is responsible for handle the data insertion related to income transaction process.
        There store the data in transaction table and expense tables
    
    Args:
        transaction_type -> type of the transaction( true for income and false for expense)
        transaction_amount,
        expense_tag -> type of transaction
        expense_reason,
        expense_addition_note
    """
    transaction_id = transaction_insertion(
        conn= conn,
        transaction_type= transaction_type,
        transaction_amount= transaction_amount
    )

    expense_insertion(conn, transaction_id, expense_tag, expense_reason, expense_note)