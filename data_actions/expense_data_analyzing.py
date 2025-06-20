from utils._database_connection import databse_connection
from utils._database_actions import get_all_expense_details

conn = databse_connection()
expense = get_all_expense_details(conn)

def analyze_monthly_expense():
    print("thjis is analyze function")