import sys
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

sys.path.append("..") # Adds higher directory to python modules path.

from graphs.itesco_weighted_evo import graph as graph1
from graphs.itesco_main_category import graph as graph2
from graphs.itesco_sub_category2 import graph as graph3
from graphs.itesco_product import graph as graph4

from navbar import layout as navbar_layout


layout = html.Div(
    [
        navbar_layout,
        html.Div(
            [
                html.Div([graph1, graph2], className="graph__container"),
                html.Div([graph3, graph4], className="graph__container"),
            ],
            className="layout-container"
        ),
    ],
    # className="layout-content__container"
)
