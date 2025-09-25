CREATE TABLE Building (
    id INT PRIMARY KEY AUTO_INCREMENT,
    address_ VARCHAR(100) NOT NULL
);

CREATE TABLE SSC (
    building_id INT,
    club VARCHAR(50),
    club_schedule VARCHAR(50),
    FOREIGN KEY (building_id) REFERENCES Building(id)
);

CREATE TABLE IRC (
    building_id INT,
    books VARCHAR(50),
    book_availability BOOLEAN,
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
    working_hours VARCHAR(50),
    FOREIGN KEY (building_id) REFERENCES Building(id)
);

CREATE TABLE Dorm (
    building_id INT,
    room_type VARCHAR(10),
    other_rooms VARCHAR(50),
    servery_schedule VARCHAR(50),
    servery_menu VARCHAR(50),
    FOREIGN KEY (building_id) REFERENCES Building(id)
);

CREATE TABLE Research_hall (
    building_id INT,
    department VARCHAR(50),
    rooms VARCHAR(50),
    schedule VARCHAR(50),
    FOREIGN KEY (building_id) REFERENCES Building(id)
);

CREATE TABLE RLH (
    building_id INT,
    services VARCHAR(50),
    services_schedule VARCHAR(50),
    services_office_number INT,
    other_room VARCHAR(50),
    FOREIGN KEY (building_id) REFERENCES Building(id)
);
