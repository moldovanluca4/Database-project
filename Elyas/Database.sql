CREATE DATABASE FOLDER;
Use FOLDER;
CREATE TABLE Event(
	Event_ID Int primary key,
    Date_ Datetime
    );
    
CREATE TABLE Exam(
	Exam_ID Int primary key,
    Event_ID Int,
    Exam_Name VARCHAR(50),
    FOREIGN KEY(Event_ID) REFERENCES Event(Event_ID)
    );
    
CREATE TABLE TOS(
	Tos_ID Int primary key,
    Event_ID Int,
    Ticket_price Int,
    Theme varchar(100),
	FOREIGN KEY(Event_ID) REFERENCES Event(Event_ID)
    );
    
CREATE TABLE Tournament(
	Tournament_ID Int primary key,
    Event_ID Int,
    Tournament_name varchar(100),
    Number_team Int,
    FOREIGN KEY(Event_ID) REFERENCES Event(Event_ID)
    );
    
CREATE TABLE CareerDay(
	CareerDay_ID Int primary key,
    Event_ID Int,
    Company varchar(100),
    Remote Boolean,
    FOREIGN KEY(Event_ID) REFERENCES Event(Event_ID)
    );
    
CREATE TABLE Cermony(
	Cermony_ID Int primary key,
    Event_ID Int,
	Name varchar(100),
	FOREIGN KEY(Event_ID) REFERENCES Event(Event_ID)
	);
    
CREATE TABLE FoodShow(
		Food_ID Int primary key,
        Event_ID Int,
        Country varchar(50),
		FOREIGN KEY(Event_ID) REFERENCES Event(Event_ID)
	);
