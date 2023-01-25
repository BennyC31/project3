from flask import Flask, render_template
import dash
import dash_html_components as html
from layouts import create_dash
import dash_bootstrap_components as dbc

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/teaminfo')
def bbutton():
    return render_template('teaminfo.html')

@app.route('/teamlocs')
def teamlocations():
    return render_template('footballmap.html')

dash_app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    server=app,
    routes_pathname_prefix='/dash/'
)
dash_app.title = 'Team History'
dash_app.layout = create_dash()

if __name__ == '__main__':
    app.run(debug=True)