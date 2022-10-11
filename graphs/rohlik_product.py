from dash import html
from dash import dcc
import plotly.express as px

from db_connection import conn, select_data

sql = '''
    select distinct "csu_subcategory" 
    from WORKSPACE_179647280."out_rohlik_spotrebni_kos_sub_cat_agg"
'''

df = select_data(conn, sql)

col_options = [dict(label=x, value=x, title='Podkategorie')
               for x in df['csu_subcategory'].unique()]

graph = html.Div(children=[
    html.H2("Rohlik: ČSÚ produkt"),
    html.P("Vyberte ČSÚ podkategorii:", className="dropdown-title"),
    dcc.Dropdown(id='csu-sub-category-dropdown-rohlik',
                 value='Drůbež', options=col_options),
    dcc.Graph(id="csu-product-graph-rohlik", figure={})
], className="graph-cell")
