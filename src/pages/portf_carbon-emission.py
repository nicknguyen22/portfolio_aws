import dash                                     
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path='/portfolio/carb-emission',
    title='Carbon Emission and Carbon Intensity of Electricity Generation Analysis',)

layout = dbc.Container(
    html.Iframe(src='http://13.55.49.102:8050/',style={"height": "1067px", "width": "100%"}),
    style={'padding-top':'50px'},fluid = True,
    )