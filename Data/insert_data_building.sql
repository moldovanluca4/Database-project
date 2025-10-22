INSERT INTO Building(id, address_, building_type)
VALUES
(1, 'Sport Convention Center', 'SCC'),
(2, 'International Research Center', 'IRC'),
(3, 'Campus Gym', 'Gym'),
(4, 'College 3', 'Dorm'),
(5, 'College Mercator', 'Dorm'),
(6, 'College Krupp', 'Dorm'),
(7, 'College Nordmetal', 'Dorm'),
(8, 'School of Computer Science & Engineering', 'Research_hall'),
(9, 'School of Science', 'Research_hall'),
(10, 'School of Businesses, Social & Decision Sciencies', 'Research_hall'),
(11, 'Reimar Lüst Hall ', 'RLH');



INSERT INTO SCC(building_id)
VALUES
(1);

INSERT INTO Clubs(scc_building_id, club_name, schedule_days, start_time, end_time)
VALUES
(1, 'Football club', 'Monday', '14:00:00', '16:00:00'),
(1, 'Basketball club', 'Wednesday', '19:00:00', '21:00:00'),
(1, 'Ping Pong club', 'Thursday', '16:00:00', '18:00:00'),
(1, 'Mens Volleyball club', 'Tuesday', '16:00:00','18:00:00'),
(1, 'Badminton club', 'Saturday', '14:00:00', '15:00:00'),
(1, 'Field Hockey club', 'Monday', '17:00:00', '18:00:00'),
(1, 'Womens Football club', 'Wednesday', '16:00:00', '18:00:00'),
(1, 'Rowing club', 'Tuesday', '17:00:00', '19:00:00'),
(1, 'Womens Volleyball club', 'Monday', '19:00:00', '21:00:00'),
(1, 'Womens Baskteball club', 'Thursday', '19:00:00', '21:00:00'),
(1, 'Crossfit club', 'Tuesday', '20:00:00', '21:00:00'),
(1, 'Netball club', 'Friday', '15:00:00', '17:00:00'),
(1, 'Dance club', 'Friday', '18:00:00', '20:00:00'),
(1, 'Taekwondo club', 'Sunday', '14:00:00', '16:00:00'),
(1, 'Tennis club', 'Saturday', '16:00:00', '18:00:00');



INSERT INTO IRC(building_id)
VALUES
(2);

INSERT INTO Books(irc_building_id, title, book_availability, book_type)
VALUES
(2, 'Introduction to Algorithms', 1, 'CS'),
(2, 'Structure and Interpretation of Computer Programs', 0, 'CS'),
(2, 'Artificial Intelligence: A Modern Approach', 1, 'CS'),
(2, 'Design Patterns: Elements of Reusable Object-Oriented Software', 1, 'CS'),
(2, 'Clean Code: A Handbook of Agile Software Craftsmanship', 0, 'CS'),
(2, 'Computer Systems: A Programmers Perspective', 1, 'CS'),
(2, 'Operating System Concepts', 0, 'CS'),
(2, 'Compilers: Principles, Techniques, & Tools (Dragon Book)', 1, 'CS'),
(2, 'Deep Learning', 1, 'CS'),
(2, 'Algorithms (4th ed.) / or The Algorithm Design Manual', 0, 'CS'),
(2, 'Introduction to Operations Research', 1, 'IEM'),
(2, 'Factory Physics', 0, 'IEM'),
(2, 'Designing & Managing the Supply Chain', 1, 'IEM'),
(2, 'Work Systems and the Methods, Measurement, and Management of Work', 1, 'IEM'),
(2, 'The Goal: A Process of Ongoing Improvement', 1, 'IEM'),
(2, 'Operations Management', 0, 'IEM');

INSERT INTO StudyArea(irc_building_id, area_name, area_capacity)
VALUES
(2, 'Bottom floor area', 25),
(2, 'First floor area', 30),
(2, 'Second floor area', 60),
(2, 'Quiet study area', 35),
(2, 'Master students Quiet Study Area', 20),
(2, 'Jetbrains study area', 20);

