# Project3 - Professional Football Visualization
Provides summary information for American Professional Football.

## Project Description
We are utilizing data from the NFL to look at team locations, team success (points for/against), and more. The data was pulled from the three sources above and loaded into PostgreSQL. To create a web application, we will use Python Flask and leaflet, dash plotly, and plotly. In leaflet, we will create a map to show all NFL teams and their locations over time. We will use dash plotly and plotly to showcase a variety of other features such as superbowl wins, general stats, and more in an interactive manner.


## Team Members
* Sarah Caldwell
* Bryan Denq
* Brendan Trafford
* Ben Calderaio

## Database Setup
* create_db.sql
    * Creates football_db database.
* football_schema.sql
    * Creates schema and tables.
        * import ProFootball_All.csv -> football_sch.profootballyearsummary
        * import team_location_latlon.csv -> football_sch.teamlocation
        * import footballchamps.csv -> football_sch.footballchamps
* sql_scripts.sql
    * Creates views and contains some sample sql.

**Note**: Please create a sql_config.py file with your database connection information.
## Setup Environment
* clone repo
    * **git clone https://github.com/BennyC31/project3.git**
* root dir (project3)
    * **python3 -m venv venv** or **python -m venv venv**
* activate environment
    * MacOS: **source venv/bin/activate**
    * Windows: **./venv/Scripts/activate**
    * Git bash: **source venv/Scripts/activate**
* install packages
    **pip install -r requirements.txt**

## Run App
* footballdashboard dir (project3/footballdashboard)
    **python app.py**
* local default host:port
    ***http://127.0.0.1:5000***

## Data Files
* ProFootball_All.csv
* team_location_latlon.csv
* locationinfo2021all.csv
* footballchamps.csv

## Data Sources
* NFL History

    https://static.www.nfl.com/image/upload/league/apps/league-site/media-guides/2022/2022_NFL_Record_and_Fact_Book.pdf

    https://www.profootballhof.com/

* NFL Games Stats
    
    https://www.kaggle.com/datasets/423c766b86dcb18c859cfd3a4d61e6531df8c488b59839931061fc9b3820c068
* NFL scores and betting data
    
    https://www.kaggle.com/datasets/tobycrabtree/nfl-scores-and-betting-data?select=spreadspoke_scores.csv