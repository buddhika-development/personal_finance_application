import pandas as pd
from utils._database_connection import databse_connection
from utils._database_actions import get_all_expense_details, get_all_income_details

conn = databse_connection()

def user_income_analyze() -> pd.DataFrame:
    """
    Convert income transaction details into montly income details

    Does:
        This function is responsible for setup transaction data into monthly data and generate indivudual month income and convert into pandas dataframe
    
    Returns:
        Return the analyzed monthly income.
    """
    
    income = get_all_income_details(conn)
    expense = get_all_expense_details(conn)
    income_dataframe = pd.DataFrame(income, columns=["Transaction Date", "Transaction Amount", "Expense Reason", "Additional notes"])
    income_dataframe["Transaction Date"] = pd.to_datetime(income_dataframe["Transaction Date"]).dt.to_period('M')

    # generate monthly income
    monthly_income = income_dataframe.groupby(by="Transaction Date")["Transaction Amount"].sum().reset_index()
    monthly_income["Transaction Date"] = monthly_income['Transaction Date'].dt.to_timestamp()
    monthly_income["Month"] = monthly_income["Transaction Date"].dt.month_name()
    monthly_income["Year"] = monthly_income["Transaction Date"].dt.year
    monthly_income = monthly_income.sort_values(by= "Year", ascending= False)

    columns = ["Year", "Month", "Transaction Amount"]
    income_processed_dataframe = monthly_income[columns].reset_index(drop= True)

    return income_processed_dataframe


def get_current_month_income() -> float:
    
    monthly_income = user_income_analyze()
    return monthly_income.iloc[0]["Transaction Amount"]