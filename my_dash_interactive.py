import json
from textwrap import dedent as d
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

dataList1 = [
                    {
                        'x': [1, 2, 3, 4],
                        'y': [4, 1, 3, 5],
                        'text': ['a', 'b', 'c', 'd'],
                        'customdata': ['c.a', 'c.b', 'c.c', 'c.d'],
                        'name': 'Trace 1',
                        'mode': 'lines+markers',
                        'marker': {'size': 5}
                    }
                ]

dataList2 = [
                    {
                        'x': [5, 6, 7, 8],
                        'y': [8, 3, 7, 3],
                        'text': ['a', 'b', 'c', 'd'],
                        'customdata': ['c.a', 'c.b', 'c.c', 'c.d'],
                        'name': 'Trace 1',
                        'mode': 'lines+markers',
                        'type': 'bar',
                        'marker': {'size': 8, 'color':'green'}
                    }
                ]

app.layout = html.Div([
        html.Div([
        dcc.Graph(
            id='basic-interactions',
            figure={
                'data': dataList1,
                'layout': {
                    'clickmode': 'event+select'
                },
            },
            hoverData={'points': [{'customdata': 'c.a'}]}
        )
    ]),
    html.Div([
            dcc.Graph(
                id='basic-interactions2',
                figure={
                    'data': dataList2,
                    'layout': {
                        'clickmode': 'event+select'
                    }
                }
            )
        ])
        
        ])
            
@app.callback(
    dash.dependencies.Output('basic-interactions2', 'figure'),
    [dash.dependencies.Input('basic-interactions', 'hoverData')])
def update_data(hoverData):
    custom_x = hoverData['points'][0]['customdata']
    return create_time_series(custom_x)

def create_time_series(custom_x):
    if custom_x == 'c.a':
        dataList2[0]['y'][0] = int(dataList2[0]['y'][0]) + 2
    elif custom_x == 'c.b':
        dataList2[0]['y'][1] = int(dataList2[0]['y'][1]) + 3
    elif custom_x == 'c.c':
        dataList2[0]['y'][2] = int(dataList2[0]['y'][2]) - 2
    else:
        dataList2[0]['y'][3] = int(dataList2[0]['y'][3])  - 1
    data_dict = {
                'data': dataList2,
                'layout': {
                    'clickmode': 'event+select'
                    }
                }
    return data_dict 
                
if __name__ == '__main__':
    app.run_server(debug=True)