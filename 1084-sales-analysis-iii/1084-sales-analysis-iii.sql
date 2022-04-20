# Write your MySQL query statement below
-- products sold in spring 2019 -- not sell in any other quarter


select product_id, product_name
from product
where product_id not in (select product_id
                        from sales
                        where sale_date < '2019-01-01'
                        or sale_date > '2019-03-31');