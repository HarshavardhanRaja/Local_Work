"""
Topics covered:
    1. Whaat is Database & DBMS?
    2. Structured Query Language (SQL)
    3. MYSQL & MYSQL workbench
    4. Entity - Relationship (ER) Diagram
    5. Normalization
    6. SQL Operations and commands
"""


# What is a Database and DBMS?
"""
What is Data?
    => Data in simple words, is distinct pieces of information or collection of facts related to any entity.

What is a Database?
    => Kind of like a container where all the data is stored.
    => Basically a systematic collection of  which supports storage and manipulation of data stored.

What is Database Management Systems (DBMS)?
    => Used to manage data in database. 
    => Bascially a collection of programs which  enables it's users to access the database, manipulate the data,
        report or represent the data.
    => A technology to store and retrive data with utmost effeciency along with appropriate security measures.
    => There are 4 types of DBMS,
        1. Hierarchial DBMS:
            Has a style of parent-child relationship of storing data.
            It has a structure like tree with nodes representing records and branches representing fields
        2. Network DBMS:
            Supports many-many relations.
            This usually results in complex atabase structures.
        3. Relational DBMS:
            This type of DBMS defines database relationships in form of tables, also know as relations.
        4. Object-Oriented DBMS:
            This type supports storage of new data types.
            The data to be stored in the form of objects.

"""

# SQL
"""
Structured Query Language (SQL):
    => A standerdized programming language which is used for managing relational databases.
    => With SQL, you can modify databases, add, update or delete rows of data, retrieve subsets of information   
        from a database and, many more.
    => Relational databases like, MySQL, ORACLE, MS SQL Server, Sysbase, etc SQL
    => Queries and other SQL operations are written as statements 
        Ex:- SELECT, INSERT, UPDATE, ADD etc.
"""


# MySQL and MySQL workbench
"""
MySQL:
    => A relational database management system.
    => Open source, provides multi-user access, supports multi storage engine, works on many platforms.
Features of MySQL:
    => Ease of management.
    => Robust transactional support.
    => Comprehensive application development.
    => High performance.
    => Low total cost of ownership.
    => Open source & 24/7 support.
    => Secure data protection.
    => High Availability.
    => Scalability & Flexibility. 

MySQL Workbench:
    => server access tool that is used to communicate with MySQL server.
    => A visual database designing and modelling access tool for MySQL server relational database.
"""


# SQL Command Catogeries
"""
There are 4 SQL command categories, 
    1. Data Definition Language (DDL):
        => Consists of commands used to define database schema.
            Ex:- CREATE, DROP, ALTER, TRUNCATE, COMMENT, RENAME
    2. Data Manipulation Language (DML):
        => The SQL commands that deals with the manipulation of data present in database.
            Ex:- SELECT, INSERT, UPDATE, DELETE
    3. Data Control Language (DCL):
        => Includes commands which mainly deals with the rights, permissions and other controls of the database system.
            Ex:- GRANT, INVOKE
    4. Transaction Control Language (TCL):
        => Includes the commands which mainly deals with he transaction of database.
            Ex:- COMMIT, ROLLBACK, SAVEPOINT, SET TRANSACTION
"""


# Data Modelling (ER, Normalization)
"""
Data Modelling:
    => Designing of database
    => There are 2 ways to design,
        -> Normalization of complete database
        -> Using Entity Relationship diagrams.


Entity Relationship Diagram (ER Diagram):
    => refer ER.py in freecodecamp_Mysql folder.


Different types of Keys in relational database:
=> There are mainly 5 types of keys in relational databases,
    1. Candidate key
        => Is basically a minimal set of attributes which can uniquely identify a tupel.
        => The value of candidate key is unique and not null for every tupel.
        => can be more than one candidate key in relation/table. 
        => can be a simple key or composite key.
    2. Super key:
        => Is a set of attributes which can uniquely identify a tuple.
    3. Primary key:
        => Primary key is also a et of attributes which can be used to uniquely dentify every tuple.
        => There can be more than one candidate key in a relation out of which one can be chosen as primary key.
        => cannot have any null value in a tuple.
    4. Alternate key:
        => The candidate key other than the primary key is called a alternate key
    5. Foreign key:
        =>  If an attribute can only take the values which are present as values of some other attribute, 
            it will basically be the foreign key to the attribute which it refers.
        => The relation which is being referenced is called 'referenced relation' and 
            corresponding attribute is called 'referenced attribute' and 
            the relation which refers to referenced relation is called 'referencing relation' and
            corresponding attribute is called 'referencing attribute'.
        => Referenced attribute of referencing attribute should be primary key.




Normalization:
    => A Technique that organizes table in such a way that redundancy and dependency of data is reduced.
        Ex:- 1NF, 2NF, 3NF, BNF, ......
        Normal Forms:
            1. First Normal Form(1NF) :
                => Each table cell should have a single value. So, basically all the records must be unique.
            2. Second Normal Form(2NF) :
                => Database should be 1NF and should also have single column primary key.
            3. Third Normal Form(3NF):
                => Database should be in 2NF and must not have any transitive functional dependencies.
                => Transitive Functional Dependencies, Changing a non-key column might cause any of the other non-key 
                    columns  to change.
            4. Boyce Codd Normal Form(BCNF):
                => If your database is in 3NF, there would be some scenarios where anamolies would be present,
                    if you have more than candidate key. Then BCNF comes into role, where you divide your tables further 
                    so that there would be only one candidate key present.  




Normalization:
    => With the help of normalization we can organize data and remove redundant data.
    => It is a technique of organizing data in a database.
    => It is a systematic way of decomposing data to eliminate data redundancy.
    => It is a multi step process that puts data in tabular form removing the duplicated data from it's relational tables.
    => Process of reducing the redundancy of data/ eliminate repeated data.
    => Improves tha data entigrity. 

Normalization came into excistense because of problems that occured in un normalized data. Thes problems are know as Data anamolies.
Data Anamolies:
    1. Insertion Anamolie 
    2. Updation Anamolie
    3. Deletion Anamolie
To eliminate all those anamolies normalization came into existence.

 Normal Forms:
    1. First Normal Form (1NF):
        => In 1st NF we tackle the problem of atomocity. Which means values in the table should not be further divided.
            In simple words a single cell cannot hold multiple values.
        => If a table contains Composite or multi-valued attributes it violates the 1NF.
        Following functions are performed on database during 1NF.
            1. Removes repeating groups from tables.
            2. Creates a seperate table for each set of related data.
            3. Identify each set of related data with a primary key.

    2. Second Normal Form (2NF):
        => It has to be in 1NF
        => Table also should not contain partial dependency. 
            Partial dependency means, the proper subset of a candidate key determines a non prime atribute.
            Attribute that form candidate key in a table are called prime attributes. and the rest of the attributes are non-prime.

    3. Third Normal Form (3NF):
        => Used To reduce the duplication of data and ensure referential entigrity
        => table has to be in 2NF.
        => There should be no transitive dependancy for non-prime attributes.
            In Simple words, If c is dependent on b, b is dependent on a then transitively c is dependent on a. This should not happen

        => It is used to eliminate undesired data anamolies. 
        => to reduce the need for restructuring over time.
        => to make the data model more informative.

    4. Boyce Codd Normal Form/ 3.5NF (BCNF):
        => Higher version of 3NF developed by Raymond F Boyce and Edgar F Codd
        => It has to be in 3NF
        => Every functional dependency A->B, then A has to be super key of that particular table.
            A superkey is a group of single or multiple keys which identifies rows in a table  
"""



