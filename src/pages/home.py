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
                html.Br(),
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
            dbc.Container([
                dbc.Col(dbc.Button('ABOUT ME', outline=False, href="/aboutme", color = 'light',
                                       style={'font-size':'14px', 'font-weight':'500',\
                                              'z-index':'15','color':'#219bff'}))
                ],class_name='px-0',style={'padding-top':'10px',}), 
    
            ],style= {
                'color':'white',
                'padding-top':'110px',
                'padding-bottom':'50px',
                'max-width':'1080px',
                }),
        ],fluid=True,class_name='bg0',style= {
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
                html.Img(src='/assets/img/pytorch_keras.jpg', style={'width':'100%',
                        'max-width':'350px','height':'auto','border-radius':'5px'},
                        className='shadow-sm'),
                ],style={'min-width':350,'max-width':350}),

            dbc.Col([
                html.P('Python - Electricity Spot Price Prediction using TensorFlow & Pytorch LSTM',
                    style = {'font-size':'15px','text-transform':'uppercase',
                        'font-weight':'700'}),
                html.P('This Python notebook demonstrates the use of Long Short-Term Memory (LSTM) networks, a type of \
                    recurrent neural network (RNN), to predict electricity spot prices. The notebook provides \
                    implementations using both TensorFlow and PyTorch, allowing users to compare and contrast the two \
                    popular libraries for LSTM modeling and forecasting.',
                    style={'font-size':'16px','font-family':'Georgia','margin-bottom':'12px'}),
                dbc.Row([
                    dbc.Col(
                        dbc.Button(html.Span([html.I(className="fa-solid fa-display me-2"),'Live Preview']),
                            outline=True, color='primary',
                            size = 'sm',
                            className="rounded-pill me-1",
                            href='https://colab.research.google.com/drive/1Dl1f6UODlIjCP22Vv3YH-ZKVWUd-s3zd?usp=sharing',
                            disabled=False,
                            target="_blank",
                            style = {'font-size':'13px','font-weight':'500',
                                    'padding-left':'10px','padding-right':'10px'}),),

                    dbc.Col(
                        dbc.Button(html.Span([html.I(className="fa-brands fa-github me-2"),'Code Repository']), 
                            outline=True, 
                            color='primary',
                            size = 'sm',
                            className="rounded-pill me-1",
                            href='https://github.com/nicknguyen22/Machine_learning/tree/a43839000bb86188d3d2820e28dee52446378b5f/spotprice_LSTM',
                            disabled=False,
                            target="_blank",
                            style = {'font-size':'13px','font-weight':'500',
                                    'padding-left':'10px','padding-right':'10px'}),),
                        ]),
                    ]),

                ],style={'padding-bottom':'20px','padding-top':'20px'}),

        html.Hr(style={'color':'#adadad'}),

        dbc.Row([
                        dbc.Col([
                            html.Img(src='/assets/img/looker.jpg', style={'width':'100%',
                                    'max-width':'360px','height':'auto','border-radius':'5px'},
                                    className='shadow-sm'),
                            ],style={'min-width':360,'max-width':360}),

                        dbc.Col([
                            html.P('Looker Studio - New Zealand COVID-19 2020 to 2023',
                                style = {'font-size':'15px','text-transform':'uppercase',
                                    'font-weight':'700'}),
                            html.P("Explore the Looker Studio Dashboard, driven by data from the Ministry of Health NZ's \
                                Covid-19 dataset. Dive into comprehensive information on cases, fatalities, and \
                                hospitalisations, segmented by region, district health board, age group, ethnicity, and \
                                more. This dashboard offers valuable insights into how the pandemic has affected NZ.",
                                style={'font-size':'16px','font-family':'Georgia','margin-bottom':'12px'}),
                            dbc.Row([
                                dbc.Col(
                                    dbc.Button(html.Span([html.I(className="fa-solid fa-display me-2"),'Live Preview']),
                                        outline=True, color='primary',
                                        size = 'sm',
                                        className="rounded-pill me-1",
                                        href='https://lookerstudio.google.com/reporting/a67173ac-a815-4920-93ca-5aa685b9b3a7',
                                        disabled=False,
                                        target="_blank",
                                        style = {'font-size':'13px','font-weight':'500',
                                                'padding-left':'10px','padding-right':'10px'}),),

                                dbc.Col(
                                    dbc.Button(html.Span([html.I(className="fa-brands fa-github me-2"),'Code Repository']), 
                                        outline=True, 
                                        color='primary',
                                        size = 'sm',
                                        className="rounded-pill me-1",
                                        href='',
                                        disabled=True,
                                        target="_blank",
                                        style = {'font-size':'13px','font-weight':'500',
                                                'padding-left':'10px','padding-right':'10px'}),),
                                    ]),
                                ]),

                            ],style={'padding-bottom':'20px','padding-top':'20px'}),

            html.Hr(style={'color':'#adadad'}),

        dbc.Row([
                        dbc.Col([
                            html.Img(src='/assets/img/powerbi.jpg', style={'width':'100%',
                                    'max-width':'360px','height':'auto','border-radius':'5px'},
                                    className='shadow-sm'),
                            ],style={'min-width':360,'max-width':360}),

                        dbc.Col([
                            html.P('Power BI & SQL - Rugby Statistic 1871 - 2023',
                                style = {'font-size':'15px','text-transform':'uppercase',
                                    'font-weight':'700'}),
                            html.P("The Power BI Dashboard, utilising a Rugby Kaggle dataset spanning from 1871 to 2023, offers \
                                a detailed analysis of rugby team statistics. It ranks teams based on various performance \
                                metrics, provides head-to-head competition details, and allows users to explore historical \
                                trends and matchups.",
                                style={'font-size':'16px','font-family':'Georgia','margin-bottom':'12px'}),
                            dbc.Row([
                                dbc.Col(
                                    dbc.Button(html.Span([html.I(className="fa-solid fa-display me-2"),'Live Preview']),
                                        outline=True, color='primary',
                                        size = 'sm',
                                        className="rounded-pill me-1",
                                        href='https://app.powerbi.com/view?r=eyJrIjoiZjVmMWMzZTYtNzI2Ni00N2FlLWFhZDMtY2VhNDI3NmVmZjQ0IiwidCI6ImZkZDU3MGNlLTg1ODAtNDM5Ny04MmMyLTQ3MTdmOTUzNzRkNSIsImMiOjEwfQ%3D%3D',
                                        disabled=False,
                                        target="_blank",
                                        style = {'font-size':'13px','font-weight':'500',
                                                'padding-left':'10px','padding-right':'10px'}),),

                                dbc.Col(
                                    dbc.Button(html.Span([html.I(className="fa-brands fa-github me-2"),'Code Repository']), 
                                        outline=True, 
                                        color='primary',
                                        size = 'sm',
                                        className="rounded-pill me-1",
                                        href='',
                                        disabled=True,
                                        target="_blank",
                                        style = {'font-size':'13px','font-weight':'500',
                                                'padding-left':'10px','padding-right':'10px'}),),
                                    ]),
                                ]),

                            ],style={'padding-bottom':'20px','padding-top':'20px'}),

                    # html.Hr(style={'color':'#adadad'}),
         
            dbc.Container([
                dbc.Col(dbc.Button('MY PORTFOLIO', color='primary',href="/portfolio",
                    style={'font-weight':'500', 'font-size':'14px'}))
            ],
            class_name='px-0',
            ),

        ],style={'padding-top':'50px','padding-bottom':'50px','max-width':'1080px',}),
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

                ],style={'text-align':'center','min-width':350,'max-width':350,
                         'padding-left':'10px','padding-right':'10px'}),

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

                ],style={'text-align':'center','min-width':350,'max-width':350,
                         'padding-left':'10px','padding-right':'10px'}),

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

                ],style={'text-align':'center','min-width':350,'max-width':350,
                         'padding-left':'10px','padding-right':'10px'}),


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

                ],style={'text-align':'center','min-width':350,'max-width':350,
                         'padding-left':'10px','padding-right':'10px'}),

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

                ],style={'text-align':'center','min-width':350,'max-width':350,
                         'padding-left':'10px','padding-right':'10px'}),

                dbc.Col([
                    html.Div([
                        DashIconify(icon="carbon:data-center", width=60),
                        html.H4('Database & Data Warehousing',
                                style={'padding-top':'40px','padding-bottom':'20px'}),
                    ],className='areatexticon'),
                    html.P('Understanding their fundamental importance as the bedrock \
                           of effective data management, I am dedicated to delving into \
                           the intricacies of these systems. The prospect of designing \
                           robust data architectures that facilitate efficient storage, \
                           retrieval, and analysis motivates me.'
                           ,style={'font-size':'16px','font-family':'Georgia'}),

                ],style={'text-align':'center','min-width':350,'max-width':350,
                         'padding-left':'10px','padding-right':'10px'}),


            ],justify='evenly'),

        ],style={'padding-top':'50px','padding-bottom':'50px','max-width':'1080px'},
        ),
    ],style={'background-color':'#d1e4ff33'},fluid=True),  

    dbc.Container([
        dbc.Container([
            html.P('SKILLS',style={'font-weight':'500','font-size':'26px','margin-bottom':'5px'}),
            html.P('1 : Basic     2 : Novice     3 : Intermediate     4 : Advanced     5 : Expert',
                   style={'white-space': 'pre','color':'gray','font-size':'13px'}),
            html.Br(),

            dbc.Row([
                dbc.Col([
                    html.P('Data Mining (Python & R) - 4',
                           style={'white-space': 'pre','margin-bottom':'5px'}),
                    html.Div(dbc.Progress(value=4, animated=True,striped=True,max=5),
                             style={'padding-bottom':'30px'}),

                    html.P('Data Wrangling (Python & R) - 5',
                           style={'white-space': 'pre','margin-bottom':'5px'}),
                    html.Div(dbc.Progress(value=5, animated=True,striped=True,max=5),
                             style={'padding-bottom':'30px'}),

                    html.P('Database (MySQL, SQLite & Postgres SQL) - 4',
                           style={'white-space': 'pre', 'margin-bottom':'5px'}),
                    html.Div(dbc.Progress(value=4, animated=True,striped=True,max=5),
                             style={'padding-bottom':'30px'}),

                    html.P('Operating system (Mac OS, Windows & Linux) - 4',
                           style={'white-space': 'pre', 'margin-bottom':'5px'}),
                    html.Div(dbc.Progress(value=4, animated=True,striped=True,max=5),
                             style={'padding-bottom':'30px'}),            
                ],style={'min-width':350,'max-width':350}),

                dbc.Col([
                    html.P('Data Analytics (Python, R & Excel) - 5',
                           style={'white-space': 'pre','margin-bottom':'5px'}),
                    html.Div(dbc.Progress(value=5, animated=True,striped=True,max=5),
                             style={'padding-bottom':'30px'}),

                    html.P('Machine learning & Deep learning - 4',
                           style={'white-space': 'pre','margin-bottom':'5px'}),
                    html.Div(dbc.Progress(value=4, animated=True,striped=True,max=5),
                             style={'padding-bottom':'30px'}),

                    html.P('Programming Language (Python, R & SQL) - 4',
                           style={'white-space': 'pre', 'margin-bottom':'5px'}),
                    html.Div(dbc.Progress(value=4, animated=True,striped=True,max=5),
                             style={'padding-bottom':'30px'}),        
                ],style={'min-width':350,'max-width':350}),

                dbc.Col([
                    html.P('Data Visualisation (PowerBI, Tableau, Python & R) - 5',
                           style={'white-space': 'pre','margin-bottom':'5px'}),
                    html.Div(dbc.Progress(value=5, animated=True,striped=True,max=5),
                             style={'padding-bottom':'30px'}),

                    html.P('Cloud Services (AWS,Azure) - 2',
                           style={'white-space': 'pre','margin-bottom':'5px'}),
                    html.Div(dbc.Progress(value=2, animated=True,striped=True,max=5),
                             style={'padding-bottom':'30px'}),

                    html.P('Distributed Computing (Hadoop, Hive & Spark) - 3',
                           style={'white-space': 'pre', 'margin-bottom':'5px'}),
                    html.Div(dbc.Progress(value=3, animated=True,striped=True,max=5),
                             style={'padding-bottom':'30px'}),                                           
                ],style={'min-width':350,'max-width':350}),

            ],style={},justify='evenly'),

        ],style={'padding-top':'50px','padding-bottom':'50px','max-width':'1080px'},
        ),
    ],style={'backgroundColor':'white'},fluid=True),
    
],
fluid=True,
class_name='px-0'
)



