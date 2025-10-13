SELECT 
    e.Exam_Name,
    t.Tournament_name AS Tournament_Match,
    f.Country AS Country_Food_Show,
    ev.Date_ AS Same_Date
FROM Exam e
JOIN Event ev ON e.Event_ID = ev.Event_ID
LEFT JOIN Tournament t ON t.Event_ID = ev.Event_ID
LEFT JOIN FoodShow f ON f.Event_ID = ev.Event_ID;

# Exam_Name	    Tournament_Match	Country_Food_Show	Same_Date
Operating System	Vollyeball	        France	        2025-11-09 09:00:00
Chemistry			                                    2025-11-09 14:00:00
Biology	            Basketball		                    2025-11-10 10:00:00
Math	            Football		                    2025-11-11 12:00:00
Database		                        China       	2025-11-12 18:00:00
Probability		                        Italy	        2025-11-13 15:00:00
Logic			                                        2025-11-09 14:00:00



SELECT 
    Exam_Name,
    COUNT(*) AS Number_of_Exams
FROM Exam
GROUP BY Exam_Name;

# Exam_Name	Number_of_Exams
Operating System	1
Chemistry	1
Biology	1
Math	1
Database	1
Probability	1
Logic	1


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

# Total_All_Events
20


SELECT Ticket_price, COUNT(*) AS Number_of_Events
FROM TOS
GROUP BY Ticket_price
HAVING Ticket_price >= 10;

# Ticket_price	Number_of_Events
10	1
20	1


