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

#######################################################################################################
#Pages(1) of Everyday_SQL by github.com/tushar2704
#######################################################################################################




#Sidebar Pages
with st.sidebar:
    logo()
    st.page_link("Home.py", label="Back to Home", icon="🏠")





def topics():
    st.header("Structured Query Language")
    st.text("""
            Structured Query Language is a domain-specific language used to manage data, 
            especially in a relational database management system. 
            It is particularly useful in handling structured data, i.e., 
            data incorporating relations among entities and variables.
            """
            )
    
    
    # col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    
    st.subheader("DDL - Data Definition Language")
    
    st.text(
        """
        Data Definition Language actually consists of the SQL commands that 
        can be used to define the database schema.
        It simply deals with descriptions of the database schema and is used 
        to create and modify the structure of database objects in the database. 
        DDL is a set of SQL commands used to create, modify, and delete database 
        structures but not data. 
        These commands are normally not used by a general user, who should be 
        accessing the database via an application. 
        """
    )
    if st.toggle("Show DDL Commands"):
        st.code( 
                """
                CREATE: This command is used to create the database or its objects (like table, index, function, views, store procedure, and triggers).
                DROP: This command is used to delete objects from the database.
                ALTER: This is used to alter the structure of the database.
                TRUNCATE: This is used to remove all records from a table, including all spaces allocated for the records are removed.
                COMMENT: This is used to add comments to the data dictionary.
                RENAME: This is used to rename an object existing in the database.
                
                """, language="markdown")
    
    # if st.toggle("Show `st.write` sample output"):
    #     st.write("Did you know I have more then 101 Supreme apps like this?")
    
    st.subheader("DQL (Data Query Language)")
    
    st.text(
        """
        DQL statements are used for performing queries on the data within schema objects. 
        The purpose of the DQL Command is to get some schema relation based on the query passed to it. 
        We can define DQL as follows it is a component of SQL statement that allows getting data from 
        the database and imposing order upon it. It includes the SELECT statement. 
        This command allows getting the data out of the database to perform operations with it. 
        When a SELECT is fired against a table or tables the result is compiled into a 
        further temporary table, which is displayed or perhaps received by the program i.e. a front-end.
        """
    )
    if st.toggle("Show DQL Commands"):
        st.code( 
                """
                SELECT: It is used to retrieve data from the database.
                """, language="markdown")
        
        
        
    st.subheader("DML- Data Manipulation Language")
    
    st.markdown(
        """
        ##### 
        """
    )
    st.code(
        """
        
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
    
    
    st.subheader("SQL - Beginner SQL Syntax")
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
    st.subheader("Intermediate SQL Concepts")
    st.subheader("LIKE")
    st.subheader("AND")
    st.subheader("OR")
    st.subheader("CASE WHEN")
    st.subheader("IN")
    st.subheader("UNION ALL")
    st.subheader("BETWEEN")
    st.subheader("ORDER BY")
    st.subheader("CAST")
    st.subheader("COALESCE")
    st.subheader("Advanced SQL Concepts")
    st.subheader("CTEs (Common Table Expressions)")
    st.subheader("SUBQUERIES")
    st.subheader("WINDOW FUNCTIONS")
    st.subheader("Joins")
    st.subheader("INNER JOIN")
    st.subheader("LEFT JOIN (or LEFT OUTER JOIN)")
    st.subheader("FULL JOIN (or FULL OUTER JOIN)")
    st.subheader("Rank Functions")
    st.subheader("ROW_NUMBER:")
    st.subheader("RANK")
    st.subheader("DENSE_RANK:")
    st.subheader("Example SQL Patterns")
    st.subheader("Select Columns Filtered on Criteria")
    st.subheader("Explore Column Values")
    st.subheader("Common Aggregations")
    st.subheader("Research Duplicates with a Subquery")
    st.subheader("If/Then Logic")
    st.subheader("Joins")
    st.subheader("Unions")
    st.subheader("Change Data Type of Column")
    st.subheader("Handle Nulls with Coalesce")
    st.subheader("CTEs")
    st.subheader("Window Functions")
        
        
        































































topics()
#######################################################################################################
#Pages(2) of Everyday_SQL by github.com/tushar2704
#######################################################################################################