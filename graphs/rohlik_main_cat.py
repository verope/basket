from dash import dcc
from dash import html

graph = html.Div(children=[
    html.H2("Rohlik: ČSÚ hlavní kategorie"),
    dcc.Graph(id="rohlik-main-cat-graph",
              figure={})
], className="graph-cell")
