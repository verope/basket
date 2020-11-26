import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px

from db_connection import itescoMainCatDf_agg as df
# the chart will be based on main categories

col_options = [dict(label=x,value=x,title='Hlavní kategorie') for x in df['csu_main_category'].unique()]

graph = html.Div(children = [
    html.H2("iTesco: ČSÚ podkategorie"),
    html.P("Vyberte ČSÚ hlavní kategorii:",className="dropdown-title"),
    dcc.Dropdown(id='csu-main-category-dropdown',value='Maso',options=col_options),
    dcc.Graph(id="csu-sub-category-graph",figure={})
], className="graph-cell")