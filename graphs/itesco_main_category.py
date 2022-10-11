from dash import dcc
from dash import html

graph = html.Div(children=[
    html.H2("iTesco: ČSÚ hlavní kategorie"),
    dcc.Graph(id="itesco-main-cat-graph-agg",
              figure={})
], className="graph-cell")
