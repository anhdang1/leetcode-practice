# Write your MySQL query statement below
SELECT distinct a.id
FROM weather a, weather b
WHERE DATEDIFF(a.recordDate,b.recordDate) = 1
and a.temperature > b.temperature;