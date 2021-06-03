
-- % = any number of  characters, _ = only one character

-- Find any client's who are an LLC
select * from client
where client_name like '%LLC';

-- Find any branch suppliers who are in the label business
select * from branch_supplier
where supplier_name like '%label%';


-- Find any employee born on the 10th day of the month
select * from employee
where birth_day like '____-10%';


-- Find any clients who are schools
select * from client
where client_name like '%school%'

