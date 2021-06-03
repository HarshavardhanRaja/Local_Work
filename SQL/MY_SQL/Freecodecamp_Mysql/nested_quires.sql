
-- Find names of all employees who have sold over 50,000
select first_name, last_name from employee
where emp_id in (
	select distinct emp_id from works_with
	where total_sales > 50000
);


-- Find all clients who are handles by the branch that Michael Scott manages
-- Assume you know Michael's ID (102)

select client_name from client 
where branch_id in (
	select branch_id from branch where mgr_id = 102
);



 -- Find all clients who are handles by the branch that Michael Scott manages
 -- Assume you DONT'T know Michael's ID
select client_name from client 
where branch_id in (
	select branch_id from branch 
    where mgr_id in (
		select emp_id from employee where first_name = 'Michael' 
    ) 
);


-- Find the names of employees who work with clients handled by the scranton branch

select first_name, last_name from employee
where branch_id = (select branch_id from branch where branch_name = 'scranton');


-- Find the names of all clients who have spent more than 100,000 dollars
select client_name from client
where client_id in (
	select distinct client_id from works_with where total_sales > 100000
);

