# Write your MySQL query statement below
SELECT a.name as Employee
FROM Employee AS a, 
Employee AS b
where a.managerId = b.id
AND
a.salary > b.salary;