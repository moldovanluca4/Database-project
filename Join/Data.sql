USE Project;

INSERT INTO Building(id, address_) VALUES
(1, 'College Ring 7'),
(2, 'Campus Ring 1'),
(3, 'Campus Ring 7'),
(4, 'College Ring 6'),
(5, 'Campus Ring 6'),
(6, 'Campus Ring 1');

INSERT INTO SCC(building_id, club, club_schedule_days, start_time, end_time) 
VALUES
(1, 'Football club', 'Monday', '14:00:00', '16:00:00'),
(2, 'Basketball club', 'Wednesday', '19:00:00', '21:00:00'),
(3, 'Ping Pong club', 'Thursday', '16:00:00', '18:00:00'),
(4, 'Mens Volleyball club', 'Tuesday', '16:00:00','18:00:00'),
(5, 'Badminton club', 'Saturday', '14:00:00', '15:00:00'),
(6, 'Field Hockey club', 'Monday', '17:00:00', '18:00:00'),
(1, 'Womens Football club', 'Wednesday', '16:00:00', '18:00:00'),
(2, 'Rowing club', 'Tuesday', '17:00:00', '19:00:00'),
(3, 'Womens Volleyball club', 'Monday', '19:00:00', '21:00:00'),
(4, 'Womens Basketball club', 'Thursday', '19:00:00', '21:00:00'),
(5, 'Crossfit club', 'Tuesday', '20:00:00', '21:00:00'),
(6, 'Netball club', 'Friday', '15:00:00', '17:00:00'),
(1, 'Dance club', 'Friday', '18:00:00', '20:00:00'),
(2, 'Taekwondo club', 'Sunday', '14:00:00', '16:00:00'),
(3, 'Tennis club', 'Saturday', '16:00:00', '18:00:00');


INSERT INTO IRC(building_id, books, book_availability, book_type, study_areas, study_area_capacity, other_rooms, other_rooms_capacity)
VALUES
(1, 'Introduction to Algorithms', 1, 'CS', 'Bottom floor area', 25, 'Bottom floor bathroom', 4),
(2, 'Structure and Interpretation of Computer Programs', 0, 'CS','First floor area', 30, 'IRC staff room', 4),
(3, 'Artificial Intelligence: A Modern Approach', 1, 'CS', 'Second floor area', 60, 'Printer room I', 3),
(4, 'Design Patterns: Elements of Reusable Object-Oriented Software', 1, 'CS', 'Quiet study area', 35, 'QSA bathroom', 5),
(5, 'Clean Code: A Handbook of Agile Software Craftsmanship', 0, 'CS', 'Master students Quiet Study Area', 20, 'Master students QSA bathroom', 3),
(6, 'Computer Systems: A Programmers Perspective', 1, 'CS', 'Jetbrains study area', 20, 'Printer room II', 3);


INSERT INTO Gym(building_id, membership_price, equipment, personnel, working_days, start_time, end_time)
VALUES
(1, 50, 'Chest press machine', 'Manolescu-Neacsu Andrei', 'Monday', '08:00:00', '11:00:00'),
(2, 50, 'Lat pulldown machine', 'Alexandru Dobleaga', 'Monday', '14:00:00', '17:00:00'),
(3, 50, 'Shoulder press machine', 'Robert Ionescu', 'Monday', '17:00:00', '22:00:00'),
(4, 50, 'Leg press machine', 'Simeon', 'Tuesday', '08:00:00', '10:00:00'),
(5, 50, 'Bicep curl machine', 'Manolescu-Neacsu Andrei', 'Tuesday', '13:00:00', '16:00:00'),
(6, 50, 'Tricep pushdown', 'Robert Ionescu', 'Tuesday', '18:00:00', '22:00:00');

INSERT INTO Dorm(building_id, room_type, other_rooms, meal_type, servery_schedule_days, start_time, end_time, servery_menu)
VALUES
(1, 'Type A', 'Common Room', 'Breakfast', 'Monday-Sunday', '08:00:00', '10:00:00', 'Pancakes, Bacon, Eggs, Bread, Marmalade'),
(2, 'Type B', 'College Office', 'Lunch', 'Monday-Sunday', '12:00:00', '14:00:00', 'Vegetable Soup, Mashed potatoes with beef, sides of vegetables'),
(3, 'Type C', 'Quiet study area', 'Dinner', 'Monday-Sunday', '16:00:00', '18:00:00', 'French fries with chicken breast, Lamb meat with rice, sides of vegetables, cheesecake'),
(4, NULL, 'Laundry room', NULL, 'Monday, Wednesday, Friday', '14:00:00', '22:00:00', 'Pizza hawaii, Pizza margherita, Pasta carbonara, Pizza quatro formaggi, pasta bolognese'),
(5, NULL, 'Floor kitchen', NULL, 'Tuesday, Thursday, Saturday', '14:00:00', '22:00:00','Beef burger with fries'),
(6, 'Type D', 'Study Hall', 'Breakfast', 'Monday-Sunday', '07:00:00', '09:00:00', 'Oatmeal, Fruits, Juice');

