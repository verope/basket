import sys
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

sys.path.append("..") # Adds higher directory to python modules path.

from app import app
from layout.navbar import navbar

import graphs_showcase.okurky as graph1
import graphs_showcase.kvetak as graph2
import graphs_showcase.lihoviny as graph3
import graphs_showcase.vepr as graph4

# product
# popisek

arr = [graph1, graph2, graph3, graph4]

def renderGraphs(data):
    return html.Div([
        html.Div(data.graph, className="showcase__graph-cell"),
        html.Div([
            html.H3(data.product,className="showcase__graph-content-heading"),
            html.P(data.popisek,className="showcase__graph-content-desc"),
        ], className="showcase__graph-content"),
    ],className="showcase__graph-container")


#   return 
graphs = map(renderGraphs, arr)
graph_list = list(graphs)

layout = html.Div([
    navbar,
    html.H1('Ukázky vlivu světových událostí na vývoj cen potravin', className="showcase__heading"),
    graph_list[0],
    graph_list[1],
    graph_list[2],
    graph_list[3]
], className="layout-content__container")

# children = [graph_list], 

# layout = html.Div(
#     [
#         navbar,
#         html.H1('showcase copy', className="showcase-heading"),
#         html.Div([
#             html.H1('Analýza spotřebního koše z online potravinových e-shopů', className="homepage__hero-heading"),
#             html.P('paragrah', className="homepage__hero-paragraph"),
#             html.A('CTA - SHOWCASE', className="homepage__hero-showcase-link", href="#showcase"),
#         ], className="homepage__hero"),
#         html.Hr(className="homepage__divider"),
#         html.H2('Podívejte se na interaktivní dashboardy pro:', className="homepage__box-heading"),
#         html.Div([
#             html.A(className="homepage__box homepage__box--itesco", href="/itesco"),
#             html.A(className="homepage__box homepage__box--rohlik", href="#rohlik"),
#             html.A(className="homepage__box homepage__box--kosik", href="#kosik"),
#         ], className="homepage__box-container"),
#         html.Hr(className="homepage__divider"),
#         # o nas 
#     ],
#     className="layout-content__container"
# )
