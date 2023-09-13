from dash_extensions.enrich import DashBlueprint, DashProxy, html, Output, Input
from flask import session

# Define a small example app.
app = DashBlueprint()
app.layout = html.Div([html.Div("Keycloak auth", id="main"), html.Div(id="greeting")])


@app.callback(
    Output('greeting', 'children'),
    [Input('main', 'children')])
def update_greeting(input_value):
    user = session["userinfo"]
    return "Hello {}!".format(user['preferred_username'])


# Run the app in "standalone" mode for debugging.
if __name__ == '__main__':
    DashProxy(blueprint=app).run_server(debug=True, port=8050)
