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

try:
    sql = 'select * from WORKSPACE_179647280."itesco_spotrebni_kos_vyvoj_v1"'
    cursor = conn.cursor()
    cursor.execute(sql)
    itescoKosDf = pd.DataFrame.from_records(
        iter(cursor), columns=[x[0]for x in cursor.description])
    cursor.close()
except Exception as e:
    print(e)

# rohlik_df -> products
itescoKosDf = pd.DataFrame(
    itescoKosDf[['nazev_hlavni_kategorie','date','basePrice']].groupby(['nazev_hlavni_kategorie','date']).sum('basePrice').reset_index())