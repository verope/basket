from layout.navbar import navbar
from graphs.rohlik_product import graph as graph4
from graphs.rohlik_sub_cat import graph as graph3
from graphs.rohlik_main_cat import graph as graph2
from graphs.rohlik_weighted_evo import graph as graph1
from layout.datepicker import datepicker
from app import app
import sys
from dash import dcc
from dash import html

sys.path.append("..")  # Adds higher directory to python modules path.


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
