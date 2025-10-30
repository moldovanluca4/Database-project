--Query 1: Finding average daily working hours for each gym personnel, we list their names along with the average working time in minutes.
SELECT 
GP.personnel_name, 
ROUND(AVG(TIME_TO_SEC(TIMEDIFF(GS.end_time, GS.start_time)) / 60)) AS Avg_Working_Minutes 
FROM GymPersonnel GP 
JOIN GymSchedule GS ON GP.id = GS.personnel_id 
GROUP BY GP.personnel_name;

--Query 2: Listing all clubs scheduled on Tuesdays along with their assigned personnel and overlapping working hours.
SELECT 
C.club_name, 
GP.personnel_name, 
C.start_time AS Club_Start, 
C.end_time AS Club_End, 
GS.start_time AS Personnel_Start, 
GS.end_time AS Personnel_End 
FROM Clubs C 
JOIN GymSchedule GS ON C.schedule_days = GS.working_days 
JOIN GymPersonnel GP ON GS.personnel_id = GP.id 
WHERE C.schedule_days = 'Tuesday' AND C.start_time < GS.end_time AND C.end_time > GS.start_time;

--Query 3: Finding research halls that accommodate 'Computer Science' majors, along with their addresses and working hours.
SELECT 
B.address_ AS Research_Hall_Address, 
B.address_ AS Research_Hall_Name, 
RHS.working_days, 
RHS.start_time, 
RHS.end_time 
FROM Building B 
JOIN Research_hall RH ON B.id = RH.building_id 
JOIN ResearchHallMajors RHM ON RH.building_id = RHM.research_hall_building_id 
JOIN Majors M ON RHM.major_id = M.id 
JOIN Research_hallSchedule RHS ON RH.building_id = RHS.research_hall_building_id 
WHERE M.major_name = 'Computer Science';
