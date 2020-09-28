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
    sql = 'select * from WORKSPACE_179647280."rohlik_test"'
    cursor = conn.cursor()
    cursor.execute(sql)
    rohlik_df = pd.DataFrame.from_records(
        iter(cursor), columns=[x[0]for x in cursor.description])
    cursor.close()
except Exception as e:
    print(e)

"""
try:
    sql = 'select * from WORKSPACE_179645670."nazara_gameplays_agg"'
    cursor = conn.cursor()
    cursor.execute(sql)
    nazara_activity_df = pd.DataFrame.from_records(
        iter(cursor), columns=[x[0]for x in cursor.description])
    cursor.close()
except Exception as e:
    print(e)


try:
    sql = 'select * from WORKSPACE_5841."nazara_vip_users"'
    cursor = conn.cursor()
    cursor.execute(sql)
    nazara_vip_users_df = pd.DataFrame.from_records(
        iter(cursor), columns=[x[0]for x in cursor.description])
    cursor.close()
except Exception as e:
    print(e)

try:
    sql = 'select * from WORKSPACE_5841."nazara_subscribed_users_cum"'
    cursor = conn.cursor()
    cursor.execute(sql)
    subscriptions_cum_df = pd.DataFrame.from_records(
        iter(cursor), columns=[x[0]for x in cursor.description])
    cursor.close()
except Exception as e:
    print(e)

try:
    sql='select * from WORKSPACE_5841."nazara_retention_all_users_fin"'
    cursor=conn.cursor()
    cursor.execute(sql)
    retention_df = pd.DataFrame.from_records(
        iter(cursor),columns=[x[0]for x in cursor.description])
    cursor.close()
except Exception as e:
    print(e)

try:
    sql='select * from WORKSPACE_5841."nazara_utm_registrations"'
    cursor=conn.cursor()
    cursor.execute(sql)
    utm_regs_df = pd.DataFrame.from_records(
        iter(cursor),columns=[x[0]for x in cursor.description])
    cursor.close()
except Exception as e:
    print(e)

try:
    sql='select * from WORKSPACE_5841."nazara_gems_agg"'
    cursor=conn.cursor()
    cursor.execute(sql)
    gems_df = pd.DataFrame.from_records(
        iter(cursor),columns=[x[0]for x in cursor.description])
    cursor.close()
except Exception as e:
    print(e)

try:
    sql = '''select t1."created"::date as "date", t1.*, 
                    case when t2."toCurrency" is null and t1."currency" = 'USD' then t1."currency_amount"
                         else t1."currency_amount"/t2."rate"
                    end as "usd_only",
                    "usd_only"*t3."usd_to_inr" as "inr_only"
    from (select "id", "user_id", "gems_amount", "currency_amount", "currency", "currency_symbol", "currency_convert_rate", "created" 
          from keboola_19.WORKSPACE_5841."nazara_withdraw_history"
          where "status"='active') t1
    left join keboola_19.WORKSPACE_5841."rates_usd" t2
    on t1."currency"=t2."toCurrency"
    and t1."created"::date=t2."date"
    left join (select "date", "rate" as "usd_to_inr" 
               from keboola_19.WORKSPACE_5841."rates_usd"
               where "toCurrency"='INR') t3
    on t1."created"::date=t3."date"'''
    cursor=conn.cursor()
    cursor.execute(sql)
    withdraw_df = pd.DataFrame.from_records(
        iter(cursor),columns=[x[0]for x in cursor.description])
    cursor.close()
except Exception as e:
    print(e) 

try:
    sql='select *, "start_time"::date as "start_date" from WORKSPACE_5841."nazara_premium_battles"'
    cursor=conn.cursor()
    cursor.execute(sql)
    battles_df = pd.DataFrame.from_records(
        iter(cursor),columns=[x[0]for x in cursor.description])
    cursor.close()
except Exception as e:
    print(e)
"""


# rohlik_df -> products
rohlik_by_date = pd.DataFrame(
    rohlik_df[['p_key', 'date']].groupby('date').count().sort_values('date'))

"""
# activity
nazara_activity_df_users = pd.DataFrame(nazara_activity_df[[
                                        'date', 'type', 'users']]).groupby(['date', 'type']).sum().reset_index()
nazara_activity_df_users.sort_values(by=['date', 'type'], inplace=True)

# VIP users -> new activations daily
nazara_vip_users_df['date'] = nazara_vip_users_df['min_created_at'].apply(
    lambda x: x.date())
activations = pd.DataFrame(nazara_vip_users_df.groupby(
    'date')['user_id'].nunique()).sort_values('date')

# Subscriptions cumulative
subscriptions_cum_df.sort_values(by='date', inplace=True)

# retention graph
retention_df['retention'] = retention_df['players']/retention_df['players0']
retention_df.sort_values(by=['min_date','day'], inplace=True)
retention_df = retention_df[retention_df['day'] != 0]

# utm campaigns
utm_regs_table_df = utm_regs_df.groupby(['registration_date','utm_source', 'utm_campaign']).sum().reset_index()
utm_regs_df = utm_regs_df[['registration_date','utm_campaign','users']].groupby(['registration_date', 'utm_campaign']).sum().reset_index()
utm_regs_df.sort_values(by='registration_date', inplace=True)

# gems
gems_df.sort_values(by='date', inplace=True)

# withdrawal history
withdraw_by_date = withdraw_df.groupby(by='date').agg({'user_id': 'nunique', 'usd_only': 'sum', 'inr_only': 'sum'}).sort_values(by='date')

# premium battles
battles_df['length'] = battles_df.apply(lambda row: (row.end_time - row.start_time).seconds, axis=1)

def human_format(seconds):
    if seconds == 1:
        return "1 seconds"
    elif seconds < 60:
        return str(seconds) + " seconds"
    elif (seconds == 60):
        return "1 minute"
    elif (seconds > 60 and seconds < (60*60)):
        return str(round(seconds/60)) + " minutes"
    elif (seconds == 60*60):
        return "1 hour"
    elif (seconds > 60*60 and seconds < 24*60*60):
        return str(round(seconds/(60*60))) + " hours"
    elif seconds == 24*60*60:
        return "1 day"
    elif seconds > 24*60*60:
        return str(round(seconds/(24*60*60))) + " days"
    else:
        return "N/A"

battles_df['length_hf'] = battles_df['length'].apply(lambda x: human_format(x))
"""