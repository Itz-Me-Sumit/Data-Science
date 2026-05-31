#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import psycopg2
import json


# In[ ]:


def read_db_config(config_file="db_config.json"):
    try:
        with open(config_file , "r") as f:
            config=json.load(f)
            print(f"Database Config Loaded from file : {config_file}")
        return config
    except Exception as e:
        print(f"Error Occured while reading file : {config_file} , Error: {e}")


# In[ ]:


def connect_to_postgres(db_name , user , password , host , port):
    connection = None
    try:
        connection=psycopg2.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        print(f"Connection To postgreSQL DB({db_name}) successful")
        return connection

    except Exception as e:
        print(f"Error Occured While Creating Connection to DB {db_name}")
        return connection


# In[ ]:


db_config = read_db_config()
print(db_config)

DB_NAME = db_config.get("db_name")
USER = db_config.get("user")
PASSWORD = db_config.get("password")
HOST = db_config.get("host")
PORT = db_config.get("port")

if db_config:
    conn=connect_to_postgres(DB_NAME,USER,PASSWORD,HOST,PORT)
    print(conn)


# In[ ]:


def execute_query(conn,query,params=None):
    try:
        cursor = conn.cursor()
        cursor.execute(query , params)

        if query.upper().startswith(("INSERT","UPDATE","DELETE")):
            cursor.commit()
            return cursor.rowcount()
        else:
            return cursor.fetchall()
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Error Occured While Running Query , Error : {e}")
        return None
    finally:
        if cursor:
            cursor.close()


# In[ ]:


query = "SELECT * FROM Artist LIMIT 20;"


# In[ ]:


if conn:
    result = execute_query(conn , query)
    if result is None:
        print("Result set is empty")
    else:
        for id ,(artist_id , artist_name) in enumerate(result):
            print(f"{id}:-> Artist Id: {artist_id} | Artist Name: {artist_name}")

