import dash_core_components as dcc
import dash_html_components as html

graph = html.Div(children = [
    html.H2("iTesco: ČSÚ hlavní kategorie"),
    dcc.Graph(id="itesco-main-cat-graph-agg",
            figure={})
], className="graph-cell")