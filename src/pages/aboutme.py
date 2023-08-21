from dash import Dash, dcc, html, Input, Output, callback
import dash
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path='/aboutme',
    title='About Me',)

layout = dbc.Container([
    # Header
    dbc.Container([
        dbc.Container([
            html.Div(className='slider-thumb1 px-0'),
            html.Div(className='slider-thumb2 px-0'),
            html.P('About Me',
                style={'color':'white','font-weight':'700', 'font-size':'60px',},
                className='page-name'),
        ],fluid = True, #style={'max-width':'1080px'},
         class_name='px-0'),
    ],class_name='bg1 px-0',fluid=True),

    # Personal Statement
    dbc.Container([
        dbc.Container([
            html.P('PERSONAL STATEMENT',style={'font-size':'26px','font-weight':'500',
            'padding-bottom':'10px'}),
              
            html.P("I've enthusiastically delved into the exciting world of data \
                science. With a master's degree and over 15 years of experience \
                in various fields like banking, pharmaceuticals, real estate, \
                and retail, I'm a determined data scientist. My goal is to use \
                my expertise to solve practical business problems by combining \
                data science skills with real-world business knowledge.",
                style={'padding-top':'0px','font-family':'Georgia',
                    'font-size':'16px'}),
            html.P("My unique background drives me to constantly learn and \
                collaborate with others. I'm passionate about using the latest \
                technologies to make positive changes and contribute to society \
                through data-driven projects. My main aim is to bridge the gap \
                between data science and business, effectively addressing real \
                corporate challenges and providing valuable solutions.",
                style={'padding-bottom':'0px','font-family':'Georgia',
                    'font-size':'16px'}),
        ],fluid=False,style={'padding-top':'50px','padding-bottom':'50px',
                            'max-width':'1080px'}, className ='px-0',
        ),
    ],fluid=True,),

    # Working Experience 
    dbc.Container([

        dbc.Container([
            html.P('EXPERIENCE',style={'font-size':'26px','font-weight':'500',
            'padding-bottom':'10px',}),

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

            ],className='timeline timeline-split'),

            ],fluid=False,class_name='timelines',style={'padding-top':'50px','padding-bottom':'50px',
            'max-width':'1080px'}),

        ],style={'background-color':'#d1e4ff33'},fluid=True),

],fluid=True,
class_name='px-0',)