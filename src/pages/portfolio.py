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
        dbc.Container([
            dbc.Accordion(
            [
                dbc.AccordionItem(
                    [
                    dbc.Row([
                        dbc.Col([
                            html.Img(src='/assets/img/tableau_thumb1.jpg', style={'width':'100%',
                                    'max-width':'360px','height':'auto','border-radius':'5px'}),
                            ],style={'min-width':360,'max-width':360}),

                        dbc.Col([
                            html.P('Tableau - How Couples Meet and Stay Together',
                                style = {'font-size':'15px','text-transform':'uppercase',
                                    'font-weight':'700'}),
                            html.P("This Tableau visualisation was generated using the dataset \
                                from the 'How Couples Meet and Stay Together 2017' study of \
                                Stanford University. The visualisation provides a comprehensive \
                                depiction of the evolution of how couples have met and maintained \
                                their relationships from the 1940s to the 2010s.",
                                style={'font-size':'16px','font-family':'Georgia','margin-bottom':'12px'}),
                            dbc.Row([
                                dbc.Col(
                                    dbc.Button(html.Span([html.I(className="fa-solid fa-display me-2"),'Live Preview']),
                                        outline=True, color='primary',
                                        size = 'sm',
                                        className="rounded-pill me-1",
                                        href='https://public.tableau.com/views/HowCouplesMeetandStayTogether_16925005618470/Relationship?:language=en-US&:display_count=n&:origin=viz_share_link',
                                        disabled=False,
                                        target="_blank",
                                        style = {'font-size':'13px','font-weight':'500',
                                                'padding-left':'15px','padding-right':'15px'}),),

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
                                                'padding-left':'15px','padding-right':'15px'}),),
                                    ]),
                                ]),

                            ],style={'padding-bottom':'20px','padding-top':'20px'}),

                    html.Hr(style={'color':'#adadad'}),

                    dbc.Row([
                        dbc.Col([
                            html.Img(src='/assets/img/tableau_thumb2.jpg', style={'width':'100%',
                                    'max-width':'360px','height':'auto','border-radius':'5px'}),
                            ],style={'min-width':360,'max-width':360}),

                        dbc.Col([
                            html.P('Tableau - Summary of Road Accidents in New Zealand from 2001 to 2020',
                                style = {'font-size':'15px','text-transform':'uppercase',
                                    'font-weight':'700'}),
                            html.P("This tableau visualisation was created utilizing the Crash Analysis \
                                System (CAS) map ArcGis dataset, made available by Waka Kotahi (NZTA). The \
                                visualisation offers a thorough portrayal of road accidents that occurred \
                                in New Zealand between 2001 and 2020.",
                                style={'font-size':'16px','font-family':'Georgia','margin-bottom':'12px'}),
                            dbc.Row([
                                dbc.Col(
                                    dbc.Button(html.Span([html.I(className="fa-solid fa-display me-2"),'Live Preview']),
                                        outline=True, color='primary',
                                        size = 'sm',
                                        className="rounded-pill me-1",
                                        href='https://public.tableau.com/shared/5PF7XQC6G?:display_count=n&:origin=viz_share_link',
                                        disabled=False,
                                        target="_blank",
                                        style = {'font-size':'13px','font-weight':'500',
                                                'padding-left':'15px','padding-right':'15px'}),),

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
                                                'padding-left':'15px','padding-right':'15px'}),),
                                    ]),
                                ]),

                            ],style={'padding-bottom':'20px','padding-top':'20px'}),

                    html.Hr(style={'color':'#adadad'}),


                    ],
                    title='Data Visualisation with Python, Tableau and PowerBI',
                ),
            ],flush=True),
        ],style={'backgroundColor':'white'},fluid=False),
    ],style={'padding-top':'20px','padding-bottom':'20px','max-width':'1080px',},
    fluid = True),

    dbc.Container([
        dbc.Container([
            dbc.Accordion(
            [
                dbc.AccordionItem(
                    [
                        html.P("This is the content of the first section"),
                        dbc.Button("Click here"),
                    ],
                    title='Machine Learning with R and Python',
                ),
            ],flush=True,start_collapsed=True),
        ],style={'backgroundColor':'white'},fluid=False),
    ],style={'padding-top':'20px','padding-bottom':'20px','max-width':'1080px',},
    fluid = True),

    dbc.Container([
        dbc.Container([
            dbc.Accordion(
            [
                dbc.AccordionItem(
                    [
                        html.P("This is the content of the first section"),
                        dbc.Button("Click here"),
                    ],
                    title='Distributed computing with Spark',
                ),
            ],flush=True,start_collapsed=True),
        ],style={'backgroundColor':'white'},fluid=False),
    ],style={'padding-top':'20px','padding-bottom':'20px','max-width':'1080px',},
    fluid = True),

    dbc.Container([
        dbc.Container([
            dbc.Accordion(
            [
                dbc.AccordionItem(
                    [
                        html.P("This is the content of the first section"),
                        dbc.Button("Click here"),
                    ],
                    title='Natural Language Processing (NLP) with Python',
                ),
            ],flush=True,start_collapsed=True),
        ],style={'backgroundColor':'white'},fluid=False),
    ],style={'padding-top':'20px','padding-bottom':'20px','max-width':'1080px',},
    fluid = True),

    dbc.Container([
        dbc.Container([
            dbc.Accordion(
            [
                dbc.AccordionItem(
                    [
                        dbc.Row([
                            dbc.Col([
                                html.Img(src='/assets/img/game_thumb1.jpg', style={'width':'100%',
                                        'max-width':'360px','height':'auto','border-radius':'5px'}),
                                ],style={'min-width':360,'max-width':360}),

                            dbc.Col([
                                html.P('Matching Game with Python - Pygame',
                                    style = {'font-size':'15px','text-transform':'uppercase',
                                        'font-weight':'700'}),
                                html.P("I like playing games in my free time to relax, especially ones that \
                                        have puzzles to solve. During my spare moments, I created this Memory \
                                        Matching Game using Python. It's a fun and enjoyable activity that brings \
                                        together Object-Oriented Programming (OOP) and the flexible PyGame library.",
                                    style={'font-size':'16px','font-family':'Georgia','margin-bottom':'12px'}),
                                dbc.Row([
                                    dbc.Col(
                                        dbc.Button(html.Span([html.I(className="fa-solid fa-display me-2"),'Live Preview']),
                                            outline=True, color='primary',
                                            size = 'sm',
                                            className="rounded-pill me-1",
                                            href='',
                                            disabled=True,
                                            target="_blank",
                                            style = {'font-size':'13px','font-weight':'500',
                                                    'padding-left':'15px','padding-right':'15px'}),),

                                    dbc.Col(
                                        dbc.Button(html.Span([html.I(className="fa-brands fa-github me-2"),'Code Repository']), 
                                            outline=True, 
                                            color='primary',
                                            size = 'sm',
                                            className="rounded-pill me-1",
                                            href='https://github.com/nicknguyen22/Python_memory_game.git',
                                            disabled=False,
                                            target="_blank",
                                            style = {'font-size':'13px','font-weight':'500',
                                                    'padding-left':'15px','padding-right':'15px'}),),
                                        ]),
                                    ]),

                        ],style={'padding-bottom':'20px','padding-top':'20px'}),

                    ],
                    title='Python Programming',
                ),
            ],flush=True,start_collapsed=True),
        ],style={'backgroundColor':'white'},fluid=False),
    ],style={'padding-top':'20px','padding-bottom':'20px','max-width':'1080px',},
    fluid = True),

],fluid=True,
class_name='px-0',)