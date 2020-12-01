# OKURKA HADOVKA
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px

from db_connection import okurkyDf as df

product = 'Okurky salátové'

popisek = '''
Sledovaly jsme také vývoj cen u konkrétních produktů v návaznosti na světové události, které by na jejich ceny mohly mít vliv. Například jsme tak zjistily, že cena okurek, které se k nám dováží ze Španělska, stoupla v únoru, což odpovídá době kdy se Španělskem prohnala bouřka Glorie, která poničila velkou část úrody. 
Zdroj: rohlik.cz
'''

df = df.sort_values(by='date')
fig = px.line(df, x="date", y="csuRelevantPrice", hover_name="itemName",
              color="itemName", 
              labels = {"itemName":'',"date":'',"csuRelevantPrice":"Cena na jednotku"},
              line_shape="linear", render_mode="webgl")

fig.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    "legend_orientation":"h",
    "margin":{"t":25,"l":50,"b":25}
})

graph = html.Div(children = [
    html.H2("Vývoj ceny za jednotku"),
    dcc.Graph(id="showcase-graph-cucumber",
            figure=fig)
], className="graph-cell")