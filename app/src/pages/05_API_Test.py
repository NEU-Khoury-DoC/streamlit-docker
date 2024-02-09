

import streamlit as st
import requests


st.set_page_config (page_title="API Test", page_icon="🙏")

st.write("# Accessing a REST API from Within Streamlit")

"""
Simply retrieving data from a REST api running in a separate Docker Container.

If the container isn't running, this will be very unhappy.  But the Streamlit app 
should not totally die. 
"""
data = {} 
try:
  data = requests.get('http://localhost:8989/data').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": 123, "c": "hello"}, "z": {"b": 456, "c": "goodbye"}}

st.dataframe(data)