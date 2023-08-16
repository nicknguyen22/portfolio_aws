from dash import Dash, dcc, html, Input, Output, callback
import dash
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path='/aboutme',
    title='About Me',)

layout = dbc.Container([
    dbc.Container([
            html.Div(className='slider-thumb1'),
            html.Div(className='slider-thumb2'),
            html.P('About Me',style={'color':'white','font-weight':'700', 'font-size':'60px',
                                     },className='page-name'),
        ],class_name='bg1 px-0',fluid=True),

    dbc.Container([
        dbc.Container([
            html.P('PERSONAL STATEMENT',style={'font-size':'26px','font-weight':'500','padding-bottom':'10px'}),
        ],fluid=False),
      
            html.P("Diving headfirst into the captivating realm of data science, \
                fortified with a master's degree and bolstered by over 15 years of \
                versatile experience spanning pharmaceuticals, banking, real estate, \
                and retail, I stand as a resolute data scientist committed to \
                unraveling real-world business conundrums through the fusion of data \
                science prowess and pragmatic business insights.",
                style={'padding-left':'40px','padding-top':'0px','font-family':'Georgia',
                    'font-size':'16px'}),
            html.P("My distinct background propels my unwavering dedication to \
                continuous evolution and collaborative pursuits. Fueled by an \
                ardent drive to harness cutting-edge technologies, my primary \
                focus resides in effecting positive metamorphoses and contributing \
                to societal progress through data-centric endeavors. My paramount \
                objective revolves around bridging the chasm between the realms \
                of data science and business acumen, adeptly addressing authentic \
                corporate challenges and delivering invaluable resolutions.",
                style={'padding-left':'40px','padding-bottom':'0px','font-family':'Georgia',
                    'font-size':'16px'}),
        ],style={'padding-top':'50px','padding-bottom':'50px',},fluid=False,),

    dbc.Container([

        dbc.Container([
            html.P('EXPERIENCE',style={'font-size':'26px','font-weight':'500','padding-bottom':'10px'}),
        ],fluid=False),
        dbc.Container([

            html.Ul([
                
                html.Li([
                    html.Div(className='timeline-info'),
                    html.Div(className='timeline-marker'),
                    html.Div(
                        html.H2('2023',className='timeline-title'),
                        className='timeline-content',
                    ),
                ],className='timeline-item period'),

                html.Li([
                    html.Div(
                        html.Span('Feb 2022 - Feb 2023'),className='timeline-info'
                    ),
                    html.Div(className='timeline-marker'),
                    html.Div([
                        html.H5('Master of Applied Data Science',className='timeline-title'),
                        html.P('University of Canterbury, New Zealand',style={'padding-top':'10px',
                                                                 'font-size':'16px'}),
                        html.P('Graduation with Distinction',style={'font-family':'Georgia',
                                                                    'font-size':'16px'}),
                    ],className='timeline-content'),
                ],className='timeline-item'),

                html.Li([
                    html.Div(
                        html.Span('Nov 2022 - Present'),className='timeline-info'
                    ),
                    html.Div(className='timeline-marker'),
                    html.Div([
                        html.H5('Data Scientist',className='timeline-title'),
                        html.P('Nexbe Ltd., New Zealand',style={'padding-top':'10px',
                                                                'font-size':'16px'}),
                    ],className='timeline-content'),
                ],className='timeline-item'),

                html.Li([
                    html.Div(className='timeline-info'),
                    html.Div(className='timeline-marker'),
                    html.Div(
                        html.H2('2022',className='timeline-title'),
                        className='timeline-content',
                    ),
                ],className='timeline-item period'),

                html.Li([
                    html.Div(
                        html.Span('Mar 2018 - Feb 2022'),className='timeline-info'
                    ),
                    html.Div(className='timeline-marker'),
                    html.Div([
                        html.H5('Advisor to The Chairman',className='timeline-title'),
                        html.P('Nadyphar JSC., Vietnam',style={'padding-top':'10px',
                                                                'font-size':'16px'}),
                    ],className='timeline-content'),
                ],className='timeline-item'),

                html.Li([
                    html.Div(
                        html.Span('Apr 2018 - March 2021'),className='timeline-info'
                    ),
                    html.Div(className='timeline-marker'),
                    html.Div([
                        html.H5('Founder & Strategic Development Director',className='timeline-title'),
                        html.P('Acexis JSC., Vietnam',style={'padding-top':'10px',
                                                                'font-size':'16px'}),
                    ],className='timeline-content'),
                ],className='timeline-item'),

                html.Li([
                    html.Div(className='timeline-info'),
                    html.Div(className='timeline-marker'),
                    html.Div(
                        html.H2('2018',className='timeline-title'),
                        className='timeline-content',
                    ),
                ],className='timeline-item period'),

                html.Li([
                    html.Div(
                        html.Span('Aug 2016 - Feb 2018'),className='timeline-info'
                    ),
                    html.Div(className='timeline-marker'),
                    html.Div([
                        html.H5('Multichannel Marketing & Project Manager',className='timeline-title'),
                        html.P('GSK (GlaxoSmithKline), Vietnam',style={'padding-top':'10px',
                                                                'font-size':'16px'}),
                    ],className='timeline-content'),
                ],className='timeline-item'),

                html.Li([
                    html.Div(className='timeline-info'),
                    html.Div(className='timeline-marker'),
                    html.Div(
                        html.H2('2016',className='timeline-title'),
                        className='timeline-content',
                    ),
                ],className='timeline-item period'),                

                html.Li([
                    html.Div(
                        html.Span('July 2013 - Aug 2016'),className='timeline-info'
                    ),
                    html.Div(className='timeline-marker'),
                    html.Div([
                        html.H5('Business Development & Project Manager',className='timeline-title'),
                        html.P('GSK (GlaxoSmithKline), Vietnam',style={'padding-top':'10px',
                                                                'font-size':'16px'}),
                    ],className='timeline-content'),
                ],className='timeline-item'),

                html.Li([
                    html.Div(className='timeline-info'),
                    html.Div(className='timeline-marker'),
                    html.Div(
                        html.H2('2013',className='timeline-title'),
                        className='timeline-content',
                    ),
                ],className='timeline-item period'),     

                html.Li([
                    html.Div(
                        html.Span('July 2012 - Nov 2013'),className='timeline-info'
                    ),
                    html.Div(className='timeline-marker'),
                    html.Div([
                        html.H5('Master of Business Administration',className='timeline-title'),
                        html.P('University of Gloucestershire, United Kingdom',
                               style={'padding-top':'10px','font-size':'16px'}),
                        html.P('Graduation with Merit',style={'font-family':'Georgia',
                                                                    'font-size':'16px'}),
                    ],className='timeline-content'),
                ],className='timeline-item'),

                html.Li([
                    html.Div(className='timeline-info'),
                    html.Div(className='timeline-marker'),
                    html.Div(
                        html.H2('2012',className='timeline-title'),
                        className='timeline-content',
                    ),
                ],className='timeline-item period'),

                html.Li([
                    html.Div(
                        html.Span('Nov 2010 - Apr 2013'),className='timeline-info'
                    ),
                    html.Div(className='timeline-marker'),
                    html.Div([
                        html.H5('Business Development & Project Manager',className='timeline-title'),
                        html.P('GB Corporation JSC., Vietnam',
                               style={'padding-top':'10px','font-size':'16px'}),
                    ],className='timeline-content'),
                ],className='timeline-item'),

                html.Li([
                    html.Div(className='timeline-info'),
                    html.Div(className='timeline-marker'),
                    html.Div(
                        html.H2('2010',className='timeline-title'),
                        className='timeline-content',
                    ),
                ],className='timeline-item period'),                

                html.Li([
                    html.Div(
                        html.Span('Mar 2009 - Oct 2010'),className='timeline-info'
                    ),
                    html.Div(className='timeline-marker'),
                    html.Div([
                        html.H5('Head Of Management Information Service & Assistant '\
                                'to Chief Operating Officer',className='timeline-title'),
                        html.P('An Binh JS. Commercial Bank, Vietnam',
                               style={'padding-top':'10px','font-size':'16px'}),
                    ],className='timeline-content'),
                ],className='timeline-item'),

                html.Li([
                    html.Div(className='timeline-info'),
                    html.Div(className='timeline-marker'),
                    html.Div(
                        html.H2('2009',className='timeline-title'),
                        className='timeline-content',
                    ),
                ],className='timeline-item period'),

                html.Li([
                    html.Div(
                        html.Span('Nov 2007 - Feb 2009'),className='timeline-info'
                    ),
                    html.Div(className='timeline-marker'),
                    html.Div([
                        html.H5('Head of Capital Market Technical Business Analyst',className='timeline-title'),
                        html.P('Sacombank Securities JSC., Vietnam',
                               style={'padding-top':'10px','font-size':'16px'}),
                    ],className='timeline-content'),
                ],className='timeline-item'),

                html.Li([
                    html.Div(className='timeline-info'),
                    html.Div(className='timeline-marker'),
                    html.Div(
                        html.H2('2007',className='timeline-title'),
                        className='timeline-content',
                    ),
                ],className='timeline-item period'),

                html.Li([
                    html.Div(
                        html.Span('July 2004 - July 2007'),className='timeline-info'
                    ),
                    html.Div(className='timeline-marker'),
                    html.Div([
                        html.H5('Bachelor of Business in Finance',className='timeline-title'),
                        html.P('Unitec Institute of Technology, New Zealand',
                               style={'padding-top':'10px','font-size':'16px'}),
                        html.P('Graduation with Merit',style={'font-family':'Georgia',
                                                                    'font-size':'16px'}),
                    ],className='timeline-content'),
                ],className='timeline-item'),

                html.Li([
                    html.Div(className='timeline-info'),
                    html.Div(className='timeline-marker'),
                    html.Div(
                        html.H2('2004',className='timeline-title'),
                        className='timeline-content',
                    ),
                ],className='timeline-item period'),

            ],className='timeline timeline-split',),

        ],fluid=False,class_name='timelines',style={'padding-left':'50px'}),
    ],style={'padding-top':'50px','padding-bottom':'50px','backgroundColor':'rgba(209, 228, 255, 0.2)'}
    ,fluid=True,
    ),

],fluid=True,
class_name='px-0',)