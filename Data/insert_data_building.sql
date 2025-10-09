INSERT INTO Building(id, address_)
VALUES
(1, 'College Ring 7'),
(2, 'Campus Ring 1'),
(3, 'Campus Ring 7'),
(4, 'College Ring 6'),
(5, 'Campus RIng 6'),
(6, 'campus Ring 1');


INSERT INTO SCC(building_id, club, club_schedule_days, start_time, end_time) 
VALUES
(1, 'Football club', 'Monday', '14:00:00', '16:00:00'),
(2, 'Basketball club', 'Wednesday', '19:00:00', '21:00:00'),
(3, 'Ping Pong club', 'Thursday', '16:00:00', '18:00:00'),
(4, 'Mens Volleyball club', 'Tuesday', '16:00:00','18:00:00'),
(5, 'Badminton club', 'Saturday', '14:00:00', '15:00:00'),
(6, 'Field Hockey club', 'Monday', '17:00:00', '18:00:00'),
(7, 'Womens Football club', 'Wednesday', '16:00:00', '18:00:00'),
(8, 'Rowing club', 'Tuesday', '17:00:00', '19:00:00'),
(9, 'Womens Volleyball club', 'Monday', '19:00:00', '21:00:00'),
(10, 'Womens Baskteball club', 'Thursday', '19:00:00', '21:00:00'),
(11, 'Crossfit club', 'Tuesday', '20:00:00', '21:00:00'),
(12, 'Netball club', 'Friday', '15:00:00', '17:00:00'),
(13, 'Dance club', 'Friday', '18:00:00', '20:00:00'),
(14, 'Taekwondo club', 'Sunday', '14:00:00', '16:00:00'),
(15, 'Tennis club', 'Saturday', '16:00:00', '18:00:00');

INSERT INTO IRC(building_id, books, book_availability, book_type, study_areas, study_area_capacity, other_rooms, other_rooms_capacity)
VALUES
(1, 'Introduction to Algorithms', 1, 'CS', 'Bottom floor area', 25, 'Bottom floor bathroom', 4),
(2, 'Structure and Interpretation of Computer Programs', 0, 'CS','First floor area', 30, 'IRC staff room', 4),
(3, 'Artificial Intelligence: A Modern Approach', 1, 'CS', 'Second floor area', 60, 'Printer room I', 3),
(4, 'Design Patterns: Elements of Reusable Object-Oriented Software', 1, 'CS', 'Quiet study area', 35, 'QSA bathroom', 5),
(5, 'Clean Code: A Handbook of Agile Software Craftsmanship', 0, 'CS', 'Master students Quiet Study Area', 20, 'Master students QSA bathroom', 3),
(6, 'Computer Systems: A Programmers Perspective', 1, 'CS', 'Jetbrains study area', 20, 'Printer room II', 3),
(7, 'Operating System Concepts', 0, 'CS', NULL, NULL, 'Seminar room I', 25),
(8, 'Compilers: Principles, Techniques, & Tools (Dragon Book)', 1, 'CS', NULL, NULL, 'Seminar room II', 40),
(9, 'Deep Learning', 1, 'CS', NULL, NULL, 'ICC East Wing', 100),
(10, 'Algorithms (4th ed.) / or The Algorithm Design Manual', 0, 'CS', NULL, NULL, 'Coffee bar', 15),
(11, 'Introduction to Operations Research', 1, 'IEM' ,NULL, NULL, 'ICC Conference Room', 45),
(12, 'Factory Physics', 0, 'IEM', NULL, NULL, 'IRC Main Area', 80),
(13, 'Designing & Managing the Supply Chain', 1, 'IEM', NULL, NULL, 'IRC Terrace', 50),
(14, 'Work Systems and the Methods, Measurement, and Management of Work', 1, 'IEM', NULL, NULL, 'ICC West Wing', 100),
(15, 'The Goal: A Process of Ongoing Improvement', 1, 'IEM', NULL, NULL, 'IRC Pond', 5),
(16, 'Operations Management', 0, 'IEM', NULL, NULL, NULL, NULL);

