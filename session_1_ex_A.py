import pandas as pd
import plotly.express as px
import dash
import dash_bootstrap_components as dbc
from dash import dcc, Input, Output, html
import numpy as np


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv")


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

group_strings={0: "Fenty Beauty's PRO FILT'R Foundation Only",
               1: "Make Up For Ever's Ultra HD Foundation Only",
               2: "US Best Sellers",
               3: "BIPOC-recommended Brands with BIPOC Founders",
               4: "BIPOC-recommended Brands with White Founders",
               5: "Nigerian Best Sellers",
               6: "Japanese Best Sellers",
               7: "Indian Best Sellers"}

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("My First dropdown in dash", className='card-title'),
                    dcc.Dropdown(id='brand-options',
                                 options=[{"label": brand, 'value': brand} for brand in df['brand'].unique()],
                                 value='Revlon')
                ])
            ])
        ])
    ],className='m-2'),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4(children="my first radio item", className='card-title'),
                    dcc.RadioItems(id='group-options',
                                   options=[{'label': group_strings[gp], 'value': gp} for gp in np.sort(df['group'].unique())])
                ])
            ])
        ])
    ],className='m-2')
])






if __name__ == "__main__":
    app.run_server(debug=True)