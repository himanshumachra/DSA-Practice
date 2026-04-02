create database colg;

USE colg;


create table SUB(
id int primary key,
SUBJECT varchar(50)
);

CREATE TABLE stud(
ROLLNO int PRIMARY KEY,
NAME VARCHAR(50),
MARKS INT,
SUB_ID VARCHAR(50),
SCHOOL VARCHAR(6) default "N.M.C",
GRADE VARCHAR(2),
CITY VARCHAR(30),
foreign key(SUB_ID) REFERENCES SUB(id)
);


INSERT INTO stud(ROLLNO, NAME, MARKS, GRADE, CITY)
VALUES
(202,"raj",96,"A+","ftb"),
(210,"raj8",45,"A+","ftbk"),
(203,"ra5j",85,"A+","ftkb"),
(220,"r5aj",81,"A+","fhtb"),
(301,"dev",79,"B2","NOR");

SHOW DATABASES;
SELECT distinct school FROM stud;
SHOW TABLES;

select count(NAME) FROM stud LIMIT 2;
select city from stud group by city;

select city,avg(MARKS) 
from stud
group by city
order by avg(MARKS) ASC;

set SQL_SAFE_UPDATES = 0;

update stud
set marks=marks-4;

select * from stud;