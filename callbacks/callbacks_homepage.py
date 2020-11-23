from graphs.itesco_main_category import layout as layout_itesco_main_cat
from db_connection import itescoMainCatDf_g

from graphs.itesco_weighted_evo import layout as layout_itesco_weighted_evo
from db_connection import itescoWeighted_s
from db_connection import itescoProductDf

from datetime import datetime as dt
import datetime
import plotly.graph_objs as go
import plotly.express as px
import json

from dash.dependencies import Input, Output
from app import app

from db_connection import itescoSubCatDf

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
    @app.callback(Output('itesco-weighted-graph','figure'),
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

def rc_itesco_main_cat_graph2(app):
    @app.callback(Output('csu-sub-category-graph','figure'),
                    Input('csu-main-category-dropdown','value'))
    def callback_itesco_main_cat_graph2(csu_main_category):
        df_sub_category = itescoSubCatDf[itescoSubCatDf['csu_main_category']==csu_main_category].sort_values(by='date')
        fig = px.line(df_sub_category, x="date", y="csuRelevantPrice", hover_name="csu_subcategory",
              color="csu_subcategory", labels={"csu_subcategory"+'<br>'},
              line_shape="spline", render_mode="svg", height=450, width=800)
        fig.update_layout({"margin":{"t":25,"l":50},"legend_orientation":"h"})
        return fig


def rc_itesco_product_graph_dropdown(app):
    @app.callback(Output('csu-product-graph','figure'),
                    Input('csu-main-category-dropdown','value'))
    def callback_itesco_main_cat_graph2(csu_main_category):
        df = itescoProductDf[itescoProductDf['csu_main_category']==csu_main_category].sort_values(by='date')
        fig = px.line(df, x="date", y="csuRelevantPrice", hover_name="csu_product",
              color="csu_product", labels={"csu_product"+'<br>'},
              line_shape="spline", render_mode="svg", height=450, width=800)
        fig.update_layout({"margin":{"t":25,"l":50},"legend_orientation":"h"})
        return fig

def rc_itesco_drilldown_sub(app):
    @app.callback(Output('csu-product-graph','figure'),
                    Input('csu-sub-category-graph','hoverData'))
    def callback_itesco_drilldown_sub(hoverData):
        if hoverData is not None:
            filter_value = hoverData['points'][0]['hovertext']
            df = itescoProductDf[itescoProductDf['csu_subcategory']==filter_value].sort_values(by='date')
            fig = px.line(df, x="date", y="csuRelevantPrice", hover_name="csu_product",
            color="csu_product", labels={"csu_product"+'<br>'},
            line_shape="spline", render_mode="svg", height=450, width=800)
            fig.update_layout({"margin":{"t":25,"l":50},"legend_orientation":"h"})
            return fig
        else:
            df = itescoProductDf.sort_values(by='date')
            fig = px.line(df, x="date", y="csuRelevantPrice", hover_name="csu_product",
            color="csu_product", labels={"csu_product"+'<br>'},
            line_shape="spline", render_mode="svg", height=450, width=800)
            fig.update_layout({"margin":{"t":25,"l":50},"legend_orientation":"h"})
            return fig

def rc_callback_hover_data(app):
    @app.callback(
        Output('hover-data', 'children'),
        Input('csu-sub-category-graph', 'hoverData'))
    def display_hover_data(hoverData):
        return json.dumps(hoverData, indent=2,ensure_ascii=True)