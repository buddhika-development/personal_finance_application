import pandas as pd
from utils._database_connection import databse_connection
from utils._database_actions import get_all_expense_details

conn = databse_connection()
expense = get_all_expense_details(conn)

def analyze_monthly_expense() -> pd.DataFrame:
    columns = ["Date", "Amount"]
    monthly_expense_details = expense[columns]
    monthly_expense_details["Date"] = monthly_expense_details["Date"].dt.to_timestamp().dt.to_period("M")

    monthly_expense_details = monthly_expense_details.groupby(by="Date")["Amount"].sum().reset_index()

    monthly_expense_details["Month"] = monthly_expense_details["Date"].dt.to_timestamp().dt.month_name()
    monthly_expense_details["Year"] = monthly_expense_details["Date"].dt.to_timestamp().dt.year

    monthly_expense_details = monthly_expense_details.sort_values(by="Date", ascending= False).reset_index(drop= True)

    return monthly_expense_details


def monthly_total_expense_value():
    expense_details = analyze_monthly_expense()
    return expense_details.iloc[0]["Amount"]