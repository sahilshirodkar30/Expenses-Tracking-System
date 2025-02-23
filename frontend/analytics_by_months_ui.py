import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def analytics_by_months_tab():
    response = requests.get(f"{API_URL}/analytics_by_months")
    response = response.json()

    #st.write(response)

    data = {
        "months" : list(response.keys()),
        "total" : [ response[x]['total'] for x in response]
    }
    df = pd.DataFrame(data)
    df_sort = df.sort_values(by = "months",ascending=False)

    #st.write(df_sort)
    st.bar_chart(data=df_sort.set_index("months")['total'], width=0, height=0, use_container_width=True)
