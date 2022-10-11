from dash import dcc
from dash import html

graph = html.Div(children=[
    html.H2("Kosik: ČSÚ hlavní kategorie"),
    dcc.Graph(id="kosik-main-cat-graph",
              figure={})
], className="graph-cell")
