import dash_bootstrap_components as dbc
import dash
from dash import Dash, Input, Output, State, dcc, html

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
                                style={'padding-top':'10px','padding-right':'0px',}),

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
                ),fluid='true',
            ),
    
    brand_href='https://nicknguyen.me',
    color='white',
    sticky='top',
    dark=False,
    fluid=False,
    class_name='px-0 shadow-sm p-2 mb-5 bg-white',
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
    ],style={
       'backgroundColor':'white',
    },
    fluid=True,
    class_name='px-0'

)

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=80, debug=False)