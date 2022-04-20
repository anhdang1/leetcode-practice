# Write your MySQL query statement below

SELECT u.name, coalesce(sub1.travelled_distance,0) as travelled_distance
FROM users u
LEFT JOIN (SELECT user_id, sum(distance) as travelled_distance 
FROM rides
GROUP BY user_id) sub1
ON u.id = sub1.user_id
ORDER BY sub1.travelled_distance desc,
u.name asc;