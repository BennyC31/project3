from sql_config import database_name,username,password,host,port,protocol
import pandas as pd
from sqlalchemy import create_engine

team_locations = []
team_summary = []
rds_connection_string = f'{protocol}://{username}:{password}@{host}:{port}/{database_name}'
engine = create_engine(rds_connection_string)

def create_team_summary_df():
    team_summary_df = pd.read_sql_query(
        'select * from football_sch.profootballyearsummary order by leag_year,leagabrv,conference,division,place',con=engine)
    return team_summary_df

def create_team_lookup_df():
    team_lookup_df = pd.read_sql_query(
        'select * from football_sch.teamlookup',con=engine)
    return team_lookup_df

def create_team_champs_df():
    team_champ_df = pd.read_sql_query(
        'select leag_year,team_id,team_location,team_name,champ_name from football_sch.footballchamps',con=engine)
    return team_champ_df

def create_team_locations_df():
    team_loc_df = pd.read_sql_query(
        'select * from football_sch.locationinfo2021all', con=engine)
    return team_loc_df

def create_data_grt_2011_df():
    data_grt_2011_df = pd.read_sql_query(
        'select * from football_sch.data_grt_2011', con=engine)
    return data_grt_2011_df

def create_data_sum_grt_2011_df():
    sum_grt_2011_df = pd.read_sql_query(
        'select * from football_sch.data_sum_grt_2011 order by team_name', con=engine)
    return sum_grt_2011_df

def close_conn():
    engine.dispose()
    

def create_team_locs(team_locs):
    for i in range(len(team_locs)):
        tl = TeamLocs()
        tl.loc_id = team_locs[i][0]
        tl.team_location = team_locs[i][1]
        tl.lat = team_locs[i][2]
        tl.lon = team_locs[i][2]
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
