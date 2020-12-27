import plotly.express as px

def generate_time_graph(df,y,breakdown,layout,y_label):
    fig = px.line(df,x="date",y=y,hover_name=breakdown,
                 color=breakdown,labels={breakdown:'', "date":'',y:y_label},
                 line_shape="linear",render_mode="webgl")
    fig.update_layout(layout)
    return fig