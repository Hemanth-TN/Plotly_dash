import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, Input, Output, html, Dash
import numpy as np
import plotly.graph_objects as go


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv")
df.dropna(how='any', inplace=True)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

option_names = {'H': 'Hue', 'S': 'Satuaration', 'V': 'Brightness', 'L': 'Lightness'}

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Using Checkbox and Graph Components"), 
                width=12, className="text-center my-5 text-primary")
    ], justify='center'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Select any two"),
                    dcc.Checklist(id='checklist_options',
                                  options=[{'label': 'Hue', 'value': 'H'},
                                           {'label': 'Saturation', 'value': 'S'},
                                           {'label': 'Brightness', 'value': 'V'},
                                           {'label': 'Lightness', 'value': 'L'}]),
                    dcc.Graph(id='scatter-plot')
                ])
            ])
        ])
    ])
])

@app.callback(
    Output(component_id='scatter-plot', component_property='figure'),
    Input(component_id='checklist_options', component_property='value'),
)
def update_scatter(selected_values):
    if not selected_values or len(selected_values) !=2:
        layout = go.Layout({'title': {'text': 'Please select exactly two options',
                                      'x': 0.5}})
        return go.Figure(layout=layout)
    
    x, y = selected_values
    fig = px.scatter(data_frame=df,
                     x=x,
                     y=y)
    fig.update_layout({'title': {'text': f"Scatter plot of {option_names[x]} vs {option_names[y]}",
                                 'x': 0.5},
                        'xaxis': {'title_text': option_names[x]},
                        'yaxis': {'title_text': option_names[y]}})
    return fig








if __name__ == "__main__":
    app.run(debug=True)