# SQL Commands
"""
SQL Attributes data types:
    => Numeric (INT, SMALLINT, FLOAT, REAL, DOUBLE, PRECISION, DECIMAL(i,j))
    => Charecter-string (CHAR(n), VARCHAR(n), CLOB)
    => Bit-string (BIT(n), BIT VARYING(n))
    => BOOLEAN (TRUE, FALSE, UNKNOWN)
    => Data&time (DATE, TIME)
    => Timestamp


Constraints: Rules that can be applied on the type of data in a table
    => NOT NULL : Ensures that a NULL value cannot be stored in a column.
    => UNIQUE: Makes sure that all the values in a column are different.
    => CHECK: Ensures that all the values in a column satisfy a specific condition.
    => DEFAULT: Consists of a set of default values for a column when no value is sepcified.
    => INDEX: Used to create and retrive data from the database very quickly.


SQL Data Defination commands:
   Command/ Option        |         Description
    => CREATE INDEX                Creates an index for a table
    => ALTER TABLE                 Modifies a table's definition (adds, modifies or delete attributes/constraints)
    => DROP TABLE                  Permanently deletes a table (and thus it's data)
    => CREATE SCHEMEA              Creates a database schema.
        AUTHORIZATION 
    => DROP VIEW                    Permanently deletes a view.
    => DROP INDEX                   Permanently delets a index.
    => CREATE VIEW                  Cretes a dynamic subset of rows/columns from one or more tables.
    => CREATE TABLE As              Creates a new table based on a query in the user's database schema.
    => CREATE TABLE                Creates a new table in user's database schema.
           NOT NULL
           UNIQUE
           DEFAULT
           CHECK
           PRIMARY KEY                  Defines a primary key for a table
           FOREIGN KEY                  Defines a foreign key for a table
           


SQL Data Manipulation Commands:
   Command/ Option        |         Description
    => UPDATE                       Modifies an attribute's value in one or more table's row.
    => COMMIT                       Permanently saves data changes.
    => INSERT                       Insert row(s) into a table.
    => SELECT                       Selects attributes from rows in one or more tables/views.
        WHERE                           Restrics the selection of rows based on conditional expression.
        GROUP BY                        Groups the selected rows based on one or more attributes.
        HAVING                          Restricts the selection of grouped rows based on a condition.
        ORDER BY                        Orders the selected rows based on one or more attributes.
    => DELETE                       Deletes one or more rows from  a table.
    => ROLLBACK                     Restores data to their original values.

Logical Operators:
    => AND/OR/NOT                   Used in conditional expressions.

Comparision Operators:
    => =, <, >, <=, >=, <>, !=      Used in conditional expressions.

Aggregate functions: 
    => COUNT                        Returns the number of rows without null values for a given column.
    => MINT                         Returns the minimum attribute values found in a given column.
    => MAX                          Returns the maximum attribute value found in a given column.
    => SUM                          Returns sum of all values from  a given column.
    => AVG                          Returns average of all the values from a given column.

Special Operators:
    => BETWEEN                      Checks whether an attribute value is within a range.
    => IS NULL                      Checks whether an attribute value is null.
    => LIKE                         Checks whether an attribute value matches with a given string.
    => IN                           Checks whether an attribute value matches any value within a value list.
    => EXISTS                       Checks whether a subquery returns any rows.
    => DISTINCT                     Limits values to unique values.                     

"""