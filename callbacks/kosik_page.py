from datetime import datetime as dt
import datetime
import plotly.express as px
from dash.dependencies import Input, Output
from assets.graph_settings import graph_layout
from functions import generate_time_graph
from db_connection import conn, select_data

def rc_kosik_weighted_evo_graph(app):
    @app.callback(Output('kosik-weighted-graph','figure'),
                    [Input('date-picker-range','start_date'),
                    Input('date-picker-range','end_date')])
    def kosik_weighted_evo(start_date,end_date):
        table_name = "kosik_spotrebni_kos_vazena_suma"
        y = "vazena_suma"
        breakdown = None
        y_label = "Cena spotřebního koše (zvážená)"
        
        if start_date is not None:
            start_date = dt.strptime(start_date,'%Y-%m-%d').date()
        if end_date is not None:
            end_date = dt.strptime(end_date,'%Y-%m-%d').date()

        if start_date is not None and end_date is not None and start_date <= end_date:
            sql = '''
                select * 
                from WORKSPACE_179647280."{}" 
                where "date" >= '{}'
                and "date" <= '{}'
                order by "date"
                ''' 
            sql = sql.format(table_name,start_date,end_date)
            df = select_data(conn,sql)
            return generate_time_graph(df,y,breakdown,graph_layout,y_label)
        else:
            sql = '''
                select * 
                from WORKSPACE_179647280."{}" 
                order by "date"
                ''' 
            sql = sql.format(table_name)
            df = select_data(conn,sql)
            return generate_time_graph(df,y,breakdown,graph_layout,y_label)


def rc_kosik_main_cat_graph(app):
    @app.callback(Output('kosik-main-cat-graph','figure'),
                    [Input('date-picker-range','start_date'),
                    Input('date-picker-range','end_date')])
    def kosik_main_cat_graph_date(start_date,end_date):
        table_name = "out_kosik_spotrebni_kos_main_cat_agg"
        y = "csuRelevantPrice"
        breakdown = "csu_main_category"
        y_label = "Cena za jednotku (průměr)"
        if start_date is not None:
            start_date = dt.strptime(start_date,'%Y-%m-%d').date()
        if end_date is not None:
            end_date = dt.strptime(end_date,'%Y-%m-%d').date()
        if start_date is not None and end_date is not None and start_date <= end_date:
            sql = '''
                select * 
                from WORKSPACE_179647280."{}" 
                where "date" >= '{}'
                and "date" <= '{}'
                order by "date"
                ''' 
            sql = sql.format(table_name,start_date,end_date)
            df = select_data(conn,sql)
            return generate_time_graph(df,y,breakdown,graph_layout,y_label)
        elif start_date is not None and end_date is not None and start_date > end_date:
            new_end_date = start_date
            sql = '''
                select * 
                from WORKSPACE_179647280."{}" 
                where "date" >= '{}'
                and "date" <= '{}'
                order by "date"
                ''' 
            sql = sql.format(table_name,start_date,new_end_date)
            df = select_data(conn,sql)
            return generate_time_graph(df,y,breakdown,graph_layout,y_label)
        else:
            sql = '''
                select * 
                from WORKSPACE_179647280."{}" 
                order by "date"
                ''' 
            sql = sql.format(table_name)
            df = select_data(conn,sql)
            return generate_time_graph(df,y,breakdown,graph_layout,y_label)

def rc_kosik_sub_cat_graph(app):
    @app.callback(Output('csu-sub-category-graph-kosik','figure'),
                    [Input('csu-main-category-dropdown-kosik','value'),
                    Input('date-picker-range','start_date'),
                    Input('date-picker-range','end_date')])
    def kosik_main_sub_graph_dropdown(csu_main_category,start_date,end_date):

        table_name = "out_kosik_spotrebni_kos_sub_cat_agg"
        y = "csuRelevantPrice"
        breakdown = "csu_subcategory"
        y_label = "Cena na jednotku (průměr)"

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
            return generate_time_graph(df,y,breakdown,graph_layout,y_label)
        if start_date is None and end_date is None and csu_main_category is not None:
            sql = '''
                select * 
                from WORKSPACE_179647280."{}" 
                where "csu_main_category" = '{}'
                order by "date"
                ''' 
            sql = sql.format(table_name,csu_main_category)
            df = select_data(conn,sql)
            return generate_time_graph(df,y,breakdown,graph_layout,y_label)
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
            return generate_time_graph(df,y,breakdown,graph_layout,y_label)
        else:
            sql = '''
                select * 
                from WORKSPACE_179647280."{}" 
                order by "date"
                ''' 
            sql = sql.format(table_name)
            df = select_data(conn,sql)
            return generate_time_graph(df,y,breakdown,graph_layout,y_label)


def rc_kosik_product_graph(app):
    @app.callback(Output('csu-product-graph-kosik','figure'),
                    [Input('csu-sub-category-dropdown-kosik','value'),
                    Input('date-picker-range','start_date'),
                    Input('date-picker-range','end_date')])
    def product_graph_dropdown(csu_subcategory,start_date,end_date):

        table_name = "out_kosik_spotrebni_kos_product_agg"
        y = "csuRelevantPrice"
        breakdown = "csu_product"
        y_label = "Cena na jednotku (průměr)"

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
            return generate_time_graph(df,y,breakdown,graph_layout,y_label)
        if start_date is None and end_date is None and csu_subcategory is not None:
            sql = '''
                select * 
                from WORKSPACE_179647280."{}" 
                where "csu_subcategory" = '{}'
                order by "date"
                ''' 
            sql = sql.format(table_name,csu_subcategory)
            df = select_data(conn,sql)
            return generate_time_graph(df,y,breakdown,graph_layout,y_label)
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
            return generate_time_graph(df,y,breakdown,graph_layout,y_label)
        else:
            sql = '''
                select * 
                from WORKSPACE_179647280."{}" 
                order by "date"
                ''' 
            sql = sql.format(table_name)
            df = select_data(conn,sql)
            return generate_time_graph(df,y,breakdown,graph_layout,y_label)

# ## not used right now - the graph is illegible when not filtered
# def rc_kosik_drilldown_sub(app):
#     @app.callback(Output('csu-product-graph','figure'),
#                     Input('csu-sub-category-graph','hoverData'))
#     def callback_kosik_drilldown_sub(hoverData):
#         if hoverData is not None:
#             filter_value = hoverData['points'][0]['hovertext']
#             df = kosikProduct[kosikProduct['csu_subcategory']==filter_value].sort_values(by='date')
#             fig = px.line(df, x="date", y="csuRelevantPrice", hover_name="csu_product",
#             color="csu_product", labels={"csu_product":'', "date": '', "csuRelevantPrice": "Cena na jednotku (průměr)"},
#             line_shape="linear", render_mode="webgl")
#             fig.update_layout({"margin":{"t":25,"l":50},
#                                 "legend_orientation":"h",
#                                 'plot_bgcolor': 'rgba(0,0,0,0)'})
#             return fig
#         else:
#             df = kosikProduct.sort_values(by='date')
#             fig = px.line(df, x="date", y="csuRelevantPrice", hover_name="csu_product",
#             color="csu_product", labels={"csu_product":'', "date": '', "csuRelevantPrice": "Cena na jednotku (průměr)"},
#             line_shape="linear", render_mode="webgl")
#             fig.update_layout({"margin":{"t":25,"l":50},
#                                 "legend_orientation":"h",
#                                 'plot_bgcolor': 'rgba(0,0,0,0)'})
#             return fig