import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html

LOGO = '/assets/logo.jpg'

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink('HOME', href='/',style={'padding-right':'30px',
                                                        'font-size':'14px',
                                                        'font-weight':'500'},)),
        dbc.NavItem(dbc.NavLink('ABOUT ME', href='/aboutme',style={'padding-right':'30px',
                                                                   'font-size':'14px',
                                                                   'font-weight':'500'},)),
        dbc.DropdownMenu(
            children=[
                # dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem('Page 2', href='#'),
                dbc.DropdownMenuItem('Page 3', href='#'),
            ],
            nav=True,
            in_navbar=True,
            label='PORTFOLIO',
            style={'padding-right':'30px','font-size':'14px','font-weight':'500'},
        ),
        dbc.NavItem(dbc.Button('RESUME', outline=False, color='primary',size = 'sm',
                                className="me-1",
                                href="/assets/resume.pdf",
                                download="my_resume.pdf",external_link=True,
                                style = {'font-size':'14px'}),
                                style={'padding-top':'10px','padding-right':'0px',}),

    ],
    
    brand= html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=LOGO, height="30px",style={'justify':'end'})),
                        dbc.Col(html.H4('NICK NGUYEN', className="ms-2", 
                                        style={'font-family':'Poppins',
                                               'font-weight':'700',
                                               'color' :'#444444'})),
                    ],
                    align="end",
                    className="g-0",
                    style={'padding-left':'0px'},
                ),
            ),
    
    brand_href='https://nicknguyen.me',
    color='white',
    sticky='top',
    dark=False,
    fluid=False,
    class_name='px-0 shadow-sm p-3 mb-5 bg-white', 
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