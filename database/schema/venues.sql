CREATE TABLE Venue (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    start_time TIME,
    finish_time TIME,
    building_id INT,
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
    access_ VARCHAR(100),
    major VARCHAR(100),
    FOREIGN KEY (venue_id) REFERENCES Venue(id)
);
 CREATE TABLE Coffee_bar (
    venue_id INT PRIMARY KEY,
    prices DECIMAL(10, 2),
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