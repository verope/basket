from graphs.itesco_main_category import layout as layout_itesco_main_cat
from db_connection import itescoMainCatDf_g

from graphs.itesco_weighted_evo import layout as layout_itesco_weighted_evo
from db_connection import itescoWeighted_s

from datetime import datetime as dt
import datetime
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from app import app

def rc_itesco_main_cat_graph(app):
    @app.callback(Output('itesco-main-graph', 'figure'),
                  [Input('date-picker-range', 'start_date'),
                   Input('date-picker-range', 'end_date')])
    def callback_itesco_main_cat_graph(start_date, end_date):
        if start_date is not None:
            start_date = dt.strptime(start_date, '%Y-%m-%d').date()
        if end_date is not None:
            end_date = dt.strptime(end_date, '%Y-%m-%d').date()
        if start_date is not None and end_date is not None:
            figure = {'data': [go.Scatter(x=itescoMainCatDf_g[(itescoMainCatDf_g['date']>=start_date) & (itescoMainCatDf_g['date']<=end_date) & (itescoMainCatDf_g['nazev_hlavni_kategorie'] == mainCategory)]['date'],
                                        y=itescoMainCatDf_g[(itescoMainCatDf_g['date']>=start_date) & (itescoMainCatDf_g['date']<=end_date) & (itescoMainCatDf_g['nazev_hlavni_kategorie'] == mainCategory)]['basePrice'],
                                        mode='lines',
                                        name=mainCategory
                                        ) for mainCategory in itescoMainCatDf_g[(itescoMainCatDf_g['date']>=start_date) & (itescoMainCatDf_g['date']<=end_date)]['nazev_hlavni_kategorie'].unique()],
                    'layout': go.Layout(
                title=layout_itesco_main_cat['chart'],
                xaxis=layout_itesco_main_cat['xaxis'],
                yaxis=layout_itesco_main_cat['yaxis'])
            }
            return figure
        else:
            figure = {'data': [go.Scatter(x=itescoMainCatDf_g[itescoMainCatDf_g['nazev_hlavni_kategorie']== mainCategory]['date'],
                                        y=itescoMainCatDf_g[itescoMainCatDf_g['nazev_hlavni_kategorie']== mainCategory]['basePrice'],
                                        mode='lines',
                                        name=mainCategory
                                        ) for mainCategory in itescoMainCatDf_g['nazev_hlavni_kategorie'].unique()],
                    'layout': go.Layout(
                title=layout_itesco_main_cat['chart'],
                xaxis=layout_itesco_main_cat['xaxis'],
                yaxis=layout_itesco_main_cat['yaxis'])
            }
            return figure

def rc_itesco_weighted_evo_graph(app):
    @app.callback(Output('itesco-weighted-grpah','figure'),
                    [Input('date-picker-range','start_date'),
                    Input('date-picker-range','end_date')])
    def callback_itesco_weighted_evo(start_date,end_date):
        if start_date is not None:
            start_date = dt.strptime(start_date,'%Y-%m-%d').date()
        if end_date is not None:
            end_date = dt.strptime(end_date,'%Y-%m-%d').date()
        if start_date is not None and end_date is not None:
            filteredDf = itescoWeighted_s[(itescoWeighted_s['date'] >= start_date) & (itescoWeighted_s['date'] >= end_date)]
            figure = {
                'data': [
                    go.Scatter(
                        x=filteredDf['date'],
                        y=filteredDf['vazena_suma'],
                        mode='lines'
                    )
                ],
                'layout': go.Layout(
                    title=layout_itesco_weighted_evo['chart'],
                    xaxis=layout_itesco_weighted_evo['xaxis'],
                    yaxis=layout_itesco_weighted_evo['yaxis']
                )
            }
            return figure
        else:
            figure = {
                'data': [
                    go.Scatter(
                        x=itescoWeighted_s['date'],
                        y=itescoWeighted_s['vazena_suma'],
                        mode='lines'
                    )
                ],
                'layout': go.Layout(
                    title=layout_itesco_weighted_evo['chart'],
                    xaxis=layout_itesco_weighted_evo['xaxis'],
                    yaxis=layout_itesco_weighted_evo['yaxis']
                )
            }