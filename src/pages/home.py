from dash import Dash, dcc, html, Input, Output, callback, ctx
import dash
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify


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
                            html.Img(src='/assets/img/spt_prc.jpg', style={'width':'100%','max-width':'350px','height':'auto'}),
                        ],className='img'),

                        html.Div('Deep Learning with TensorFlow LSTM and Electricity Spot Price',
                                     className='project-heading'),

                    ],className='img-cont',href='/spt_prc'
                    ),
                ],style={'min-width':360,'max-width':360}),

                dbc.Col([
                    html.A([

                        html.Div([
                            html.Img(src='/assets/img/viz_1.jpg', style={'width':'100%','max-width':'350px','height':'auto'}),
                        ],className='img'),

                        html.Div('Electricity Generation & Carbon Emission 2002-2022 '\
                                 'Visualisation', className='project-heading'),

                    ],className='img-cont',href='/portfolio/carb-emission'
                    ),
                ],style={'min-width':360,'max-width':360}),

                dbc.Col([
                    html.A([

                        html.Div([
                            html.Img(src='/assets/img/viz_2.jpg', style={'width':'100%','max-width':'350px','height':'auto'}),
                        ],className='img'),

                        html.Div('Analysing Electricity Usage Patterns and '\
                                 'Interacting with Data Tables', className='project-heading'),

                    ],className='img-cont',href='/useranalysis'
                    ),
                ],style={'min-width':360,'max-width':360}),

            ],style={'padding-left':'40px','padding-top':'10px','padding-bottom':'30px',
                    'padding-right':'40px',},justify='evenly'),

            dbc.Container([
                dbc.Col(dbc.Button('MY PORTFOLIO', color='primary',href="/portfolio",
                    style={'font-weight':'500', 'font-size':'14px'}))
            ],
            # class_name='px-0',
            style={'padding-left':'40px'},
            ),

        ],style={'padding-top':'50px','padding-bottom':'50px'},
        # class_name='px-0',
        ),
    ],style={'backgroundColor':'white'},fluid=True),

    dbc.Container([
        dbc.Container([
            html.P('AREAS OF INTEREST',style={'font-size':'26px','font-weight':'500'}),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        DashIconify(icon="carbon:chart-multitype", width=60),
                        html.H4('Data Analytics & Visualisation',
                                style={'padding-top':'40px','padding-bottom':'20px'}),
                    ],className='areatexticon'),
                    html.P('Passionate about crafting compelling data narratives, \
                           I thrive on delving into intricate datasets to unveil \
                           solutions for complex problems. I take pride in \
                           transforming data into engaging visualizations that \
                           resonate and communicate effectively.'
                           ,style={'font-size':'16px','font-family':'Georgia'}),

                ],style={'text-align':'center','min-width':360,'max-width':360}),

                dbc.Col([
                    html.Div([
                        DashIconify(icon="carbon:machine-learning-model", width=60),
                        html.H4('Machine Learning & Deep Learning',
                                style={'padding-top':'40px','padding-bottom':'20px'}),
                    ],className='areatexticon'),
                    html.P('I delve into their complexities to drive impactful \
                           contributions in technology. The potential for industry \
                           revolution and innovation within these fields captivates \
                           me, prompting me to stay updated and embark on \
                           transformative personal projects.'
                           ,style={'font-size':'16px','font-family':'Georgia'}),

                ],style={'text-align':'center','min-width':360,'max-width':360}),

                dbc.Col([
                    html.Div([
                        DashIconify(icon="carbon:ibm-watson-natural-language-understanding", width=60),
                        html.H4('Natural Language Processing',
                                style={'padding-top':'40px','padding-bottom':'20px'}),
                    ],className='areatexticon'),
                    html.P('Fascinated by the nuances of communication, the ability \
                           to imbue machines with the understanding of human \
                           language opens avenues for enhanced interactions and \
                           insights. I am driven to learn the depths of NLP, \
                           exploring its potential in reshaping how we interact with \
                           technology and information.'
                           ,style={'font-size':'16px','font-family':'Georgia'}),

                ],style={'text-align':'center','min-width':360,'max-width':360}),


            ],justify='evenly'),
            
            html.Br(),html.Br(),

            dbc.Row([
                dbc.Col([
                    html.Div([
                        DashIconify(icon="carbon:ibm-cloud-pak-manta-automated-data-lineage", width=60),
                        html.H4('Distributed Computing',
                                style={'padding-top':'40px','padding-bottom':'20px'}),
                    ],className='areatexticon'),
                    html.P('Acknowledging its potential to extract insights from \
                           extensive datasets, expedite data processing, and elevate \
                           analytical capacities, I am committed to delving into \
                           and mastering the complexities of distributed systems. \
                           My goal is to adeptly employ this knowledge to streamline \
                           the efficient processing and analysis of substantial datasets.'
                           ,style={'font-size':'16px','font-family':'Georgia'}),

                ],style={'text-align':'center','min-width':360,'max-width':360}),

                dbc.Col([
                    html.Div([
                        DashIconify(icon="carbon:cloud-app", width=60),
                        html.H4('Cloud Services',
                                style={'padding-top':'40px','padding-bottom':'20px'}),
                    ],className='areatexticon'),
                    html.P('I am deeply intrigued by the realm of Cloud Services, \
                           including industry leaders like AWS, Azure, and Google Cloud. \
                           Recognising their pivotal role in revolutionising how \
                           businesses operate and scale, I am interested in understanding \
                           their diverse tools to design innovative solutions, \
                           optimise performance, and ensure seamless scalability.'
                           ,style={'font-size':'16px','font-family':'Georgia'}),

                ],style={'text-align':'center','min-width':360,'max-width':360}),

                dbc.Col([
                    html.Div([
                        DashIconify(icon="carbon:data-center", width=60),
                        html.H4('Database Design & Data Warehousing',
                                style={'padding-top':'40px','padding-bottom':'20px'}),
                    ],className='areatexticon'),
                    html.P('Understanding their fundamental importance as the bedrock \
                           of effective data management, I am dedicated to delving into \
                           the intricacies of these systems. The prospect of designing \
                           robust data architectures that facilitate efficient storage, \
                           retrieval, and analysis motivates me.'
                           ,style={'font-size':'16px','font-family':'Georgia'}),

                ],style={'text-align':'center','min-width':360,'max-width':360}),


            ],justify='evenly'),

        ],
        # class_name='px-0'
        ),
    ],style={'padding-top':'50px','padding-bottom':'50px','background-color':'#d1e4ff33'},
    fluid=True,),   

    dbc.Container([
        dbc.Container([
            html.P('SKILLS',style={'font-weight':'500','font-size':'26px','margin-bottom':'5px'}),
            html.P('1 - Basic       2 - Novice      3 - Intermediate        4 - Advanced        5 - Expert',
                   style={'white-space': 'pre','color':'gray','font-size':'13px'}),
            html.Br(),

            dbc.Row([
                dbc.Col([
                    html.P('Data Mining (Python and R) - 4',
                           style={'white-space': 'pre','margin-bottom':'5px'}),
                    html.Div(dbc.Progress(value=4, animated=True,striped=True,max=5),
                             style={'padding-bottom':'30px'}),

                    html.P('Data Wrangling (Python and R) - 5',
                           style={'white-space': 'pre','margin-bottom':'5px'}),
                    html.Div(dbc.Progress(value=5, animated=True,striped=True,max=5),
                             style={'padding-bottom':'30px'}),

                    html.P('Database (MySQL, SQLite and Postgres SQL) - 4',
                           style={'white-space': 'pre', 'margin-bottom':'5px'}),
                    html.Div(dbc.Progress(value=4, animated=True,striped=True,max=5),
                             style={'padding-bottom':'30px'}),

                    html.P('Operating system (Mac OS, Windows and Linux) - 4',
                           style={'white-space': 'pre', 'margin-bottom':'5px'}),
                    html.Div(dbc.Progress(value=4, animated=True,striped=True,max=5),
                             style={'padding-bottom':'30px'}),            
                ],style={'min-width':360,'max-width':360}),

                dbc.Col([
                    html.P('Data Analytics (Python, R and Excel) - 5',
                           style={'white-space': 'pre','margin-bottom':'5px'}),
                    html.Div(dbc.Progress(value=5, animated=True,striped=True,max=5),
                             style={'padding-bottom':'30px'}),

                    html.P('Machine learning & Deep learning - 4',
                           style={'white-space': 'pre','margin-bottom':'5px'}),
                    html.Div(dbc.Progress(value=4, animated=True,striped=True,max=5),
                             style={'padding-bottom':'30px'}),

                    html.P('Programming Language (Python, R and SQL) - 4',
                           style={'white-space': 'pre', 'margin-bottom':'5px'}),
                    html.Div(dbc.Progress(value=4, animated=True,striped=True,max=5),
                             style={'padding-bottom':'30px'}),        
                ],style={'min-width':360,'max-width':360}),

                dbc.Col([
                    html.P('Data Visualisation (Power BI, Tableau, Python,and R) - 5',
                           style={'white-space': 'pre','margin-bottom':'5px'}),
                    html.Div(dbc.Progress(value=5, animated=True,striped=True,max=5),
                             style={'padding-bottom':'30px'}),

                    html.P('Cloud Services (AWS,Azure) - 2',
                           style={'white-space': 'pre','margin-bottom':'5px'}),
                    html.Div(dbc.Progress(value=2, animated=True,striped=True,max=5),
                             style={'padding-bottom':'30px'}),

                    html.P('Distributed Computing (Hadoop,Hive and Spark) - 3',
                           style={'white-space': 'pre', 'margin-bottom':'5px'}),
                    html.Div(dbc.Progress(value=3, animated=True,striped=True,max=5),
                             style={'padding-bottom':'30px'}),                                           
                ],style={'min-width':360,'max-width':360}),

            ],style={},justify='evenly'),

        ],style={'padding-top':'50px','padding-bottom':'50px'},
        # class_name='px-0',
        ),
    ],style={'backgroundColor':'white'},fluid=True),
    
    dbc.Container([
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H4('Contact Me',style={'padding-bottom':'5px'}),
                    dbc.Row([
                        dcc.Location(id='hidden-div'),   
                        html.A(DashIconify(icon="mdi:email", width=30),
                            className="logoicon px-2",id='mailto',href='#0'),
                            
                        html.A(DashIconify(icon="mdi:github", width=30),className="logoicon px-2",
                            href='https://github.com/nicknguyen22', target='_blank'),
                        
                        html.A(DashIconify(icon="mdi:linkedin", width=30),className="logoicon px-2",
                            href='https://www.seek.co.nz/profile/hieu-nguyen-VbL4nl8v3p', 
                            target='_blank'),

                    ],style={'display':'inline'}),
            
                ],style={'text-align':'left','min-width':360,'max-width':360,'padding-top':'50px'}),

                dbc.Col([
                    html.H4('About This Page',style={'padding-bottom':'5px'}),
                    html.P('This website was coded in Python, Flask Framework, and CSS based on Dash\
                        Plotly. It is hosted on a EC2 instance from Amazon Web Services (AWS). \
                        Python portfolio web applications are deployed on AWS, while \
                        R Shiny Apps are deployed on Microsoft Azure',
                        style={'font-size':'16px', 'font-family':'Georgia'}),
                ],style={'padding-top':'50px'}),

            dbc.Row([
                dcc.Markdown(''' Copyright &copy; 2023 | Nick Nguyen. All rights reserved.''',
                style={'text-align':'center','padding-top':'30px','font-size':'12px'}),
                html.P('Proudly powered by coffee.',style={'text-align':'center',
                                                        'font-size':'12px',
                                                        'margin-top':'-10px'}),
            ])
        ],style={'color':'white','padding-bottom':'10px'}),
            ],
            # class_name='px-0'
            ),
    
    ],fluid=True,
    class_name='px-0',
    style={'backgroundColor':'#444444',},
    ),

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

