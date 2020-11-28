import dash_html_components as html
import dash_bootstrap_components as dbc

APIFY_LOGO = 'https://sdk.apify.com/img/apify_logo.svg'

navbar = dbc.Navbar(
    [
        html.Div([
            html.A([html.Img(src=APIFY_LOGO)], className="navbar__logo", href="https://apify.com"),
            html.A([html.H1('Online Spotřební Koš')], className="navbar__heading", href="/"),
            html.Div([
                html.A('Ukázky', href="/showcase"),
                html.A('iTesco', href="/itesco"),
                html.A('Rohlik.cz', href="/rohlik"),
                html.A('Kosik.cz', href="#2"),
            ], className="navbar__items-container"), 
        ], className="navbar-container"),
        # html.A(
        #     # Use row and col to control vertical alignment of logo / brand
        #     dbc.Row(
        #         [
        #             dbc.Col(html.Img(src=APIFY_LOGO, height="50px"), align="left"),
        #             dbc.Col(dbc.NavbarBrand("Online Spotřební Koš", className="page-title")),
        #         ],
        #         align="center",
        #         no_gutters=False,
        #     ),
        #     href="https://apify.com",
        # ),
        # dbc.DropdownMenu(
        #     children=[
        #         dbc.DropdownMenuItem("More pages", header=True),
        #         dbc.DropdownMenuItem("Page 2", href="#"),
        #         dbc.DropdownMenuItem("Page 3", href="#"),
        #     ],
        #     nav=True,
        #     in_navbar=True,
        #     label="More",
        # ),
        # # dbc.NavbarToggler(id="navbar-toggler"),
        # # dbc.Collapse(search_bar, id="navbar-collapse", navbar=True),
    ],
    color="dark",
)



# import dash_html_components as html
# from dash.dependencies import Input, Output, State

# search_bar = dbc.Row(
#     [
#         dbc.Col(dbc.Input(type="search", placeholder="Search")),
#         dbc.Col(
#             dbc.Button("Search", color="primary", className="ml-2"),
#             width="auto",
#         ),
#     ],
#     no_gutters=True,
#     className="ml-auto flex-nowrap mt-3 mt-md-0",
#     align="center",
# )



# add callback for toggling the collapse on small screens
# @app.callback(
#     Output("navbar-collapse", "is_open"),
#     [Input("navbar-toggler", "n_clicks")],
#     [State("navbar-collapse", "is_open")],
# )
# def toggle_navbar_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open



# import dash_bootstrap_components as dbc

# navbar = dbc.NavbarSimple(
#     children=[
#         dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        # dbc.DropdownMenu(
        #     children=[
        #         dbc.DropdownMenuItem("More pages", header=True),
        #         dbc.DropdownMenuItem("Page 2", href="#"),
        #         dbc.DropdownMenuItem("Page 3", href="#"),
        #     ],
        #     nav=True,
        #     in_navbar=True,
        #     label="More",
        # ),
#     ],
#     brand="NavbarSimple",
#     brand_href="#",
#     color="dark",
#     dark=True,
# )