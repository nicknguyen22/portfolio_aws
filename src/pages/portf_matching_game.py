import dash                                     
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path='/portfolio/matching_game',
    title='Matching Game with Python - PyGame',)

layout = dbc.Container([
    html.H3('Matching Game with Python - Pygame'),
    html.Br(),html.Br(),
    html.P("I like playing games in my free time to relax, especially ones that \
        have puzzles to solve. During my spare moments, I created this Memory \
        Matching Game using Python. It's a fun and enjoyable activity that brings \
        together Object-Oriented Programming (OOP) and the flexible PyGame library. \
        Prepare yourself to see how good your memory is as you flip cards and try \
        to find pairs that match. Each flip will give your brain a workout and \
        help improve your memory skills. Plus, you'll get to experience the cool \
        visuals and interactive features that PyGame offers.  This game is great \
        for kids, I made all the graphics myself or got them from open sources.",
        style={'font-family':'Georgia','font-size':'16px'}),
    html.Br(),
    dbc.Row([
        dbc.Col(html.Img(src='/assets/img/game_1.jpg', className = 'resp')),
        dbc.Col(html.Img(src='/assets/img/game_2.jpg', className = 'resp')),
    ],justify='evenly'),
    html.Br(),
    html.A('Codes on Github Repository',href="https://github.com/nicknguyen22/Python_memory_game.git", target="_blank"),

],style={'padding-top':'100px'},fluid = False,
)