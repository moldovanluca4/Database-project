INSERT INTO Event(Event_ID, Venue_ID, Date_) VALUES
(1, 1, '2025-11-05 09:00:00'),
(2, 1, '2025-11-07 09:30:00'),
(3, 1, '2025-11-10 10:00:00'),
(4, 1, '2025-11-12 09:00:00'),
(5, 1, '2025-11-15 10:30:00'),
(6, 4, '2025-11-09 21:00:00'),
(7, 4, '2025-11-16 22:00:00'),
(8, 4, '2025-11-23 20:30:00'),
(9, 4, '2025-12-07 21:30:00'),
(10, 4, '2025-12-14 22:00:00'),
(11, 4, '2025-12-21 20:00:00'),
(12, 6, '2025-11-18 14:00:00'),
(13, 6, '2025-11-25 15:00:00'),
(14, 6, '2025-12-02 13:30:00'),
(15, 6, '2025-12-10 16:00:00'),
(16, 6, '2025-12-18 14:30:00'),
(17, 5, '2025-11-20 11:00:00'),
(18, 5, '2025-11-27 10:00:00'),
(19, 5, '2025-12-04 11:30:00'),
(20, 5, '2025-12-11 09:30:00'),
(21, 5, '2025-12-18 10:00:00'),
(22, 9, '2025-11-08 12:00:00'),
(23, 9, '2025-11-22 14:00:00'),
(24, 9, '2025-12-06 13:00:00'),
(25, 9, '2025-12-13 15:00:00'),
(26, 9, '2025-12-20 12:30:00'),
(27, 7, '2025-11-10 18:00:00'),
(28, 7, '2025-11-17 19:00:00'),
(29, 8, '2025-11-24 18:30:00'),
(30, 8, '2025-12-05 19:30:00'),
(31, 8, '2025-12-12 18:00:00');


INSERT INTO Exam(Exam_ID, Event_ID, Exam_Name, Major, Duration) VALUES
(1, 1, 'Operating System', 'Computer Science', '02:00:00'),
(2, 2, 'Probability', 'Mathematics', '01:30:00'),
(3, 3, 'Functional programming', 'Software Engineering', '02:00:00'),
(4, 4, 'Ethical aspect of cybersecurity', 'Cybersecurity', '01:45:00'),
(5, 5, 'Database', 'Information Systems', '02:30:00');


INSERT INTO TOS(Tos_ID, Event_ID, Ticket_price, Theme) VALUES
(1, 6, 5, 'Movie Night'),
(2, 7, 10, 'Karaoke Party'),
(3, 8, 3, 'DJ Night'),
(4, 9, 20, 'Indoor Concert'),
(5, 10, 7, 'Beach Bonfire'),
(6, 11, 6, 'Stargazing Night');


INSERT INTO Tournament(Tournament_ID, Event_ID, Tournament_name, Number_of_registered_teams) VALUES
(1, 12, 'Football Tournament', 6),
(2, 13, 'Basketball Match', 7),
(3, 14, 'Tennis Championship', 20),
(4, 15, 'Table Tennis Cup', 15),
(5, 16, 'Badminton Tournament', 10);

INSERT INTO CareerDay(CareerDay_ID, Event_ID, Company, Remote_) VALUES
(1, 17, 'Google Career Session', True),
(2, 18, 'Amazon Networking Event', True),
(3, 19, 'Microsoft Internship Fair', False),
(4, 20, 'Tesla Career Talk', True),
(5, 21, 'Siemens Hiring Event', False);


INSERT INTO Ceremony(Ceremony_ID, Event_ID, Name_) VALUES
(1, 22, 'Opening Ceremony'),
(2, 23, 'Graduation Ceremony'),
(3, 24, 'Honors Day'),
(4, 25, 'Student Awards'),
(5, 26, 'Closing Ceremony');

INSERT INTO FoodShow(Food_ID, Event_ID, Country) VALUES
(1, 27, 'Italian Food Festival'),
(2, 28, 'Japanese Cuisine Night'),
(3, 29, 'Mexican Food Fiesta'),
(4, 30, 'Indian Food Show'),
(5, 31, 'French Gourmet Evening');

