import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from datetime import datetime as dt
import datetime
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app = dash.Dash(__name__) 
app.title = 'Online Spotřební Koš'
server = app.server

app.config.suppress_callback_exceptions = True
# why are you here my friend?

from apps import homepage
from apps import itesco_page
from db_connection import conn
from callbacks.callbacks_itesco_page import rc_itesco_weighted_evo_graph, rc_itesco_main_cat_graph2, rc_itesco_drilldown_sub, rc_itesco_main_cat_graph_agg, rc_itesco_product_graph_dropdown

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return homepage.layout
    if pathname == '/itesco':
        return itesco_page.layout
    # elif pathname == '/kos':
    #     return kos.layout # --> add!
    # elif pathname == '/zajimavosti':
    #     return zajimavosti.layout # --> add!
    else:
        return '404'

rc_itesco_weighted_evo_graph(app)
rc_itesco_main_cat_graph2(app)
# rc_itesco_drilldown_sub(app)
rc_itesco_main_cat_graph_agg(app)
rc_itesco_product_graph_dropdown(app)

if __name__ == '__main__':
    app.run_server(debug=True,host='127.0.0.1',port = 8050)
    # app.run_server(debug=False)
    # server debug does not work -> fix!