INSERT INTO OtherRooms(irc_building_id, other_room_name, other_rooms_capacity)
VALUES
(2, 'Bottom floor bathroom', 4),
(2, 'IRC staff room', 4),
(2, 'Printer room I', 3),
(2, 'QSA bathroom', 5),
(2, 'Master students QSA bathroom', 3),
(2, 'Printer room II', 3),
(2, 'Seminar room I', 25),
(2, 'Seminar room II', 40),
(2, 'ICC East Wing', 100),
(2, 'Coffee bar', 15),
(2, 'ICC Conference Room', 45),
(2, 'IRC Main Area', 80),
(2, 'IRC Terrace', 50),
(2, 'ICC West Wing', 100),
(2, 'IRC Pond', 5);

INSERT INTO Gym(building_id, membership_price)
VALUES
(3, 50);

INSERT INTO GymEquipment(gym_building_id, equipment_name)
VALUES
(3, 'Chest press machine'),
(3, 'Lat pulldown machine'),
(3, 'Shoulder press machine'),
(3, 'Leg press machine'),
(3, 'Bicep curl machine'),
(3, 'Tricep pushdown'),
(3, 'Treadmill'),
(3, 'Seated Row machine'),
(3, 'Butterfly machine'),
(3, 'Cable machine'),
(3, 'Squat machine'),
(3, 'Bench press'),
(3, 'Dumbbells'),
(3, 'Leg curl machine'),
(3, 'Leg extension machine'),
(3, 'Stationary bike'),
(3, 'Stepper');

INSERT INTO GymPersonnel(gym_building_id, personnel_name)
VALUES
(3, 'Manolescu-Neacsu Andrei'),
(3, 'Alexandru Dobleaga'),
(3, 'Robert Ionescu'),
(3, 'Simeon');


INSERT INTO GymSchedule(gym_building_id, personnel_id, working_days, start_time, end_time)
VALUES
(3, 1, 'Monday', '08:00:00', '11:00:00'),
(3, 2, 'Monday', '14:00:00', '17:00:00'),
(3, 3, 'Monday', '18:00:00', '22:00:00'),
(3, 4, 'Tuesday', '08:00:00', '10:00:00'),
(3, 1, 'Tuesday', '13:00:00', '16:00:00'),
(3, 3, 'Tuesday', '18:00:00', '22:00:00'),
(3, 4, 'Wednesday', '09:00:00', '11:00:00'),
(3, 2, 'Wednesday', '14:00:00', '16:00:00'),
(3, 1, 'Wednesday', '18:00:00', '22:00:00'),
(3, 1, 'Thursday', '08:00:00', '13:00:00'),
(3, 3, 'Thursday', '14:00:00', '16:00:00'),
(3, 2, 'Thursday', '18:00:00', '22:00:00'),
(3, 4, 'Friday', '10:00:00', '12:00:00'),
(3, 3, 'Friday', '14:00:00', '17:00:00'),
(3, 2, 'Friday', '19:00:00', '22:00:00'), 
(3, 4, 'Saturday', '14:00:00', '17:00:00'),
(3, 1, 'Saturday', '19:00:00', '22:00:00'),
(3, 2, 'Sunday', '10:00:00', '14:00:00');


INSERT INTO Dorm(building_id)
VALUES
(4),
(5),
(6),
(7);

