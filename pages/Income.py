import pandas as pd
import streamlit as st
from utils._database_connection import databse_connection
from utils._database_actions import get_all_income_details

conn = databse_connection()
income_details = get_all_income_details(conn)
income_titles = ["transaction_date", "transaction_amount", "income_source", "income_additional_note"]

income_dataframe_details = pd.DataFrame(income_details, columns= income_titles)

st.title("Income Details")
st.dataframe(income_dataframe_details)