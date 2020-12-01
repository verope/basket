import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from datetime import datetime as dt

from app import app
# from datetime import datetime as dt
from db_connection import rohlikKosVahy as df

df = df.sort_values(by='date')

fig = px.line(df, x="date", y="vazena_suma", hover_name="vazena_suma",
              labels= {"vazena_suma":"Cena spotřebního koše (zvážená)","date":""},
              line_shape="linear", render_mode="webgl")

fig.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    "legend_orientation":"h",
    "margin":{"t":25,"l":50,"b":25}
})

graph = html.Div(children = [
    html.H2("Rohlik: Cena spotřebního koše"),
    dcc.Graph(id="rohlik-weighted-graph",
            figure=fig)
], className="graph-cell")