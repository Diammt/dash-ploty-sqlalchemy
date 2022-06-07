from dash.html import (
    Div, Nav, A, Button, I, Li, Ul, Span, Main, H4, P, Br, Hr,
    Section, Form, Label, Button, Aside, Img
)
from dash.dcc import (
    Input, Location
)


aside = Aside(
    className="sidenav navbar navbar-vertical navbar-expand-xs border-0 border-radius-xl my-3 fixed-start ms-3   bg-gradient-dark",
    id="sidenav-main",
    children=[
        Div(
            className="sidenav-header",
            children=[
                I(
                    className="fas fa-times p-3 cursor-pointer text-white opacity-5 position-absolute end-0 top-0 d-none d-xl-none",
                    **{'aria-hidden': "true"},
                    id="iconSidenav"
                ),
                A(
                    className="navbar-brand m-0",
                    href="#",
                    children=[
                        Img(
                            src="/assets/img/logo-ct.png",
                            className="navbar-brand-img h-100",
                            alt="main_logo"
                        ),
                        Span(
                            className="ms-1 font-weight-bold text-white",
                            children="Dash-ploty-sqlachemy"
                        )
                    ]
                )
            ]
        ),
        Hr(
            className="horizontal light mt-0 mb-2"
        ),
        Div(
            className="collapse navbar-collapse  w-auto ",
            id="sidenav-collapse-main",
            children=Ul(
                className="navbar-nav",
                children=[
                    Li(
                        className="nav-item",
                        children=[
                            A(
                                className="nav-link text-white active bg-gradient-primary",
                                href="/",
                                children=[
                                    Div(
                                        className="text-white text-center me-2 d-flex align-items-center justify-content-center",
                                        children=I(
                                            className="material-icons opacity-10",
                                            children="dashboard"
                                        )
                                    ),
                                    Span(
                                        className="nav-link-text ms-1",
                                        children="Dashboard"
                                    )
                                ]
                            )
                        ]
                    ),
                    Li(
                        className="nav-item",
                        children=[
                            A(
                                className="nav-link text-white ",
                                href="/",
                                children=[
                                    Div(
                                        className="text-white text-center me-2 d-flex align-items-center justify-content-center",
                                        children=I(
                                            className="material-icons opacity-10",
                                            children="dashboard"
                                        )
                                    ),
                                    Span(
                                        className="nav-link-text ms-1",
                                        children="Dashboard"
                                    )
                                ]
                            )
                        ]
                    ),
                    Li(
                        className="nav-item",
                        children=[
                            A(
                                className="nav-link text-white ",
                                href="/",
                                children=[
                                    Div(
                                        className="text-white text-center me-2 d-flex align-items-center justify-content-center",
                                        children=I(
                                            className="material-icons opacity-10",
                                            children="dashboard"
                                        )
                                    ),
                                    Span(
                                        className="nav-link-text ms-1",
                                        children="Dashboard"
                                    )
                                ]
                            )
                        ]
                    )
                ]
            )
        ),
        Div(
            className="sidenav-footer position-absolute w-100 bottom-0 ",
            children=Div(
                className="mx-3 text-uppercase",
                children=A(
                    className="btn bg-gradient-primary mt-4 w-100",
                    children="Nous contacter",
                    href="#"
                )
            )
        )
    ]
)