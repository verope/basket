import dash_core_components as dcc
import dash_html_components as html

graph = html.Div(children = [
    html.H2("iTesco: Cena spotřebního koše"),
    dcc.Graph(id="itesco-weighted-graph",
            figure={})
], className="graph-cell")