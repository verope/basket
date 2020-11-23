import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html

from app import app
from datetime import datetime as dt
from dash.dependencies import Input, Output
from db_connection import itescoWeighted_s


layout = {
    'chart': 'iTesco - vývoj vážené ceny spotřebního koše',
    'xaxis': {'title': 'Datum'},
    'yaxis': {'title': 'Vážená cena', 'rangemode': 'tozero'}
}

graph = html.Div(
    [
        dcc.Graph(id='itesco-weighted-graph',
                  figure={
                      'data': [go.Scatter(
                          x=itescoWeighted_s['date'],
                          y=itescoWeighted_s['vazena_suma'],
                          mode='lines'
                      )],
                      'layout':go.Layout(
                          title=layout['chart'],
                          xaxis=layout['xaxis'],
                          yaxis=layout['yaxis']
                      )
                  })
    ],
    className="graph-cell"
)