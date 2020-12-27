# VEPROVE
import dash_html_components as html
import dash_core_components as dcc

from db_connection import conn, select_data
from assets.graph_settings import graph_layout
from functions import generate_time_graph

table_name = "out_rohlik_spotrebni_kos_sub_cat_agg"
category = "csu_subcategory"
name = 'Vepřové maso'

sql = """
    SELECT * 
    FROM WORKSPACE_179647280."{}" 
    WHERE "{}" = '{}'
    ORDER BY "date"
"""
sql = sql.format(table_name,category,name)

df = select_data(conn,sql)
y = "csuRelevantPrice"
breakdown = "csu_subcategory"
y_label = "Cena na jednotku"

fig = generate_time_graph(df,y,breakdown,graph_layout,y_label)

product = 'Vepřové maso'

popisek = '''
Vývoj vepřového masa byl hned několikrát ovlivněn prasečím morem — poprvé v listopadu 2019, kdy se začal šířit africký mor v Číně, odkud pochází polovina světové produkce. Následně v září 2020, kdy se africký mor rozjel v Německu a odbyt z Německa mimo EU se snížil, což na Evropském trhu způsobilo přebytek.
Zdroj: rohlik.cz
'''

graph = html.Div(children = [
    html.H2("Vývoj ceny za jednotku"),
    dcc.Graph(id="showcase-graph-pork",
            figure=fig)
], className="graph-cell")