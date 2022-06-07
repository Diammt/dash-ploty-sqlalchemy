from dash import dcc, html
import dash_bootstrap_components as dbc

html_input = dbc.Row(
    [
        dbc.Label("Contenu html", html_for="content-html", width=2),
        dbc.Col(
            dbc.Textarea(
                id="content-html", placeholder="Entrer le contenu html"
            ),
        ),
        dbc.Button(children='Convertir', n_clicks=0,
                    type='submit', id='submit-html-convert',
                   ),
    ],
    className="mb-3",
)

html_to_dash_output = dbc.Row(
    children=dbc.Col(
        id="html-dash-output"
    )
)
convert_page = html.Div(
    children=[
        html_input,
        html_to_dash_output
    ]
)

