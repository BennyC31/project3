# Project3 - Professional Football Visualization
Provides summary information for American Professional Football.

## Project Description
We are utilizing data from the NFL to look at team locations, team success (points for/against), and more. The data was pulled from the three sources above and loaded into PostgreSQL. To create a web application, we will use Python Flask and leaflet, dash plotly, and plotly. In leaflet, we will create a map to show all NFL teams and their locations over time. We will use dash plotly and plotly to showcase a variety of other features such as superbowl wins, general stats, and more in an interactive manner.


## Team Members
* Sarah Caldwell
* Bryan Denq
* Brendan Trafford
* Ben Calderaio

## Setup Environment
* clone repo
    * **git clone https://github.com/BennyC31/project3.git**
* root dir (project3)
    * **python3 -m venv venv** or **python -m venv venv**
* activate environment
    * MacOS: **source venv/bin/activate** or Windows **./venv/Scripts/activate**
* install packages
    **pip install -r requirements.txt**

## Run App
* footballdashboard dir (project3/footballdashboard)
    **python app.py**
* local default host:port
    ***http://127.0.0.1:5000***

## Data Sources
* NFL History

    https://static.www.nfl.com/image/upload/league/apps/league-site/media-guides/2022/2022_NFL_Record_and_Fact_Book.pdf

    https://www.profootballhof.com/

* NFL Games Stats
    
    https://www.kaggle.com/datasets/423c766b86dcb18c859cfd3a4d61e6531df8c488b59839931061fc9b3820c068
* NFL scores and betting data
    
    https://www.kaggle.com/datasets/tobycrabtree/nfl-scores-and-betting-data?select=spreadspoke_scores.csv