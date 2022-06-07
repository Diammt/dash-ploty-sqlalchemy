from dash import Dash, dcc, html
from components.aside import aside as aside_component
from dash.html import (
    Div, A, I, Main, H4, P, Br, Ol, Li, H6, Ul,
    Section, Button, Footer, Nav, Label, Select,
    Option, Span
)
from dash.dcc import (
    Input, Location
)








def get_breadcrumb_component(breadcrumb_elts: list=[], breadcrumb_name: str="N/A"):
    breadcrumb_component = Nav(
        className="",
        children=[
            Ol(
                className="breadcrumb bg-transparent mb-0 pb-0 pt-1 px-0 me-sm-6 me-5",
                children=[
                    get_li_compononent_for_breadcrumb(item) for item in breadcrumb_elts
                ]
            ),
            H6(
                className="font-weight-bolder mb-0",
                children=breadcrumb_name
            )
        ]
    )
    return breadcrumb_component

def get_li_compononent_for_breadcrumb(item: dict):
    if item.get("active", False):
        return Li(
            className="breadcrumb-item text-sm text-dark active",
            **{"aria-current": "page"},
            children=item.get("name", "N/A")
        )
    else:
        return Li(
            className="breadcrumb-item text-sm",
            children=A(
                className="opacity-5 text-dark",
                href=item.get("href", "javascript:;"),
                children=item.get("name", "N/A")
            )
        )



def get_navbar(breadcrumb_elts: list, breadcrumb_name="Accueil"):
    navbar = Nav(
        className="navbar navbar-main navbar-expand-lg px-0 mx-4 shadow-none border-radius-xl",
        id="navbarBlur",
        **{'aria-navbar-scroll': "true"},
        children=Div(
            className="container-fluid py-1 px-3",
            children=[
                get_breadcrumb_component(breadcrumb_elts, breadcrumb_name),
                Div(
                    className="collapse navbar-collapse mt-sm-0 mt-2 me-md-0 me-sm-4",
                    id="navbar",
                    children=[
                        Div(
                            className="ms-md-auto pe-md-3 d-flex align-items-center",
                            children=Div(
                                className="row",
                                children=[]
                            )
                        ),
                        Ul(
                            className="navbar-nav  justify-content-end",
                            # Logout here
                            children=[
                                Li(
                                    className="nav-item d-flex align-items-center",
                                    children=A(
                                        className="nav-link text-body font-weight-bold px-0",
                                        href="/logout",
                                        children=[
                                            I(
                                                className="fa fa-user me-sm-1",
                                            ),
                                            Span(
                                                className="d-sm-inline d-none",
                                                children="Se déconnecter"
                                            )
                                        ]
                                    )

                                )
                            ]
                        )
                    ]
                )
            ]
        )
    )
    return navbar

