import dash_bootstrap_components as dbc
from dash import Input, Output, State, callback
from dash.html import Div, Nav, A, Button, I, Li, Ul, Span

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"




nav = Nav(
    className="navbar navbar-expand-lg blur border-radius-lg top-0 z-index-3 shadow position-absolute mt-4 py-2 start-0 end-0 mx-4",
    children=Div(
        className="container-fluid ps-2 pe-0",
        children=[
            A(children='\n Dash-ploty-sqlachemy by Mahussi Jeff F. Datongnon\n ', className='navbar-brand font-weight-bolder ms-lg-0 ms-3 ', href='/'),
            Button(children=[Span(children=[Span(className='navbar-toggler-bar bar1'), Span(className='navbar-toggler-bar bar2'), Span(className='navbar-toggler-bar bar3')], className='navbar-toggler-icon mt-2')], className='navbar-toggler shadow-none ms-2', type='button', **{'aria-expanded': 'false', 'data-bs-toggle': 'collapse', 'aria-controls': 'navigation', 'aria-label': 'Toggle navigation', 'data-bs-target': '#navigation'}),
            Div(
                children=[
                    Ul(
                        children=[],
                        className='navbar-nav mx-auto'),
                    Ul(children=[Li(children=[A(children='Nous contacter', className='btn btn-sm mb-0 me-1 bg-gradient-dark', href='#')], className='nav-item')], className='navbar-nav d-lg-block d-none')
                ], id='navigation', className='collapse navbar-collapse'
            )
        ]
    )
)

navbar_auth = Div(
        className="container position-sticky z-index-sticky top-0",
        children=Div(
            className="row",
            children=Div(
                className="col-12",
                children=[
                    nav
                ]
            )
        )
    )
