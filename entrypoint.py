"""
This file is the entry point for the 
"""
import flask
from flask import render_template, abort
from jinja2 import TemplateNotFound
from flask_keycloak import FlaskKeycloak
from dash_extensions.enrich import DashProxy
import dash_no_auth
import dash_keycloak_auth


# List of URL patterns (regex) that do not require login.
white_list = [
    "/\Z",  # match index page
    "/static_html_page\Z",  # match the static html page
    "/no_auth_app",  # match all sub pages of the app prefix
]

# Setup the flask server that hosts everything.
server = flask.Flask(__name__, template_folder='templates')
FlaskKeycloak.from_kc_oidc_json(server, config_path='keycloak.json', uri_whitelist=white_list)

# Route html templates, including the index.
@server.route('/', defaults={'page': 'index'})
@server.route('/<page>')
def show(page):
    try:
        print(f'{page}.html')
        return render_template(f'{page}.html')
    except TemplateNotFound:
        abort(404)

# Bind Dash apps here.
no_auth_app = DashProxy(blueprint=dash_no_auth.app, url_base_pathname="/no_auth_app/", server=server)
keycloak_auth_app = DashProxy(blueprint=dash_keycloak_auth.app, url_base_pathname="/keycloak_auth_app/", server=server)

# Run the complete collection of apps/pages.
if __name__ == '__main__':
    server.run()
