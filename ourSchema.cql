DROP KEYSPACE project;
CREATE KEYSPACE project WITH REPLICATION = {'class':'SimpleStrategy', 'replication_factor':3};
CREATE TABLE project.tweets (
    recordid timeuuid PRIMARY KEY, 
    name varchar,
    text varchar,
    date varchar,
    latitude double,
    longitude double,
    emotionscore double,
    emotion varchar 
);
CREATE TABLE project.shen (
    recordid timeuuid PRIMARY KEY,
    name varchar,
    text varchar,
    date varchar,
    latitude double,
    longitude double,
    emotionscore double,
    emotion varchar
);

