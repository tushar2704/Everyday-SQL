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

# main_title()

#######################################################################################################
#Page Config of Everyday_SQL by github.com/tushar2704
#######################################################################################################
custom_style()
#######################################################################################################
#Body of Everyday_SQL by github.com/tushar2704
#######################################################################################################
page_header('''
            ''')

#######################################################################################################
#Pages(1) of Everyday_SQL by github.com/tushar2704
#######################################################################################################




#Sidebar Pages
with st.sidebar:
    logo()
    st.page_link("Home.py", label="Back to Home", icon="🏠")
    
    
    


def page1():
    st.header("SQL Concepts")


page1()




def topics():
    st.header("Structured Query Language")
    
    # Create a two-column layout
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("DDL - Data Definition Language")
        
        st.markdown(
            """
            ##### To read the entire content of a file:
            """
        )
        st.code(
            """
            with open('Tushar.txt', 'r') as file:
                content = file.read()
                print(content)
           
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("DML- Data Manipulation Language")
        
        st.markdown(
            """
            ##### To write text to a file, overwriting existing content:
            """
        )
        st.code(
            """
            with open('Tushar.txt', 'w') as file:
                content= file.write("www.tushar-aggarwal.com")
                print(content)
           
            """
        )
        
        
        
        
        st.subheader("DCL - Data Control Language")
        
        st.markdown(
            """
            ##### To add text to the end of an existing file:
            """
        )
        st.code(
            """
            with open('Tushar.txt', 'a') as file:
                content = file.write("\n https://www.linkedin.com/in/tusharaggarwalinseec/")
                print(content)
           
            """
        )
        
        
        st.subheader("TCL - Transaction Control Language")
        
        st.markdown(
            """
            ##### To read a file line by line into a list:
            """
        )
        st.code(
            """
            with open('Tushar.txt', 'r') as file:
                content = file.readlines()
                print(content)
           
            """
        )
        
        
        
        st.subheader("SELECT")
        
        st.markdown(
            """
            ##### To process each line in a file:
            """
        )
        st.code(
            """
            with open('Tushar.txt', 'a') as file:
                for line in file:
                    print(line.strip())
           
            """
        )
            
        
    with col2:
        st.subheader("FROM")
        
        st.markdown(
            """
            ##### To check if a file exists before performing file operations:
            """
        )
        st.code(
            """
            import os
            if os.path.exists("Tushar.txt"):
                print("File exists.")
            else:
                print("File does not exists.")
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("WHERE")
        
        st.markdown(
            """
            ##### To write each element of a list to a new line in a file:
            """
        )
        st.code(
            """
            lines = ['First line', 'Second line', 'Third line']
            with open("Tushar.txt","w") as file:
                for line in lines:
                    file.write(f'{file}\n')           
            """
        )
        
        
        
        
        st.subheader("GROUP BY")
        
        st.markdown(
            """
            ##### To work with multiple files simultaneously using `with` blocks:
            """
        )
        st.code(
            """
            with open("source.txt","r") as source,
                open("destination.txt","w") as destination
                
                content = source.read()
                destination.write(content)
            """
        )
        
        
        st.subheader("HAVING")
        
        st.markdown(
            """
            ##### To safely delete a file if it exists:
            """
        )
        st.code(
            """
            import os
            if os.path.exists("Tushar.txt"):
                os.remove("Tushar.txt")
                print("File deleted.")
            else:
                print("File does not exist.")
            """
        )
        
        
        
        st.subheader("ORDER BY")
        
        st.markdown(
            """
            ##### To read from and write to a file in binary mode (useful for images, videos,etc.):
            """
        )
        st.code(
            """
            # Reading a binary file
            with open('image.jpg','rb') as file:
                content = file.read()
            #Writing to a binary file
            with open('copy.jpg','wb') as file:
                file.write(content)
            """
        )
        
        
        
        
        st.subheader("Aggregation Functions")
        st.subheader("SUM(column_name)")
        st.subheader("COUNT()")
        st.subheader("COUNT(DISTINCT column_name)")
        st.subheader("MIN(column_name)")
        st.subheader("MAX(column_name)")
        st.subheader("ORDER BY")
        st.subheader("ORDER BY")
        st.subheader("ORDER BY")
        st.subheader("ORDER BY")
        st.subheader("ORDER BY")
        st.subheader("ORDER BY")
        st.subheader("ORDER BY")
        st.subheader("ORDER BY")
        st.subheader("ORDER BY")
        






























































