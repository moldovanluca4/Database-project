--superclass
CREATE TABLE Building (
    id INT PRIMARY KEY AUTO_INCREMENT,
    address_ VARCHAR(100) NOT NULL
);

--subclasses
CREATE TABLE SCC (
    building_id INT,
    club VARCHAR(50),
    club_schedule_days VARCHAR(50),
    start_time TIME,
    end_time TIME
    FOREIGN KEY (building_id) REFERENCES Building(id)
);

CREATE TABLE IRC (
    building_id INT,
    books VARCHAR(300),
    book_availability BOOLEAN,
    book_type VARCHAR(10),
    study_areas VARCHAR(80),
    study_area_capacity INT,
    other_rooms VARCHAR(80),
    other_rooms_capacity INT,
    FOREIGN KEY (building_id) REFERENCES Building(id)
);

CREATE TABLE Gym (
    building_id INT,
    membership_price INT,
    equipment VARCHAR(300),
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
    meal_type VARCHAR(30),
    servery_schedule_days VARCHAR(100),
    start_time TIME,
    end_time TIME,
    servery_menu VARCHAR(300),
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
    services VARCHAR(100),
    services_schedule_days VARCHAR(50),
    start_time TIME,
    end_time TIME,
    services_office_number INT,
    other_room VARCHAR(50),
    FOREIGN KEY (building_id) REFERENCES Building(id)
);
