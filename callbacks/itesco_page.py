from datetime import datetime as dt
import datetime
import plotly.express as px
from dash.dependencies import Input, Output

from functions import generate_time_graph
from db_connection import conn, select_data
from assets.graph_settings import graph_layout

def rc_itesco_main_cat_graph(app):
    @app.callback(Output('itesco-main-cat-graph-agg','figure'),
                    [Input('date-picker-range','start_date'),
                    Input('date-picker-range','end_date')])
    def callback_itesco_main_cat_graph_agg(start_date,end_date):
        table_name = "out_itesco_spotrebni_kos_main_cat_agg"
        if start_date is not None:
            start_date = dt.strptime(start_date,'%Y-%m-%d').date()
        if end_date is not None:
            end_date = dt.strptime(end_date,'%Y-%m-%d').date()
        if start_date is not None and end_date is not None:
            sql = '''
                select * 
                from WORKSPACE_179647280."{}" 
                where "date" >= '{}'
                and "date" <= '{}'
                order by "date"
                ''' 
            sql = sql.format(table_name,start_date,end_date)
            df = select_data(conn,sql)
            y = "csuRelevantPrice"
            breakdown = "csu_main_category"
            y_label = "Cena na jednotku (suma)"
            return generate_time_graph(df,y,breakdown,graph_layout,y_label)
        else:
            sql = '''
                select * 
                from WORKSPACE_179647280."{}" 
                order by "date"
                ''' 
            sql = sql.format(table_name)
            df = select_data(conn,sql)
            y = "csuRelevantPrice"
            breakdown = "csu_main_category"
            y_label = "Cena na jednotku (suma)"
            return generate_time_graph(df,y,breakdown,graph_layout,y_label)

def rc_itesco_weighted_evo_graph(app):
    @app.callback(Output('itesco-weighted-graph','figure'),
                    [Input('date-picker-range','start_date'),
                    Input('date-picker-range','end_date')])
    def callback_itesco_weighted_evo(start_date,end_date):
        table_name = "itesco_spotrebni_kos_vazena_suma"
        if start_date is not None:
            start_date = dt.strptime(start_date,'%Y-%m-%d').date()
        if end_date is not None:
            end_date = dt.strptime(end_date,'%Y-%m-%d').date()
        if start_date is not None and end_date is not None:
            sql = '''
                select * 
                from WORKSPACE_179647280."{}" 
                where "date" >= '{}'
                and "date" <= '{}'
                order by "date"
                ''' 
            sql = sql.format(table_name,start_date,end_date)
            df = select_data(conn,sql)
            return generate_time_graph(df,"vazena_suma",None,graph_layout,"Cena spotřebního koše (zvážená)")
        else:
            sql = '''
                select * 
                from WORKSPACE_179647280."{}"
                order by "date"
                ''' 
            sql = sql.format(table_name)
            df = select_data(conn,sql)
            return generate_time_graph(df,"vazena_suma",None,graph_layout,"Cena spotřebního koše (zvážená)")

def rc_itesco_sub_cat_graph(app):
    @app.callback(Output('csu-sub-category-graph','figure'),
                    [Input('csu-main-category-dropdown','value'),
                    Input('date-picker-range','start_date'),
                    Input('date-picker-range','end_date')])
    def callback_itesco_sub_cat_graph(csu_main_category,start_date,end_date):
        table_name = "out_itesco_spotrebni_kos_sub_cat_agg"
        if start_date is not None:
            start_date = dt.strptime(start_date,'%Y-%m-%d').date()
        if end_date is not None:
            end_date = dt.strptime(end_date,'%Y-%m-%d').date()
        if start_date is not None and end_date is not None and csu_main_category is not None:
            sql = '''
                select * 
                from WORKSPACE_179647280."{}" 
                where "date" >= '{}'
                and "date" <= '{}'
                and "csu_main_category" = '{}'
                order by "date"
                ''' 
            sql = sql.format(table_name,start_date,end_date,csu_main_category)
            df = select_data(conn,sql)
            return generate_time_graph(df,"csuRelevantPrice","csu_subcategory",graph_layout,"Cena na jednotku (průměr)")
        if start_date is None and end_date is None and csu_main_category is not None:
            sql = '''
                select * 
                from WORKSPACE_179647280."{}" 
                where "csu_main_category" = '{}'
                order by "date"
                ''' 
            sql = sql.format(table_name,csu_main_category)
            df = select_data(conn,sql)
            return generate_time_graph(df,"csuRelevantPrice","csu_subcategory",graph_layout,"Cena na jednotku (průměr)")
        if start_date is not None and end_date is not None and csu_main_category is None:
            sql = '''
                select * 
                from WORKSPACE_179647280."{}" 
                where "date" >= '{}'
                and "date" <= '{}'
                order by "date"
                ''' 
            sql = sql.format(table_name,start_date,end_date)
            df = select_data(conn,sql)
            return generate_time_graph(df,"csuRelevantPrice","csu_subcategory",graph_layout,"Cena na jednotku (průměr)")
        
        else:
            sql = '''
                select * 
                from WORKSPACE_179647280."{}" 
                order by "date"
                ''' 
            sql = sql.format(table_name)
            df = select_data(conn,sql)
            return generate_time_graph(df,"csuRelevantPrice","csu_subcategory",graph_layout,"Cena na jednotku (průměr)")


