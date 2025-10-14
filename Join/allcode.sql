
    CREATE TABLE Building (
    id INT PRIMARY KEY AUTO_INCREMENT,
    address_ VARCHAR(100) NOT NULL
);

CREATE TABLE SCC (
    building_id INT,
    club VARCHAR(50),
    club_schedule_days VARCHAR(50),
    start_time TIME,
    end_time TIME,
    FOREIGN KEY (building_id) REFERENCES Building(id)
);

CREATE TABLE IRC (
    building_id INT,
    books VARCHAR(250),
    book_availability BOOLEAN,
    book_type VARCHAR(10),
    study_areas VARCHAR(50),
    study_area_capacity INT,
    other_rooms VARCHAR(50),
    other_rooms_capacity INT,
    FOREIGN KEY (building_id) REFERENCES Building(id)
);

CREATE TABLE Gym (
    building_id INT,
    membership_price INT,
    equipment VARCHAR(50),
    personnel VARCHAR(50),
    working_days VARCHAR(50),
    start_time TIME,
    end_time TIME,
    FOREIGN KEY (building_id) REFERENCES Building(id)
);

CREATE TABLE Dorm (
    building_id INT,
    room_type VARCHAR(10),
    other_rooms VARCHAR(50),
    meal_type VARCHAR(15),
    servery_schedule_days VARCHAR(100),
    start_time TIME,
    end_time TIME,
    servery_menu VARCHAR(250),
    FOREIGN KEY (building_id) REFERENCES Building(id)
);

CREATE TABLE Research_hall (
    building_id INT,
    department VARCHAR(50),
    rooms VARCHAR(50),
    schedule_days VARCHAR(50),
    start_time TIME,
    end_time TIME,
    FOREIGN KEY (building_id) REFERENCES Building(id)
);

CREATE TABLE RLH (
    building_id INT,
    services VARCHAR(50),
    services_schedule_days VARCHAR(50),
    start_time TIME,
    end_time TIME,
    services_office_number INT,
    other_room VARCHAR(50),
    FOREIGN KEY (building_id) REFERENCES Building(id)
);

CREATE TABLE Venue (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    opening_hours VARCHAR(100),
    building_id INT NOT NULL,
    FOREIGN KEY (building_id) REFERENCES Building(id)
);

CREATE TABLE LECTURE_HALL (
    venue_id INT PRIMARY KEY,
    name_ VARCHAR(100),
    address_ VARCHAR(100),
    capacity INT,
    FOREIGN KEY (venue_id) REFERENCES Venue(id)
);

CREATE TABLE Lab (
    venue_id INT PRIMARY KEY,
    equipment VARCHAR(100),
    major VARCHAR(100),
    FOREIGN KEY (venue_id) REFERENCES Venue(id)
);

 CREATE TABLE COFFEE_BAR (
    venue_id INT PRIMARY KEY,
    prices VARCHAR(50),
    products VARCHAR(100),
    FOREIGN KEY (venue_id) REFERENCES Venue(id)
);

CREATE TABLE Theater (
    venue_id INT PRIMARY KEY,
    capacity INT,
    Ticket_price INT, 
    play VARCHAR(255), 
    FOREIGN KEY (venue_id) REFERENCES Venue(id)
);

CREATE TABLE MeetingRoom (
    venue_id INT PRIMARY KEY,
    capacity INT,
    registration_required BOOLEAN,
    equipment VARCHAR(255),
    hybrid_capable BOOLEAN,
    FOREIGN KEY (venue_id) REFERENCES Venue(id)
);

CREATE TABLE Cinema (
    venue_id INT PRIMARY KEY,
    booking_price DECIMAL(8, 2) NOT NULL, 
    snacks VARCHAR(50),
    snack_prices INT,      
    available_time_slots VARCHAR(255),   
    FOREIGN KEY (venue_id) REFERENCES Venue(id)
);

CREATE TABLE Event(
	Event_ID Int primary key,
    Venue_ID Int Not Null,
    Date_ Datetime,
	FOREIGN KEY (Venue_id) REFERENCES Venue(id)
    );
    
CREATE TABLE Exam(
	Exam_ID Int primary key,
    Event_ID Int,
    Exam_Name VARCHAR(50),
    Major VARCHAR(50),
    Duration TIME,
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
    Number_of_registered_teams Int,
    Sport VARCHAR(50),
    FOREIGN KEY(Event_ID) REFERENCES Event(Event_ID)
    );
    
CREATE TABLE CareerDay(
	CareerDay_ID Int primary key,
    Event_ID Int,
    Company varchar(100),
    Remote_ Boolean,
    Date_ Datetime,
    FOREIGN KEY(Event_ID) REFERENCES Event(Event_ID)
    );
    
CREATE TABLE Cermony(
	Cermony_ID Int primary key,
    Event_ID Int,
	Name_ varchar(100),
    Date_ Datetime,
	FOREIGN KEY(Event_ID) REFERENCES Event(Event_ID)
	);
    
CREATE TABLE FoodShow(
		Food_ID Int primary key,
        Event_ID Int,
        Country varchar(50),
        Chefs VARCHAR(50),
		FOREIGN KEY(Event_ID) REFERENCES Event(Event_ID)
	);
    
