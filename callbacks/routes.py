from dash import Input, Output, callback, State, no_update
from flask_login import (
    current_user,
    logout_user
)


from layouts import (
    page1_layout,
    page2_layout,
    success_layout,
    login_layout,
    logout_layout,
    failed_layout,
    index_page,
    convert_page,
    welcome_layout
)


with_auth_routes = [
    {
        'path': '/page2',
        'view': page2_layout,
    }
]
without_auth_routes = [
    {
        'path': '/page1',
        'view': page1_layout,
    },
    {
        'path': '/convert',
        'view': convert_page,
    }
]

@callback(Output('page-content', 'children'),
            Output('redirect', 'pathname'),
          Input('url', 'pathname'))
def display_page(pathname):
    view = None
    url = no_update
    if pathname == '/login':
        if current_user and not current_user.is_authenticated:
            view = login_layout
        else:
            view = success_layout
            url = ''
    elif pathname == '/':
        if current_user and current_user.is_authenticated:
            # view = success_layout
            view = welcome_layout
        else:
            view = failed_layout
    elif pathname == '/logout':
        if current_user and current_user.is_authenticated:
            logout_user()
            # view = logout_layout
            view = 'Redirection vers la page de connexion ...'
            url = '/login'
        else:
            view = login_layout
            url = '/login'
    elif pathname == '/page1':
        view = page1_layout
    elif pathname == '/page2':
        if current_user and current_user.is_authenticated:
            view = page2_layout
        else:
            view = 'Redirection vers la page de connexion ...'
            url = '/login'
    else:
        # register no auth routes
        for route in without_auth_routes:
            if pathname == route.get('path'):
                view = route.get('view')

        # register auth routes
        if view is None:
            for route in with_auth_routes:
                if pathname == route.get('path'):
                    if current_user and current_user.is_authenticated:
                        view = route.get('view')
                    else:
                        view = 'Redirection vers la page de connexion ...'
                        url = '/login'

    if view is None:
        view = index_page
    return view, url
