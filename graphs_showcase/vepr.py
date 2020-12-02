# VEPROVE
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px

from db_connection import veprDf as df

product = 'Vepřové maso'

popisek = '''
Vývoj vepřového masa byl hned několikrát ovlivněn prasečím morem — poprvé v listopadu 2019, kdy se začal šířit africký mor v Číně, odkud pochází polovina světové produkce. Následně v září 2020, kdy se africký mor rozjel v Německu a odbyt z Německa mimo EU se snížil, což na Evropském trhu způsobilo přebytek.
Zdroj: rohlik.cz
'''

# df = df.sort_values(by='date')
fig = px.line(df, x="date", y="csuRelevantPrice", hover_name="csu_subcategory",
              color="csu_subcategory", 
              labels = {"csu_subcategory":'',"date":'',"csuRelevantPrice":"Cena na jednotku"},
              line_shape="linear", render_mode="webgl")

fig.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    "legend_orientation":"h",
    "margin":{"t":25,"l":50,"b":25}
})

graph = html.Div(children = [
    html.H2("Vývoj ceny za jednotku"),
    dcc.Graph(id="showcase-graph-pork",
            figure=fig)
], className="graph-cell")