INSERT INTO Research_hall(building_id, department, rooms, schedule_days, start_time, end_time)
VALUES
(1, 'School of Computer Science & Engineering', 'Offices, Laboratories, Lecture halls', 'Monday-Friday', '08:00:00', '16:00:00'),
(2, 'School of Science', 'Offices, Laboratories, Lecture halls', 'Monday-Friday', '08:00:00', '16:00:00'),
(3, 'School of Businesses, Social & Decision Sciences', 'Offices, laboratories, Lecture halls', 'Monday-Friday', '08:00:00', '16:00:00'),
(4, 'School of Humanities', 'Offices, Laboratories, Lecture halls', 'Monday-Friday', '08:00:00', '16:00:00'),
(5, 'School of Engineering', 'Offices, Laboratories, Lecture halls', 'Monday-Friday', '08:00:00', '16:00:00'),
(6, 'School of Economics', 'Offices, Laboratories, Lecture halls', 'Monday-Friday', '08:00:00', '16:00:00');

INSERT INTO RLH(building_id, services, services_schedule_days, start_time, end_time, services_office_number, other_room)
VALUES
(1, 'IT Helpdesk', 'Monday-Friday', '09:00:00', '17:00:00', 101, 'Conference Room'),
(2, 'Academic Advising', 'Monday-Friday', '08:00:00', '16:00:00', 102, 'Meeting Room'),
(3, 'Career Services', 'Monday-Friday', '09:00:00', '17:00:00', 103, 'Lounge Area'),
(4, 'Counseling Services', 'Monday-Thursday', '09:00:00', '15:00:00', 104, 'Quiet Room'),
(5, 'Financial Aid Office', 'Monday-Friday', '09:30:00', '17:30:00', 105, 'Office Supplies Room'),
(6, 'Registrar Office', 'Tuesday-Saturday', '08:30:00', '16:30:00', 106, 'Student Records Room');

INSERT INTO Venue(id, name, opening_hours, building_id) VALUES
(1, 'Main Lecture Hall', '08:00-18:00', 1),
(2, 'Chemistry Lab', '09:00-17:00', 2),
(3, 'Campus Coffee Bar', '07:00-20:00', 3),
(4, 'Campus Theater', '10:00-22:00', 4),
(5, 'Conference Room A', '08:00-18:00', 5),
(6, 'C3 Cinema', '10:00-23:00', 6),
(7, 'College 3 Venue', '08:00-18:00', 5),
(8, 'Conrad Neiber Venue', '08:00-18:00', 2);


INSERT INTO LECTURE_HALL(venue_id, name_, address_) VALUES
(1, 'IRC Lecture Hall A', 'Campus Ring 1'),
(2, 'IRC Lecture Hall B', 'Campus Ring 1'),
(3, 'East Hall Lecture Hall', 'East Hall, Campus Ring 2'),
(4, 'West Hall Lecture Hall', 'West Hall, Campus Ring 3'),
(5, 'College 1 Lecture Hall', 'College 1, Campus Ring 4'),
(6, 'College 2 Lecture Hall', 'College 2, Campus Ring 5'),
(7, 'College 3 Lecture Hall', 'College 3, Campus Ring 6'),
(8, 'Conrad Neiber Lecture Hall', 'Campus Ring 1');


INSERT INTO Lab(venue_id, equipment, major) VALUES
(1, 'Biochemistry Lab, PCR Machines, Centrifuges', 'Biochemistry and Cell Biology'),
(2, 'Organic Chemistry Lab, Fume Hoods, Spectrometers', 'Chemistry and Biotechnology'),
(3, 'Physics Lab, Particle Accelerators, Lasers', 'Physics and Data Science'),
(4, 'Earth Sciences Lab, Rock Cutters, Soil Analyzers', 'Earth Sciences and Environmental Resources'),
(5, 'Robotics Lab, 3D Printers, Sensors', 'Robotics and Intelligent Systems'),
(6, 'Electrical Engineering Lab, Circuit Boards, Oscilloscopes', 'Electrical and Computer Engineering'),
(7, 'Data Science Lab, High-Performance Computers, Data Servers', 'Data Science for Society and Business');


