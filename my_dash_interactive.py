import json
from textwrap import dedent as d
import plotly.graph_objs as go
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

cities=['Haryana', 'Delhi', 'Mumbai', 'Bangalore', 'Kerela', 'Chennai']
maleLiteracy=[60, 90, 85, 95, 100, 98]
femaleLiteracy=[30, 40, 55, 55, 60, 20]

df = pd.DataFrame({"cities":cities, "maleLiteracyRate":maleLiteracy, "femaleLiteracyRate":femaleLiteracy})

scatter_data = [
                    {
                        'x': cities,
                        'y': femaleLiteracy,
                        'text': ['a', 'b', 'c', 'd'],
                        'customdata': ['c.a', 'c.b', 'c.c', 'c.d'],
                        'name': 'Male literacy rate',
                        'mode': 'lines+markers',
                        'marker': {'size': 5}
                    }
                ]

bar_data = [
                    {
                        'x': cities,
                        'y': femaleLiteracy,
                        'text': ['a', 'b', 'c', 'd'],
                        'customdata': ['c.a', 'c.b', 'c.c', 'c.d'],
                        'name': 'Female Literacy rate',
                        'mode': 'lines+markers',
                        'type': 'bar',
                        'marker': {'size': 8, 'color':'green'}
                    }
                ]

app.layout = html.Div([
        html.Div([
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict("rows"),
        )
    ], style={'width': '40%', 'display': 'inline-block', 'font-size':'20px'}),
    html.Div([
            dcc.Dropdown(
                id='select_literacy',
                options=[{'label': 'Male Literacy rate', 'value': 'male'}, {'label': 'Female Literacy rate', 'value': 'female'}],
                value='male'
            )
        ], style={'width': '49%', 'display': 'inline-block', 'padding-left':'10px'}),
        html.Div([
        dcc.Graph(
            id='scatter_chart',
            figure={
                'data': scatter_data,
                'layout': {
                    'clickmode': 'event+select'
                },
            },
            hoverData={'points': [{'customdata': 'c.a'}]}
        )
    ], style={'width': '49%', 'display': 'inline-block'}),
    html.Div([
            dcc.Graph(
                id='bar_chart',
                figure={
                    'data': bar_data,
                    'layout': {
                        'clickmode': 'event+select'
                    }
                }
            )
        ], style={'width': '49%', 'display': 'inline-block'})
    ])

@app.callback(
    dash.dependencies.Output('scatter_chart', 'figure'),
    [dash.dependencies.Input('select_literacy', 'value')])
def update_chart1(value):
    scatter_data[0]['y'] = femaleLiteracy
    if value=='male':
        scatter_data[0]['y'] = maleLiteracy

    data_dict = {
                'data': scatter_data,
                'layout': {
                    'clickmode': 'event+select'
                    }
                }
    return data_dict

@app.callback(
    dash.dependencies.Output('bar_chart', 'figure'),
    [dash.dependencies.Input('select_literacy', 'value')])
def update_chart2(value):
    bar_data[0]['y'] = femaleLiteracy
    if value=='male':
        bar_data[0]['y'] = maleLiteracy

    data_dict = {
                'data': bar_data,
                'layout': {
                    'clickmode': 'event+select'
                    }
                }
    return data_dict
            
#@app.callback(
#    dash.dependencies.Output('basic-interactions2', 'figure'),
#    [dash.dependencies.Input('basic-interactions', 'hoverData')])
#def update_data(hoverData):
#    custom_x = hoverData['points'][0]['customdata']
#    return create_time_series(custom_x)

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