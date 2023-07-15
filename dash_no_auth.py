from dash_extensions.enrich import DashBlueprint, DashProxy, html, Output, Input

# Define a small example app.
app = DashBlueprint()
app.layout = html.Div([html.Div("No auth"), html.Button("Click me", id="btn"), html.Div(id="log")])

@app.callback(Output("log", "children"), Input("btn", "n_clicks"))
def update(n_clicks: int):
    """
    Simple callback function.
    """
    return str(n_clicks)

# Run the app in "standalone" mode for debugging.
if __name__ == '__main__':
    DashProxy(blueprint=app).run_server(debug=True, port=8050)
