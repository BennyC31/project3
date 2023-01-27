--DROP VIEW football_sch.nfl2021;

create view football_sch.nfl2021
as
select distinct p.team_id ,p.team_location ,p.team_name  
from football_sch.profootballyearsummary p 
join football_sch.teamlocation t on p.team_location = t.football_location 
where p.leag_year =2021
order by team_location, team_id;

--DROP VIEW football_sch.locationinfo2021;

create view football_sch.locationinfo2021 
as
select n.team_location as football_location, n.team_name,
t.team_location, t.lat, t.lon, t.state_code, n.team_id
from football_sch.nfl2021 n 
join football_sch.teamlocation t on n.team_location = t.football_location
where t.team_location <> 'New York';

--DROP VIEW football_sch.locationinfo2021all;

create view football_sch.locationinfo2021all
as
select l.football_location, l.team_name, l.team_location,
l.state_code, l.lat, l.lon, p.conference, p.division, l.team_id 
from football_sch.locationinfo2021 l
join football_sch.profootballyearsummary p on l.team_id = p.team_id 
where p.leag_year = 2021
order by p.conference, p.division, l.football_location, l.team_name;

-- DROP VIEW football_sch.teamlookup;

create view football_sch.teamlookup
as
select distinct p.team_id,p.team_location,p.team_name,
concat(p.team_location, ' ', p.team_name) as fullname  
from football_sch.profootballyearsummary p
order by p.team_id ;

-- 01/26/2023:
-- DROP VIEW football_sch.data_grt_2011;

create view football_sch.data_grt_2011
as
select * 
from football_sch.profootballyearsummary p
where p.leag_year > 2011 and p.leagabrv = 'NFL';

-- DROP VIEW football_sch.data_sum_grt_2011;

create view football_sch.data_sum_grt_2011
as
select la.football_location, la.team_name, la.team_id, a.w, a.l, a.t, a.pf, a.pa
from football_sch.locationinfo2021all la
join
(select dg.team_id, sum(w) as w, sum(l) as l, sum(t) as t, sum(pf) as pf, sum(pa) as pa
from football_sch.data_grt_2011 dg 
group by dg.team_id) a on la.team_id = a.team_id
order by a.w desc, a.l asc, a.pf desc, a.pa asc;