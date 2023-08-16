from dash import Dash, dcc, html, Input, Output, callback
import dash
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path='/portfolio',
    title='Portfolio',)

layout = dbc.Container([
    dbc.Container([
            html.Div(className='slider-thumb1'),
            html.Div(className='slider-thumb2'),
            html.P('Portfolio',style={'color':'white','font-weight':'700', 'font-size':'60px',
                                     },className='page-name'),
        ],class_name='bg2 px-0',fluid=True),

    dbc.Container([
       dbc.Accordion(
        [
            dbc.AccordionItem(
                [
                    html.P("This is the content of the first section"),
                    dbc.Button("Click here"),
                ],
                title='Data Visualisation with Python, Tableau and PowerBI',
            ),
            dbc.AccordionItem(
                [
                    html.P("This is the content of the second section"),
                    dbc.Button("Don't click me!", color="danger"),
                ],
                title="Machine Learning with R and Python",
            ),
            dbc.AccordionItem(
                "This is the content of the third section",
                title="Distributed computing with Spark",
            ),
            dbc.AccordionItem(
                "This is the content of the third section",
                title="Natural Language Processing (NLP) with Python",
            ),
            dbc.AccordionItem([
                html.Br(),
                dbc.Row([
                    dbc.Col(
                        html.A([

                            html.Div([
                                html.Img(src='/assets/img/game_thumb.jpg', style={'width':'100%','max-width':'350px','height':'auto'}),
                            ],className='img'),

                            html.Div('Matching Game with Python - Pygame', 
                            className='project-heading'),

                        ],className='img-cont',href='/portfolio/matching_game'),
                    style={'min-width':360,'max-width':360}),
                    dbc.Col(),
                ])
            ],title="Small Games with Python",
            ),
        ],
        flush = True,
    )
      

    ],style={'padding-top':'50px','padding-bottom':'50px',},fluid=False,),


],fluid=True,
class_name='px-0',)