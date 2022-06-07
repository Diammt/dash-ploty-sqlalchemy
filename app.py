from flask import Flask
server = Flask(__name__)
server.app_context().push()

import os
import dash
from dash import Dash, dcc, html, Input, Output, callback
import callbacks
from models import *
from flask_login import LoginManager
import dash_bootstrap_components as dbc
from components import navbar

external_stylesheets = [
    # dbc.themes.BOOTSTRAP,
    # Fonts and icons
    'https://fonts.googleapis.com/css?family=Roboto:300,400,500,700,900|Roboto+Slab:400,700',
    # Material Icons
    'https://fonts.googleapis.com/icon?family=Material+Icons+Round',

]
external_scripts = [
    # Font Awesome Icons
    'https://kit.fontawesome.com/42d5adcbca.js'
]
app = Dash(__name__, server=server,
                title='Example Dash-ploty with Flask-SqlAlchemy',
                update_title='Chargement...',
                suppress_callback_exceptions=True,
                external_stylesheets=external_stylesheets,
                external_scripts=external_scripts
           )

from services.commands import register_all_commands
register_all_commands()

# Updating the Flask Server configuration with Secret Key to encrypt the user session cookie
server.config.update(SECRET_KEY=os.getenv('SECRET_KEY'))
server.config.from_object('config')

# Login manager object will be used to login / logout users
login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = '/login'

@login_manager.user_loader
def load_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user

app.layout = html.Div(
    children=[
        dcc.Location(id='url', refresh=False),
        dcc.Location(id='redirect', refresh=True),
        dcc.Store(id='login-status', storage_type='session'),
        html.Div(id='user-status-div'),
        html.Div(id='page-content')
    ]
)




if __name__ == '__main__':
    app.run_server(debug=True)
