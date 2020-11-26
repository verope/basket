import sys
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

sys.path.append("..") # Adds higher directory to python modules path.

from app import app
from layout.navbar import navbar


layout = html.Div(
    [
        navbar,
        html.Div([
            html.H1('Analýza spotřebního koše z online potravinových e-shopů', className="homepage__hero-heading"),
            html.P('paragrah', className="homepage__hero-paragraph"),
            html.A('CTA - SHOWCASE', className="homepage__hero-showcase-link", href="/showcase"),
        ], className="homepage__hero"),
        html.Hr(className="homepage__divider"),
        html.H2('Podívejte se na interaktivní dashboardy pro:', className="homepage__box-heading"),
        html.Div([
            html.A(className="homepage__box homepage__box--itesco", href="/itesco"),
            html.A(className="homepage__box homepage__box--rohlik", href="#rohlik"),
            html.A(className="homepage__box homepage__box--kosik", href="#kosik"),
        ], className="homepage__box-container"),
        html.Hr(className="homepage__divider"),
        # o nas 
    ],
    className="layout-content__container"
)
