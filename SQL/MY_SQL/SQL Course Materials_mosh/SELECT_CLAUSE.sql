-- SELECT Clause

select * from customers;

select first_name, last_name from customers;

select last_name, first_name from customers;

select last_name, first_name, points from customers;

-- USING Arithemetic expressions (+, -, *, /, %[remainder of division])

select last_name, first_name, points +10 from customers;
select last_name, first_name, points, points +10 from customers;

-- order of operators *,/ has higher order than +,- hence we use brackets in those situations
select last_name, first_name, points, points + 10 * 100  from customers;
select last_name, first_name, points, (points + 10) * 100 as discount_factor  from customers;

-- DISTINCT we can query only distinct results


-- Excercise
-- Return all the products (name, unit price, new price[unit price * 1.1])

select name, unit_price as 'unit price', unit_price * 1.1 as 'new price ' from products; 






