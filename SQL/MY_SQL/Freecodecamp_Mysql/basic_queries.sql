
-- Find all employees
select * from employee;

-- Find all clients
select * from client;

-- Find all employees ordered by salary
-- ASC by default order by clause will be asscending order
select * from employee 
order by salary;
-- desc
select * from employee
order by salary desc;

-- Find all employees ordered by sex then name
select * from employee
order by sex, first_name, last_name;

-- Find the first 5 employees in the table
select * from employee limit 5;

-- Find the first and last names of all employees
select first_name, last_name from employee;

-- Find the forename and surnames names of all employees
select first_name as forename, last_name as surname from employee;

-- Find out all the different genders
select distinct sex from employee;

-- Find all male employees
select * from employee 
where sex = 'M';

-- Find all employees at branch 2
select * from employee 
where branch_id = 2;

-- Find all employee's id's and names who were born after 1969
select emp_id, first_name, last_name from employee
where birth_day >= 01/01/1970;


-- Find all female employees at branch 2
select * from employee 
where sex = 'F'  and branch_id =2;

-- Find all employees who are female & born after 1969 or who make over 80000
select * from employee
where (sex = 'F' and birth_day > 31/12/1969) or salary > 80000;

-- Find all employees born between 1970 and 1975
select * from employee 
where birth_day between 01/01/1970 and  01/01/1975;


-- Find all employees named Jim, Michael, Johnny or David
select * from employee
where first_name in ('Jim' , 'Michael' , 'Johnny' , 'David');
