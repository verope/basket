import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# from app import app
from datetime import datetime as dt
from dash.dependencies import Input, Output

from db_connection import itescoMainCatDf_agg as df 

product = 'Okurky salátové'

popisek = '''
Sledovaly jsme také vývoj cen u konkrétních produktů v návaznosti na světové události, které by na jejich ceny mohly mít vliv. Například jsme tak zjistily, že cena okurek, které se k nám dováží ze Španělska, stoupla v únoru, což odpovídá době kdy se Španělskem prohnala bouřka Glorie, která poničila velkou část úrody. 
'''

fig = px.line(df, x="date", y="csuRelevantPrice", hover_name="csu_main_category",
              color="csu_main_category", 
              labels=dict(csu_main_category='',date='',csuRelevantPrice="Cena na jednotku (suma)"),
              line_shape="spline", render_mode="svg")

fig.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)',
    "legend_orientation":"h",
    "margin":{"t":25,"l":50,"b":25}
})


graph = html.Div(children = [
    html.H2("iTesco: ČSÚ hlavní kategorie"),
    dcc.Graph(id="itesco-main-cat-graph-agg",
            figure=fig)
], className="graph-cell")