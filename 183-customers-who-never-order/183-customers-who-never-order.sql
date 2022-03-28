# Write your MySQL query statement below
select name as Customers
from
(select id, name
from customers
where id NOT IN (select customerId from orders)) as t;