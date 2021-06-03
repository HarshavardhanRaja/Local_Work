
-- (INNER) JOIN: Returns records that have matching values in both tables
-- LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table
-- RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table
-- FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table




-- Add the extra branch
INSERT INTO branch VALUES(4, "Buffalo", NULL, NULL);

-- inner join
select e.emp_id, e.first_name, e.last_name, b.branch_id, b.branch_name, b.mgr_id
from employee e
join branch b
on e.emp_id = b.mgr_id;

-- left outer join
select e.emp_id, e.first_name, e.last_name, b.branch_id, b.branch_name, b.mgr_id
from employee e
left join branch b
on e.emp_id = b.mgr_id;

-- right outer join
select e.emp_id, e.first_name, e.last_name, b.branch_id, b.branch_name, b.mgr_id
from employee e
right join branch b
on e.emp_id = b.mgr_id;

-- full puter join
-- mysql doesnot have full outer join / full join command but we can emulate it indirectly from below code i.e by using union for left & right joins
select e.emp_id, e.first_name, e.last_name, b.branch_id, b.branch_name, b.mgr_id
from employee e
left join branch b
on e.emp_id = b.mgr_id
Union
select e.emp_id, e.first_name, e.last_name, b.branch_id, b.branch_name, b.mgr_id
from employee e
right join branch b
on e.emp_id = b.mgr_id;
