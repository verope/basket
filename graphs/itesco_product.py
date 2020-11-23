import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px

from db_connection import itescoMainCatDf_agg as df
# the chart will be based on main categories

graph = html.Div(children = [
    html.H2("ČSÚ produkt: vývoj ceny koše"),
    dcc.Graph(id="csu-product-graph",figure={})
])