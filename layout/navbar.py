from dash import html
import dash_bootstrap_components as dbc

APIFY_LOGO = 'https://sdk.apify.com/img/apify_logo.svg'

navbar = dbc.Navbar(
    [
        html.Div([
            html.A([html.Img(src=APIFY_LOGO)],
                   className="navbar__logo", href="https://apify.com"),
            html.A([html.H1('Online spotřební koš')],
                   className="navbar__heading", href="/"),
            html.Div([
                html.A('Ukázky', href="/showcase"),
                html.A('iTesco', href="/itesco"),
                html.A('Rohlik.cz', href="/rohlik"),
                html.A('Kosik.cz', href="/kosik"),
            ], className="navbar__items-container"),
        ], className="navbar-container"),
    ],
    color="dark",
)
