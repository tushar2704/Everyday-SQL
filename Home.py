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

main_title()

#######################################################################################################
#Page Config of Everyday_SQL by github.com/tushar2704
#######################################################################################################
custom_style()
#######################################################################################################
#Body of Everyday_SQL by github.com/tushar2704
#######################################################################################################
page_header('''
            ''')


#Sidebar Pages
with st.sidebar:
    logo()
    st.page_link("Home.py", label="Everyday Cheat Sheets", icon="🐍")
    
    st.page_link("pages/page1.py", label="Top SQL Queries", icon="🐍")
   
    

 
#######################
#Body

    

#######################################################################################################
#End of Everyday_SQL by github.com/tushar2704
#######################################################################################################










footer()
#######################################################################################################
#End of Everyday_SQL by github.com/tushar2704
#######################################################################################################
