-- Outer join

-- inner join: returns records only that matches join condition
-- left outer join: All the records from the left table are return wheather join condition is true or not 
-- right outer join: All the records from right table are return

-- Inner join
select c.customer_id, concat(c.first_name, " ", left(c.last_name, 1)) as customer_name, o.order_id
from customers c
join orders o
	on c.customer_id = o.customer_id;


-- Left outer join
select c.customer_id, concat(c.first_name, " ", left(c.last_name, 1)) as customer_name, o.order_id
from customers c
left join orders o
	on c.customer_id = o.customer_id;
    
    
-- right outer join
select c.customer_id, concat(c.first_name, " ", left(c.last_name, 1)) as customer_name, o.order_id
from customers c
right join orders o
	on c.customer_id = o.customer_id;    

-- Execise
-- product, order_items.     product_id, name, quantity

select p.product_id, p.name, o.quantity
from products as p
left join order_items as o
	on p.product_id = o.product_id;
    
    
    
    
-- outer joins between multiple tables
select c.customer_id, concat(c.first_name, " ", left(c.last_name, 1)) as customer_name, o.order_id
from customers c
left join orders o
	on c.customer_id = o.customer_id
join shippers as sh
	on o.shipper_id = sh.shipper_id;
    
select c.customer_id, concat(c.first_name, " ", left(c.last_name, 1)) as customer_name, o.order_id, sh.name as shipper
from customers c
left join orders o
	on c.customer_id = o.customer_id
left join shippers as sh
	on o.shipper_id = sh.shipper_id;
    
    
-- Exercise:
-- order_date, order_id, first_name, shipper, status
select o.order_date, o.order_id, c.first_name, sh.name, os.name
from orders as o
left join customers as c
	on o.customer_id = c.customer_id
left join shippers as sh
	on sh.shipper_id = o.shipper_id
left join order_statuses as os
	on o.status = os.order_status_id;
    




-- self outer joins
select e.employee_id, e.first_name, m.first_name as manager
from sql_hr.employees as e
left join sql_hr.employees as m
	on e.reports_to = m.employee_id; 



-- Using clause
-- can only be used if both tables as same column names
select c.customer_id, concat(c.first_name, " ", left(c.last_name, 1)) as customer_name, o.order_id
from customers c
join orders o
	on c.customer_id = o.customer_id;

select c.customer_id, concat(c.first_name, " ", left(c.last_name, 1)) as customer_name, o.order_id
from customers c
join orders o
	-- on c.customer_id = o.customer_id;
    using(customer_id);

-- can also be usrd if both tables have same composite keys names
select *
from order_items as oi
join order_item_notes as oin
	on oi.order_id = oin.order_id
    and oi.product_id = oin.product_id;

select *
from order_items as oi
join order_item_notes as oin
	using(order_id, product_id);

-- Exercise
-- use sql_invoicing db
-- date, client, amount, name
select p.date, c.name as client, p.amount, pm.name 
from sql_invoicing.payments as p
join sql_invoicing.clients as c
	using(client_id)
join sql_invoicing.payment_methods as pm
	on pm.payment_method_id = p.payment_method;

