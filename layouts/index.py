from dash import dcc, html
from dash import Input, Output, callback, State, no_update
from flask_login import (
    current_user
)
from .auth import login as login_layout
from .welcome import welcome as welcome_layout

index_page = login_layout

# print("current_user: ", current_user)
if current_user and current_user.is_authenticated:
    # index get dashboard
    index_page = welcome_layout

