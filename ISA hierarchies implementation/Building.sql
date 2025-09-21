CREATE TABLE SSC(
    club VARCHAR(50),
    club_schedule VARCHAR(50)
);

CREATE TABLE IRC(
    books VARCHAR(50),
    book_availability BOOLEAN,
    study_areas VARCHAR(50),
    study_area_capacity INT,
    other_rooms VARCHAR(50),
    other_rooms_capacity INT
);

CREATE TABLE Gym(
    member_ship_price INT,
    equipment VARCHAR(50),
    personnel VARCHAR(50),
    working_hours TIME,
);

CREATE TABLE Dorm(
    room_type VARCHAR(10),
    other_rooms VARCHAR(50),
    servery_schedule TIME,
    servery_menu VARCHAR(50),
);

CREATE TABLE Research_hall(
    department VARCHAR(50),
    rooms VARCHAR(50),
    schedule VARCHAR(50)
);

CREATE TABLE RLH(
    services VARCHAR(50),
    services_schedule TIME,
    services_office_number INT,
    other_room VARCHAR(50)
);