from flask_sqlalchemy import SQLAlchemy
from services.server import server
import logging as lg
from flask import g
from werkzeug.local import LocalProxy


def get_db():
    if 'db' not in g:
        database = SQLAlchemy(server)
        g.db = database

    return g.db

db:SQLAlchemy = get_db()