import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from datetime import datetime as dt

from app import app
from datetime import datetime as dt
from dash.dependencies import Input, Output
from db_connection import itescoWeighted_s as df

fig = px.line(df, x="date", y="vazena_suma", hover_name="vazena_suma",
              labels= {"vazena_suma":"Cena spotřebního koše (zvážená)","date":""},
              line_shape="spline", render_mode="svg")

fig.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)',
    "legend_orientation":"h",
    "margin":{"t":25,"l":50,"b":25}
})

graph = html.Div(children = [
    html.H2("iTesco: Cena spotřebního koše"),
    dcc.Graph(id="itesco-weighted-graph",
            figure=fig)
], className="graph-cell")


# layout = {
#     'chart': 'iTesco - vývoj vážené ceny spotřebního koše',
#     'xaxis': {'title': 'Datum'},
#     'yaxis': {'title': 'Vážená cena', 'rangemode': 'tozero'}
# }

# graph = html.Div(
#     [
#         dcc.Graph(id='itesco-weighted-graph',
#                   figure={
#                       'data': [go.Scatter(
#                           x=itescoWeighted_s['date'],
#                           y=itescoWeighted_s['vazena_suma'],
#                           mode='lines'
#                       )],
#                       'layout':go.Layout(
#                           title=layout['chart'],
#                           xaxis=layout['xaxis'],
#                           yaxis=layout['yaxis']
#                       )
#                   })
#     ],
#     className="graph-cell"
# )