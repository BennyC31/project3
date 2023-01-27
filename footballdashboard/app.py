from flask import Flask, render_template,jsonify
import dash
import dash_html_components as html
from layouts import create_dash
import dash_bootstrap_components as dbc
import models as m



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/teaminfo')
def teaminfo():
    return render_template('teaminfo.html')


@app.route('/teamlocs')
def teamlocations():
    return render_template('footballmap.html')

@app.route('/locdata')
def send_team_loc_data():
    data = []
    team_locs = m.create_team_locations_df().to_dict('records')
    sum_data = m.create_data_sum_grt_2011_df().to_dict('records')
    year_data = m.create_data_grt_2011_df().to_dict('records')
    data.append(team_locs)
    data.append(sum_data)
    data.append(year_data)
    m.close_conn()
    return data


@app.route('/teamdata')
def send_team_data():
    team_data = m.create_team_summary_df().to_dict('records')
    m.close_conn()
    return team_data

dash_app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    server=app,
    routes_pathname_prefix='/teamhistory/'
)
dash_app.title = 'Team History'
dash_app.layout = create_dash()

if __name__ == '__main__':
    app.run(debug=True)
