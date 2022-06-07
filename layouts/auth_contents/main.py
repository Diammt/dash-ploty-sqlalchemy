from dash.html import (
    Div, A, I, Main, H4, P, Br,
    Section, Button
)
from dash.dcc import (
    Input, Location
)


main = Main(
    className='main-content mt-0',
    children=[
        Location(id='url_login', refresh=True),
        Section(
            children=Div(
                className='page-header min-vh-100',
                children=Div(
                    className='container',
                    children=Div(
                        className='row',
                        children=[
                            Div(children=[Div(children='\n ', className='position-relative bg-gradient-primary h-100 m-3 px-7 border-radius-lg d-flex flex-column justify-content-center', style={'backgroundImage': " url('../assets/img/illustrations/illustration-signup.jpg')", ' backgroundSize': ' cover'})], className='col-6 d-lg-flex d-none h-100 my-auto pe-0 position-absolute top-0 start-0 text-center justify-content-center flex-column'),
                            Div(
                                className='col-xl-4 col-lg-5 col-md-7 d-flex flex-column ms-auto me-auto ms-lg-auto me-lg-5',
                                children=Div(
                                    className='card card-plain',
                                    children=[
                                        Div(
                                            className='card-header',
                                            children=[
                                                H4(children='Se connecter', className='font-weight-bolder'),
                                                P(children='Entrer votre email et votre mot de passe pour vous connecter', className='mb-0')
                                            ]
                                        ),
                                        Div(
                                            className='card-body',
                                            children=Div(
                                                # role="form",
                                                children=[
                                                    Div(
                                                        className='input-group input-group-outline mb-3',
                                                        children=[
                                                            # Label(
                                                            #     className='form-label',
                                                            #     children='Email'
                                                            # ),
                                                            Input(
                                                                id="email",
                                                                type="email",
                                                                className="form-control",
                                                                placeholder="Email"
                                                            )
                                                        ]
                                                    ),
                                                    Div(
                                                        className='input-group input-group-outline mb-3',
                                                        children=[
                                                            # Label(
                                                            #     className='form-label',
                                                            #     children='Mot de passe'
                                                            # ),
                                                            Input(
                                                                id="password",
                                                                type="password",
                                                                className="form-control",
                                                                placeholder="Mot de passe"
                                                            )
                                                        ]
                                                    ),
                                                    Div(
                                                        className="text-center text-danger",
                                                        children='',
                                                        id="login-output-state"
                                                    ),
                                                    Div(
                                                        className="text-center",
                                                        children=Button(
                                                            id="login-button",
                                                            className="btn btn-lg bg-gradient-primary btn-lg w-100 mt-4 mb-0",
                                                            children='Se connecter',
                                                            type='submit'
                                                        )
                                                    )
                                                ]
                                            )
                                        ),
                                        Div(
                                            className='card-footer text-center pt-0 px-lg-2 px-1r',
                                            children=P(
                                                className="mb-2 text-sm mx-auto",
                                                children=[
                                                    " © 2022 Dash-ploty-sqlachemy avec ",
                                                    I(className='fa fa-heart text-danger me-1'),
                                                    "par ",
                                                    A(
                                                        className="text-primary text-gradient font-weight-bold",
                                                        href="https://www.jeffdat.ibudohub.co",
                                                        children="Mahussi Jeff F. Datongnon",
                                                        target='_blank'
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            )
        )
    ]
)