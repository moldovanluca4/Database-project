-- Insert Venues 
INSERT INTO Venue(name, opening_hours) VALUES
('Main Lecture Hall', '08:00-18:00'),        
('Chemestry Lab', '09:00-17:00'),          
('Campus Coffee Bar', '07:00-20:00'),     
('Campus Theater', '10:00-22:00'),          
('Conference Room A', '08:00-18:00'),        
('C3 Cinema', '10:00-23:00'),                 
('College 1 Lecture Hall', '08:00-18:00'),    
('College 3 Lecture Hall', '08:00-18:00'),   
('Conrad Neiber Lecture Hall', '08:00-18:00');

INSERT INTO LECTURE_HALL(venue_id, name_, address_, capacity) VALUES
(1, 'IRC Lecture Hall A', 'Campus Ring 1', 400),
(2, 'IRC Lecture Hall B', 'Campus Ring 1', 350),
(3, 'East Hall Lecture Hall', 'East Hall, Campus Ring 2', 300),
(4, 'West Hall Lecture Hall', 'West Hall, Campus Ring 3', 300),
(5, 'College 1 Lecture Hall', 'College 1, Campus Ring 4', 250),
(6, 'College 2 Lecture Hall', 'College 2, Campus Ring 5', 250),
(7, 'College 3 Lecture Hall', 'College 3, Campus Ring 6', 250),
(10, 'Conrad Neiber Lecture Hall', 'Campus Ring 1', 450);

INSERT INTO Lab (venue_id, equipment, access_, major) VALUES
(1, 'Biochemistry Lab, PCR Machines, Centrifuges', 'Biochemistry and Cell Biology Students', 'Biochemistry and Cell Biology'),
(2, 'Organic Chemistry Lab, Fume Hoods, Spectrometers', 'Chemistry and Biotechnology Students', 'Chemistry and Biotechnology'),
(3, 'Physics Lab, Particle Accelerators, Lasers', 'Physics and Data Science Students', 'Physics and Data Science'),
(4, 'Earth Sciences Lab, Rock Cutters, Soil Analyzers', 'Earth Sciences and Sustainable Management of Environmental Resources Students', 'Earth Sciences and Sustainable Management of Environmental Resources'),
(5, 'Robotics Lab, 3D Printers, Sensors', 'Robotics and Intelligent Systems Students', 'Robotics and Intelligent Systems'),
(6, 'Electrical Engineering Lab, Circuit Boards, Oscilloscopes', 'Electrical and Computer Engineering Students', 'Electrical and Computer Engineering'),
(7, 'Data Science Lab, High-Performance Computers, Data Servers', 'Data Science for Society and Business Students', 'Data Science for Society and Business');

INSERT INTO Coffee_bar (venue_id, prices, products) VALUES 
(1, '2.50, 2.00, 4.50', 'Coffee, Tea, Sandwiches'), 
(2, '3.80', 'Espresso, Latte, Sandwiches'), 
(3, '2.90, 3.50, 5.00', 'Cappuccino, Iced Coffee, Wraps'), 
(4, '2.50, 3.00, 4.20', 'Black Coffee, Croissant, Smoothie'), 
(5, '3.20, 3.50, 5.50', 'Flat White, Matcha Latte, Panini'), 
(6, '2.70, 3.20, 4.80', 'Americano, Hot Chocolate, Donuts'), 
(7, '3.00, 3.80, 5.20', 'Mocha, Espresso, Brownies');
INSERT INTO Theater (venue_id, capacity, Ticket_price, play) VALUES
(1, 500, 15, 'Drama'),
(2, 300, 12, 'Student Performances'),
(3, 450, 18, 'Guest Lectures'),
(4, 200, 10, 'Workshops'),
(5, 600, 20, 'Film Screenings'),
(6, 350, 16, 'Music Concerts'),
(7, 250, 8, 'Dance Rehearsals');

INSERT INTO MeetingRoom (venue_id, capacity, registration_required, equipment, hybrid_capable) VALUES
(1, 30, TRUE, 'Projector, Whiteboard', TRUE),
(2, 15, FALSE, 'TV Screen, HDMI Cable', TRUE),
(3, 50, TRUE, 'Smartboard, Video Conferencing', TRUE),
(4, 20, FALSE, 'Round Table, Wi-Fi', FALSE),
(5, 40, TRUE, 'Projector, Microphones', TRUE),
(6, 25, FALSE, 'Whiteboard, Speakers', FALSE);

INSERT INTO Cinema (venue_id, booking_price, snacks, snack_prices, available_time_slots) VALUES
(1, 10.00, 'Popcorn', '5.00', '14:00, 21:00'),
(2, 9.50, 'Chips', '4.00', '17:00, 22:00'),
(3, 8.00, 'Nachos', '6.00', '15:00, 22:00'),
(4, 11.00, 'Popcorn', '5.00', '20:00, 23:00'),
(5, 9.00, 'Chocolate', '5.50', '16:00, 20:30'),
(6, 10.50, 'Pretzels', '6.00', '18:00, 22:30'),
(7, 8.50, 'Candy', '4.00', '13:00, 19:00');
