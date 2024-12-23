# ''' THis is from the youtube https://www.youtube.com/watch?v=0mfIK8zxUds&list=PLh3I780jNsiS3xlk-eLU2dpW3U-wCq4LW&ab_channel=CharmingData'''

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import pandas_datareader.data as web
import datetime
import plotly.express as px
import plotly.graph_objects as go

# start = datetime.datetime(2020,1,1)
# end = datetime.datetime(2024,12,12)

# df = web.DataReader(name=['AMZN', 'GOOGL', 'META','PFE', 'BNTX', 'MRNA'],
#                     data_source='stooq', start=start, end=end)
# df = df.stack().reset_index()

# df.to_csv("./Data/mystocks.csv", index=False)

df = pd.read_csv("./Data/mystocks.csv", index_col=0, parse_dates=True)


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width ,initial-scale=1.0'}])




# Layout section : bootstrap

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1(children="Stock Market Dashboard", 
                        className="text-center text-primary mb-4"),
                width=12)
            ]),
             
    dbc.Row([
        dbc.Col([dcc.Dropdown(id='my-drop-down-1',
                              multi=False,
                              value='AMZN',
                              options=[{'label':x, 'value':x} for x in sorted(df['Symbols'].unique())]
                              ),
                dcc.Graph(id='line-fig-1', figure={})
                ],# width={'size':5, 'offset':1, 'order':1},
                xs=12, sm=12, md=12, lg=5, xl=5),

        dbc.Col([dcc.Dropdown(id='my-drop-down-2',
                              multi=True,
                              value=['PFE','BNTX'],
                              options=[{'label': x, 'value':x} for x in sorted(df['Symbols'].unique())]
                              ),
                dcc.Graph(id='line-fig-2', figure={})
                ], #width={'size':5, 'offset':0.5, 'order':2}
                xs=12, sm=12, md=12, lg=5, xl=5)
            ],
            justify='start'), # center, end, between, around

    dbc.Row([dbc.Col([html.P(children="Select Company Stock",style={'textDecoration': 'underline'}),
                      dcc.Checklist(id="checklist",
                                    options=[{'label': x, 'value':x} for x in sorted(df.Symbols.unique())],
                                    value=['META','GOOGL','AMZN'],
                                    inline=True,
                                    labelClassName='me-3 text-success'),
                      dcc.Graph(id='my-histogram', figure={})
                      ],#width={'size': 5, 'offset':0}
                      xs=12, sm=12, md=12, lg=5, xl=5)
            ])
],fluid=True)


@app.callback(
    Output(component_id='line-fig-1', component_property='figure'),
    Input(component_id='my-drop-down-1', component_property='value')
    )
def update_single_timeseries_graph(company):

    filtered_data = df.loc[df['Symbols']==company].reset_index() 
    
    fig = px.scatter(filtered_data, x='Date', y='High', title=f"{company} Time Series Plot")
    return fig


@app.callback(
    Output(component_id='line-fig-2', component_property='figure'),
    [Input(component_id='my-drop-down-2', component_property='value')]
    )
def update_multiple_timeseries_graph(company_list):

    data = [go.Scatter(x=df.loc[df['Symbols']==cmp, 'Open'].index, y=df.loc[df['Symbols']==cmp, 'Open'], name=cmp) for cmp in company_list]
    
    layout = go.Layout(title="Time series for "+", ".join(company_list))
    
    fig = go.Figure(data=data, layout=layout)
    return fig

@app.callback(
    Output(component_id='my-histogram', component_property='figure'),
    [Input(component_id='checklist', component_property='value')]
    )
def update_bar_graph(company_list):
    
    fig = px.histogram(df.loc[df['Symbols'].isin(company_list)], x='Symbols', y='High', histfunc='sum')
    return fig




if __name__ == "__main__":
    app.run_server(debug=True)
