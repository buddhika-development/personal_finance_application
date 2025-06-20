import pandas as pd
import streamlit as st
from utils._database_connection import databse_connection
from utils._database_actions import get_all_income_details
from data_actions.income_data_analyzing import user_income_analyze, get_current_month_income

conn = databse_connection()
income_details = get_all_income_details(conn)
income_titles = ["Transaction Date", "Transaction Amount", "income_source", "income_additional_note"]
income_dataframe_details = pd.DataFrame(income_details, columns= income_titles)
income_dataframe_details["Transaction Date"] = pd.to_datetime(income_dataframe_details["Transaction Date"]).dt.date
income_dataframe_details = income_dataframe_details.sort_values(by= "Transaction Date", ascending= False)
income_dataframe_details = income_dataframe_details.reset_index(drop= True)


# generate mean value of the monthly income
monthly_mean_income = income_dataframe_details["Transaction Amount"].mean()

monthly_income_details = user_income_analyze()
current_month_income = get_current_month_income()
st.title("Income Details")

total_income_ui ,average_income_ui = st.columns(2)

with total_income_ui:
    with st.container(border= True):
        st.text("Monthly Income")
        st.subheader(f"rs.{current_month_income:.2f}")

with average_income_ui:
    with st.container( border= True):
        st.text("Average Monthly Income")
        st.subheader(f"rs.{monthly_mean_income:.2f}")


st.dataframe(income_dataframe_details)

st.title("Monthly Income Details")
st.dataframe(monthly_income_details)