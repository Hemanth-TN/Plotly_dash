import pandas as pd
import plotly.express as px
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, Dash



df = pd.read_csv("./Data/2011_us_ag_exports.csv")


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width ,initial-scale=1.0'}])



app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1(children='Statewise Aggregation of Food exports in US',
                        id='my-title'), class_name='text-center my-5 text-primary')
            ]),
    dbc.Row([
        dbc.Col([dcc.Dropdown(id='state-dropdown',
                              multi=True,
                              value=['Alabama','Arkansas'],
                              options=[{'label':x, 'value':x} for x in df['state'].unique()]),
                dcc.Graph(id='graph1', figure={})
                              ])
    ])
])


@app.callback(
    Output(component_id='graph1', component_property='figure'),
    [Input(component_id='state-dropdown', component_property='value')]
)
def update_bar(state_selected):
    df_country = df.loc[df['state'].isin(state_selected)].copy()
    fig = px.bar(df_country, x='state',y=['beef','pork','fruits fresh'])
    return fig



if __name__ =="__main__":
    app.run_server(debug=True)


