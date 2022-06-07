from dash import Dash, dcc, html
from components.aside import aside as aside_component
from dash.html import (
    Div, A, I, Main, H4, P, Br, Ul, Li,
    Section, Button, Footer, Span
)
from dash.dcc import (
    Input, Location
)
from components.navbar import get_navbar

breadcrumb_elts = [
    {
        "name": "Dash-ploty-sqlachemy",
        "href": "#",
        "active": False
    },
    {
        "name": "Dash-ploty-sqlachemy level2",
        "href": "#",
        "active": False
    },
    {
        "name": "Accueil",
        "active": True
    }
]

navbar = get_navbar(breadcrumb_elts, "Accueil")

main_content = Main(
    className="main-content position-relative max-height-vh-100 h-100 border-radius-lg ",
    children=[
        navbar,
        Div(
            className="container-fluid py-4",
            children=[
                Div(
                    className="card card-body",
                    children=Div(
                        className="row gx-4 mb-2",
                        children=Div(
                            className="col-lg-4 col-md-6",
                            children=Div(
                                className="nav-wrapper position-relative end-0",
                                children=Ul(
                                    className="nav nav-pills nav-fill p-1",
                                    role="tablist",
                                    children=[
                                        Li(
                                            className="nav-item",
                                            children=A(
                                                className="nav-link mb-0 px-0 py-1 active ",
                                                **{
                                                    "data-bs-toggle": "tab",
                                                    "aria-selected": "true"
                                                },
                                                href="javascript:;",
                                                role="tab",
                                                children=[
                                                    I(
                                                        className="material-icons text-lg position-relative",
                                                        children="home"
                                                    ),
                                                    Span(
                                                        className="ms-1",
                                                        children="Element 1"
                                                    )
                                                ]
                                            )
                                        ),
                                        Li(
                                            className="nav-item",
                                            children=A(
                                                className="nav-link mb-0 px-0 py-1 ",
                                                **{
                                                    "data-bs-toggle": "tab",
                                                    "aria-selected": "false"
                                                },
                                                href="javascript:;",
                                                role="tab",
                                                children=[
                                                    I(
                                                        className="material-icons text-lg position-relative",
                                                        children="email"
                                                    ),
                                                    Span(
                                                        className="ms-1",
                                                        children="Element 2"
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                )
                            )
                        )
                    )
                ),
                Div(
                    className="row"
                ),
                Footer(
                    className="footer py-4  "
                )
            ]
        )
    ]
)

welcome = html.Div([
    aside_component,
    main_content
])

