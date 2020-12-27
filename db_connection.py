#!/usr/local/bin/python

import os
import snowflake.connector
import pandas as pd
import pyarrow

# !!! FOR LOCAL ENVIRONMENT
# from dotenv import load_dotenv
# load_dotenv('config.env')

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

def select_data(conn,sql):
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

# DATA LOAD


##################
# SHOWCASES
##################

# OKURKY
try:
    sql = 'select * from WORKSPACE_179647280."out_rohlik_spotrebni_kos_item_agg" WHERE "csu_product" = \'Okurky salátové\''
    cursor = conn.cursor()
    cursor.execute(sql)
    okurkyDf = pd.DataFrame.from_records(
        iter(cursor), columns=[x[0]for x in cursor.description])
    cursor.close()
except Exception as e:
    print(e)

# KVETAK
try:
    sql = 'select * from WORKSPACE_179647280."out_rohlik_spotrebni_kos_item_agg" WHERE "csu_product" = \'Květák bílý celý\''
    cursor = conn.cursor()
    cursor.execute(sql)
    kvetakDf = pd.DataFrame.from_records(
        iter(cursor), columns=[x[0]for x in cursor.description])
    cursor.close()
except Exception as e:
    print(e)

# LIHOVINY
try:
    sql = 'SELECT * FROM "out_rohlik_spotrebni_kos_product_agg" WHERE "csu_main_category" = \'Lihoviny\''
    cursor = conn.cursor()
    cursor.execute(sql)
    lihovinyDf = pd.DataFrame.from_records(
        iter(cursor), columns=[x[0]for x in cursor.description])
    cursor.close()
except Exception as e:
    print(e)

# VEPROVY
try:
    sql = 'SELECT * FROM "out_rohlik_spotrebni_kos_sub_cat_agg" WHERE "csu_subcategory" = \'Vepřové maso\''
    cursor = conn.cursor()
    cursor.execute(sql)
    veprDf = pd.DataFrame.from_records(
        iter(cursor), columns=[x[0]for x in cursor.description]).sort_values(by='date')
    cursor.close()
except Exception as e:
    print(e)
