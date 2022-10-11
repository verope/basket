# OKURKA HADOVKA
from dash import html
from dash import dcc
import plotly.express as px

from db_connection import conn, select_data
from assets.graph_settings import graph_layout
from functions import generate_time_graph

table_name = "out_rohlik_spotrebni_kos_item_agg"
product_name = "Okurky salátové"

sql = """
    SELECT * 
    FROM WORKSPACE_179647280."{}" 
    WHERE "csu_product" = '{}'
    ORDER BY "date"
"""
sql = sql.format(table_name, product_name)

df = select_data(conn, sql)
y = "csuRelevantPrice"
breakdown = "itemName"
y_label = "Cena na jednotku"

fig = generate_time_graph(df, y, breakdown, graph_layout, y_label)

product = 'Okurky salátové'

popisek = '''
Sledovaly jsme také vývoj cen u konkrétních produktů v návaznosti na světové události, které by na jejich ceny mohly mít vliv. Například jsme tak zjistily, že cena okurek, které se k nám dováží ze Španělska, stoupla v únoru, což odpovídá době kdy se Španělskem prohnala bouřka Glorie, která poničila velkou část úrody. 
Zdroj: rohlik.cz
'''

graph = html.Div(children=[
    html.H2("Vývoj ceny za jednotku"),
    dcc.Graph(id="showcase-graph-cucumber",
              figure=fig)
], className="graph-cell")
