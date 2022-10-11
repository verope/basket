#!/usr/local/bin/python

import os
import snowflake.connector
import pandas as pd
import pyarrow

# !!! FOR LOCAL ENVIRONMENT
from dotenv import load_dotenv
load_dotenv('config.env')

DATABASE = os.getenv('DATABASE')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
DB_USER = os.getenv('DB_USER')
SCHEMA = os.getenv('SCHEMA')
WAREHOUSE = os.getenv('WAREHOUSE')
ACCOUNT = os.getenv('ACCOUNT')

conn = snowflake.connector.connect(
    user=DB_USER,
    password=PASSWORD,
    account=ACCOUNT,
    warehouse=WAREHOUSE,
    database=DATABASE,
    schema=SCHEMA
)


def select_data(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        df = pd.DataFrame.from_records(
            iter(cursor), columns=[x[0]for x in cursor.description]
        )
        cursor.close()
        return df
    except Exception as e:
        return e
