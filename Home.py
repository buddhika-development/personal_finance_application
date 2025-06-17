import streamlit as st
from functions._add_new_transaction import add_new_income_transaction_, add_new_expense_transaction
from utils._database_connection import database_connection

st.title("Add new Transaction")
database_connection()

with st.container():

    transaction_amount_input, transaction_type_input = st.columns([2,1])

    with transaction_amount_input:
        transaction_amount = st.number_input("Tranaction Amount")
    with transaction_type_input:
        transaction_type = st.selectbox("Transaction Type", ["Income", "Expense"])

    if transaction_type.lower() == "income":
        income_resource = st.selectbox("Income Source", ["Job", "Business Income", "Investment"])
        income_note = st.text_area("Additional Notes")

        income_add = st.button("Add new Income")

        if income_add:
            add_new_income_transaction_()
    
    if transaction_type.lower() == "expense":

        expense_tag_,expense_reason_ = st.columns([2,5])

        with expense_tag_:
            expense_tag = st.selectbox("Expense Category", ["Monthly Bills", "Rent", "Gods", "Subscriptions"])
        with expense_reason_:
            expense_reason = st.text_input("Expense Reasone")

        expense_additional_note = st.text_area("Additional note")
        expense_add = st.button("Add new Expense")

        if expense_add:
            add_new_expense_transaction()