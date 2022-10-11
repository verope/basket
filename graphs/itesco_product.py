import dash
from dash import html
from dash import dcc
import plotly.express as px

# from db_connection import itescoSubCatDf as df

from db_connection import conn, select_data

sql = '''
    select distinct "csu_subcategory" 
    from WORKSPACE_179647280."out_itesco_spotrebni_kos_sub_cat_agg"
'''

df = select_data(conn, sql)

col_options = [dict(label=x, value=x, title='Podkategorie')
               for x in df['csu_subcategory'].unique()]

graph = html.Div(children=[
    html.H2("iTesco: ČSÚ produkt"),
    html.P("Vyberte ČSÚ podkategorii:", className="dropdown-title"),
    dcc.Dropdown(id='csu-sub-category-dropdown',
                 value='Drůbež', options=col_options),
    dcc.Graph(id="csu-product-graph", figure={})
], className="graph-cell")
