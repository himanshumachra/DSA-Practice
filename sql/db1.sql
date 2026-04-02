CREATE DATABASE collage;

use collage; 

CREATE table students(
sr_no int PRIMARY KEY,
roll_no int NOT NULL,
Name varchar(50) NOT NULL    
);


CREATE DATABASE ll;

DROP TABLE students;


DROP TABLE gtudents;
SHOW TABLES ;

DROP TABLE gtudents;
SELECT * FROM students;

INSERT INTO students
(sr_no,roll_no,Name)
VALUES
(1,101,"raj"),
(2,102,"dev"),
(3,103,"devraj")

CREATE DATABASE company;

CREATE TABLE employee(
empID int primary key,
);
