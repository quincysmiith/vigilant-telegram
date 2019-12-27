import pandas as pd
import sqlite3
import os

def query_result_stats(query, database_name):
    
    # connect to database
    conn = sqlite3.connect(os.path.join('Exercise Files', 'db', database_name))
    
    # perform query
    data = pd.read_sql_query(query, conn)
    
    row_num = len(data)
    col_num = len(data.columns)
    
    print("### Query Summary ###")
    print()
    print("DATABASE QUERIED: {}".format(database_name))
    print("QUERY: ||| {} |||".format(query))
    print()
    print("There are {} rows in the query results table".format(row_num))
    print("There are {} columns in the query results table".format(col_num))
    print()
    print("First 5 rows of the query results:")
    print(data.head())
    
    # close database connection
    conn.close()
    
    return None

    
def perform_insert_and_stats(query, database_name):
    
    # connect to database
    conn = sqlite3.connect(os.path.join('Exercise Files', 'db', database_name))
    
    # perform insert    
    conn.execute(query)
    conn.commit()

    print("### Query Summary ###")
    print()
    print("DATABASE QUERIED: {}".format(database_name))
    print("QUERY: ||| {} |||".format(query))

    # close database connection
    conn.close()
    
    return None