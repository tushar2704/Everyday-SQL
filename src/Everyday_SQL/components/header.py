##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Everyday_SQL
#######################################################################################################
#Importing dependecies
#######################################################################################################

import streamlit as st
from pathlib import Path
import base64
import sys
from pathlib import Path
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent
sys.path.append(str(project_root))
import warnings
warnings.filterwarnings("ignore")
import os


#######################################################################################################
#Importing from SRC
#######################################################################################################
from src.Everyday_SQL.components.header import *
from src.Everyday_SQL.components.body import *
from src.Everyday_SQL.components.navigation import *
from src.Everyday_SQL.components.siderbar import *
from src.Everyday_SQL.components.metrics import *
from src.Everyday_SQL.components.charts import *
from src.Everyday_SQL.components.test import *

#######################################################################################################
#Header of Everyday_SQL by github.com/tushar2704
#######################################################################################################

def main_title():
    st.set_page_config(page_title="Everday SQL Sheets",
                   page_icon=":🤝:",
                    layout='wide')
    # ---- HIDE STREAMLIT STYLE ----
    hide_st_style = """
                <style>
                MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)
    
    
def page_header(header):
    # custom_css = """
    #         <style>
    #         .stApp > header {
    #             background-color: transparent;
    #         }

    #         .stApp {
    #             margin: auto;
    #             font-family: 'Roboto', sans-serif;
    #             overflow: auto;
    #             background: linear-gradient(315deg, #7690CF 15%, #7dc4ff 38%, #FCE043 28%, #D3DCF2 98%);
    #             animation: gradient 15s ease infinite;
    #             background-size: 400% 400%;
    #             background-attachment: fixed;
    #         }


    #         </style>
    #         """
            
    # st.markdown(custom_css, unsafe_allow_html=True)
    st.title("🌐🤝Everyday SQL Sheets🌐🤝")
    st.markdown('''
            <style>
                div.block-container{padding-top:0px;}
                font-family: 'Roboto', sans-serif; /* Add Roboto font */
                color: blue; /* Make the text blue */
            </style>
                ''',
            unsafe_allow_html=True)
    
    st.markdown(header)
    
    
    
    
    
    
    