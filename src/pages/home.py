import dash                                     
from dash import Dash, dcc, html, Input, Output, callback, ctx
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify
import webbrowser


dash.register_page(
    __name__,
    path='/',
    title='Nick Nguyen',)

layout = dbc.Container([
    
    dbc.Container([
        dbc.Container([
            dbc.Row([
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
            dbc.Row([
                    dbc.Col(dbc.Button('ABOUT ME', color='light',href="/aboutme",
                                       style={'font-size':'14px', 'font-weight':'500',\
                                              'color':'#444','z-index':'15'}))
                ],class_name='px-0',style={'padding-top':'10px',}), 
        ],style= {
                'color':'white',
                'padding-top':'110px',
                'padding-left':'50px',
                'padding-bottom':'50px',
                },),
    ],fluid=True,class_name='bg0 px-0',
    style= {
                'width':'100%',
                'height':'100%',
                'max-height':'500px'
                },
    ),

    dbc.Container([
        dbc.Container([
            html.P('MOST RECENT PROJECTS ',style={'font-weight':'500','font-size':'26px'}),
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

            dbc.Container([
                dbc.Col(dbc.Button('MY PORTFOLIO', color='primary',href="/portfolio",
                    style={'font-weight':'500', 'font-size':'14px'}))
            ],
            # class_name='px-0',
            style={'padding-left':'40px'},
            ),

        ],style={'padding-top':'70px','padding-bottom':'80px'},
        # class_name='px-0',
        ),
    ],style={'backgroundColor':'white'},fluid=True),

    dbc.Container([
        dbc.Container([
            html.P('AREAS OF INTEREST',style={'font-size':'26px','font-weight':'500'}),
            
            dbc.Row([
                dbc.Col([
                    html.Div([
                        DashIconify(icon="carbon:chart-multitype", width=60),
                        html.H4('Data Analytics & Visualisation',
                                style={'padding-top':'40px','padding-bottom':'20px'}),
                    ],className='areatexticon'),
                    html.P('Driven by a passion for weaving captivating stories \
                           through data. I relish the challenge of diving into \
                           intricate and diverse datasets, uncovering the essence \
                           of complex issues, and devising pragmatic solutions. \
                           Data speaks volumes, and I take pride in translating \
                           its tale into compelling visualisations that resonate \
                           with others, ensuring clarity and engagement.'
                           ,style={'font-size':'16px','font-family':'Georgia'}),

                ],width=4,style={'text-align':'center','padding-left':'30px',
                                 'padding-right':'30px'}),

                dbc.Col([
                    html.Div([
                        DashIconify(icon="carbon:machine-learning-model", width=60),
                        html.H4('Machine Learning',
                                style={'padding-top':'40px','padding-bottom':'20px'}),
                    ],className='areatexticon'),
                    html.P('Driven by a passion for weaving captivating stories \
                           through data. I relish the challenge of diving into \
                           intricate and diverse datasets, uncovering the essence \
                           of complex issues, and devising pragmatic solutions. \
                           Data speaks volumes, and I take pride in translating \
                           its tale into compelling visualisations that resonate \
                           with others, ensuring clarity and engagement.'
                           ,style={'font-size':'16px','font-family':'Georgia'}),

                ],width=4,style={'text-align':'center','padding-left':'30px',
                                 'padding-right':'30px'}),

                dbc.Col([
                    html.Div([
                        DashIconify(icon="carbon:ibm-watson-natural-language-understanding", width=60),
                        html.H4('Natural Language Processing',
                                style={'padding-top':'40px','padding-bottom':'20px'}),
                    ],className='areatexticon'),
                    html.P('Driven by a passion for weaving captivating stories \
                           through data. I relish the challenge of diving into \
                           intricate and diverse datasets, uncovering the essence \
                           of complex issues, and devising pragmatic solutions. \
                           Data speaks volumes, and I take pride in translating \
                           its tale into compelling visualisations that resonate \
                           with others, ensuring clarity and engagement.'
                           ,style={'font-size':'16px','font-family':'Georgia'}),

                ],width=4,style={'text-align':'center','padding-left':'30px',
                                 'padding-right':'30px'}),


            ],justify='evenly'),
            
            html.Br(),html.Br(),

                        dbc.Row([
                dbc.Col([
                    html.Div([
                        DashIconify(icon="carbon:ibm-cloud-pak-manta-automated-data-lineage", width=60),
                        html.H4('Distributed Computing',
                                style={'padding-top':'40px','padding-bottom':'20px'}),
                    ],className='areatexticon'),
                    html.P('Driven by a passion for weaving captivating stories \
                           through data. I relish the challenge of diving into \
                           intricate and diverse datasets, uncovering the essence \
                           of complex issues, and devising pragmatic solutions. \
                           Data speaks volumes, and I take pride in translating \
                           its tale into compelling visualisations that resonate \
                           with others, ensuring clarity and engagement.'
                           ,style={'font-size':'16px','font-family':'Georgia'}),

                ],width=4,style={'text-align':'center','padding-left':'30px',
                                 'padding-right':'30px'}),

                dbc.Col([
                    html.Div([
                        DashIconify(icon="carbon:cloud-app", width=60),
                        html.H4('Cloud Platforms',
                                style={'padding-top':'40px','padding-bottom':'20px'}),
                    ],className='areatexticon'),
                    html.P('Driven by a passion for weaving captivating stories \
                           through data. I relish the challenge of diving into \
                           intricate and diverse datasets, uncovering the essence \
                           of complex issues, and devising pragmatic solutions. \
                           Data speaks volumes, and I take pride in translating \
                           its tale into compelling visualisations that resonate \
                           with others, ensuring clarity and engagement.'
                           ,style={'font-size':'16px','font-family':'Georgia'}),

                ],width=4,style={'text-align':'center','padding-left':'30px',
                                 'padding-right':'30px'}),

                dbc.Col([
                    html.Div([
                        DashIconify(icon="carbon:data-center", width=60),
                        html.H4('Data Warehousing',
                                style={'padding-top':'40px','padding-bottom':'20px'}),
                    ],className='areatexticon'),
                    html.P('Driven by a passion for weaving captivating stories \
                           through data. I relish the challenge of diving into \
                           intricate and diverse datasets, uncovering the essence \
                           of complex issues, and devising pragmatic solutions. \
                           Data speaks volumes, and I take pride in translating \
                           its tale into compelling visualisations that resonate \
                           with others, ensuring clarity and engagement.'
                           ,style={'font-size':'16px','font-family':'Georgia'}),

                ],width=4,style={'text-align':'center','padding-left':'30px',
                                 'padding-right':'30px'}),


            ],justify='evenly'),

        ],
        # class_name='px-0'
        ),
    ],style={'padding-top':'70px','padding-bottom':'70px','background-color':'#d1e4ff33'},
    fluid=True,),   

    dbc.Container([
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H4('Contact Me'),
                    html.Br(),
                    dbc.Row([
                        html.A(DashIconify(icon="mdi:email", width=30),
                            className="logoicon me-2",id='mailto',href='#0'),

                        dcc.Location(id='hidden-div'),   
                            
                        html.A(DashIconify(icon="mdi:github", width=30),className="logoicon me-2",
                            href='https://github.com/nicknguyen22', target='_blank'),
                        
                        html.A(DashIconify(icon="mdi:linkedin", width=30),className="logoicon me-2",
                            href='https://www.seek.co.nz/profile/hieu-nguyen-VbL4nl8v3p', 
                            target='_blank'),

                    ],style={'display':'inline'}),
            
                ],width = 3,style={'text-align':'left'}),

                dbc.Col([
                    html.H4('About This Page'),
                    html.Br(),
                    html.P('This website was coded in Python, Flask Framework, and CSS based on Dash\
                        Plotly. It is hosted on a EC2 instance from Amazon Web Services (AWS). \
                        Python portfolio web applications are deployed on AWS, while \
                        R Shiny Apps are deployed on Microsoft Azure',
                        style={'font-size':'16px', 'font-family':'Georgia'}),
                ],width = 9),

            dbc.Row([
                dcc.Markdown(''' Copyright &copy; 2023 | Nick Nguyen. All rights reserved.''',
                style={'text-align':'center','padding-top':'30px','font-size':'12px'}),
                html.P('Proudly powered by coffee.',style={'text-align':'center',
                                                        'font-size':'12px',
                                                        'margin-top':'-10px'}),
            ])
        ],style={'color':'white', 'padding-top':'50px','padding-bottom':'10px'}),
            ],
            # class_name='px-0'
            ),
    
    ],fluid=True,
    class_name='px-0',
    style={'backgroundColor':'#444444',},
    )
],
fluid=True,
class_name='px-0'
)

@callback(
    Output('hidden-div','href'),
    Input('mailto', 'n_clicks'),
)
def mailto_button(btn1):
    if 'mailto' == ctx.triggered_id:
        return 'mailto:hieu@nicknguyen.me'

