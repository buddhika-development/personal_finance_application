import pandas as pd
import streamlit as st
from utils._database_connection import databse_connection
from utils._database_actions import get_all_expense_details
from data_actions.expense_data_analyzing import analyze_monthly_expense, monthly_total_expense_value

conn = databse_connection()
expense_database_details=  get_all_expense_details(conn)
expense_titles = ["Transaction Date", "Transaction Amount", "Expense Category", "Expense Reason", "Expense Additional Note"]
expense_details = pd.DataFrame(expense_database_details, columns= expense_titles)

# generate mean value
expense_monthly_mean = expense_details["Transaction Amount"].mean()

monthly_total_expense = monthly_total_expense_value()
expense_analyze_details = analyze_monthly_expense()

st.title("Expense Details")

# show statistics related to monthly income
monthly_total_expense_ui, averate_expense_value = st.columns(2)

with monthly_total_expense_value:
    with st.container(border= True):
        st.text("Total Of Monthly Expense")
        st.title(f"rs.{monthly_total_expense:.2f}")

with averate_expense_value:
    with st.container(border= True):
        st.text("Average expense")
        st.title(f"rs.{expense_monthly_mean:.2f}")

st.title("Monethly Expense Details")
st.dataframe(expense_analyze_details)

st.title("Expense Details")
st.dataframe(expense_details)