def rc_itesco_product_graph(app):
    @app.callback(Output('csu-product-graph','figure'),
                    [Input('csu-sub-category-dropdown','value'),
                    Input('date-picker-range','start_date'),
                    Input('date-picker-range','end_date')])
    def callback_itesco_product_graph(csu_subcategory,start_date,end_date):
        table_name = "out_itesco_spotrebni_kos_product_agg"
        if start_date is not None:
            start_date = dt.strptime(start_date,'%Y-%m-%d').date()
        if end_date is not None:
            end_date = dt.strptime(end_date,'%Y-%m-%d').date()
        if start_date is not None and end_date is not None and csu_subcategory is not None:
            sql = '''
                select * 
                from WORKSPACE_179647280."{}" 
                where "date" >= '{}'
                and "date" <= '{}'
                and "csu_subcategory" = '{}'
                order by "date"
                ''' 
            sql = sql.format(table_name,start_date,end_date,csu_subcategory)
            df = select_data(conn,sql)
            return generate_time_graph(df,"csuRelevantPrice","csu_product",graph_layout,"Cena na jednotku (průměr)")
        if start_date is None and end_date is None and csu_subcategory is not None:
            sql = '''
                select * 
                from WORKSPACE_179647280."{}" 
                where "csu_subcategory" = '{}'
                order by "date"
                ''' 
            sql = sql.format(table_name,csu_subcategory)
            df = select_data(conn,sql)
            return generate_time_graph(df,"csuRelevantPrice","csu_product",graph_layout,"Cena na jednotku (průměr)")
        if start_date is not None and end_date is not None and csu_subcategory is None:
            sql = '''
                select * 
                from WORKSPACE_179647280."{}" 
                where "date" >= '{}'
                and "date" <= '{}'
                order by "date"
                ''' 
            sql = sql.format(table_name,start_date,end_date)
            df = select_data(conn,sql)
            return generate_time_graph(df,"csuRelevantPrice","csu_product",graph_layout,"Cena na jednotku (průměr)")
        
        else:
            sql = '''
                select * 
                from WORKSPACE_179647280."{}" 
                order by "date"
                ''' 
            sql = sql.format(table_name)
            df = select_data(conn,sql)
            return generate_time_graph(df,"csuRelevantPrice","csu_product",graph_layout,"Cena na jednotku (průměr)")

## not used right now - the graph is illegible when not filtered
# def rc_itesco_drilldown_sub(app):
#     @app.callback(Output('csu-product-graph','figure'),
#                     Input('csu-sub-category-graph','hoverData'))
#     def callback_itesco_drilldown_sub(hoverData):
#         if hoverData is not None:
#             filter_value = hoverData['points'][0]['hovertext']
#             df = itescoProductDf[itescoProductDf['csu_subcategory']==filter_value].sort_values(by='date')
#             fig = px.line(df, x="date", y="csuRelevantPrice", hover_name="csu_product",
#             color="csu_product", labels={"csu_product":'', "date": '', "csuRelevantPrice": "Cena na jednotku (průměr)"},
#             line_shape="linear", render_mode="webgl")
#             fig.update_layout({"margin":{"t":25,"l":50},
#                                 "legend_orientation":"h",
#                                 'plot_bgcolor': 'rgba(0,0,0,0)'})
#             return fig
#         else:
#             df = itescoProductDf.sort_values(by='date')
#             fig = px.line(df, x="date", y="csuRelevantPrice", hover_name="csu_product",
#             color="csu_product", labels={"csu_product":'', "date": '', "csuRelevantPrice": "Cena na jednotku (průměr)"},
#             line_shape="linear", render_mode="webgl")
#             fig.update_layout({"margin":{"t":25,"l":50},
#                                 "legend_orientation":"h",
#                                 'plot_bgcolor': 'rgba(0,0,0,0)'})
#             return fig