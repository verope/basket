from callbacks.itesco_page import rc_itesco_weighted_evo_graph
from callbacks.kosik_page import rc_kosik_weighted_evo_graph
from callbacks.kosik_page import rc_kosik_product_graph
from callbacks.kosik_page import rc_kosik_sub_cat_graph
from callbacks.kosik_page import rc_kosik_main_cat_graph
from callbacks.rohlik_page import rc_rohlik_weighted_evo_graph
from callbacks.rohlik_page import rc_rohlik_product_graph
from callbacks.rohlik_page import rc_rohlik_sub_cat_graph
from callbacks.rohlik_page import rc_rohlik_main_cat_graph
from callbacks.itesco_page import rc_itesco_product_graph
from callbacks.itesco_page import rc_itesco_main_cat_graph
from callbacks.itesco_page import rc_itesco_sub_cat_graph
from db_connection import conn

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from datetime import datetime as dt
import datetime
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
# I just need a commit and push. Don't we all.

app = dash.Dash(__name__)
app.title = 'Online spotřební koš'
server = app.server

app.config.suppress_callback_exceptions = True
# why are you here my friend?


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    from apps import homepage
    from apps import showcase_page
    from apps import itesco_page
    from apps import rohlik_page
    from apps import kosik_page
    if pathname == '/':
        return homepage.layout
    elif pathname == '/showcase':
        return showcase_page.layout
    elif pathname == '/itesco':
        return itesco_page.layout
    elif pathname == '/rohlik':
        return rohlik_page.layout
    elif pathname == '/kosik':
        return kosik_page.layout
    else:
        return '404'


# from callbacks.itesco_page import rc_itesco_drilldown_sub


rc_itesco_weighted_evo_graph(app)
rc_itesco_sub_cat_graph(app)
# rc_itesco_drilldown_sub(app)
rc_itesco_main_cat_graph(app)
rc_itesco_product_graph(app)

rc_rohlik_weighted_evo_graph(app)
rc_rohlik_main_cat_graph(app)
rc_rohlik_sub_cat_graph(app)
rc_rohlik_product_graph(app)

rc_kosik_weighted_evo_graph(app)
rc_kosik_main_cat_graph(app)
rc_kosik_sub_cat_graph(app)
rc_kosik_product_graph(app)


if __name__ == '__main__':
    from apps import homepage
    from apps import showcase_page
    from apps import itesco_page
    from apps import rohlik_page
    from apps import kosik_page
    app.run_server(debug=True, host='127.0.0.1', port=8050)
    # app.run_server(debug=False)
