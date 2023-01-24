--DROP VIEW football_sch.nfl2021;

create view football_sch.nfl2021
as
select distinct p.team_id ,p.team_location ,p.team_name  
from profootballyearsummary p 
join teamlocation t on p.team_location = t.football_location 
where p.leag_year =2021
order by team_location, team_id;

--DROP VIEW football_sch.locationinfo2021;

create view football_sch.locationinfo2021 
as
select n.team_location as football_location, n.team_name,
t.team_location, t.lat, t.lon, t.state_code, n.team_id
from nfl2021 n 
join teamlocation t on n.team_location = t.football_location
where t.team_location <> 'New York';

--DROP VIEW football_sch.locationinfo2021all;

create view football_sch.locationinfo2021all
as
select l.football_location, l.team_name, l.team_location,
l.state_code, l.lat, l.lon, p.conference, p.division, l.team_id 
from locationinfo2021 l
join profootballyearsummary p on l.team_id = p.team_id 
where p.leag_year = 2021
order by p.conference, p.division, l.football_location, l.team_name;