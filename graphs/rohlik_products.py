import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from db_connection import rohlik_by_date

layout = {
    'chart': 'Rohlík - produkty',
    'xaxis': {'title': 'Date'},
    'yaxis': {'title': 'Produkty', 'rangemode': 'tozero'}
}

graph = html.Div(
    [
        dcc.Graph(id='rohlik-products-graph',
                  figure={
                      'data': [go.Scatter(x=rohlik_by_date.index,  
                                          y=rohlik_by_date['p_key'],
                                          mode='lines')],
                      'layout':go.Layout(
                          title=layout['chart'],
                          xaxis=layout['xaxis'],
                          yaxis=layout['yaxis'])
                  })
    ],
    className="graph-cell"
)