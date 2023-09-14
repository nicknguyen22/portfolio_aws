from dash import Dash, dcc, html, Input, Output, callback, ctx
import dash
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify
import flask
import os

LOGO = '/assets/logo.jpg'

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink('HOME', href='/',style={'padding-right':'30px',
                                                        'font-size':'14px',
                                                        'font-weight':'500'},)),
        
        dbc.NavItem(dbc.NavLink('ABOUT ME', href='/aboutme',style={'padding-right':'30px',
                                                                   'font-size':'14px',
                                                                   'font-weight':'500'},)),
        
        dbc.NavItem(dbc.NavLink('PORTFOLIO', href='/portfolio',style={'padding-right':'30px',
                                                                   'font-size':'14px',
                                                                   'font-weight':'500'},)),
    
        dbc.NavItem(dbc.Button('RESUME', outline=False, color='primary',size = 'sm',
                                className="me-1",
                                href="/assets/resume.pdf",
                                download="resume.pdf",external_link=True,
                                style = {'font-size':'14px','font-weight':'500'}),
                                style={'padding-top':'10px','padding-right':'30px',}),

    ],
    
    brand= dbc.Container(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=LOGO, height="30px",style={'justify':'end'})),
                        dbc.Col(html.H4('NICK NGUYEN', className="ms-2", 
                                        style={'font-family':'Roboto',
                                               'font-weight':'700',
                                               'color' :'#444444'})),
                    ],
                    align="end",
                    className="g-0 px-0",
                    style={'padding-left':'0px'},
                ),fluid=True,
            ),
    
    brand_href='https://nicknguyen.me',
    color='white',
    sticky='top',
    dark=False,
    fluid=False,
    class_name='px-0 shadow-sm p-2 mb-5 bg-white',
)

footer =  dbc.Container([
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
                        
                        html.A(html.Img(src='/assets/seek_logo.png',style={'width':'24px'}),className="px-2",
                            href='https://www.seek.co.nz/profile/hieu-nguyen-VbL4nl8v3p', 
                            target='_blank'),

                    ],style={'display':'inline'}),
            
                ],style={'text-align':'left','min-width':200,'max-width':200,'padding-bottom':'30px'}),

                dbc.Col([
                    html.H4('About This Page',style={'padding-bottom':'5px'}),
                    html.P('The coding for this website utilized Python, the Flask \
                        Framework, and CSS with a foundation in Dash Plotly. The \
                        website is currently live on an EC2 instance through Amazon \
                        Web Services (AWS). For Python portfolio web applications, \
                        deployment occurs on AWS Lambda Serverless, complemented by \
                        an AWS RDS database. In contrast, R Shiny Apps find their \
                        deployment on Microsoft Azure',
                        style={'font-size':'16px', 'font-family':'Georgia'}),
                ],style={'min-width':350,}),

            dbc.Row([
                dcc.Markdown(''' Copyright &copy; 2023 | Nick Nguyen. All rights reserved.''',
                style={'text-align':'center','padding-top':'30px','font-size':'12px'}),
                html.P('Proudly powered by coffee.',style={'text-align':'center',
                                                        'font-size':'12px',
                                                        'margin-top':'-10px'}),
            ])
        ],style={'color':'white'}),
            ],style ={'max-width':'1080px','padding-top':'50px','padding-bottom':'20px'},
            ),
    
    ],fluid=True,
    style={'backgroundColor':'#444444'}
    )

# # Define components
app = dash.Dash(__name__,
                use_pages=True, 
                external_stylesheets=[
                    dbc.themes.MATERIA,
                    dbc.icons.FONT_AWESOME,
                ]
)
app.title = 'Nick Nguyen'
app._favicon = ("favicon_nn.png")
server = app.server


# Layout 
app.layout = dbc.Container([
    navbar,
    dash.page_container,
    footer,
    ],style={
       'backgroundColor':'white',
    },
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

@app.server.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=80, debug=False)