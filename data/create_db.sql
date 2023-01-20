-- drop database if exists football_db;

create database football_db
with
owner = postgres
encoding='UTF-8'
tablespace=pg_default
connection limit=-1;