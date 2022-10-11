from dash import dcc
from dash import html

graph = html.Div(children=[
    html.H2("iTesco: Cena spotřebního koše"),
    dcc.Graph(id="itesco-weighted-graph",
              figure={})
], className="graph-cell")
