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

# DATA LOAD

try:
    sql = 'select * from WORKSPACE_179647280."itesco_spotrebni_kos_vazena_suma"'
    cursor = conn.cursor()
    cursor.execute(sql)
    itescoWeightedDf = pd.DataFrame.from_records(
        iter(cursor), columns=[x[0]for x in cursor.description])
    cursor.close()
except Exception as e:
    print(e)

try:
    sql = 'select * from WORKSPACE_179647280."out_itesco_spotrebni_kos_sub_cat_agg"'
    cursor = conn.cursor()
    cursor.execute(sql)
    itescoSubCatDf = pd.DataFrame.from_records(
        iter(cursor), columns=[x[0]for x in cursor.description])
    cursor.close()
except Exception as e:
    print(e)

try:
    sql = 'select * from WORKSPACE_179647280."out_itesco_spotrebni_kos_main_cat_agg"'
    cursor = conn.cursor()
    cursor.execute(sql)
    itescoMainCatDf_agg = pd.DataFrame.from_records(
        iter(cursor), columns=[x[0]for x in cursor.description]).sort_values(by='date')
    cursor.close()
except Exception as e:
    print(e)

try:
    sql = 'select * from WORKSPACE_179647280."out_itesco_spotrebni_kos_product_agg"'
    cursor = conn.cursor()
    cursor.execute(sql)
    itescoProductDf = pd.DataFrame.from_records(
        iter(cursor), columns=[x[0]for x in cursor.description])
    cursor.close()
except Exception as e:
    print(e)


# DATA TRANSFORMATIONS

# itescoWeightedDf
itescoWeighted_s = itescoWeightedDf[['date','vazena_suma']].sort_values(by='date')