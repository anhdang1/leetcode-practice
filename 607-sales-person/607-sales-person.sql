# Write your MySQL query statement below
-- names of all sales persons who did not have any orders related to the company named "RED"

-- left join from the salesperson table


SELECT s.name
FROM salesperson s
WHERE s.sales_id not in (SELECT o.sales_id
                        FROM orders o
                        JOIN company c
                        ON o.com_id = c.com_id
                        WHERE c.name = "RED");      
