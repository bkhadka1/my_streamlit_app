import pandas as pd
import streamlit as st

df = pd.read_csv('API_NPL_DS2_en_excel_v2_5882607 (1).csv')

st.dataframe(df)
