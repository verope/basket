import sys
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

sys.path.append("..") # Adds higher directory to python modules path.

from app import app
from layout.navbar import navbar
from assets import o_projektu

layout = html.Div(
    [
        navbar,
        html.Div([
            html.H1('eSPOKO', className="homepage__hero-heading"),
            html.H3('Interaktivní tool pro sledování vývoje cen potravin v eshopech s výběrem produktů'),
            html.P(o_projektu.subtitle, className="homepage__hero-paragraph"),
            html.A('UKÁZKY', className="homepage__hero-showcase-link", href="/showcase"),
        ], className="homepage__hero"),
        html.Hr(className="homepage__divider"),
        html.H2('Vizualizace pro jednotlivé eshopy', className="homepage__box-heading"),
        html.H4('Klikněte na logo eshopu pro zobrazení interaktivního toolu'),
        html.Div([
            html.A(className="homepage__box homepage__box--itesco", href="/itesco"),
            html.A(className="homepage__box homepage__box--rohlik", href="#rohlik"),
            html.A(className="homepage__box homepage__box--kosik", href="#kosik"),
        ], className="homepage__box-container"),
        html.Hr(className="homepage__divider"),
        html.Div([
            html.H2('O projektu'),
            html.P(o_projektu.popis_projektu),
            ])
    ],
    className="layout-content__container"
)
