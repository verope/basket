from dash import dcc
from dash import html

graph = html.Div(children=[
    html.H2("Kosik: Cena spotřebního koše"),
    dcc.Graph(id="kosik-weighted-graph",
              figure={})
], className="graph-cell")
