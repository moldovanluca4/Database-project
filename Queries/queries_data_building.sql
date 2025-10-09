--find how many CS books are available in IRC
SELECT b.books, b.book_availability, b.book_type
FROM IRC b
WHERE b.book_availability = 1 
    AND b.book_type = 'CS';

--Display all the gym session that happened before any club activity in the SCC
Include the gym equipment, club name, and their start times.
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

--count how many offices are there in RLH
SELECT 
    B.id AS building_id,
    COUNT(R.services_office_number) AS total_offices
FROM RLH R
JOIN Building B ON R.building_id = B.id
WHERE R.services_office_number IS NOT NULL
GROUP BY B.id;

