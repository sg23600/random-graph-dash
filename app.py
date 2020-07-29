import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input
import plotly
import plotly.graph_objs as go
import random
from collections import deque

X = deque(maxlen=20)
Y = deque(maxlen=20)
X.append(1)
Y.append(1)

app = dash.Dash(__name__)
app.layout = html.Div(children=

    [   html.H1(children='Random Graph using Dash'),
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1000,  # ms
            n_intervals=0
        ),
    ]
)


@app.callback(Output('live-graph', 'figure'),
              [Input('graph-update', 'n_intervals')])
def update_graph(n):
    X.append(X[-1] + 1)
    Y.append(Y[-1] * (1 + random.uniform(-0.1, 0.1)))
    # Y.append(Y[-1]+Y[-1]*random.uniform(-0.1, 0.1))

    data = go.Scatter(
        x=list(X),
        y=list(Y),
        name='Scatter Plot',
        mode='lines+markers'
    )
    return {'data': [data], 'layout': go.Layout(xaxis=dict(range=[min(X), max(X)]),
                                                yaxis=dict(range=[min(Y), max(Y)]))}


if __name__ == '__main__':
    app.run_server(debug=True)
