import dash_html_components as html
import dash_core_components as dcc
from filters.date_range import date_range_picker


page_logo = html.Div(
    [
        html.Img(
            src='https://www.startupjobs.cz/uploads/02be2dede49cec6ffca6e8783797def7.png'
        )
    ], className='page-logo')

page_title = html.Div(
    [
        html.H1('RINGLE <3 Online Spotřební Koš zkouška sirén')
    ], className='page-title')

navbar = html.Nav(
    [
        html.A('Interaktivní dashboard', href="/",
               className="nav-button"),
        html.A('Online Spotřební Koš', href="/kos",
               className="nav-button"),
        html.A('Zajímavosti', href="/zajimavosti",
               className="nav-button"),
    ], className="navbar"
)

layout = html.Div(
    [
        html.Div(
            [
                page_logo,
                page_title,
                navbar
            ], className="navbar"),
        html.Div(
            [
                date_range_picker
            ], className="filter__container"
        )
    ]
)
