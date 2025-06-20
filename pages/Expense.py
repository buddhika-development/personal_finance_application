import pandas as pd
import streamlit as st
from utils._database_connection import databse_connection
from utils._database_actions import get_all_expense_details
from data_actions.expense_data_analyzing import get_all_expense_details

conn = databse_connection()
expense_database_details=  get_all_expense_details(conn)
expense_titles = ["Transaction Date", "Transaction Amount", "Expense Category", "Expense Reason", "Expense Additional Note"]
expense_details = pd.DataFrame(expense_database_details, columns= expense_titles)

get_all_expense_details()

st.title("Expense Details")
st.dataframe(expense_details)