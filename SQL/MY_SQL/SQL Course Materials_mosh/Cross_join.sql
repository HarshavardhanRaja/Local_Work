-- Natural join/cross join

-- Natural join
select o.order_id, c.first_name
from orders o
natural join customers c;


-- cross join
-- used to combine every record from first table to every record of second table
select *
from customers as c
cross join products as p;

-- implicit cross join
select *
from customers as c, products as p;




-- Exercise:
-- Do a cross join between shippers and products 

-- using the implicit syntax
select * 
from shippers, products;

-- using the explicit syntax
select *
from shippers as s
cross join products as p; 

