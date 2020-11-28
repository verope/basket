import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px

from db_connection import rohlikSubCat as df

col_options = [dict(label=x,value=x,title='Podkategorie') for x in df['csu_subcategory'].unique()]

graph = html.Div(children = [
    html.H2("Rohlik: ČSÚ produkt"),
    html.P("Vyberte ČSÚ podkategorii:",className="dropdown-title"),
    dcc.Dropdown(id='csu-sub-category-dropdown-rohlik',value='Drůbež',options=col_options),
    dcc.Graph(id="csu-product-graph-rohlik",figure={})
], className="graph-cell")