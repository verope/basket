from dash import dcc
from dash import html

graph = html.Div(children=[
    html.H2("Rohlik: Cena spotřebního koše"),
    dcc.Graph(id="rohlik-weighted-graph",
              figure={})
], className="graph-cell")
