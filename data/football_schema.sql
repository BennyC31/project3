-- DROP SCHEMA football_sch;

CREATE SCHEMA football_sch AUTHORIZATION postgres;

-- football_sch.profootballyearsummary definition

-- Drop table

-- DROP TABLE football_sch.profootballyearsummary;

CREATE TABLE football_sch.profootballyearsummary (
	leag_year int NULL,
	team_id varchar(50) NULL,
	team_location varchar(50) NULL,
	team_name varchar(50) NULL,
	conference varchar(50) NULL,
	division varchar(50) NULL,
	w int NULL,
	l int NULL,
	t int NULL,
	pf int NULL,
	pa int NULL,
	place int NULL,
	leagabrv varchar(50) NULL
);

-- football_sch.teamlocation definition

-- Drop table

-- DROP TABLE football_sch.teamlocation;

CREATE TABLE football_sch.teamlocation (
	loc_id int primary key,
	team_location varchar(50) NOT NULL,
	lat float4 NULL,
	lon float4 NULL
);