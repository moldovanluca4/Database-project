SELECT 
    books, 
    book_availability, 
    book_type
FROM IRC
WHERE book_availability = 1 
  AND book_type = 'CS';


SELECT 
    g.working_days,
    g.start_time AS gym_start,
    g.equipment AS gym_equipment,
    s.club AS club_name,
    s.start_time AS club_start
FROM Gym g
JOIN SCC s 
    ON g.working_days = s.club_schedule_days
WHERE g.start_time < s.start_time
ORDER BY g.working_days, g.start_time;


SELECT 
    B.id AS building_id,
    COUNT(R.services_office_number) AS total_offices
FROM RLH R
JOIN Building B 
    ON R.building_id = B.id
WHERE R.services_office_number IS NOT NULL
GROUP BY B.id;


SELECT 
    v.name AS venue_name,
    lh.name_ AS hall_name,
    lh.address_,
    lh.capacity
FROM LECTURE_HALL lh
JOIN Venue v ON lh.venue_id = v.id
WHERE lh.capacity > 100;


SELECT 
    m.registration_required,
    COUNT(m.venue_id) AS total_rooms,
    SUM(CASE WHEN m.hybrid_capable = TRUE THEN 1 ELSE 0 END) AS hybrid_rooms
FROM MeetingRoom m
GROUP BY m.registration_required;

SELECT 'Lecture Hall' AS venue_type, COUNT(lh.venue_id) AS total
FROM LECTURE_HALL lh
UNION ALL
SELECT 'Lab', COUNT(l.venue_id)
FROM Lab l
UNION ALL
SELECT 'Coffee Bar', COUNT(cb.venue_id)
FROM COFFEE_BAR cb
UNION ALL
SELECT 'Theater', COUNT(t.venue_id)
FROM Theater t
UNION ALL
SELECT 'Meeting Room', COUNT(m.venue_id)
FROM MeetingRoom m
UNION ALL
SELECT 'Cinema', COUNT(c.venue_id)
FROM Cinema c;


SELECT 
    e.Exam_Name,
    t.Tournament_name AS Tournament_Match,
    f.Country AS Country_Food_Show,
    ev.Date_ AS Same_Date
FROM Exam e
JOIN Event ev ON e.Event_ID = ev.Event_ID
LEFT JOIN Tournament t ON t.Event_ID = ev.Event_ID
LEFT JOIN FoodShow f ON f.Event_ID = ev.Event_ID;


SELECT 
    Exam_Name,
    COUNT(*) AS Number_of_Exams
FROM Exam
GROUP BY Exam_Name;


SELECT SUM(total_events) AS Total_All_Events
FROM (
    SELECT COUNT(*) AS total_events FROM Exam
    UNION ALL
    SELECT COUNT(*) FROM TOS
    UNION ALL
    SELECT COUNT(*) FROM Tournament
    UNION ALL
    SELECT COUNT(*) FROM CareerDay
    UNION ALL
    SELECT COUNT(*) FROM Cermony
    UNION ALL
    SELECT COUNT(*) FROM FoodShow
) AS total_counts;


SELECT Ticket_price, COUNT(*) AS Number_of_Events
FROM TOS
GROUP BY Ticket_price
HAVING Ticket_price >= 10;





