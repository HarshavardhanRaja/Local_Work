

-- inner join
select *
from orders
join customers 
on orders.customer_id = customers.customer_id;

select order_id, first_name, last_name
from orders
join customers 
on orders.customer_id = customers.customer_id;


-- we have to prefix with table name for common column 
select order_id, customers.customer_id, first_name, last_name
from orders
join customers 
on orders.customer_id = customers.customer_id;

-- using aliasis for tables
select order_id, c.customer_id, first_name, last_name
from orders o 
join customers c
on o.customer_id = c.customer_id;

-- Exercise
-- join orders_items table with products table to add product name column in orders_items table.
select o.order_id, o.product_id, p.name, o.quantity, o.unit_price
from order_items o
join products p
	on o.product_id = p.product_id;





-- join table if they are in different databases (joining across databases)
-- here current order_items is in current active db hence we don't have to mention. 
select *
from  order_items o
join sql_inventory.products p
 on o.product_id = p.product_id;



-- self joins

select e.first_name, e.last_name, m.first_name as manager_first_name, m.last_name as manager_last_name
from sql_hr.employees e
join sql_hr.employees m
 on e.reports_to = m.employee_id ;




-- joining multiple tables
select * 
from orders o
join customers c
	on o.customer_id = c.customer_id
join order_statuses as os
	on o.status = os.order_status_id;


select o.order_id,  o.order_date, concat(c.first_name,' ', left(c.last_name, 1)) as customer_name, os.name as order_status
from orders o
join customers c 
	on o.customer_id = c.customer_id
join order_statuses as os
	on o.status = os.order_status_id;

-- Exercise
-- sql_invoicing db, payments tb, join with clients tb, join with payments method table

select *
from sql_invoicing.payments as p
join sql_invoicing.clients as c
	on p.client_id = c.client_id
join sql_invoicing.payment_methods as pm
	on p.payment_method = pm.payment_method_id;
    
select p.client_id, p.invoice_id, p.date, c.name, pm.name as payment_method, p.amount 
from sql_invoicing.payments as p
join sql_invoicing.clients as c
	on p.client_id = c.client_id
join sql_invoicing.payment_methods as pm
	on p.payment_method = pm.payment_method_id;







-- compund join conditions
-- how to join if a table has composite primary key (multiple columns as primary key)

select *
from order_items as oi
join order_item_notes as oin
	on oi.order_id = oin.order_id
    and oi.product_id = oin.product_id;
    


-- implicit join syntax
select *
from orders as o, customers as c
where o.customer_id = c.customer_id;

