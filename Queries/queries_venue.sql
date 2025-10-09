--find lecture halls that can host large classes
SELECT v.name AS venue_name,
       lh.name_ AS hall_name,
       lh.address_,
       lh.capacity
FROM Lecture_Hall lh
JOIN Venue v ON lh.venue_id = v.id
WHERE lh.capacity > 100;

--list all meeting rooms by registration requirement and count how many support hybrid meetings
SELECT 
    m.registration_required,
    COUNT(m.venue_id) AS total_rooms,
    SUM(CASE WHEN m.hybrid_capable = TRUE THEN 1 ELSE 0 END) AS hybrid_rooms
FROM MeetingRoom m
GROUP BY m.registration_required
HAVING COUNT(m.venue_id) > 0;

--find how many venues exist for each facility type on campus
SELECT 
    'Lecture Hall' AS venue_type, COUNT(lh.venue_id) AS total
FROM Lecture_Hall lh
UNION ALL
SELECT 
    'Lab', COUNT(l.venue_id)
FROM Lab l
UNION ALL
SELECT 
    'Coffee Bar', COUNT(cb.venue_id)
FROM Coffee_Bar cb
UNION ALL
SELECT 
    'Theater', COUNT(t.venue_id)
FROM Theater t
UNION ALL
SELECT 
    'Meeting Room', COUNT(m.venue_id)
FROM MeetingRoom m
UNION ALL
SELECT 
    'Cinema', COUNT(c.venue_id)
FROM Cinema c;