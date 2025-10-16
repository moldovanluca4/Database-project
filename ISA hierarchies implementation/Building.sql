--superclass
CREATE TABLE Building(
    id INT PRIMARY KEY AUTO_INCREMENT,
    address_ VARCHAR(100) NOT NULL,
    building_type VARCHAR(30) NOT NULL
);


--scc
CREATE TABLE SCC(
    building_id INT PRIMARY KEY,
    FOREIGN KEY (building_id) REFERENCES Building(id)
);

CREATE TABLE Clubs(
    id INT PRIMARY KEY AUTO_INCREMENT,
    scc_building_id INT,
    club_name VARCHAR(70),
    schedule_days VARCHAR(50),
    start_time TIME,
    end_time TIME,
    FOREIGN KEY (scc_building_id) REFERENCES SCC(building_id)
);


--irc
CREATE TABLE IRC(
    building_id INT PRIMARY KEY,
    FOREIGN KEY (building_id) REFERENCES Building(id)
);

CREATE TABLE Books(
    id INT PRIMARY KEY AUTO_INCREMENT,
    irc_building_id INT,
    title VARCHAR(300),
    book_availability BOOLEAN,
    book_type VARCHAR(10),
    FOREIGN KEY (irc_building_id) REFERENCES IRC(building_id)
);

CREATE TABLE StudyArea(
    id INT PRIMARY KEY AUTO_INCREMENT,
    irc_building_id INT,
    area_name VARCHAR(100),
    area_capacity INT,
    FOREIGN KEY (irc_building_id) REFERENCES IRC(building_id)
);

CREATE TABLE OtherRooms(
    id INT PRIMARY KEY AUTO_INCREMENT,
    irc_building_id INT,
    other_room_name VARCHAR(100),
    other_rooms_capacity INT,
    FOREIGN KEY (irc_building_id) REFERENCES IRC(building_id)
);


--gym building
CREATE TABLE Gym(
    building_id INT PRIMARY KEY,
    membership_price INT,
    FOREIGN KEY (building_id) REFERENCES Building(id)
);

CREATE TABLE GymEquipment(
    id INT PRIMARY KEY AUTO_INCREMENT,
    gym_building_id INT, 
    equipment_name VARCHAR(100),
    FOREIGN KEY (gym_building_id) REFERENCES Gym(building_id)
);

CREATE TABLE GymPersonnel(
    id INT PRIMARY KEY AUTO_INCREMENT,
    gym_building_id INT,
    personnel_name VARCHAR(100),
    FOREIGN KEY (gym_building_id) REFERENCES Gym(building_id)
);

CREATE TABLE GymSchedule(
    id INT PRIMARY KEY AUTO_INCREMENT,
    gym_building_id INT,
    personnel_id INT,
    working_days VARCHAR(50),
    start_time TIME,
    end_time TIME,
    FOREIGN KEY (gym_building_id) REFERENCES Gym(building_id),
    FOREIGN KEY (personnel_id) REFERENCES GymPersonnel(id)
);


--Residential buildings
CREATE TABLE Dorm(
    building_id INT PRIMARY KEY,
    FOREIGN KEY (building_id) REFERENCES Building(id)
);

CREATE TABLE DormServery(
    id INT PRIMARY KEY AUTO_INCREMENT,
    dorm_building_id INT, 
    meal_type VARCHAR(50),
    servery_menu VARCHAR(300),
    working_days VARCHAR(50),
    start_time TIME,
    end_time TIME,
    FOREIGN KEY (dorm_building_id) REFERENCES Dorm(building_id)
);

CREATE TABLE DormRoom(
    id INT PRIMARY KEY AUTO_INCREMENT,
    dorm_building_id INT,
    room_type VARCHAR(50),
    room_capacity INT,
    other_rooms VARCHAR(20),
    furniture VARCHAR(50),
    FOREIGN KEY (dorm_building_id) REFERENCES Dorm(building_id)
);

CREATE TABLE DormStructure(
    id INT PRIMARY KEY AUTO_INCREMENT,
    dorm_building_id INT,
    dorm_block VARCHAR(5),
    other_rooms VARCHAR(100),
    FOREIGN KEY (dorm_building_id) REFERENCES Dorm(building_id)
);

--research buildings
CREATE TABLE Research_hall(
    building_id INT PRIMARY KEY,
    FOREIGN KEY (building_id) REFERENCES Building(id)
);

CREATE TABLE Research_hallSchedule(
    id INT PRIMARY KEY AUTO_INCREMENT,
    research_hall_building_id INT,
    working_days VARCHAR(50),
    start_time TIME,
    end_time TIME,
    FOREIGN KEY (research_hall_building_id) REFERENCES Research_hall(building_id)
);

CREATE TABLE Majors(
    id INT PRIMARY KEY AUTO_INCREMENT,
    major_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE ResearchHallMajors(
    research_hall_building_id INT,
    major_id INT,
    PRIMARY KEY (research_hall_building_id, major_id),
    FOREIGN KEY (research_hall_building_id) REFERENCES Research_hall(building_id),
    FOREIGN KEY (major_id) REFERENCES Majors(id)
);

CREATE TABLE RLH(
    building_id INT PRIMARY KEY,
    FOREIGN KEY (building_id) REFERENCES Building(id)
);

CREATE TABLE RLHServices(
    id INT PRIMARY KEY AUTO_INCREMENT,
    rlh_building_id INT,
    service_name_ VARCHAR(100),
    service_office_number INT,
    other_room VARCHAR(100),
    other_room_number INT,
    FOREIGN KEY (rlh_building_id) REFERENCES RLH(building_id)
);

CREATE TABLE RLHServicesSchedule(
    id INT PRIMARY KEY AUTO_INCREMENT,
    rlh_building_id INT,
    service_id INT,
    service_schedule_days VARCHAR(50),
    start_time TIME,
    end_time TIME,
    FOREIGN KEY (rlh_building_id) REFERENCES RLH(building_id),
    FOREIGN KEY (service_id) REFERENCES RLHServices(id)
);





