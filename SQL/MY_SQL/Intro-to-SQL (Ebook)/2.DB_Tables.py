# ==============================================================================
# Creating a Database:
"""
    -> First access MySql
    my sql -u root -p

    -> Create a database:
    CREATE DATABASE <database_name>;
    *the <database_name> needs to be unique

    -> switch to the database:
    USE <database_name>;
"""

# Creating Tables:
"""
    CREATE TABLE <table_name> 
    (
        id INT,
        username VARCHAR(255),
        about TEXT,
        birthday DATE,
        active BOOLEAN,
    )

To list the available tables, you could run the following command:
    SHOW TABLES;

Create Table from another table:
    CREATE TABLE users2 AS
    (
    SELECT * FROM users
    );


Allowing NULL values:
(By default, each column in your table can hold NULL values. In case that
you don't wanted to allow NULL values for some of the columns in a
specific table, you need to specify this during the table creation or later
on change the table to allow that.)
    
    CREATE TABLE users
    (
    id INT,
    username VARCHAR(255) NOT NULL,
    about TEXT,
    birthday DATE,
    active BOOL
    );


Specifying a primary key:
(The primary key column, which in our case is the id column, is a unique
identifier for our users.
We want the id column to be unique, and also, whenever we add new
users, we want the ID of the user to autoincrement for each new user.
This can be achieved with a primary key and AUTO_INCREMENT. The
primary key column needs to be NOT NULL as well.)

    CREATE TABLE users
    (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    about TEXT,
    birthday DATE,
    active BOOL,
    );
"""

"""
Rename Tables:
    ALTER TABLE user2 RENAME TO user3

Droping Tables:
    DROP TABLE user2;

Updating Tables: (add or remove a new column)
    ALTER TABLE users ADD email VARCHAR(255);
    ALTER TABLE table_name DROP COLUMN column_name;

Describe Table:
    DESCRIBE users;

Truncate table: (delete all of the data from
an existing table, but not the table itself)
    TRUNCATE TABLE table_name;


Insert Data:
    INSERT INTO users (username, email, active)
    VALUES ('bobby', 'bobby@bobbyiliev.com', true);

Select Data:
    SELECT * FROM users;
    SELECT username, email FROM users;

Update Data:
    UPDATE users SET username='bobbyiliev' WHERE id=1;

NOTE: If we don't specify a WHERE clause, all of the entries inside the
users table would be updated, and all users would have the username
set to bobbyiliev. You need to be careful when you use the UPDATE
statement without a WHERE clause, as every single row will be updated.


Delete Data:
    DELETE FROM users WHERE id=1;

Comments:
    Inline comments: (--)
        SELECT * FROM users; -- Get all users

    Multiple-line comments: (/* */)
        /*
        Get all of the users
        from your database
        */
        SELECT * FROM users;
"""