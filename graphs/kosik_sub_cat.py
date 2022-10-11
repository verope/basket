from dash import html
from dash import dcc
from db_connection import conn, select_data

sql = '''
    select distinct "csu_main_category" 
    from WORKSPACE_179647280."out_kosik_spotrebni_kos_sub_cat_agg"
'''

df = select_data(conn, sql)

col_options = [dict(label=x, value=x, title='Hlavní kategorie')
               for x in df['csu_main_category'].unique()]

graph = html.Div(children=[
    html.H2("Kosik: ČSÚ podkategorie"),
    html.P("Vyberte ČSÚ hlavní kategorii:", className="dropdown-title"),
    dcc.Dropdown(id='csu-main-category-dropdown-kosik',
                 value='Maso', options=col_options),
    dcc.Graph(id="csu-sub-category-graph-kosik", figure={})
], className="graph-cell")