INSERT INTO COFFEE_BAR(venue_id, prices, products) VALUES
(1, '2.50,2.00,4.50', 'Coffee, Tea, Sandwiches'),
(2, '3.80', 'Espresso, Latte, Sandwiches'),
(3, '2.90,3.50,5.00', 'Cappuccino, Iced Coffee, Wraps'),
(4, '2.50,3.00,4.20', 'Black Coffee, Croissant, Smoothie'),
(5, '3.20,3.50,5.50', 'Flat White, Matcha Latte, Panini'),
(6, '2.70,3.20,4.80', 'Americano, Hot Chocolate, Donuts'),
(7, '3.00,3.80,5.20', 'Mocha, Espresso, Brownies');


INSERT INTO Theater(venue_id, capacity, Ticket_price, play) VALUES
(1, 500, 20, 'Drama, Comedy, Musical'),
(2, 300, 15, 'Student Performances, Debates'),
(3, 450, 18, 'Guest Lectures, Stand-Up Shows'),
(4, 200, 0, 'Workshops, Rehearsals'),
(5, 600, 25, 'Film Screenings, Campus Gala'),
(6, 350, 22, 'Music Concerts, Talks'),
(7, 250, 0, 'Practice Sessions, Dance Rehearsals');


INSERT INTO MeetingRoom(venue_id, capacity, registration_required, equipment, hybrid_capable) VALUES
(1, 30, TRUE, 'Projector, Whiteboard', TRUE),
(2, 15, FALSE, 'TV Screen, HDMI Cable', TRUE),
(3, 50, TRUE, 'Smartboard, Video Conferencing', TRUE),
(4, 20, FALSE, 'Round Table, Wi-Fi', FALSE),
(5, 40, TRUE, 'Projector, Microphones', TRUE),
(6, 25, FALSE, 'Whiteboard, Speakers', FALSE);


INSERT INTO Cinema(venue_id, booking_price, snacks, snack_prices, available_time_slots) VALUES
(1, 10.00, 'Popcorn', 5, '14:00,21:00'),
(2, 9.50, 'Nachos', 4, '17:00,22:00'),
(3, 8.00, 'Chocolate', 3, '15:00,22:00'),
(4, 11.00, 'Candy', 3, '20:00,23:00'),
(5, 9.00, 'Soda', 2, '16:00,20:30'),
(6, 10.50, 'Chips', 3, '18:00,22:30'),
(7, 8.50, 'Popcorn', 2, '13:00,19:00');

INSERT INTO Event(Event_ID, Venue_ID, Date_) VALUES
(1, 1, '2025-11-09 09:00:00'),
(2, 2, '2025-11-09 14:00:00'),
(3, 3, '2025-11-10 10:00:00'),
(4, 4, '2025-11-11 12:00:00'),
(5, 5, '2025-11-12 18:00:00'),
(6, 6, '2025-11-13 15:00:00'),
(7, 1, '2025-11-13 15:00:00'),
(8, 2, '2025-11-14 00:00:00');


INSERT INTO Exam(Exam_ID, Event_ID, Exam_Name, Major, Duration) VALUES
(1, 1, 'Operating System', 'Computer Science', '02:00:00'),
(2, 2, 'Probability', 'Mathematics', '01:30:00'),
(3, 3, 'Functional programming', 'Software Engineering', '02:00:00'),
(4, 4, 'Ethical aspect of cybersecurity', 'Cybersecurity', '01:45:00'),
(5, 5, 'Database', 'Information Systems', '02:30:00');


INSERT INTO TOS(Tos_ID, Event_ID, Ticket_price, Theme) VALUES
(1, 5, 10, 'Speak Night'),
(2, 7, 5, 'Evening Chill'),
(3, 8, 20, 'End of Semester');


INSERT INTO Tournament(Tournament_ID, Event_ID, Tournament_name, Number_of_registered_teams) VALUES
(1, 3, 'Basketball', 6),
(2, 4, 'Football', 4),
(3, 1, 'Vollyeball', 8);


INSERT INTO CareerDay(CareerDay_ID, Event_ID, Company, Remote_) VALUES
(1, 6, 'Google', TRUE),
(2, 1, 'Microsoft', FALSE);


INSERT INTO Ceremony(Ceremony_ID, Event_ID, Name_) VALUES
(1, 7, 'Welcome Ceremony'),
(2, 5, 'Award Ceremony');


INSERT INTO FoodShow(Food_ID, Event_ID, Country) VALUES
(1, 6, 'Italy'),
(2, 1, 'France'),
(3, 5, 'China');
