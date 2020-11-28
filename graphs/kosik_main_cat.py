import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

from db_connection import kosikMainCat as df 

df = df.sort_values(by='date')

fig = px.line(df, x="date", y="csuRelevantPrice", hover_name="csu_main_category",
              color="csu_main_category", 
              labels=dict(csu_main_category='',date='',csuRelevantPrice="Cena na jednotku (průměr)"),
              line_shape="spline", render_mode="svg")

fig.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    "legend_orientation":"h",
    "margin":{"t":25,"l":50,"b":25}
})


graph = html.Div(children = [
    html.H2("Kosik: ČSÚ hlavní kategorie"),
    dcc.Graph(id="kosik-main-cat-graph",
            figure=fig)
], className="graph-cell")