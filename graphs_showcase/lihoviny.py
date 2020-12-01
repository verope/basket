# LIHOVINY
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px

from db_connection import lihovinyDf as df

product = 'Lihoviny'

popisek = '''
Dopad zvýšené spotřební daně na lihoviny (konec ledna 2020).
Zdroj: rohlik.cz
'''

breakdownCol = 'csu_product'
df['csuRelevantPrice'] = df['csuRelevantPrice'].astype(float)
df = df.sort_values(by='date')

fig = px.line(df, x="date", y="csuRelevantPrice", hover_name=breakdownCol,
              color=breakdownCol, 
              labels = {breakdownCol:'',"date":'',"csuRelevantPrice":"Cena na jednotku"},
              line_shape="linear", render_mode="webgl")

fig.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    "legend_orientation":"h",
    "margin":{"t":25,"l":50,"b":25}
})

graph = html.Div(children = [
    html.H2("Vývoj ceny za jednotku"),
    dcc.Graph(id="showcase-graph-alcohol",
            figure=fig)
], className="graph-cell")