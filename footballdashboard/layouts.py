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
champ_df.rename(columns={'leag_year': 'year',
                         'team_location': 'location', 'team_name': 'name', 'champ_name': 'title'}, inplace=True)
title_df = champ_df
m.close_conn()

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/", external_link=True)),
        # dbc.NavItem(dbc.NavLink(
        #     "Team Info", href="/teaminfo", external_link=True)),
        # dbc.NavItem(dbc.NavLink("Team Locations",
        #                         href="/teamlocs", external_link=True)),
        # dbc.NavItem(dbc.NavLink("Team History",
        #                         href="/teamhistory/", external_link=True)),
    ],
    # brand="AFD",
    # brand_href="/",
    color="primary",
    dark=True,
)

card_left = dbc.Card(
    [dbc.CardHeader('View Team History'),
     dbc.CardBody([
         html.Div([
             dcc.Dropdown(id='team', className="dropdown",
                          options=[{"label": team, "value": team}
                                   for team in team_fn],
                          clearable=True,
                          value='',
                          multi=False, style={'font-size': '12px'}),
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
                 'whitespace': 'normal',
                 'font-size': '12px'
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
                     'backgroundColor': 'tan',
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
    [dbc.CardHeader('Championships',id='title_id'),
     dbc.CardBody([
         html.Div([
             dash_table.DataTable(id='team_title', css=[{'selector': '.row', 'rule': 'margin: 0; display: block'}],
                                  columns=[
                 {"name": i, "id": i} for i in champ_df.columns],
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
                 'whitespace': 'normal',
                 'font-size': '12px'
             },
                 style_data_conditional=[
                 {
                     'if': {
                         'column_id': 'location',
                     },
                     'backgroundColor': 'white',
                     'fontStyle': 'italic',

                 },

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
         ], className='mb-3'
         )
     ])
     ]
)


def create_dash():
    dash_index = html.Div([
        navbar,
        dbc.Row([
        dbc.Col(card_left, width=7, style={'paddingLeft': '20px'}),
        dbc.Col(card_right, width=5, style={'paddingLeft': '20px'})
    ])
    ])
    
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
    df_team = new_df[(new_df['team_id'] == team_to_display)]
    return df_team.to_dict('records')


@callback(
    Output('team_title', 'data'),
    Output('title_id', 'children'),
    Input('team', 'value')
)
def update_table(value):
    team_to_display = get_team_id(value)
    df_team = title_df[(title_df['team_id'] == team_to_display)]
    return df_team.to_dict('records'),f'Championships {len(df_team)}'
