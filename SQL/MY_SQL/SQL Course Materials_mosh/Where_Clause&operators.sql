-- where clause used to filter data
-- Comparision operators
	--  > 
    -- >=
    -- <
    -- <=
    -- =
    -- != or <>
    
select * from customers where points>3000;
select * from customers where state = "VA";
select * from customers where state <> "VA";
select * from customers where birth_date > '1990-01-01';

-- Exercise
-- Get the orders placed this year
select * from orders where order_date >= '2019-01-01';




-- AND, OR, NOT operators

-- AND operator : all conditions should be true
select * from customers where birth_date > '1990-01-01' and points > 3000 ;

-- OR operator: Atleast one of the condition is true
select * from customers where birth_date > '1990-01-01' or points > 3000 ;

-- NOT operator: used to negate a condition
select * from customers where birth_date > '1990-01-01' or points > 1000;
select * from customers where NOT (birth_date > '1990-01-01' or points > 1000);
select * from customers where birth_date <= '1990-01-01' and points <= 1000;  

-- order of operators AND > OR but can be over ride using brackets
select * from customers where birth_date > '1990-01-01' or points > 3000 and state = 'VA';
select * from customers where (birth_date > '1990-01-01' or points > 3000) and state = 'VA';

-- Exercise
-- from the order_items table get the items for order #6, where total price is greater than 30
select * from order_items where order_id = 6 and unit_price*quantity > 30;




-- IN operator: 

select * from customers where state = 'VA' or state = 'GA' or state = 'FL';
select * from customers where state IN ('VA', 'GA', 'FL');
select * from customers where state NOT IN ('VA', 'GA', 'FL');

-- Exercise
-- Return products with quantity in stock equal to 49, 38, 72
select * from products where quantity_in_stock IN (49, 38, 72);




-- BETWEEN operator: to select a range of values
select * from customers where points >=1000 and points<=3000;
select * from customers where points between 1000 and 3000;
 
 -- Return customers born between 1/1/1990 and 1/1/2000
 select * from customers where birth_date between '1990-01-01' and '2000-01-01';
 
 
 
 
 -- LIKE operator: 
 -- % any number of charecters after this
 -- _ only one charecter
 
select * from customers where last_name like 'b%';
select * from customers where last_name like '%b%';
select * from customers where last_name like '%b';

select * from customers where last_name like 'b_';
select * from customers where last_name like '_b_';
select * from customers where last_name like '_b';
select * from customers where last_name like 'b_____y';

-- Exercise 
-- Get the customers whose address contains TRAIL or AVENUE, phone numbers end with 9
select * from customers where (address like '%TRAIL%' or address like '%AVENUE%');
select * from customers where phone like '%9';




-- REGEXP operator:
-- ^ indicates begining of a string
-- $ indicates end of a string
-- | to search for multiple patterns
-- [] to match any single charecter listed in the brackets
-- [-] to represent a range of charecters like a-k, l-p 
select * from customers where last_name like '%field%';
select * from customers where last_name  REGEXP 'field'; -- last_name must contain field anywher
select * from customers where last_name  REGEXP '^field'; -- last_name must start with field
select * from customers where last_name  REGEXP '^field'; -- last_name must end with field

select * from customers where last_name  REGEXP 'field|mac'; -- last_name must contain field or mac anyewhere
select * from customers where last_name  REGEXP 'field|mac|rose';
select * from customers where last_name  REGEXP '^field|mac|rose'; -- last_name must start with field/mac/rose
select * from customers where last_name  REGEXP 'field$|mac|rose';

select * from customers where last_name  REGEXP '[gim]e'; -- last_name contains ge/ie/me
select * from customers where last_name  REGEXP 'e[fmq]';
select * from customers where last_name  REGEXP '[a-h]e ';

-- Exercise
-- get the customers whose 

-- first names are ELKA or AMBUR
select * from customers where first_name REGEXP 'ELKA|AMBUR';

-- last names end with EY or ON
select * from customers where last_name REGEXP 'EY$|ON$'; 

-- last names start with MY or contains SE
select * from customers where last_name REGEXP '^MY|SE';

-- last names contain B followed by R or u 
select * from customers where last_name REGEXP 'b[r,u]';



-- NULL operator

select * from customers where phone is not null;

-- Exercise
-- get the orders that are not shipped yet
select * from orders where shipper_id is  null;

 




 


