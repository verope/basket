import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html

# from app import app
from datetime import datetime as dt
from dash.dependencies import Input, Output
from db_connection import itescoKosDf

layout = {
    'chart': 'iTesco Spotrebni Kos',
    'xaxis': {'title': 'Date'},
    'yaxis': {'title': 'Vyvoj ceny', 'rangemode': 'tozero'}
}

itescoKosTraces = [go.Scatter(
    x=itescoKosDf[itescoKosDf['nazev_hlavni_kategorie']
                  == mainCategory]['date'],
    y=itescoKosDf[itescoKosDf['nazev_hlavni_kategorie']
                  == mainCategory]['basePrice'],
    mode='lines',
    name=mainCategory
) for mainCategory in itescoKosDf['nazev_hlavni_kategorie'].unique()]

graph = html.Div(
    [
        dcc.Graph(
            id='itesco-main-graph',
            style={
                'height':800
                },
            figure={
                'data': itescoKosTraces,
                'layout': go.Layout(
                title=layout['chart'],
                xaxis=layout['xaxis'],
                yaxis=layout['yaxis'],
                legend=dict(
                    y=-2,
                    yanchor="bottom"
                    )
                    )
                    }
                  )
    ],
    className="graph-cell"
)
