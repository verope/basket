import sys
import dash_core_components as dcc
import dash_html_components as html

sys.path.append("..") # Adds higher directory to python modules path.

from app import app
from layout.datepicker import datepicker

from graphs.kosik_weighted_evo import graph as graph1
from graphs.kosik_main_cat import graph as graph2
from graphs.kosik_sub_cat import graph as graph3
from graphs.kosik_product import graph as graph4

from layout.navbar import navbar

layout = html.Div(
    [
        navbar,
        datepicker,
        html.Div(
            [
                html.Div([graph1, graph2], className="graph__container"),
                html.Div([graph3, graph4], className="graph__container"),
            ],
            className="layout-container"
        ),
    ],
    className="layout-content__container"
)
