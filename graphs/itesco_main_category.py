# import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# from app import app
from datetime import datetime as dt
from dash.dependencies import Input, Output

from db_connection import itescoMainCatDf_agg as df 

fig = px.line(df, x="date", y="csuRelevantPrice", hover_name="csu_main_category",
              color="csu_main_category", 
              labels=dict(csu_main_category='',date='',csuRelevantPrice="Cena na jednotku (průměr)"),
              line_shape="linear", render_mode="webgl")

fig.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    "legend_orientation":"h",
    "margin":{"t":25,"l":50,"b":25}
})


graph = html.Div(children = [
    html.H2("iTesco: ČSÚ hlavní kategorie"),
    dcc.Graph(id="itesco-main-cat-graph-agg",
            figure=fig)
], className="graph-cell")