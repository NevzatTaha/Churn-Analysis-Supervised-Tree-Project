import streamlit as st
import pandas as pd

df=pd.read_csv("Telco-Customer-Churn.csv")
df.set_index("customerID")
st.header('CHURN ANALYSİS')
st.subheader("General Information")

st.write("This is a dashboard of the final project for the supervise learning for Python for Machine Learning Data Science Master Class.")

if st.checkbox('Show Table'):
    st.markdown(' The Project Data at the below')
    st.write(df)


st.text_input("Your name", key="name")

# You can access the value at any point with:
st.write('Welcome the Board', st.session_state.name)