INSERT INTO Gym(building_id, membership_price, equipment, personnel, working_days, start_time, end_time)
VALUES
(1, 50, 'Chest press machine', 'Manolescu-Neacsu Andrei', 'Monday', '08:00:00', '11:00:00'),
(2, 50, 'Lat pulldown machine', 'Alexandru Dobleaga', 'Monday', '14:00:00', '17:00:00'),
(3, 50, 'Shoulder press machine', 'Robert Ionescu', 'Monday', '17:00:00', '22:00:00'),
(4, 50, 'Leg press machine', 'Simeon', 'Tuesday', '08:00:00', '10:00:00'),
(5, 50, 'Bicep curl machine', 'Manolescu-Neacsu Andrei', 'Tuesday', '13:00:00', '16:00:00'),
(6, 50, 'Tricep pushdown', 'Robert Ionescu', 'Tuesday', '18:00:00', '22:00:00'),
(7, 50, 'Treadmill', 'Simeon', 'Wednesday','09:00:00', '11:00:00'),
(8, 50, 'Seated Row machine', 'Alexandru Dobleaga', 'Wednesday', '14:00:00', '16:00:00'),
(9, 50, 'Butterfly machine', 'Manolescu-Neacsu Andrei', 'Wednesday', '18:00:00', '22:00:00'),
(10, 50, 'Cable machine', 'Manolescu-Neacsu Andrei', 'Thursday', '08:00:00', '13:00:00'),
(11, 50, 'Squat machine', 'Robert Ionescu', 'Thursday', '13:00:00', '16:00:00'),
(12, 50, 'Bench press', 'Alexandru Dobleaga', 'Thursday', '18:00:00', '22:00:00'),
(13, 50, 'Dumbbells', 'Simeon', 'Friday', '10:00:00', '12:00:00'),
(14, 50, 'Leg curl machine', 'Robert Ionescu', 'Friday', '14:00:00', '17:00:00'),
(15, 50, 'Leg extension machine', 'Alexandru Dobleaga', 'Friday', '19:00:00', '22:00:00'), 
(16, 50, 'Stationary bike', 'Simeon', 'Saturday', '14:00:00', '17:00:00'),
(17, 50, 'Stepper', 'Manolescu-Neacsu Andrei', 'Saturday', '19:00:00', '22:00:00');

INSERT INTO Dorm(building_id, room_type, other_rooms, meal_type, servery_schedule_days, start_time, end_time, servery_menu)
VALUES
(1, 'Type A', 'Common Room', 'Breakfast', 'Monday-Sunday', '08:00:00', '10:00:00', 'Pancakes, Bacon, Eggs, Bread, Marmalade'),
(2, 'Type B', 'College Office', 'Lunch', 'Monday-Sunday', '12:00:00', '14:00:00', 'Vegetable Soup, Mashed potatoes with beef, sides of vegetables'),
(3, 'Type C', 'Quiet study area', 'Dinner', 'Monday-Sunday', '16:00:00', '18:00:00', 'French fries with chicken breast, Lamb meat with rice, sides of vegetables, cheesecake'),
(4, NULL, 'Laundry room', NULL, 'Monday, Wednesday, Friday', '14:00:00', '22:00:00', 'Pizza hawaii, Pizza margherita, Pasta carbonara, Pizza quatro formaggi, pasta bolognese'),
(5, NULL, 'Floor kitchen', NULL, 'Tuesday, Thursday, Saturday', '14:00:00', '22:00:00','Beef burger with fries');

INSERT INTO Research_hall(building_id, department, rooms, schedule_days, start_time, end_time)
VALUES
(1, 'School of Computer Science & Engineering', 'Offices, Laboratories, Lecture halls', 'Monday-Friday', '08:00:00', '16:00:00'),
(2, 'School of Science', 'Offices, Laboratories, Lecture halls', 'Monday-Friday', '08:00:00', '16:00:00'),
(3, 'School of Businesses, Social & Decision Sciencies', 'Offices, laboratories, Lecture halls', 'Monday-Friday', '08:00:00', '16:00:00');


INSERT INTO RLH(building_id, services, services_schedule_days, start_time, end_time, services_office_number, other_room)
VALUES
(1, 'IT Helpdesk', 'Monday-Friday', '09:00:00', '17:00:00', 101, 'Conference Room'),
(2, 'Academic Advising', 'Monday-Friday', '08:00:00', '16:00:00', 102, 'Meeting Room'),
(3, 'Career Services', 'Monday-Friday', '09:00:00', '17:00:00', 103, 'Lounge Area'),
(4, 'Counseling Services', 'Monday-Thursday', '09:00:00', '15:00:00', 104, 'Quiet Room'),
(5, 'Financial Aid Office', 'Monday-Friday', '09:30:00', '17:30:00', 105, 'Office Supplies Room'),
(6, 'Registrar Office', 'Tuesday-Saturday', '08:30:00', '16:30:00', 106, 'Student Records Room'),
(7, 'International Student Office', 'Monday-Friday', '10:00:00', '18:00:00', 107, 'Cultural Exchange Room'),
(8, 'TK Health Insurance', 'Monday-Thursday', '08:00:00', '15:30:00', 108, 'Health Resource Room'),
(9, 'Housing Office', 'Tuesday-Saturday', '09:00:00', '17:00:00', 109, 'Housing Resource Room'),
(10, 'Security Office', 'Monday-Friday', '07:00:00', '15:00:00', 110, 'Security Monitoring Room'),
(11, 'Leading board', 'Monday-Friday', '11:00:00', '19:00:00', 111, 'Event Planning Room'),
(12, 'Student Activities Office', 'Monday-Friday', '08:30:00', '16:30:00', 112, 'Activity Resource Room');



