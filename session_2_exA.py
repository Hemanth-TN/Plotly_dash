import pandas as pd
import plotly.express as px
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, Dash



df = pd.read_csv("./Data/2011_us_ag_exports.csv")


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = 



if __name__ =="__main__":
    app.run_server(debug=True)


