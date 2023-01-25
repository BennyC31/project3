from dash import dcc, html, dash_table, callback, callback_context
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import models as m
import pandas as pd

tm_df = m.create_team_summary_df()
team_lu = m.create_team_lookup_df()
team_fn = team_lu['fullname'].sort_values()
team_id_fn = team_lu[['team_id', 'fullname']].to_dict('records')
tm_df.rename(columns={'leag_year': 'year',
             'team_location': 'location', 'team_name': 'name', 'leagabrv': 'league'}, inplace=True)
new_df = tm_df
champ_df = m.create_team_champs_df()
print(champ_df)
m.close_conn()

card_left = dbc.Card(
    [dbc.CardHeader('View Team History'),
     dbc.CardBody([
         html.Div([
             #  html.H3("Select a Team"),
             dcc.Dropdown(id='team', className="dropdown",
                          options=[{"label": team, "value": team}
                                   for team in team_fn],
                          clearable=True,
                          value='',
                          multi=False),
             dash_table.DataTable(id='team_table', css=[{'selector': '.row', 'rule': 'margin: 0; display: block'}],
                                  columns=[
                 {"name": i, "id": i} for i in tm_df.columns],
                 editable=False,
                 sort_action='native',
                 sort_mode='multi',
                 style_table={
                 'overflowX': 'auto', 'width': 'auto',
                 'overflowY': 'scroll'},
                 style_cell={
                 'height': 'auto',
                 'minWidth': 'auto', 'width': 'auto', 'maxWidth': 'auto',
                 'textAlign': 'left',
                 'whitespace': 'normal'
             },
                 style_data_conditional=[
                 {
                     'if': {
                         'column_id': 'location',
                     },
                     'backgroundColor': 'white',
                     'fontStyle': 'italic',

                 },
                 {
                     'if': {
                         'filter_query': '{place} = 1',

                     },
                     'backgroundColor': 'aqua',
                     'fontWeight': 'bold'
                 }

             ],
                 style_cell_conditional=[
                 {
                     'if': {
                         'column_id': 'team_id',
                     },
                     'display': 'none'
                 }
             ]
             )
         ])
     ])

     ]
)
card_right = dbc.Card(
    [dbc.CardHeader('Championships'),
     dbc.CardBody([
         html.Div([
             html.H3("Team")
         ]
         )
     ])
     ]
)

def create_dash():
    dash_index = dbc.Row([
        dbc.Col(card_left, width=9,style={'paddingLeft':'20px'}),
        dbc.Col(card_right, width=3,style={'paddingRight':'20px'})
    ],class_name='mb-2')
    return dash_index


def get_team_id(fullname):
    if fullname is not None and len(fullname) > 0:
        team_rec = {id['fullname']: id for id in team_id_fn}
        team_id = team_rec[fullname]
        team_to_display = team_id['team_id']
        return team_to_display
    else:
        return ''


@callback(
    Output('team_table', 'data'),
    Input('team', 'value')
)
def update_table(value):
    team_to_display = get_team_id(value)
    # print(team_to_display)
    df_team = new_df[(new_df['team_id'] == team_to_display)]
    return df_team.to_dict('records')
