
-- Find the number of employees
select count(*) from employee;

-- Find the average of all employee's salaries
select avg(salary) from employee;

-- Find the sum of all employee's salaries
select sum(salary) from employee;


-- Find out how many males and females there are
select count(sex), sex
from employee
group by sex;


-- Find the total sales of each salesman
select sum(total_sales), emp_id 
from works_with
group by emp_id;


-- Find the total amount of money spent by each client
select sum(total_sales), client_id
from works_with
group by client_id;
