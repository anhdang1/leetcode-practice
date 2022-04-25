# Write your MySQL query statement below
-- group by sell_date



SELECT sell_date, count(distinct product) as num_sold, group_concat(distinct product) as products
FROM activities
GROUP BY sell_date;

