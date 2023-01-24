from dash import dcc,html,dash_table
import models as m
import pandas as pd

tm_df = m.create_team_summary_df()
team_fn = tm_df['team_name'].sort_values().unique()

def create_dash():
    dash_index = html.Div([
        html.H3("Select a Team"),
        html.Div([
            dcc.Dropdown(id='team', className="dropdown",
                             options=[{"label": team, "value": team}
                                      for team in team_fn],
                             clearable=True,
                             value='',
                             multi=False),
            dash_table.DataTable(tm_df.to_dict('records'),
            [{"name": i, "id": i} for i in tm_df.columns], id='teams_data',
            )
        ]),
        html.Div([
            html.H2('Bottom of page')
        ])
    ])
    return dash_index