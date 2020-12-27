import sys
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# sys.path.append("..") # Adds higher directory to python modules path.

from app import app
from layout.navbar import navbar
from assets import o_projektu

import base64
# assets/basket_illustration_transparent.png
image_filename = 'assets/basket_illustration_transparent_small.png'
encoded_image = base64.b64encode(open(image_filename,'rb').read())

layout = html.Div(
    [
        navbar,
        html.Div([
            html.Div([

                html.Div([
                    html.H1('eSPOKO', className="homepage__hero-heading"),
                    html.H3('Interaktivní tool pro sledování vývoje cen potravin v eshopech s výběrem produktů'),
                    html.P(o_projektu.subtitle, className="homepage__hero-paragraph"),
                    html.A('UKÁZKY', className="homepage__hero-showcase-link", href="/showcase"),
                ], className="homepage__hero-text"),
                html.Div([
                    html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()))
                ], className="homepage__hero-image")
            ], className="homepage__hero-container")
        ], className="homepage__hero"),
        html.Hr(className="homepage__divider"),
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
            html.A(className="homepage__box homepage__box--rohlik", href="/rohlik"),
            html.A(className="homepage__box homepage__box--kosik", href="/kosik"),
        ], className="homepage__box-container"),
        html.Hr(className="homepage__divider"),
        html.Div([
            html.H2('O projektu'),
            html.P(o_projektu.popis_projektu),
            html.H2('Spotřební koš'),
            html.P(o_projektu.popis_kos),
            ]),
        html.Hr(className="homepage__divider"),    
        html.Div([
            html.A('GitHub repozitář projektu', href="https://github.com/verope/basket", className="homepage__link"),
            html.Br(),
            html.A('Medium článek projektu', href="https://ringle-czechitas.medium.com/spot%C5%99ebn%C3%AD-potravinov%C3%BD-ko%C5%A1-c171d38c906d",className="homepage__link"),
        ], className = "homepage__link-container")
    ],
    className="layout-content__container"
)
