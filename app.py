import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from datetime import datetime as dt
import datetime
import plotly.graph_objs as go

app = dash.Dash(__name__) 
server = app.server
app.config.suppress_callback_exceptions = True

from apps import homepage
from db_connection import conn
from callbacks.callbacks_homepage import rc_rohlik_products_graph

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
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

rc_rohlik_products_graph(app)

if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1', port = 8050)
    # server debug does not work -> fix!