import psycopg2
from sql_config import database_name,username,password,host,port
import pandas as pd

team_locations = []
team_summary = []
# team_summary_df = pd.DataFrame()

def create_team_summary_df():
    conn = psycopg2.connect(dbname=database_name,user=username,password=password,host=host,port=port)
    team_summary_df = pd.read_sql_query('select * from football_sch.profootballyearsummary order by leag_year,leagabrv,conference,division,place',conn)
    conn.close()
    return team_summary_df

def create_data_objects():
    team_locs = []
    football_sum = []
    conn = psycopg2.connect(dbname=database_name,user=username,password=password,host=host,port=port)

    cur = conn.cursor()

    cur.execute('select * from football_sch.teamlocation order by team_location asc')
    team_locs = cur.fetchall()
    create_team_locs(team_locs=team_locs)
    cur.execute('select * from football_sch.profootballyearsummary order by leag_year,leagabrv,conference,division,place')
    football_sum = cur.fetchall()
    create_football_sum(football_sum=football_sum)

    team_summary_df = pd.read_sql_query('select * from football_sch.profootballyearsummary order by leag_year,leagabrv,conference,division,place',conn)
    # print(team_summary_df)

    # for i in range(len(team_locs)):
    #     print(team_locs[i][1])
    # print(team_locs)
    # print(type(team_locs))
    
    cur.close()
    conn.close()
    

def create_team_locs(team_locs):
    for i in range(len(team_locs)):
        tl = TeamLocs()
        tl.loc_id = team_locs[i][0]
        tl.team_location = team_locs[i][1]
        # tl.lat = team_locs[i][2]
        # tl.lon = team_locs[i][2]
        team_locations.append(tl)


def create_football_sum(football_sum):
    for i in range(len(football_sum)):
        fs = FootballYear()
        fs.leag_year= football_sum[i][0]
        fs.team_id= football_sum[i][1] 
        fs.team_location= football_sum[i][2]
        fs.team_name= football_sum[i][3]
        fs.conference= football_sum[i][4]
        fs.division= football_sum[i][5]
        fs.w= football_sum[i][6]
        fs.l= football_sum[i][7] 
        fs.t = football_sum[i][8]
        fs.pf= football_sum[i][9]
        fs.pa= football_sum[i][10]
        fs.place= football_sum[i][11]
        fs.leagabrv= football_sum[i][12]
        team_summary.append(fs)


#classes loc_id,team_location,lat,lon
class TeamLocs():
    def __init__(self,loc_id=None,team_location=None,lat=0.0,lon=0.0):
        self.loc_id = loc_id
        self.team_location = team_location
        self.lat = lat
        self.lon = lon
    
    def __repr__(self):
        return f'id: {self.loc_id}|location: {self.team_location}|lat: {self.lat}| lon: {self.lon}'

class FootballYear():
    def __init__(self, leag_year=0,team_id=None,team_location=None,team_name=None,
                conference=None,division=None,w=0,l=0,t=0,pf=0,pa=0,place=0,leagabrv=None):
                self.leag_year= leag_year
                self.team_id= team_id 
                self.team_location= team_location
                self.team_name= team_name
                self.conference= conference
                self.division= division
                self.w= w
                self.l= l 
                self.t = t
                self.pf= pf
                self.pa= pa
                self.place= place
                self.leagabrv= leagabrv
    
    def __repr__(self):
        return f'team_id: {self.team_id}|team_location: {self.team_location}|team_name: {self.team_name}'

# create_data_objects()
# print(f'locs:{team_locations}')
# print(f'teams:{len(team_summary)}')