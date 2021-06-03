-- LIMIT clause
-- offset 
select * from customers; 
select * from customers limit 3; 

-- offset 
select * from customers limit 6,3; -- skip first 6 records and result following 3


-- Exercise 
-- get top 3 loyal customers
select * from customers order by points desc limit 3; 
