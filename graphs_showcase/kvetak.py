# KVETAK
from dash import html
from dash import dcc
from db_connection import conn, select_data
from assets.graph_settings import graph_layout
from functions import generate_time_graph

table_name = "out_rohlik_spotrebni_kos_item_agg"
category = "csu_product"
name = 'Květák bílý celý'

sql = """
    SELECT * 
    FROM WORKSPACE_179647280."{}" 
    WHERE "{}" = '{}'
    ORDER BY "date"
"""
sql = sql.format(table_name, category, name)

df = select_data(conn, sql)
y = "csuRelevantPrice"
breakdown = "itemName"
y_label = "Cena na jednotku"

fig = generate_time_graph(df, y, breakdown, graph_layout, y_label)

popisek = '''
Dále jsme zjistily, že během první vlny koronakrize vzrostla cena květáku. To může být způsobeno tím, že květák se dováží z Francie, do které se kvůli protipandemickým opatřením nemohli dostat zahraniční pracovníci provádějící sklizeň. Stoupla tak cena za práci při sklizni a v důsledku stouply i ceny květáku.
Zdroj: rohlik.cz
'''
product = 'Květák bílý celý'

graph = html.Div(children=[
    html.H2("Vývoj ceny za jednotku"),
    dcc.Graph(id="showcase-graph-cauliflower",
              figure=fig)
], className="graph-cell")
