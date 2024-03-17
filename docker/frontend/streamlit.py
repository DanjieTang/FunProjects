import requests
import streamlit as st

request = requests.get("http://docker-backend-1:80/funny_words")
st.title(request.text)
