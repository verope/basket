import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from datetime import datetime as dt
import datetime
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# app = dash.Dash(__name__) 
app.title = 'Online Spotřební Koš'
# server = app.server

app.config.suppress_callback_exceptions = True
# why are you here my friend?

from apps import homepage
from db_connection import conn
from callbacks.callbacks_homepage import rc_itesco_weighted_evo_graph, rc_itesco_main_cat_graph2, rc_callback_hover_data, rc_itesco_drilldown_sub, rc_itesco_main_cat_graph_agg

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return homepage.layout
    # elif pathname == '/kos':
    #     return kos.layout # --> add!
    # elif pathname == '/zajimavosti':
    #     return zajimavosti.layout # --> add!
    else:
        return '404'

rc_itesco_weighted_evo_graph(app)
rc_itesco_main_cat_graph2(app)
rc_callback_hover_data(app)
rc_itesco_drilldown_sub(app)
rc_itesco_main_cat_graph_agg(app)

if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1', port = 8050)
    # , host='127.0.0.1', port = 8050
    # server debug does not work -> fix!