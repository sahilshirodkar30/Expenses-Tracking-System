import streamlit as st
from add_update_ui import add_update_tab
from analytics_UI import analytics_tab
from analytics_by_months_ui import analytics_by_months_tab

API_URL = "http://localhost:8000"

st.title("Expense Management System")

tab1, tab2 ,tab3= st.tabs(["ADD/UPDATE", "ANALYTICS BY Category","Analytics by Months"])

with tab1:
    add_update_tab()

with tab2:
    analytics_tab()

with tab3:
    analytics_by_months_tab()