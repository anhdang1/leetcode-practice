# Write your MySQL query statement below
-- split to two tables
-- a.stock_name = b.stock_name
-- order by operation_day
-- b.price - a.price - capital_gain_loss



SELECT a.stock_name as stock_name, (b.price - a.price) as capital_gain_loss
FROM
(SELECT stock_name, sum(price) as price
FROM stocks
WHERE operation = "Buy"
GROUP BY stock_name) a,
(SELECT stock_name, sum(price) as price
FROM stocks
WHERE operation = "Sell"
GROUP BY stock_name) b
WHERE a.stock_name = b.stock_name;

