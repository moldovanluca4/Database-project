CREATE TABLE Venue (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    opening_hours VARCHAR(100)
);
CREATE TABLE LECTURE_HALL (
    venue_id INT PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(100),
    FOREIGN KEY (venue_id) REFERENCES Venue(id)
);
CREATE TABLE Lab (
    venue_id INT PRIMARY KEY,
    facilities VARCHAR(100),
    Access VARCHAR(100),
    major VARCHAR(100),
    FOREIGN KEY (venue_id) REFERENCES Venue(id)
);
 CREATE TABLE COFFEE_BAR (
    venue_id INT PRIMARY KEY,
    prices DECIMAL(10, 2),
    products VARCHAR(100),
    FOREIGN KEY (venue_id) REFERENCES Venue(id)
);
CREATE TABLE Theater (
    venue_id INT PRIMARY KEY,
     capacity INT,
    ticketed_events BOOLEAN, 
    event_theme VARCHAR(255), 
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
    available_themes VARCHAR(255),       
    available_time_slots VARCHAR(255),   
    FOREIGN KEY (venue_id) REFERENCES Venue(id)
);