
-- Find a list of employee and branch names
select first_name from employee
union
select branch_name from branch;

-- Find a list of all clients & branch suppliers' names
select client_name from client
union
select supplier_name from branch_supplier;

-- Find a list of all money spent or earned by the company 
select salary from employee
union
select total_sales from works_with;

-- mytest
-- select sum(profit) as net_profit  from (
-- select salary * -1  as profit from employee
-- union
-- select total_sales  from works_with);