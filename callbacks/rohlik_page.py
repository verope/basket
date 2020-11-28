from db_connection import rohlikKosVahy
from db_connection import rohlikMainCat
from db_connection import rohlikSubCat
from db_connection import rohlikProduct

from datetime import datetime as dt
import datetime
import plotly.graph_objs as go
import plotly.express as px

from dash.dependencies import Input, Output
from app import app

graph_layout = {
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    "legend_orientation":"h",
    "margin":{"t":25,"l":50,"b":25}
    }

def generate_time_graph(df,y,breakdown,layout,y_label):
    fig = px.line(df,x="date",y=y,hover_name=breakdown,
                 color=breakdown,labels={breakdown:'', "date":'',y:y_label},
                 line_shape="spline",render_mode="svg")
    fig.update_layout(layout)
    return fig


def rc_rohlik_main_cat_graph(app):
    @app.callback(Output('rohlik-main-cat-graph','figure'),
                    [Input('date-picker-range','start_date'),
                    Input('date-picker-range','end_date')])
    def rohlik_main_cat_graph_date(start_date,end_date):
        if start_date is not None:
            start_date = dt.strptime(start_date,'%Y-%m-%d').date()
        if end_date is not None:
            end_date = dt.strptime(end_date,'%Y-%m-%d').date()
        if start_date is not None and end_date is not None and start_date <= end_date:
            df = rohlikMainCat[(rohlikMainCat['date'] >= start_date) & (rohlikMainCat['date'] <= end_date)].sort_values(by='date')
            return generate_time_graph(df,"csuRelevantPrice","csu_main_category",graph_layout,"Cena za jednotku (průměr)")
            # fig = px.line(
            #     df, x="date", 
            #     y="csuRelevantPrice", 
            #     hover_name="csu_main_category",
            #     color="csu_main_category", 
            #     labels = {"csu_main_category":'',"date":'',"csuRelevantPrice":"Cena na jednotku (průměr)"},
            #     line_shape="spline", 
            #     render_mode="svg"
            #     )
            # fig.update_layout(graph_layout)
            # return fig
        elif start_date is not None and end_date is not None and start_date > end_date:
            new_end_date = start_date
            df = rohlikMainCat[(rohlikMainCat['date'] >= start_date) & (rohlikMainCat['date'] <= new_end_date)].sort_values(by='date')
            return generate_time_graph(df,"csuRelevantPrice","csu_main_category",graph_layout,"Cena za jednotku (průměr)")
        else:
            df = rohlikMainCat.sort_values(by='date')
            return generate_time_graph(df,"csuRelevantPrice","csu_main_category",graph_layout,"Cena za jednotku (průměr)")
            # fig = px.line(df, x="date", y="csuRelevantPrice", hover_name="csu_main_category",
            #   color="csu_main_category", 
            #   labels = {"csu_main_category":'',"date":'',"csuRelevantPrice":"Cena na jednotku (suma)"},
            #   line_shape="spline", render_mode="svg")
            # fig.update_layout(graph_layout)
            # return fig


def rc_rohlik_weighted_evo_graph(app):
    @app.callback(Output('rohlik-weighted-graph','figure'),
                    [Input('date-picker-range','start_date'),
                    Input('date-picker-range','end_date')])
    def rohlik_weighted_evo(start_date,end_date):
        if start_date is not None:
            start_date = dt.strptime(start_date,'%Y-%m-%d').date()
        if end_date is not None:
            end_date = dt.strptime(end_date,'%Y-%m-%d').date()
        if start_date is not None and end_date is not None and start_date <= end_date:
            df = rohlikKosVahy[(rohlikKosVahy['date'] >= start_date) & (rohlikKosVahy['date'] <= end_date)].sort_values(by='date')
            return generate_time_graph(df,"vazena_suma",None,graph_layout,"Cena spotřebního koše (zvážená)") 
        else:
            df = rohlikKosVahy.sort_values(by='date')
            return generate_time_graph(df,"vazena_suma",None,graph_layout,"Cena spotřebního koše (zvážená)") 

