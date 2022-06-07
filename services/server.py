from flask import (
        g,
        current_app as current_server,
        Flask
    )

def get_server():
    if 'server' not in g:
        g.server = current_server

    return g.server

server:Flask = get_server()