from dash import Dash, dcc, html, Input, Output, callback
import dash
import dash_bootstrap_components as dbc
# from pathlib import Path
# import flask
# import os

dash.register_page(
    __name__,
    path='/portfolio',
    title='Portfolio',)

layout = dbc.Container([

    # Header
    dbc.Container([
        dbc.Container([
            html.Div(className='slider-thumb1 px-0'),
            html.Div(className='slider-thumb2 px-0'),
            html.P('Portfolio',
                style={'color':'white','font-weight':'700', 'font-size':'60px',},
                className='page-name'),
        ], fluid = True,
        #style={'max-width':'1080px'},
        class_name='px-0'),
        ],class_name='bg2 px-0',fluid=True),

    # All Accordions
    dbc.Container([

        dbc.Container([
            dbc.Accordion(
            [
                dbc.AccordionItem(
                    [
                    # Looker Studio 
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

                    # Power BI 1
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

                    html.Hr(style={'color':'#adadad'}),


                    # Power BI 2
                    dbc.Row([
                        dbc.Col([
                            html.Img(src='/assets/img/powerbi.jpg', style={'width':'100%',
                                    'max-width':'360px','height':'auto','border-radius':'5px'},
                                    className='shadow-sm'),
                            ],style={'min-width':360,'max-width':360}),

                        dbc.Col([
                            html.P('Power BI & SQL - eCommerce YTD Sales & Sales Breakdown Analysis',
                                style = {'font-size':'15px','text-transform':'uppercase',
                                    'font-weight':'700'}),
                            html.P("This visualisation is a comprehensive data analytics project that leverages \
                                mock-up data to provide valuable insights into the sales performance of an \
                                eCommerce business over a two-year period. This analysis combines the power \
                                of Microsoft Power BI and SQL to extract, transform, and visualize data for \
                                decision-makers.",
                                style={'font-size':'16px','font-family':'Georgia','margin-bottom':'12px'}),
                            dbc.Row([
                                dbc.Col(
                                    dbc.Button(html.Span([html.I(className="fa-solid fa-display me-2"),'Live Preview']),
                                        outline=True, color='primary',
                                        size = 'sm',
                                        className="rounded-pill me-1",
                                        href='https://app.powerbi.com/view?r=eyJrIjoiOGVhOTkwZjMtNmUwZC00Njg0LWI1NGYtYWRjNzJjMjcxZmRlIiwidCI6ImZkZDU3MGNlLTg1ODAtNDM5Ny04MmMyLTQ3MTdmOTUzNzRkNSIsImMiOjEwfQ%3D%3D',
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

                    # Python 1
                    dbc.Row([
                        dbc.Col([
                            html.Img(src='/assets/img/py_plotly.jpg', style={'width':'100%',
                                    'max-width':'360px','height':'auto','border-radius':'5px'},
                                    className='shadow-sm'),
                            ],style={'min-width':360,'max-width':360}),

                        dbc.Col([
                            html.P('Python & SQL - Electricity Generation & Carbon Emissions: 2002 - 2022 ',
                                style = {'font-size':'15px','text-transform':'uppercase',
                                    'font-weight':'700'}),
                            html.P("Powering this Python dashboard is a dataset derived from SQL queries \
                                applied to wrangled data on electricity generation, sourced from the \
                                Electricity Authority. These visuals provide information on \
                                electricity generation, carbon emissions, carbon intensity, and electricity \
                                spot prices, all presented with detailed breakdown to trading periods.",
                                style={'font-size':'16px','font-family':'Georgia','margin-bottom':'12px'}),
                            dbc.Row([
                                dbc.Col(
                                    dbc.Button(html.Span([html.I(className="fa-solid fa-display me-2"),'Live Preview']),
                                        outline=True, color='primary',
                                        size = 'sm',
                                        className="rounded-pill me-1",
                                        href='https://u9vrdlgso2.execute-api.ap-southeast-2.amazonaws.com/eleccarb',
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
                                        href='https://github.com/nicknguyen22/DashApps_AWSLambda_ver/tree/82a92bada6f972d764611f2f8f974c2529d13245/Electricity_carbon_emis',
                                        disabled=False,
                                        target="_blank",
                                        style = {'font-size':'13px','font-weight':'500',
                                                'padding-left':'10px','padding-right':'10px'}),),
                                    ]),
                                ]),

                            ],style={'padding-bottom':'20px','padding-top':'20px'}),

                    html.Hr(style={'color':'#adadad'}),

                    # Python 2
                    dbc.Row([
                        dbc.Col([
                            html.Img(src='/assets/img/py_plotly.jpg', style={'width':'100%',
                                    'max-width':'360px','height':'auto','border-radius':'5px'},
                                    className='shadow-sm'),
                            ],style={'min-width':360,'max-width':360}),

                        dbc.Col([
                            html.P('Python - Electricity Consumption vs. Solar power generation ',
                                style = {'font-size':'15px','text-transform':'uppercase',
                                    'font-weight':'700'}),
                            html.P("This dashboard offers a comprehensive breakdown at the trading period \
                                level, showcasing the consumption and generation of electricity by various \
                                solar panel arrays. It also illustrates the potential cost and revenue \
                                outcomes from exporting surplus electricity back to the grid. This real-world \
                                case study is based on an anonymous ICP's data.",
                                style={'font-size':'16px','font-family':'Georgia','margin-bottom':'12px'}),
                            dbc.Row([
                                dbc.Col(
                                    dbc.Button(html.Span([html.I(className="fa-solid fa-display me-2"),'Live Preview']),
                                        outline=True, color='primary',
                                        size = 'sm',
                                        className="rounded-pill me-1",
                                        href='https://2vxgeto5k7.execute-api.ap-southeast-2.amazonaws.com/ksviz',
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
                                        href='https://github.com/nicknguyen22/DashApps_AWSLambda_ver/tree/82a92bada6f972d764611f2f8f974c2529d13245/KS_viz',
                                        disabled=False,
                                        target="_blank",
                                        style = {'font-size':'13px','font-weight':'500',
                                                'padding-left':'10px','padding-right':'10px'}),),
                                    ]),
                                ]),

                            ],style={'padding-bottom':'20px','padding-top':'20px'}),

                    html.Hr(style={'color':'#adadad'}),

                    # Python 3
                    dbc.Row([
                        dbc.Col([
                            html.Img(src='/assets/img/py_plotly.jpg', style={'width':'100%',
                                    'max-width':'360px','height':'auto','border-radius':'5px'},
                                    className='shadow-sm'),
                            ],style={'min-width':360,'max-width':360}),

                        dbc.Col([
                            html.P('Python - Recognition and Customisation of Electricity Consumption Patterns ',
                                style = {'font-size':'15px','text-transform':'uppercase',
                                    'font-weight':'700'}),
                            html.P("Using genuine anonymous household electricity usage logs, this visualization \
                                detects consumption patterns. It applies these patterns to diverse electricity \
                                plans, predicting yearly bills and associated carbon emissions. Adjusting the \
                                pattern reveals potential cost savings under new usage patterns.",
                                style={'font-size':'16px','font-family':'Georgia','margin-bottom':'12px'}),
                            dbc.Row([
                                dbc.Col(
                                    dbc.Button(html.Span([html.I(className="fa-solid fa-display me-2"),'Live Preview']),
                                        outline=True, color='primary',
                                        size = 'sm',
                                        className="rounded-pill me-1",
                                        href='http://13.55.49.102:8050/icpanalysis/',
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
                                        href='https://github.com/nicknguyen22/DashApps_AWSLambda_ver/tree/82a92bada6f972d764611f2f8f974c2529d13245/ICP_usage_analysis',
                                        disabled=False,
                                        target="_blank",
                                        style = {'font-size':'13px','font-weight':'500',
                                                'padding-left':'10px','padding-right':'10px'}),),
                                    ]),
                                ]),

                            ],style={'padding-bottom':'20px','padding-top':'20px'}),

                    html.Hr(style={'color':'#adadad'}),

                    # Tableau 1
                    dbc.Row([
                        dbc.Col([
                            html.Img(src='/assets/img/tableau.jpg', style={'width':'100%',
                                    'max-width':'360px','height':'auto','border-radius':'5px'},
                                    className='shadow-sm'),
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

                    # Tableau 2
                    dbc.Row([
                        dbc.Col([
                            html.Img(src='/assets/img/tableau.jpg', style={'width':'100%',
                                    'max-width':'360px','height':'auto','border-radius':'5px'},
                                    className='shadow-sm'),
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


                    ],
                    title='Data Analysis & Visualisation with Python, Tableau, PowerBI and Looker Studio',
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
                    # Data project
                    dbc.Row([
                        dbc.Col([
                            html.Img(src='/assets/img/r_julia.jpg', style={'width':'100%',
                                    'max-width':'360px','height':'auto','border-radius':'5px'},
                                    className='shadow-sm'),
                            ],style={'min-width':360,'max-width':360}),

                        dbc.Col([
                            html.P('R, Julia and SQL  - New Zealand Crash Analysis System (CAS) Data wrangling',
                                style = {'font-size':'15px','text-transform':'uppercase',
                                    'font-weight':'700'}),
                            html.P("This project focuses on handling and transforming data from multiple \
                                sources. Data sources involved Crash Analysis System (CAS) data from NZ, \
                                regional population statistics, and Vehicle Kilometer Travelled (VKT). \
                                This project is utilising a combination of R & Julia for web scraping, \
                                ArcGIS API requests, and SQL database creation .",
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
                                                'padding-left':'10px','padding-right':'10px'}),),

                                dbc.Col(
                                    dbc.Button(html.Span([html.I(className="fa-brands fa-github me-2"),'Code Repository']), 
                                        outline=True, 
                                        color='primary',
                                        size = 'sm',
                                        className="rounded-pill me-1",
                                        href='https://github.com/nicknguyen22/Data-wrangling.git',
                                        disabled=False,
                                        target="_blank",
                                        style = {'font-size':'13px','font-weight':'500',
                                                'padding-left':'10px','padding-right':'10px'}),),
                                    ]),
                                ]),

                            ],style={'padding-bottom':'20px','padding-top':'20px'}),

                    ],
                    title='Data Wrangling',
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
                                html.Img(src='/assets/img/spark_py.jpg', style={'width':'100%',
                                        'max-width':'360px','height':'auto','border-radius':'5px'},
                                        className='shadow-sm'),
                                ],style={'min-width':360,'max-width':360}),

                            dbc.Col([
                                html.P("Spark & SQL - Global Historical Climate Network Data Analysis using Spark",
                                    style = {'font-size':'15px','text-transform':'uppercase',
                                        'font-weight':'700'}),
                                html.P("Analysing Global Historical Climate Network (GHCN) data using the power of Spark. \
                                    In this notebook, we'll harness the capabilities of distributed computing in Spark, \
                                    along with HDFS command-line tools, PySpark, Spark DataFrames, and Spark SQL, all \
                                    within the familiar environment of Jupyter Notebook. ",
                                    style={'font-size':'16px','font-family':'Georgia','margin-bottom':'12px'}),
                                dbc.Row([
                                    dbc.Col(
                                        dbc.Button(html.Span([html.I(className="fa-solid fa-display me-2"),'Live Preview']),
                                            outline=True, color='primary',
                                            size = 'sm',
                                            className="rounded-pill me-1",
                                            href= 'https://nicknguyen.me/static/GHCN_Spark.html',
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
                                            href='https://github.com/nicknguyen22/Spark/tree/8cf26e4e0c4291e9090ce4b417b2374b6b68dc1f/GHCN',
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
                                html.Img(src='/assets/img/spark_py.jpg', style={'width':'100%',
                                        'max-width':'360px','height':'auto','border-radius':'5px'},
                                        className='shadow-sm'),
                                ],style={'min-width':360,'max-width':360}),

                            dbc.Col([
                                html.P("Spark - Audio Similarity: Binary & Multiclass classification",
                                    style = {'font-size':'15px','text-transform':'uppercase',
                                        'font-weight':'700'}),
                                html.P("This notebook uses Spark Machine Learning Library, on Spark Distributed \
                                    Computing Platform to predict song genres from audio data. It applies Ridge \
                                    Regression, Random Forest, and Gradient Boosted Tree algorithms on large-scale \
                                    data for efficient binary classification and multiclass classification.",
                                    style={'font-size':'16px','font-family':'Georgia','margin-bottom':'12px'}),
                                dbc.Row([
                                    dbc.Col(
                                        dbc.Button(html.Span([html.I(className="fa-solid fa-display me-2"),'Live Preview']),
                                            outline=True, color='primary',
                                            size = 'sm',
                                            className="rounded-pill me-1",
                                            href= 'https://nicknguyen.me/static/MSD_Audio_similarity.html',
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
                                            href='https://github.com/nicknguyen22/Spark/tree/2703786a3a173af277a4168bc4f9196cbce451db/MSD_Audio_similarity',
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
                                html.Img(src='/assets/img/spark_py.jpg', style={'width':'100%',
                                        'max-width':'360px','height':'auto','border-radius':'5px'},
                                        className='shadow-sm'),
                                ],style={'min-width':360,'max-width':360}),

                            dbc.Col([
                                html.P("Spark - Song Recommendations by Collaborative Filtering (ALS)",
                                    style = {'font-size':'15px','text-transform':'uppercase',
                                        'font-weight':'700'}),
                                html.P("This Spark notebook is dedicated to creating a song recommendation system \
                                    through collaborative filtering. Leveraging the power of the Spark.ml library, it \
                                    employs an implicit matrix factorization model using Alternating Least Squares (ALS) \
                                    to provide personalized song recommendations.",
                                    style={'font-size':'16px','font-family':'Georgia','margin-bottom':'12px'}),
                                dbc.Row([
                                    dbc.Col(
                                        dbc.Button(html.Span([html.I(className="fa-solid fa-display me-2"),'Live Preview']),
                                            outline=True, color='primary',
                                            size = 'sm',
                                            className="rounded-pill me-1",
                                            href= 'https://nicknguyen.me/static/MSD_Song_recommendations.html',
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
                                            href='https://github.com/nicknguyen22/Spark/tree/cbec2395f8d470961678b0a73b9f61fde248481f/MSD_Song_recommendations',
                                            disabled=False,
                                            target="_blank",
                                            style = {'font-size':'13px','font-weight':'500',
                                                    'padding-left':'10px','padding-right':'10px'}),),
                                        ]),
                                    ]),

                                ],style={'padding-bottom':'20px','padding-top':'20px'}),

                    html.Hr(style={'color':'#adadad'}),


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

                    dbc.Row([
                        dbc.Col([
                            html.Img(src='/assets/img/pytorch_keras.jpg', style={'width':'100%',
                                    'max-width':'360px','height':'auto','border-radius':'5px'},
                                    className='shadow-sm'),
                            ],style={'min-width':360,'max-width':360}),

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
                            html.Img(src='/assets/img/colab_jup.jpg', style={'width':'100%',
                                    'max-width':'360px','height':'auto','border-radius':'5px'},
                                    className='shadow-sm'),
                            ],style={'min-width':360,'max-width':360}),

                        dbc.Col([
                            html.P('Python - Time series data pattern recognitions',
                                style = {'font-size':'15px','text-transform':'uppercase',
                                    'font-weight':'700'}),
                            html.P('This notebook utilised an unsupervised machine learning technique known as time \
                                series k-means clustering to identify underlying patterns within the time series data \
                                representing Carbon Intensity. The dataset encompassed Carbon Intensity values for each \
                                30-minute Trading Period, spanning from 2018 to 2022 in NZ',
                                style={'font-size':'16px','font-family':'Georgia','margin-bottom':'12px'}),
                            dbc.Row([
                                dbc.Col(
                                    dbc.Button(html.Span([html.I(className="fa-solid fa-display me-2"),'Live Preview']),
                                        outline=True, color='primary',
                                        size = 'sm',
                                        className="rounded-pill me-1",
                                        href='https://colab.research.google.com/drive/1GGWpRxXxfUlCp0vksWZ-mSLfEicb0RzM?usp=sharing',
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
                                        href='https://github.com/nicknguyen22/Machine_learning/tree/a43839000bb86188d3d2820e28dee52446378b5f/Timeseries_pattern_recognition',
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
                            html.Img(src='/assets/img/py_keras_optuna.jpg', style={'width':'100%',
                                    'max-width':'360px','height':'auto','border-radius':'5px'},
                                    className='shadow-sm'),
                            ],style={'min-width':360,'max-width':360}),

                        dbc.Col([
                            html.P('Python - Classifying Fashion with a 4-Layer Convolutional Neural Network',
                                style = {'font-size':'15px','text-transform':'uppercase',
                                    'font-weight':'700'}),
                            html.P('This notebook utilizes a Convolutional Neural Network (CNN) classifier constructed \
                                using the Keras deep learning library. The CNN architecture comprises four convolutional \
                                layers and has been fine-tuned using Optuna hyperparameter optimisation and augmented with \
                                data augmentation techniques. The results are visualised using TensorBoard.',
                                style={'font-size':'16px','font-family':'Georgia','margin-bottom':'12px'}),
                            dbc.Row([
                                dbc.Col(
                                    dbc.Button(html.Span([html.I(className="fa-solid fa-display me-2"),'Live Preview']),
                                        outline=True, color='primary',
                                        size = 'sm',
                                        className="rounded-pill me-1",
                                        href='https://colab.research.google.com/drive/11HTjho6MbseW0-7kIATSU0F8D13uBh7-?usp=sharing',
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
                                        href='https://github.com/nicknguyen22/Machine_learning/tree/a1d3640b064ac5a2d32b371294cde12c60d12166/Classification_CNN4Layers',
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
                            html.Img(src='/assets/img/rlogo.jpg', style={'width':'100%',
                                    'max-width':'360px','height':'auto','border-radius':'5px'},
                                    className='shadow-sm'),
                            ],style={'min-width':360,'max-width':360}),

                        dbc.Col([
                            html.P('R - Banknotes classification with Logistic Regression, LDA and QDA',
                                style = {'font-size':'15px','text-transform':'uppercase',
                                    'font-weight':'700'}),
                            html.P("This R notebook compares the results of multiple regression algorithms for the \
                                detection of forged banknotes. We'll be evaluating the performance of logistic \
                                regression analysis, linear discriminant analysis (LDA), and quadratic discriminant \
                                analysis (QDA) to determine their effectiveness in distinguishing genuine banknotes from forged ones.",
                                style={'font-size':'16px','font-family':'Georgia','margin-bottom':'12px'}),
                            dbc.Row([
                                dbc.Col(
                                    dbc.Button(html.Span([html.I(className="fa-solid fa-display me-2"),'Live Preview']),
                                        outline=True, color='primary',
                                        size = 'sm',
                                        className="rounded-pill me-1",
                                        href= 'https://nicknguyen.me/static/Banknote_classification.html',
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
                                        href='https://github.com/nicknguyen22/Machine_learning/tree/3007bf548b173bf85ba9856dffc6799cec6273e2/Banknote_classification',
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
                            html.Img(src='/assets/img/rlogo.jpg', style={'width':'100%',
                                    'max-width':'360px','height':'auto','border-radius':'5px'},
                                    className='shadow-sm'),
                            ],style={'min-width':360,'max-width':360}),

                        dbc.Col([
                            html.P('R - Backward, Stepwise, Ridge and LASSO Regression Comparision ',
                                style = {'font-size':'15px','text-transform':'uppercase',
                                    'font-weight':'700'}),
                            html.P('This R notebook focused on assessing the performance of four distinct regression \
                                techniques - Backward Regression, Stepwise Regression, LASSO Regression, and Ridge \
                                Regression. Our analysis centers around the Residential Building Dataset, aiming to \
                                compare the efficacy of these methods within the context of residential building data.',
                                style={'font-size':'16px','font-family':'Georgia','margin-bottom':'12px'}),
                            dbc.Row([
                                dbc.Col(
                                    dbc.Button(html.Span([html.I(className="fa-solid fa-display me-2"),'Live Preview']),
                                        outline=True, color='primary',
                                        size = 'sm',
                                        className="rounded-pill me-1",
                                        href= 'https://nicknguyen.me/static/Backward_stepwise_LASSO_Ridge.html',
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
                                        href='https://github.com/nicknguyen22/Machine_learning/tree/c027c3f49516735389504de108f663723024210d/Backward_stepwise_lasso_ridge',
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
                            html.Img(src='/assets/img/rlogo.jpg', style={'width':'100%',
                                    'max-width':'360px','height':'auto','border-radius':'5px'},
                                    className='shadow-sm'),
                            ],style={'min-width':360,'max-width':360}),

                        dbc.Col([
                            html.P("R - Parkinson's disease UPDRS analysis with LASSO Regression",
                                style = {'font-size':'15px','text-transform':'uppercase',
                                    'font-weight':'700'}),
                            html.P("This R notebook, where we delve into the analysis of Parkinson's disease UPDRS \
                                (Unified Parkinson's Disease Rating Scale) using LASSO Regression. In this exploration, \
                                we aim to uncover the relative importance of features within the fitted model, shedding \
                                light on the key factors contributing to the UPDRS scores in Parkinson's disease patients.",
                                style={'font-size':'16px','font-family':'Georgia','margin-bottom':'12px'}),
                            dbc.Row([
                                dbc.Col(
                                    dbc.Button(html.Span([html.I(className="fa-solid fa-display me-2"),'Live Preview']),
                                        outline=True, color='primary',
                                        size = 'sm',
                                        className="rounded-pill me-1",
                                        href= 'https://nicknguyen.me/static/Parkinsons_UPDRS_analysis_LASSORegession.html',
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
                                        href='https://github.com/nicknguyen22/Machine_learning/tree/c027c3f49516735389504de108f663723024210d/Parkinson_LASSO_analysis',
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
                            html.Img(src='/assets/img/rlogo.jpg', style={'width':'100%',
                                    'max-width':'360px','height':'auto','border-radius':'5px'},
                                    className='shadow-sm'),
                            ],style={'min-width':360,'max-width':360}),

                        dbc.Col([
                            html.P("R - Support Vector Machine (SVM) Algorithms via the Caret Pipeline",
                                style = {'font-size':'15px','text-transform':'uppercase',
                                    'font-weight':'700'}),
                            html.P("We harness the power of Support Vector Machine (SVM) algorithms within the Caret \
                                Pipeline to tackle the critical task of classifying breast cancer patients. In this \
                                notebook, we'll explore how SVM, coupled with efficient data preprocessing and model \
                                evaluation through the Caret framework, can aid in distinguishing between different \
                                cancer results.",
                                style={'font-size':'16px','font-family':'Georgia','margin-bottom':'12px'}),
                            dbc.Row([
                                dbc.Col(
                                    dbc.Button(html.Span([html.I(className="fa-solid fa-display me-2"),'Live Preview']),
                                        outline=True, color='primary',
                                        size = 'sm',
                                        className="rounded-pill me-1",
                                        href= 'https://nicknguyen.me/static/SVM_caret.html',
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
                                        href='https://github.com/nicknguyen22/Machine_learning/tree/ced022dedc8453d14866855d1c60cebec51307cf/SVM_Caret_pipeline',
                                        disabled=False,
                                        target="_blank",
                                        style = {'font-size':'13px','font-weight':'500',
                                                'padding-left':'10px','padding-right':'10px'}),),
                                    ]),
                                ]),

                            ],style={'padding-bottom':'20px','padding-top':'20px'}),

                    html.Hr(style={'color':'#adadad'}),

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

                    dbc.Row([
                        dbc.Col([
                            html.Img(src='/assets/img/py_spacy.jpg', style={'width':'100%',
                                    'max-width':'360px','height':'auto','border-radius':'5px'},
                                    className='shadow-sm'),
                            ],style={'min-width':360,'max-width':360}),

                        dbc.Col([
                            html.P('Python & Spacy - Text Information Extraction',
                                style = {'font-size':'15px','text-transform':'uppercase',
                                    'font-weight':'700'}),
                            html.P("In the modern data-driven landscape, leveraging the capabilities of natural language \
                                processing (NLP) is paramount for extracting valuable insights from unstructured textual \
                                data. This Python notebook is dedicated to the core mission of delving into and comprehending \
                                how the Spacy library can proficiently carry out information extraction.  ",
                                style={'font-size':'16px','font-family':'Georgia','margin-bottom':'12px'}),
                            dbc.Row([
                                dbc.Col(
                                    dbc.Button(html.Span([html.I(className="fa-solid fa-display me-2"),'Live Preview']),
                                        outline=True, color='primary',
                                        size = 'sm',
                                        className="rounded-pill me-1",
                                        href='https://colab.research.google.com/drive/16dRCG5zV0tdZxpfGdSwgOfj11AFvcRnq?usp=sharing',
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
                                        href='https://github.com/nicknguyen22/NLP/tree/953ab103d54bbd117e5aaae7fb8e841b843a6952/Information_extraction',
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
                            html.Img(src='/assets/img/py_gensim.jpg', style={'width':'100%',
                                    'max-width':'360px','height':'auto','border-radius':'5px'},
                                    className='shadow-sm'),
                            ],style={'min-width':360,'max-width':360}),

                        dbc.Col([
                            html.P('Python & Spacy - Text Information Extraction',
                                style = {'font-size':'15px','text-transform':'uppercase',
                                    'font-weight':'700'}),
                            html.P("In this Python notebook, we embark on an exciting journey through TED.com transcripts, \
                                applying advanced topic modeling techniques. Leveraging the power of the Gensim library and \
                                the Mallet library, we explore the rich content of TED talks to uncover hidden themes and \
                                insights.",
                                style={'font-size':'16px','font-family':'Georgia','margin-bottom':'12px'}),
                            dbc.Row([
                                dbc.Col(
                                    dbc.Button(html.Span([html.I(className="fa-solid fa-display me-2"),'Live Preview']),
                                        outline=True, color='primary',
                                        size = 'sm',
                                        className="rounded-pill me-1",
                                        href='https://colab.research.google.com/drive/1DvNuyndrxJqpMjpmxrk3Zd1Puxi5rv89?usp=sharing',
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
                                        href='https://github.com/nicknguyen22/NLP/tree/d115e4edb3ca2092b5cb7e8f59e1d832cf4a6dbc/Topic_modelling',
                                        disabled=False,
                                        target="_blank",
                                        style = {'font-size':'13px','font-weight':'500',
                                                'padding-left':'10px','padding-right':'10px'}),),
                                    ]),
                                ]),

                            ],style={'padding-bottom':'20px','padding-top':'20px'}),

                    html.Hr(style={'color':'#adadad'}),

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
                                html.Img(src='/assets/img/py_pygame.jpg', style={'width':'100%',
                                    'max-width':'360px','height':'auto','border-radius':'5px'},
                                    className='shadow-sm'),
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
                                                    'padding-left':'10px','padding-right':'10px'}),),

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
                                                    'padding-left':'10px','padding-right':'10px'}),),
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
