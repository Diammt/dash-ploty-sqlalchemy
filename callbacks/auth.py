from dash import Input, Output, callback, State
from models import User
from services.db import db
from flask_login import login_user
# Callback function to login the user, or update the screen if the username or password are incorrect

# print("load login callback")
@callback(
    Output('url_login', 'pathname'),
    Output('login-output-state', 'children'),
    [Input('login-button', 'n_clicks')],
    [State('email', 'value'), State('password', 'value')])
def login_button_click(n_clicks, email, password):
    print("n_clicks: ", n_clicks)
    if n_clicks is not None and n_clicks > 0:
        test_email = "test@test.test"
        if email == test_email and password == 'test':
            user = User.query.filter_by(email=test_email).first()
            if user:
                login_user(user)
                return '/', ''

        return '/login', 'Email ou mot de passe incorrecte'
    return '/login', ''