INSERT INTO DormServery(dorm_building_id, meal_type, servery_menu, working_days, start_time, end_time)
VALUES
(4, 'Breakfast', 'Pancakes, Bacon, Eggs, Bread, Marmalade', 'Monday-Sunday', '08:00:00', '10:00:00'),
(4, 'Lunch', 'Vegetable Soup, Mashed potatoes with beef, sides of vegetables', 'Monday-Sunday', '12:00:00', '14:00:00'),
(4, 'Dinner', 'French fries with chicken breast, Lamb meat with rice, sides of vegetables, cheesecake', 'Monday-Sunday', '16:00:00', '18:00:00'),
(5, NULL, 'Pizza hawaii, Pizza margherita, Pasta carbonara, Pizza quatro formaggi, pasta bolognese', 'Monday, Wednesday, Friday', '14:00:00', '22:00:00'),
(6, NULL,'Beef burger with fries', 'Tuesday, Thursday, Saturday', '14:00:00', '22:00:00'),
(7, 'Breakfast', 'Pancakes, Joghurt, Hashbrowns, Croissants', 'Monday-Sunday', '08:00:00', '10:00:00'),
(7, 'Lunch', 'Chicken noodle soup, Spaghetti with tomato sauce, sides of vegetables', 'Monday-Sunday', '12:00:00', '14:00:00'),
(7, 'Dinner', 'Roasted potatoes with pork, Grilled fish with rice, sides of vegetables, fruit salad', 'Monday-Sunday', '16:00:00', '18:00:00');

INSERT INTO DormRoom(dorm_building_id, room_type, room_capacity, other_rooms, furniture)
VALUES
(4, 'Type A', 1, 'Bathroom', 'Bed, Desk, Chair, Wardrobe, Shelves'),
(4, 'Type B', 1, 'Shared Bathroom and hallway', 'Bed, Desk, Chair, Wardrobe, Shelve'),
(4, 'Type C', 2, 'Bathroom', '2 Beds, 2 Desks, 2 Chairs, 2 Wardrobes'),
(5, 'Type A', 1, 'Bathroom', 'Bed, Desk, Chair, Wardrobe, Shelves'),
(5, 'Type B', 1, 'Shared Bathroom and hallway', 'Bed, Desk, Chair, Wardrobe, Shelve'),
(5, 'Type C', 2, 'Bathroom', '2 Beds, 2 Desks, 2 Chairs, 2 Wardrobes'),
(6, 'Type A', 1, 'Bathroom', 'Bed, Desk, Chair, Wardrobe, Shelves'),
(6, 'Type B', 1, 'Shared Bathroom and hallway', 'Bed, Desk, Chair, Wardrobe, Shelve'),
(6, 'Type C', 2, 'Bathroom', '2 Beds, 2 Desks, 2 Chairs, 2 Wardrobes'),
(7, 'Type A', 1, 'Bathroom', 'Bed, Desk, Chair, Wardrobe, Shelves'),
(7, 'Type B', 1,'Shared Bathroom and hallway', 'Bed, Desk, Chair, Wardrobe, Shelve'),
(7,'Type C', 2,'Bathroom', '2 Beds, 2 Desks, 2 Chairs, 2 Wardrobes');

INSERT INTO DormStructure(dorm_building_id, dorm_block, other_rooms)
VALUES
(4, 'A', 'Laundry Room, Kitchenette'),
(4, 'B', 'Laundry Room, Kitchenette'),
(4, 'C', 'Laundry Room, Kitchenette'),
(4, 'D', 'Laundry Room, Kitchenette'),
(4, 'E', 'Common Room, Quiet Study Area, College Office, Servery'),
(5, 'A', 'Laundry Room, Kitchenette'),
(5, 'B', 'Laundry Room, Kitchenette'),
(5, 'C', 'Laundry Room, Kitchenette'),
(5, 'D', 'Common Room, Quiet Study Area, College Office, Servery'),
(6, 'A', 'Laundry Room, Kitchenette'),
(6, 'B', 'Laundry Room, Kitchenette'),
(6, 'C', 'Laundry Room, Kitchenette'),
(6, 'D', 'Common Room, Quiet Study Area, College Office, Servery'),
(6, 'E', 'Laundry Room, Kitchenette'),
(6, 'F', 'Laundry Room, Kitchenette'),
(7, 'A', 'Laundry Room, Kitchenette'),
(7, 'B', 'Common Room, Quiet Study Area, College Office, Servery'),
(7, 'C', 'Laundry Room, Kitchenette');


