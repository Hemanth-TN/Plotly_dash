import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, Input, Output, html, Dash
import numpy as np
import dash_ag_grid as dag


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv")

app = Dash()

columnDefs = [{'field': col, 'filter': True} for col in df.columns]

grid = dag.AgGrid(
    id="get-started-example-basic",
    rowData=df.to_dict("records"),
    columnDefs=columnDefs,
    dashGridOptions={"pagination": True, "animateRows": False},
    columnSize='sizeToFit'
)

app.layout = html.Div([grid])

if __name__ == "__main__":
    app.run(debug=True)