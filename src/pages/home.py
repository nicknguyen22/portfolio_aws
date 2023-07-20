import dash                                     
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc


dash.register_page(
    __name__,
    path='/',
    title='Nick Nguyen',)

layout = dbc.Container([
    
    dbc.Container([
        dbc.Container([
            dbc.Col([
                html.Div(className='slider-thumb0'),
                html.Br(),html.Br(),
                html.Div([
                    html.P("Greetings ! I go by the name",style={'font-size':'16px',
                                                                'font-family':'Georgia'}),
                    html.H4("Nick Nguyen"),
                    html.H5("Data Scientist : Turning Coffee into Data-Driven Insights since 2022"),
                    html.Br(),
                    html.P("I'm your friendly neighborhood Data Scientist by day, "\
                        "Spreadsheet Jedi by night, fueled by a passion for tackling "\
                        "complex problems, empowering right decision-making through data. "\
                        "From decoding complex data mysteries to predicting trends and the "\
                        "bizarre pizza-productivity ratio, I'm the quirky data "\
                        "scientist you never knew you needed.",style={'font-size':'16px',
                                                                'font-family':'Georgia'}),
                ],className='page-name'),
            ],style = {'text-align':'left'}),
        ],style= {
                'color':'white',
                'padding-top':'100px',
                'padding-left':'50px',
                'padding-bottom':'70px',
                },),
    ],fluid=True,class_name='bg0 px-0',
    style= {
                'width':'100%',
                'height':'400px',
                },
    ),

    dbc.Container([
        dbc.Container([
            html.P('SUMMARY',style={'font-family':'Arial','font-size':'26px'}),
            html.P("With a diverse background encompassing more than 15 years of "\
                "professional expertise across multiple sectors such as Pharmaceutical, "\
                "Banking & Finance, and Property Development, I have recently embarked "\
                "on a new journey within the dynamic realm of Data Science. Equipped "\
                "with a Master's degree in Applied Data Science, I now assume the "\
                "role of a dedicated Data Scientist, earnestly striving to make a "\
                "meaningful impact within the industry.",
                style={'padding-left':'40px','padding-top':'0px','font-family':'Georgia',
                    'font-size':'16px'}),
            html.P("My distinctive amalgamation of experience, skills, and knowledge "\
                "serves as the impetus behind my unwavering dedication to continuous "\
                "professional growth and collaboration with peers in the field. "\
                "Fueled by an ardent enthusiasm for harnessing state-of-the-art "\
                "technologies, I wholeheartedly focus on fostering positive "\
                "transformation and contributing to the advancement of society "\
                "through my endeavors.",
                style={'padding-left':'40px','padding-bottom':'30px','font-family':'Georgia',
                    'font-size':'16px'}),

        dbc.Row([
                dbc.Col(dbc.Button('ABOUT ME', color='primary',href="/aboutme",))
            ],class_name='px-0'), 
        ]),
    ],style={'padding-top':'70px','padding-bottom':'70px',},fluid=True,class_name='px-0'),   

    dbc.Container([
        dbc.Container([
            html.P('MOST RECENT PROJECTS ',style={'font-family':'Arial','font-size':'26px'}),
            dbc.Row([
                dbc.Col([
                    html.A([

                        html.Div([
                            html.Img(src='/assets/spt_prc.jpg', style={'width':'100%','max-width':'350px','height':'auto'}),
                        ],className='img'),

                        html.Div('Deep Learning with TensorFlow LSTM and Electricity Spot Price',
                                     className='project-heading'),

                    ],className='img-cont',href='/spt_prc'
                    ),
                    
                    html.Hr(),
                    html.P('Lorem ipsum dolor sit amet, utroque invidunt at sea, '\
                           'sit tibique appareat et, te eum natum adhuc. Denique '\
                           'eleifend pri cu. Fuisset maluisset percipitur ad qui, '\
                           'magna audiam id mel. Et has partem mucius',
                           style={'font-family':'Georgia','font-size':'16px'}
                    ),
                
                ],style={'max-width':'350px'}),

                dbc.Col([
                    html.A([

                        html.Div([
                            html.Img(src='/assets/viz_1.jpg', style={'width':'100%','max-width':'350px','height':'auto'}),
                        ],className='img'),

                        html.Div('Electricity Generation & Carbon Emission 2002-2022 '\
                                 'Visualisation', className='project-heading'),

                    ],className='img-cont',href='/elec2022'
                    ),
                    
                    html.Hr(),
                    html.P('Lorem ipsum dolor sit amet, utroque invidunt at sea, '\
                           'sit tibique appareat et, te eum natum adhuc. Denique '\
                           'eleifend pri cu. Fuisset maluisset percipitur ad qui, '\
                           'magna audiam id mel. Et has partem mucius',
                           style={'font-family':'Georgia','font-size':'16px'}
                    ),
                
                ],style={'max-width':'350px'}),

                dbc.Col([
                    html.A([

                        html.Div([
                            html.Img(src='/assets/viz_2.jpg', style={'width':'100%','max-width':'350px','height':'auto'}),
                        ],className='img'),

                        html.Div('Analysing Electricity Usage Patterns and '\
                                 'Interacting with Data Tables', className='project-heading'),

                    ],className='img-cont',href='/useranalysis'
                    ),
                    
                    html.Hr(),
                    html.P('Lorem ipsum dolor sit amet, utroque invidunt at sea, '\
                           'sit tibique appareat et, te eum natum adhuc. Denique '\
                           'eleifend pri cu. Fuisset maluisset percipitur ad qui, '\
                           'magna audiam id mel. Et has partem mucius',
                           style={'font-family':'Georgia','font-size':'16px'}
                    ),
                
                ],style={'max-width':'350px'}),

            ],style={'padding-left':'40px','padding-top':'10px','padding-bottom':'60px',
                    'padding-right':'40px',},justify='evenly'),

            dbc.Row([
                dbc.Col(dbc.Button('MY PORTFOLIO', color='primary',href="/portfolio",
                    ))
            ],class_name='px-0'),

        ],style={'padding-top':'70px','padding-bottom':'80px'},class_name='px-0'),
    ],style={'backgroundColor':'rgba(209, 228, 255, 0.2)'},fluid=True),

    dbc.Container([
    dbc.Container(
        [dbc.Row([
            dbc.Col([
                html.H4('Contact Me'),
                html.Br(),
                html.P('HIEU NGUYEN (NICK)',style={'font-size':'18px',
                                                'font-family':'Georgia','margin-bottom':'0px'}),
                html.P('hieu@nicknguyen.me',style={'font-size':'16px',
                                                'font-family':'Georgia','margin-bottom':'0px'}),
                html.P('https://github.com/nicknguyen22',
                    style={'font-size':'16px', 'font-family':'Georgia','margin-bottom':'0px'}),
                html.P('Christchurch or New Zealand Wide',
                    style={'font-size':'16px','font-family':'Georgia','margin-bottom':'0px'}),
            ],width = 6,style={'text-align':'left'}),

            dbc.Col([
                html.H4('About This Page'),
                html.Br(),
                html.P('This website was coded in Python, Flask Framework, and CSS based on Dash\
                    Plotly. It is hosted on a EC2 instance from Amazon Web Services (AWS).',
                    style={'font-size':'16px', 'font-family':'Georgia'}),
            ],width = 6),

        dbc.Row([
            dcc.Markdown(''' Copyright &copy; 2023 | Nick Nguyen. All rights reserved.''',
               style={'text-align':'center','padding-top':'30px','font-size':'12px'}),
            html.P('Proudly powered by coffee.',style={'text-align':'center',
                                                       'font-size':'12px',
                                                       'margin-top':'-10px'}),
        ])
    ],style={'color':'white', 'padding-top':'50px','padding-bottom':'10px'}),
        ]),
    
],fluid=True,class_name='px-0',style={'backgroundColor':'#444444',},
)
],
fluid=True,
class_name='px-0'
)

