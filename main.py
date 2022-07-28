import pandas as pd
import streamlit as st



st.set_page_config(
     page_title="Streamlit Main",
     page_icon=":goat:",
     layout="wide"
 )

st.title("Main")
st.header("Features")
st.subheader("Multipages app")
st.subheader("Login Authentication")
st.sidebar.success("Select a page above")
