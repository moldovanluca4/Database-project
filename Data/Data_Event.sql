INSERT INTO Event(Event_ID, Venue_ID, Date_) VALUES
(1,1,'2025-11-09 09:00:00'),
(2,2,'2025-11-09 14:00:00'),
(3,3,'2025-11-10 10:00:00'),
(4,4,'2025-11-11 12:00:00'),
(5,5,'2025-11-12 18:00:00'),
(6,6,'2025-11-13 15:00:00'),
(7,1,'2025-11-13 15:00:00'),
(8,2,'2025-11-14 00:00:00');

INSERT INTO Exam(Exam_ID, Event_ID, Exam_Name) VALUES
(1, 1, 'Operating System'),
(2, 2, 'Chemistry'),
(3, 3, 'Biology'),
(4, 4, 'Math'),
(5, 5, 'Database'),
(6, 6, 'Probability'),
(7, 2, 'Logic'); 


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

INSERT INTO Cermony(Cermony_ID, Event_ID, Name_) VALUES
(1, 7, 'Welcome Ceremony'),
(2, 5, 'Award Ceremony');

INSERT INTO FoodShow(Food_ID, Event_ID, Country) VALUES
(1, 6, 'Italy'),
(2, 1, 'France'),
(3, 5, 'China');
