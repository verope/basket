import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px

from db_connection import itescoSubCatDf as df
# the chart will be based on main categories

col_options = [dict(label=x,value=x,title='Podkategorie') for x in df['csu_subcategory'].unique()]

graph = html.Div(children = [
    html.H2("iTesco: ČSÚ produkt"),
    html.P("Vyberte ČSÚ podkategorii:",className="dropdown-title"),
    dcc.Dropdown(id='csu-sub-category-dropdown',value='Drůbež',options=col_options),
    dcc.Graph(id="csu-product-graph",figure={})
], className="graph-cell")