-- ORDER BY

select * from customers order by first_name; -- by default ascending or use asec
select * from customers order by first_name desc; -- use desc to change to decending order
select * from customers order by state desc, first_name; 

select first_name, last_name, 10 as points from customers order by points, first_name;
 
select first_name, last_name, 10 as points from customers order by 1,2 ; -- sort by column position in select clause i.e 1 = first_name, 2= last_name 

-- Exercise
select * from order_items where order_id = 2 order by quantity*unit_price desc;