# Write your MySQL query statement below
SELECT actor_id, director_id
from actordirector
group by actor_id, director_id
having count(*) >= 3; 