create table student(
	student_id INT PRIMARY KEY,
    name VARCHAR(20),
    major VARCHAR(20)
);

DESCRIBE student;

ALTER TABLE student ADD gpa DECIMAL(3,2);

ALTER TABLE student DROP COLUMN gpa;

DROP TABLE student;


insert into student values(2, 'tori', 'blue');

insert into student(student_id, name) values(3, 'dustin');

select * from student;