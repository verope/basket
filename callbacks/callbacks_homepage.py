# from graphs.itesco_weighted_evo import layout as layout_itesco_weighted_evo
from db_connection import itescoWeighted_s
from db_connection import itescoProductDf
from db_connection import itescoMainCatDf_agg

from datetime import datetime as dt
import datetime
import plotly.graph_objs as go
import plotly.express as px
import json

from dash.dependencies import Input, Output
from app import app

from db_connection import itescoSubCatDf


def rc_itesco_main_cat_graph_agg(app):
    @app.callback(Output('itesco-main-cat-graph-agg','figure'),
                    [Input('date-picker-range','start_date'),
                    Input('date-picker-range','end_date')])
    def callback_itesco_main_cat_graph_agg(start_date,end_date):
        if start_date is not None:
            start_date = dt.strptime(start_date,'%Y-%m-%d').date()
        if end_date is not None:
            end_date = dt.strptime(end_date,'%Y-%m-%d').date()
        if start_date is not None and end_date is not None:
            df = itescoMainCatDf_agg[(itescoMainCatDf_agg['date'] >= start_date) & (itescoMainCatDf_agg['date'] <= end_date)].sort_values(by='date')
            fig = px.line(df, x="date", y="csuRelevantPrice", hover_name="csu_main_category",
              color="csu_main_category", 
              labels = {"csu_main_category":'',"date":'',"csuRelevantPrice":"Cena na jednotku (suma)"},
              line_shape="spline", render_mode="svg")
            fig.update_layout({
                'plot_bgcolor': 'rgba(0,0,0,0)',
                "legend_orientation":"h",
                "margin":{"t":25,"l":50,"b":25}
            })
            return fig
        else:
            df = itescoMainCatDf_agg.sort_values(by='date')
            fig = px.line(df, x="date", y="csuRelevantPrice", hover_name="csu_main_category",
              color="csu_main_category", 
              labels = {"csu_main_category":'',"date":'',"csuRelevantPrice":"Cena na jednotku (suma)"},
              line_shape="spline", render_mode="svg")
            fig.update_layout({
                'plot_bgcolor': 'rgba(0,0,0,0)',
                "legend_orientation":"h",
                "margin":{"t":25,"l":50,"b":25}
            })
            return fig


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
            df = itescoWeighted_s[(itescoWeighted_s['date'] >= start_date) & (itescoWeighted_s['date'] <= end_date)].sort_values(by='date')
            fig = px.line(df, x="date", y="vazena_suma", hover_name="vazena_suma",
              labels= {"vazena_suma":"Cena spotřebního koše (zvážená)","date":""},
              line_shape="spline", render_mode="svg")
            fig.update_layout({
                'plot_bgcolor': 'rgba(0,0,0,0)',
                "legend_orientation":"h",
                "margin":{"t":25,"l":50,"b":25}
            })
            return fig
        else:
            df = itescoWeighted_s.sort_values(by='date')
            fig = px.line(df, x="date", y="vazena_suma", hover_name="vazena_suma",
              labels= {"vazena_suma":"Cena spotřebního koše (zvážená)","date":""},
              line_shape="spline", render_mode="svg")
            fig.update_layout({
                'plot_bgcolor': 'rgba(0,0,0,0)',
                "legend_orientation":"h",
                "margin":{"t":25,"l":50,"b":25}
            })
            return fig

def rc_itesco_main_cat_graph2(app):
    @app.callback(Output('csu-sub-category-graph','figure'),
                    Input('csu-main-category-dropdown','value'))
    def callback_itesco_main_cat_graph2(csu_main_category):
        df_sub_category = itescoSubCatDf[itescoSubCatDf['csu_main_category']==csu_main_category].sort_values(by='date')
        fig = px.line(df_sub_category, x="date", y="csuRelevantPrice", hover_name="csu_subcategory",
              color="csu_subcategory", labels={"csu_subcategory":'', "date": '', "csuRelevantPrice": "Cena na jednotku (průměr)"},
              line_shape="spline", render_mode="svg")
        fig.update_layout({"margin":{"t":25,"l":50},
                            "legend_orientation":"h",
                            'plot_bgcolor': 'rgba(0,0,0,0)'})
        return fig


def rc_itesco_product_graph_dropdown(app):
    @app.callback(Output('csu-product-graph','figure'),
                    Input('csu-main-category-dropdown','value'))
    def callback_itesco_main_cat_graph2(csu_main_category):
        df = itescoProductDf[itescoProductDf['csu_main_category']==csu_main_category].sort_values(by='date')
        fig = px.line(df, x="date", y="csuRelevantPrice", hover_name="csu_product",
              color="csu_product", labels={"csu_product":'', "date": '', "csuRelevantPrice": "Cena na jednotku (průměr)"},
              line_shape="spline", render_mode="svg")
        fig.update_layout({"margin":{"t":25,"l":50},
                            "legend_orientation":"h",
                            'plot_bgcolor': 'rgba(0,0,0,0)'})
        return fig

def rc_itesco_drilldown_sub(app):
    @app.callback(Output('csu-product-graph','figure'),
                    Input('csu-sub-category-graph','hoverData'))
    def callback_itesco_drilldown_sub(hoverData):
        if hoverData is not None:
            filter_value = hoverData['points'][0]['hovertext']
            df = itescoProductDf[itescoProductDf['csu_subcategory']==filter_value].sort_values(by='date')
            fig = px.line(df, x="date", y="csuRelevantPrice", hover_name="csu_product",
            color="csu_product", labels={"csu_product":'', "date": '', "csuRelevantPrice": "Cena na jednotku (průměr)"},
            line_shape="spline", render_mode="svg")
            fig.update_layout({"margin":{"t":25,"l":50},
                                "legend_orientation":"h",
                                'plot_bgcolor': 'rgba(0,0,0,0)'})
            return fig
        else:
            df = itescoProductDf.sort_values(by='date')
            fig = px.line(df, x="date", y="csuRelevantPrice", hover_name="csu_product",
            color="csu_product", labels={"csu_product":'', "date": '', "csuRelevantPrice": "Cena na jednotku (průměr)"},
            line_shape="spline", render_mode="svg")
            fig.update_layout({"margin":{"t":25,"l":50},
                                "legend_orientation":"h",
                                'plot_bgcolor': 'rgba(0,0,0,0)'})
            return fig