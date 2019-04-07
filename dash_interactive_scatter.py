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
df = pd.read_excel('literacy.xlsx')

app.layout = html.Div([
        html.Div([
            dcc.Graph(
                id='scatter_chart_1',
                hoverData={'points': [{'customdata': 'Delhi', 'text': 'Delhi'}]}
            )
        ], style={'width': '49%', 'display': 'inline-block'}),
        html.Div([
        dcc.Dropdown(
            id='select_literacy',
            options=[{'label': 'Male Literacy rate', 'value': 'Male'}, {'label': 'Female Literacy rate', 'value': 'Female'}],
            value='Male'
        )
    ], style={'width': '49%', 'display': 'inline-block', 'padding-left':'10px'}),
        html.Div([
        dcc.Graph(
            id='scatter_chart'
        )
    ], style={'width': '49%', 'display': 'inline-block'}),
    html.Div([
            dcc.Graph(
                id='bar_chart'
            )
        ], style={'width': '49%', 'display': 'inline-block'})
    ])

@app.callback(
    dash.dependencies.Output('scatter_chart_1', 'figure'),
    [dash.dependencies.Input('select_literacy', 'value')])
def update_graph(value):
    return {
        'data': [go.Scatter(
            x=df['Male'],
            y=df['Female'],
            text=df['City'],
            customdata=df['City'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': go.Layout(
            xaxis={
                'title': 'Male',
                'type': 'linear'
            },
            yaxis={
                'title': 'Female',
                'type': 'linear'
            },
            margin={'l': 40, 'b': 30, 't': 10, 'r': 0},
            height=450,
            hovermode='closest'
        )
    }


@app.callback(
    dash.dependencies.Output('scatter_chart', 'figure'),
    [dash.dependencies.Input('scatter_chart_1', 'hoverData'),
     dash.dependencies.Input('select_literacy', 'value')])
def update_chart1(hoverData, value):
    city = hoverData['points'][0]['customdata']
    dff = df[df['City'] == city]
    return    {
        'data': [go.Scatter(
            x=dff['Year'],
            y=dff[value],
            mode='markers+lines',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': go.Layout(
            xaxis={
                'title': 'Year',
                'type': 'linear'
            },
            yaxis={
                'title': value,
                'type': 'linear'
            },
            margin={'l': 40, 'b': 30, 't': 10, 'r': 0},
            height=450,
            hovermode='closest'
        )
    }
    
@app.callback(
    dash.dependencies.Output('bar_chart', 'figure'),
    [dash.dependencies.Input('scatter_chart_1', 'hoverData'),
     dash.dependencies.Input('select_literacy', 'value')])
def update_chart2(hoverData, value):
    city = hoverData['points'][0]['customdata']
    dff = df[df['City'] == city]
    return    {
        'data': [go.Bar(
            x=dff['Year'],
            y=dff[value]
        )],
        'layout': go.Layout(
            xaxis={
                'title': 'Year'
            },
            yaxis={
                'title': value
            }
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True)