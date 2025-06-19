from utils._database_connection import databse_connection
from utils._database_actions import transaction_insertion

conn = databse_connection()

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


def add_new_expense_transaction():
    print("this is expense tranaction")