def rc_rohlik_sub_cat_graph(app):
    @app.callback(Output('csu-sub-category-graph-rohlik','figure'),
                    Input('csu-main-category-dropdown-rohlik','value'))
    def rohlik_main_sub_graph_dropdown(csu_main_category):
        if csu_main_category is not None:
            df = rohlikSubCat[rohlikSubCat['csu_main_category']==csu_main_category].sort_values(by='date')
            return generate_time_graph(df,"csuRelevantPrice","csu_subcategory",graph_layout,"Cena za jednotku (průměr)")
            # fig = px.line(df, x="date", y="csuRelevantPrice", hover_name="csu_subcategory",
            #     color="csu_subcategory", labels={"csu_subcategory":'', "date": '', "csuRelevantPrice": "Cena na jednotku (průměr)"},
            #     line_shape="spline", render_mode="svg")
            # fig.update_layout({"margin":{"t":25,"l":50},
            #                     "legend_orientation":"h",
            #                     'plot_bgcolor': 'rgba(0,0,0,0)'})
            # return fig
        else:
            df = rohlikSubCat.sort_values(by='date')
            return generate_time_graph(df,"csuRelevantPrice","csu_subcategory",graph_layout,"Cena za jednotku (průměr)")
            # fig = px.line(df, x="date", y="csuRelevantPrice", hover_name="csu_subcategory",
            #     color="csu_subcategory", labels={"csu_subcategory":'', "date": '', "csuRelevantPrice": "Cena na jednotku (průměr)"},
            #     line_shape="spline", render_mode="svg")
            # fig.update_layout({"margin":{"t":25,"l":50},
            #                     "legend_orientation":"h",
            #                     'plot_bgcolor': 'rgba(0,0,0,0)'})
            # return fig


def rc_rohlik_product_graph(app):
    @app.callback(Output('csu-product-graph-rohlik','figure'),
                    Input('csu-sub-category-dropdown-rohlik','value'))
    def product_graph_dropdown(csu_subcategory):
        if csu_subcategory is not None:
            df = rohlikProduct[rohlikProduct['csu_subcategory']==csu_subcategory].sort_values(by='date')
            return generate_time_graph(df,"csuRelevantPrice","csu_product",graph_layout,"Cena za jednotku (průměr)")
            # fig = px.line(df, x="date", y="csuRelevantPrice", hover_name="csu_product",
            #     color="csu_product", labels={"csu_product":'', "date": '', "csuRelevantPrice": "Cena na jednotku (průměr)"},
            #     line_shape="spline", render_mode="svg")
            # fig.update_layout({"margin":{"t":25,"l":50},
            #                     "legend_orientation":"h",
            #                     'plot_bgcolor': 'rgba(0,0,0,0)'})
            # return fig
        else:
            df = rohlikProduct.sort_values(by='date')
            return generate_time_graph(df,"csuRelevantPrice","csu_product",graph_layout,"Cena za jednotku (průměr)")
            # fig = px.line(df, x="date", y="csuRelevantPrice", hover_name="csu_product",
            #     color="csu_product", labels={"csu_product":'', "date": '', "csuRelevantPrice": "Cena na jednotku (průměr)"},
            #     line_shape="spline", render_mode="svg")
            # fig.update_layout({"margin":{"t":25,"l":50},
            #                     "legend_orientation":"h",
            #                     'plot_bgcolor': 'rgba(0,0,0,0)'})
            # return fig

# ## not used right now - the graph is illegible when not filtered
# def rc_rohlik_drilldown_sub(app):
#     @app.callback(Output('csu-product-graph','figure'),
#                     Input('csu-sub-category-graph','hoverData'))
#     def callback_rohlik_drilldown_sub(hoverData):
#         if hoverData is not None:
#             filter_value = hoverData['points'][0]['hovertext']
#             df = rohlikProduct[rohlikProduct['csu_subcategory']==filter_value].sort_values(by='date')
#             fig = px.line(df, x="date", y="csuRelevantPrice", hover_name="csu_product",
#             color="csu_product", labels={"csu_product":'', "date": '', "csuRelevantPrice": "Cena na jednotku (průměr)"},
#             line_shape="spline", render_mode="svg")
#             fig.update_layout({"margin":{"t":25,"l":50},
#                                 "legend_orientation":"h",
#                                 'plot_bgcolor': 'rgba(0,0,0,0)'})
#             return fig
#         else:
#             df = rohlikProduct.sort_values(by='date')
#             fig = px.line(df, x="date", y="csuRelevantPrice", hover_name="csu_product",
#             color="csu_product", labels={"csu_product":'', "date": '', "csuRelevantPrice": "Cena na jednotku (průměr)"},
#             line_shape="spline", render_mode="svg")
#             fig.update_layout({"margin":{"t":25,"l":50},
#                                 "legend_orientation":"h",
#                                 'plot_bgcolor': 'rgba(0,0,0,0)'})
#             return fig