import pandas as pd
import streamlit as st
from utils._database_connection import databse_connection
from utils._database_actions import get_all_income_details

conn = databse_connection()
income_details = get_all_income_details(conn)
income_titles = ["Transaction Date", "Transaction Amount", "income_source", "income_additional_note"]
income_dataframe_details = pd.DataFrame(income_details, columns= income_titles)
income_dataframe_details["Transaction Date"] = pd.to_datetime(income_dataframe_details["Transaction Date"]).dt.date
income_dataframe_details = income_dataframe_details.sort_values(by= "Transaction Date", ascending= False)
income_dataframe_details = income_dataframe_details.reset_index(drop= True)


# generate mean value of the monthly income
monthly_mean_income = income_dataframe_details["Transaction Amount"].mean()

# generaete month income
selected_columns = ["Transaction Date", "Transaction Amount"]
_income = income_dataframe_details[selected_columns]
_income["Transaction Date"] = pd.to_datetime(_income["Transaction Date"]).dt.to_period('M')

monthly_income = _income.groupby('Transaction Date')['Transaction Amount'].sum().reset_index()

# Rename columns for clarity
monthly_income.columns = ['Transaction Date', 'Total Income']
monthly_income.sort_values(by= "Transaction Date", ascending= False)

print(monthly_income)

st.title("Income Details")

with st.container( border= True):
    st.text("Average Monthly Income")
    st.subheader(f"rs.{monthly_mean_income:.2f}")


st.dataframe(income_dataframe_details)

st.title("Monthly Income")
st.dataframe(monthly_income)