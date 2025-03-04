import os, sys 
import pandas as pd 
import numpy as np
import streamlit as st
from github import Github
from databricks import sql 
import sqlparse
import streamlit_authenticator as stauth
import yaml 
from yaml.loader import SafeLoader
from dotenv import load_dotenv
load_dotenv()


import streamlit as st


# Page Config
st.set_page_config(
    page_title="SQLGenPro",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="expanded",
)



# The App design
st.markdown("<h1 style='text-align: center; color: orange;'> SQLGenPro &#128640; </h1>", unsafe_allow_html=True)

st.markdown("<h6 style='text-align: center; color: white;'> Productivity Improvement tool for Product Managers, Business stakeholders and even intermediate-coders when it comes to working with data stored in a traditional SQL database. </h6>", unsafe_allow_html=True)

# Authentication
with open("authenticator.yaml", "")