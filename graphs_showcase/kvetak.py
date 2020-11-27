# KVETAK
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px

from db_connection import kvetakDf as df

popisek = '''
Dále jsme zjistily, že během první vlny koronakrize vzrostla cena květáku. To může být způsobeno tím, že květák se dováží z Francie, do které se kvůli protipandemickým opatřením nemohli dostat zahraniční pracovníci provádějící sklizeň. Stoupla tak cena za práci při sklizni a v důsledku stouply i ceny květáku.
</n>zdroj: rohlik.cz
'''
product = 'Květák bílý celý'

df = df.sort_values(by='date')

fig = px.line(df, x="date", y="csuRelevantPrice", hover_name="itemName",
              color="itemName", 
              labels = {"itemName":'',"date":'',"csuRelevantPrice":"Cena na jednotku"},
              line_shape="spline", render_mode="svg")

fig.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    "legend_orientation":"h",
    "margin":{"t":25,"l":50,"b":25}
})

graph = html.Div(children = [
    html.H2("Vývoj ceny za jednotku"),
    dcc.Graph(id="showcase-graph-cauliflower",
            figure=fig)
], className="graph-cell")