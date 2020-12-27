# LIHOVINY
import dash_html_components as html
import dash_core_components as dcc

from db_connection import conn, select_data
from assets.graph_settings import graph_layout
from functions import generate_time_graph

table_name = "out_rohlik_spotrebni_kos_product_agg"
category = "csu_main_category"
name = 'Lihoviny'

sql = """
    SELECT * 
    FROM WORKSPACE_179647280."{}" 
    WHERE "{}" = '{}'
    ORDER BY "date"
"""
sql = sql.format(table_name,category,name)

df = select_data(conn,sql)
y = "csuRelevantPrice"
breakdown = "csu_product"
y_label = "Cena na jednotku"

fig = generate_time_graph(df,y,breakdown,graph_layout,y_label)

product = 'Lihoviny'

popisek = '''
Dopad zvýšené spotřební daně na lihoviny (konec ledna 2020).
Zdroj: rohlik.cz
'''

graph = html.Div(children = [
    html.H2("Vývoj ceny za jednotku"),
    dcc.Graph(id="showcase-graph-alcohol",
            figure=fig)
], className="graph-cell")