INSERT INTO Research_hall(building_id)
VALUES
(8),
(9),
(10);

INSERT INTO Research_hallSchedule(id, research_hall_building_id, working_days, start_time, end_time)
VALUES
(1, 8, 'Monday-Friday', '08:00:00', '16:00:00'),
(2, 9, 'Monday-Friday', '08:00:00', '16:00:00'),
(3, 10, 'Monday-Friday', '08:00:00', '16:00:00');


INSERT INTO Majors(major_name) VALUES
('Computer Science'), ('Electrical and Computer Engineering'), ('Mathematics'), ('Modeling and Data Analytics'), ('Robotics and Intelligent Systems'),
('Biochemistry and Cell Biology'), ('Chemistry and Biotechnology'), ('Earth Sciences and Sustainable Management of Environmental Resources'), ('Medicial Chemistry and Chemical Biology'), ('Physics and Data Science'),
('Global Economics and Management'), ('Integrated Social and Cognitive Psychology'), ('International Business Administration'), ('International Relations: Politics and History'), ('Industrial Engineering and Management'), ('Management Decisions and Data Analitycs');

INSERT INTO ResearchHallMajors(research_hall_building_id, major_id) VALUES
(8, 1), (8, 2), (8, 3), (8, 4), (8, 5),
(9, 6), (9, 7), (9, 8), (9, 9), (9, 10),
(10, 11), (10, 12), (10, 13), (10, 14), (10, 15), (10, 16);


INSERT INTO RLH(building_id)
VALUES
(11);

INSERT INTO RLHServices(id, rlh_building_id, service_name_, service_office_number, other_room, other_room_number)
VALUES
(1, 11, 'IT Helpdesk', 101, 'Conference Room', 201),
(2, 11, 'Academic Advising', 102, 'Meeting Room', 202),
(3, 11, 'Career Services', 103, 'Lounge Area', 203),
(4, 11, 'Counseling Services', 104, 'Quiet Room', 204),
(5, 11, 'Financial Aid Office', 105, 'Office Supplies Room', 205),
(6, 11, 'Registrar Office', 106, 'Student Records Room', 206),
(7, 11, 'International Student Office', 107, 'Cultural Exchange Room', 207),
(8, 11, 'TK Health Insurance', 108, 'Health Resource Room', 208),
(9, 11, 'Housing Office', 109, 'Housing Resource Room', 209),
(10, 11, 'Security Office', 110, 'Security Monitoring Room', 210),
(11, 11, 'Leading board', 111, 'Event Planning Room', 211),
(12, 11, 'Student Activities Office', 112, 'Activity Resource Room', 212);

INSERT INTO RLHServicesSchedule(id, rlh_building_id, service_schedule_days, start_time, end_time)
VALUES
(1, 11, 'Monday-Friday', '09:00:00', '17:00:00'),
(2, 11, 'Monday-Friday', '08:00:00', '16:00:00'),
(3, 11, 'Monday-Friday', '09:00:00', '17:00:00'),
(4, 11, 'Monday-Thursday', '09:00:00', '15:00:00'),
(5, 11, 'Monday-Friday', '09:30:00', '17:30:00'),
(6, 11, 'Tuesday-Saturday', '08:30:00', '16:30:00'),
(7, 11, 'Monday-Friday', '10:00:00', '18:00:00'),
(8, 11, 'Monday-Thursday', '08:00:00', '15:30:00'),
(9, 11, 'Tuesday-Saturday', '09:00:00', '17:00:00'),
(10, 11, 'Monday-Friday', '07:00:00', '15:00:00'),
(11, 11, 'Monday-Friday', '11:00:00', '19:00:00'),
(12, 11, 'Monday-Friday', '08:30:00', '16:30:00');


