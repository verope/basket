import dash_core_components as dcc
import dash_html_components as html

graph = html.Div(children = [
    html.H2("Rohlik: ČSÚ hlavní kategorie"),
    dcc.Graph(id="rohlik-main-cat-graph",
            figure={})
], className="graph-cell")