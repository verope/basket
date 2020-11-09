import sys
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

sys.path.append("..") # Adds higher directory to python modules path.

from graphs.itesco_main_category import graph as graph1
from navbar import layout as navbar_layout


layout = html.Div(
    [
        navbar_layout,
        html.Div(
            [
                graph1
            ],
            className="graph__container"),
    ],
    className="layout-content__container"
)
