from graphs.rohlik_products import layout as layout_rohlik_products
from db_connection import rohlik_by_date
from datetime import datetime as dt
import datetime
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from app import app

def rc_rohlik_products_graph(app):
    @app.callback(Output('rohlik-products-graph', 'figure'),
                  [Input('date-picker-range', 'start_date'),
                   Input('date-picker-range', 'end_date')])
    def callback_rohlik_products_graph(start_date, end_date):
        if start_date is not None:
            start_date = dt.strptime(start_date, '%Y-%m-%d').date()
        if end_date is not None:
            end_date = dt.strptime(end_date, '%Y-%m-%d').date()
        if start_date is not None and end_date is not None:
            figure = {'data': [go.Scatter(x=rohlik_by_date[(rohlik_by_date.index >= start_date) & (rohlik_by_date.index <= end_date)].index,
                                          y=rohlik_by_date['p_key'],
                                          mode='lines'
                                          )],
                      'layout': go.Layout(
                title=layout_rohlik_products['chart'],
                xaxis=layout_rohlik_products['xaxis'],
                yaxis=layout_rohlik_products['yaxis'])
            }
            return figure
        else:
            figure = {'data': [go.Scatter(x=rohlik_by_date.index,
                                          y=rohlik_by_date['user_id'],
                                          mode='lines'
                                          )],
                      'layout': go.Layout(
                title=layout_rohlik_products['chart'],
                xaxis=layout_rohlik_products['xaxis'],
                yaxis=layout_rohlik_products['yaxis'])
            }
            return figure