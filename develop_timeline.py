# Streamlit Timeline Component Example
import streamlit as st
from streamlit_timeline import timeline

# use full page width
st.set_page_config(page_title="LG생활건강 인턴", layout="wide") 

# load data
with open('develop_timeline.json', "r") as f:    
    data = f.read()

# render timeline
timeline(data, height=700) 