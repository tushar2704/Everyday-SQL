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
from src.Everyday_SQL.components.elements import *
#######################################################################################################
#Body of Everyday_SQL by github.com/tushar2704
#######################################################################################################

def sql():
    # D:\QueryMaster-priv\src\QueryMaster\SQL.mp4
    st.markdown('''#### SQL Overview''')
    path=os.path.join('src', 'Everyday_SQL', 'style','SQL.gif')
    st.image(path)

def topics():
    
    
    terms()
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
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
            
            
            
        
    
    
    
    with col2:
        st.subheader("DML- Data Manipulation Language")
        
        st.text(
            """
            The SQL commands that deal with the manipulation of data present in the database 
            belong to DML or Data Manipulation Language and this includes most of the SQL statements. 
            It is the component of the SQL statement that controls access to data and to the database. 
            Basically, DCL statements are grouped with DML statements.
            """
        )
        if st.toggle("Show DML Commands"):
            st.code( 
                    """
                    INSERT: It is used to insert data into a table.
                    UPDATE: It is used to update existing data within a table.
                    DELETE: It is used to delete records from a database table.
                    LOCK: Table control concurrency.
                    CALL: Call a PL/SQL or JAVA subprogram.
                    EXPLAIN PLAN: It describes the access path to data.
                    """, language="markdown")
            
            
            
        st.subheader("DCL - Data Control Language")
        
        st.text(
            """
            DCL includes commands such as GRANT and REVOKE which mainly deal with the rights, 
            permissions, and other controls of the database system. 
            """
        )
        if st.toggle("Show DCL Commands"):
            st.code( 
                    """
                    GRANT: This command gives users access privileges to the database.
                    # Syntax:
                    GRANT SELECT, UPDATE ON MY_TABLE TO SOME_USER, ANOTHER_USER;
                    
                    REVOKE: This command withdraws the user’s access privileges given 
                    by using the GRANT command.
                    # Syntax:
                    REVOKE SELECT, UPDATE ON MY_TABLE FROM USER1, USER2;  
                    
                    """, language="markdown")
        
        
        st.subheader("TCL - Transaction Control Language")
        
        
        
        st.text(
            """
            Transactions group a set of tasks into a single execution unit. 
            Each transaction begins with a specific task and ends when all the 
            tasks in the group are successfully completed. If any of the tasks fail, 
            the transaction fails. 
            Therefore, a transaction has only two results: success or failure. 
            """
        )
        if st.toggle("Show TCL Commands"):
            st.code( 
                    """
                    BEGIN: Opens a Transaction.
                    # Syntax:
                    COMMIT;  
                    
                    ROLLBACK: Rollbacks a transaction in case of any error occurs.
                    # Syntax:
                    ROLLBACK;   
                    
                    SAVEPOINT: Sets a save point within a transaction.
                    # Syntax:
                    SAVEPOINT SAVEPOINT_NAME;  
                    
                    """, language="markdown")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    st.divider()
    
    ###########################################################################################
    # Basics to Advanced Commands
    ###########################################################################################
    
    
    st.subheader("SQL - Beginner SQL Syntax")
    st.divider()
    
    col3, col4 = st.columns([0.5, 0.5], gap="small")
    
    with col3:
        st.subheader("SELECT")
        st.text("""The SELECT statement is used to select columns in a database. 
                It defines the data you want to retrieve from one or more tables""")
        
        st.code(
            """
            /*Example usage:*/
            SELECT 
                column_name1,
                column_name2,
                column_name3
            FROM
                table_name;
            """, language="sql"
        )
                
            
        
        st.subheader("FROM")
        
        st.text("""The FROM clause specifies the table from which to pull the data.  
                It's used in conjunction with SELECT to define the source of the data.""")
        
        st.code(
            """
            /*Example usage:*/
            SELECT 
                column_name1,
                column_name2,
                column_name3
            FROM 
                table_name;
            """, language="sql"
        )
        
        
        
        
        st.subheader("WHERE")
        
        st.text("""Use the WHERE clause to filter the data based on specific conditions. 
                It helps in narrowing down the data to only those rows that meet the criteria.""")
        
        st.code(
            """
            /*Example usage:*/
            SELECT column_name
            FROM table_name
            WHERE date >= ‘2023-01-01’
            """, language="sql"
        )
        
    
    
    with col4:
        st.subheader("GROUP BY")
        
        st.text("""The GROUP BY statement groups rows that have the same values in specified columns. 
                It's often used with aggregate functions (COUNT, MAX, MIN, SUM, AVG) 
                to group the resultset by one or more columns""")
        
        st.code(
            """
            /*Example usage:*/
            SELECT 
                column_name, 
                COUNT(*) 
            FROM table_name 
            GROUP BY column_name;
            """, language="sql"
        )
        
        
        st.subheader("HAVING")
        
        st.text("""The HAVING clause is used to filter groups created by the GROUP BY clause. 
                It's like a WHERE clause, but for groups.""")
        
        st.code(
            """
            /*Example usage:*/
            SELECT 
                column_name, 
                COUNT(*)
            FROM table_name
            GROUP BY column_name
            HAVING COUNT(*) > 1;
            """, language="sql"
        )
        
        
        st.subheader("ORDER BY")
        
        st.text("""Use ORDER BY to sort the result set in either ascending or descending order.
                It specifies the order in which the rows appear in the resultset.""")
        
        st.code(
            """
            /*Example usage:*/
            SELECT 
                column_name1,
                column_name2,
                column_name3,
            FROM table_name
            ORDER BY column_name3 DESC;
            """, language="sql"
        )
        
        
    ##########
    #Aggregation Functions
    #########
    st.divider() 
     
    st.subheader("Aggregation Functions")
    
    st.divider()
    
    
    
    col5, col6 = st.columns([0.5, 0.5], gap="small")
    
    with col5:
        st.subheader("SUM(column_name)")
        st.text("""The SUM function calculates the total sum of a numeric column. 
                It adds up all the values in the specified column.""")
        
        st.code(
            """
            /*Example usage:*/
            SELECT SUM(column_name)
            FROM table_name;
            """, language="sql"
        )
                
            
        
        st.subheader("COUNT()")
        
        st.text("""The COUNT function returns the number of rows that matches a specified criterion.   
                   COUNT() counts all rows in a table.""")
        
        st.code(
            """
            /*Example usage:*/
            SELECT COUNT(*)
            FROM table_name;
            """, language="sql"
        )
        
        
        
        
        st.subheader("COUNT(DISTINCT column_name)")
        
        st.text("""This variant of the COUNT function counts the number of distinct (unique) values in a column. """)
        
        st.code(
            """
            /*Example usage:*/
            SELECT COUNT(DISTINCT column_name)
            FROM table_name;
            """, language="sql"
        )
        
    
    
    with col6:
        st.subheader("AVG(column_name)")
        
        st.text("""The AVG function returns the average value of a numeric column.  
                It calculates the sum of the values and divides it by the number of values.""")
        
        st.code(
            """
            /*Example usage:*/
            SELECT AVG(column_name) 
            FROM table_name;
            """, language="sql"
        )
        
        
        st.subheader("MIN(column_name)")
        
        st.text("""The MIN function returns the smallest value of the selected column. 
                It's useful for finding the lowest number, earliest date, etc.""")
        
        st.code(
            """
            /*Example usage:*/
            SELECT MIN(column_name) 
            FROM table_name;
            """, language="sql"
        )
        
        
        st.subheader("MAX(column_name)")
        
        st.text("""The MAX function returns the largest value of the selected column,
                which is helpful for identifying the highest number, latest date, and so on.""")
        
        st.code(
            """
            /*Example usage:*/
            SELECT MAX(column_name)
            FROM table_name;
            """, language="sql"
        )
        
    ##########
    #Intermediate SQL Concepts
    #########
    st.divider() 
     
    st.subheader("Intermediate SQL Concepts")
    
    st.divider()
    
    
    
    col7, col8 = st.columns([0.5, 0.5], gap="small")
    
    with col7:
        st.subheader("LIKE")
        st.text("""The LIKE operator is used to search for a specified pattern in a column. 
                It's often used in a WHERE clause.""")
        
        st.code(
            """
            /*Example usage:*/
            SELECT *
            FROM table_name
            WHERE column_name LIKE ‘%thequery%’;
            """, language="sql"
        )
                
            
        
        st.subheader("AND")
        
        st.text("""The AND operator combines two or more conditions in a WHERE clause. 
                It returns rows where all the conditions are true.""")
        
        st.code(
            """
            /*Example usage:*/
            SELECT  
            FROM table_name 
            WHERE condition1 
                AND condition2;
            """, language="sql"
        )
        
        
        
        
        st.subheader("COUNT(DISTINCT column_name)")
        
        st.text("""This variant of the COUNT function counts the number of distinct (unique) values in a column. """)
        
        st.code(
            """
            /*Example usage:*/
            SELECT COUNT(DISTINCT column_name)
            FROM table_name;
            """, language="sql"
        )
        
        st.subheader("BETWEEN")
        
        st.text("""The BETWEEN operator selects values within a given range.  
                It's used in a WHERE clause for filtering.""")
        
        st.code(
            """
            /*Example usage:*/
            SELECT  
            FROM table_name 
            WHERE column_name 
            BETWEEN value1 AND value2;
            """, language="sql"
        )
        
        st.subheader("COALESCE")
        
        st.text("""The COALESCE function returns the first nonnull value in a list of arguments.  
                It's useful for handling NULL values.""")
        
        st.code(
            """
            /*Example usage:*/
            SELECT 
                COALESCE(column1, column2, ...) 
            FROM table_name;
            """, language="sql"
        )
        
    
    
    with col8:
        st.subheader("OR")
        
        st.text("""The OR operator is used in a WHERE clause to combine conditions.   
                It returns rows where any of the conditions are true.""")
        
        st.code(
            """
            /*Example usage:*/
            SELECT  
            FROM table_name 
            WHERE condition1 
                OR condition2;
            """, language="sql"
        )
        
        
        st.subheader("CASE WHEN")
        
        st.text("""The CASE WHEN statement provides if then else logic within SQL. 
                It's used for conditional expressions.""")
        
        st.code(
            """
            /*Example usage:*/
            SELECT 
                CASE WHEN condition THEN result
                    ELSE alternative END 
            FROM table_name;
            """, language="sql"
        )
        
        
        st.subheader("IN")
        
        st.text("""The IN operator allows you to specify multiple values in a WHERE clause. 
                It's useful for filtering by a list of items.""")
        
        st.code(
            """
            /*Example usage:*/
            SELECT  
            FROM table_name 
            WHERE column_name IN (value1, value2, ...);
            """, language="sql"
        )
        
        st.subheader("UNION ALL")
        
        st.text("""The UNION ALL operator is used to combine the resultset of two or more SELECT statements.  
                It includes all duplicates.""")
        
        st.code(
            """
            /*Example usage:*/
            SELECT column_name 
            FROM table1 
            UNION ALL 
            SELECT column_name 
            FROM table2;
            """, language="sql"
        )

        
        st.subheader("CAST")
        
        st.text("""The CAST function converts one data type into another.  
                It's used for type conversion in queries.""")
        
        st.code(
            """
            /*Example usage:*/
            SELECT 
                CAST(column_name AS data_type) 
            FROM table_name;
            """, language="sql"
        )
    
    
    
    
    
    
    
    ##########
    #Intermediate SQL Concepts
    #########
    st.divider() 
     
    st.subheader("Advanced SQL Concepts")
    
    st.divider()
    
    
    
    col7, col8 = st.columns([0.5, 0.5], gap="small")
    
    with col7:
        st.subheader("CTEs (Common Table Expressions)")
        st.text("""CTEs, or Common Table Expressions, provide a way to write cleaner 
                and more readable SQL. They allow you to define a temporary result set 
                which you can then reference within your SELECT, INSERT, UPDATE, or DELETE queries.""")
        
        st.code(
            """
            /*Example usage:*/
            WITH cte_name AS (
                SELECT *
                FROM table_name
                ) SELECT * 
            FROM cte_name;
            """, language="sql"
        )
                
            
        
        st.subheader("SUBQUERIES")
        
        st.text("""Subqueries are nested queries within a larger query. 
                They're used to perform operations in a sequence and can be found
                within SELECT, INSERT, UPDATE, or DELETE statements, often 
                in a WHERE or HAVING clause.""")
        
        st.code(
            """
            /*Example usage:*/
            SELECT *
            FROM table_name 
            WHERE column_name IN (
                SELECT column_name 
                FROM another_table
            );
            """, language="sql"
        )
        
        
        
        
        
        
        
        
    
    
    with col8:
        st.subheader("WINDOW FUNCTIONS")
        
        st.text("""Window Functions perform calculations across a set 
                of table rows that are somehow related to the current row.
                They provide powerful tools for data analysis, such as 
                running totals, moving averages, and cumulative counts.""")
        
        st.code(
            """
            /*Example usage:*/
            SELECT SUM() OVER (ORDER BY column_name) as running_total
            FROM table_name;
            """, language="sql"
        )
    
    
    
    
    
    ##########
    #Joins Concepts
    #########
    st.divider() 
     
    st.subheader("Joins")
    
    st.divider()
    
    # st.subheader("SUM(column_name)")
    # st.subheader("COUNT()")
    # st.subheader("COUNT(DISTINCT column_name)")
    # st.subheader("MIN(column_name)")
    # st.subheader("MAX(column_name)")
    # st.subheader("Intermediate SQL Concepts")
    # st.subheader("LIKE")
    # st.subheader("AND")
    # st.subheader("OR")
    # st.subheader("CASE WHEN")
    # st.subheader("IN")
    # st.subheader("UNION ALL")
    # st.subheader("BETWEEN")
    # st.subheader("ORDER BY")
    # st.subheader("CAST")
    # st.subheader("COALESCE")
    # st.subheader("Advanced SQL Concepts")
    # st.subheader("CTEs (Common Table Expressions)")
    # st.subheader("SUBQUERIES")
    # st.subheader("WINDOW FUNCTIONS")
    # st.subheader("Joins")
    # st.subheader("INNER JOIN")
    # st.subheader("LEFT JOIN (or LEFT OUTER JOIN)")
    # st.subheader("FULL JOIN (or FULL OUTER JOIN)")
    # st.subheader("Rank Functions")
    # st.subheader("ROW_NUMBER:")
    # st.subheader("RANK")
    # st.subheader("DENSE_RANK:")
    # st.subheader("Example SQL Patterns")
    # st.subheader("Select Columns Filtered on Criteria")
    # st.subheader("Explore Column Values")
    # st.subheader("Common Aggregations")
    # st.subheader("Research Duplicates with a Subquery")
    # st.subheader("If/Then Logic")
    # st.subheader("Joins")
    # st.subheader("Unions")
    # st.subheader("Change Data Type of Column")
    # st.subheader("Handle Nulls with Coalesce")
    # st.subheader("CTEs")
    # st.subheader("Window Functions")
        
        
        































































