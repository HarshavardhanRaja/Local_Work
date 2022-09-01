# ==============================================================================
# Intro to SQL - Chapter 4: CUD (Create, Update, Delete)
# ==============================================================================
# Create, Update, Delete (CUD)
# ==============================================================================
# Create:
#   Insert a new record into a table.
# Update:
#   Update an existing record in a table.
# Delete:
#   Delete an existing record from a table.
# ==============================================================================
# Create:
#   INSERT INTO table_name (column1, column2, column3, ...)
#   VALUES (value1, value2, value3, ...);
# ==============================================================================
# Update:
#   UPDATE table_name
#   SET column1 = value1, column2 = value2, ...
#   WHERE some_column = some_value;
# ==============================================================================
# Delete:
#   DELETE FROM table_name
#   WHERE some_column = some_value;
# ==============================================================================


"""
Insert:
    -> To add data to your database, you would use the INSERT statement.
    -> You can insert data into one table at a time only.
    Ex:-
        INSERT INTO table_name
            (column_name_1,column_name_2,column_name_n)
        VALUES
            ('value_1', 'value_2', 'value_3');

    Multiple Records:
        INSERT INTO table_name
            (column_name_1,column_name_2,column_name_n)
        VALUES
            ('value_1', 'value_2', 'value_3'),
            ('value_4', 'value_5', 'value_6'),
            ('value_7', 'value_8', 'value_9');
    
    Multiple Records from another table:
        INSERT INTO table_name
            (column_name_1,column_name_2,column_name_n)
        SELECT column_name_1,column_name_2,column_name_n
        FROM table_name_2;


UPDATE:
    -> To update data in your database, you would use the UPDATE statement.
    -> You can update data in one table at a time only.
    -> You can use the UPDATE statement to update multiple columns in a single table
    Ex:-
        UPDATE table_name
        SET column_name_1 = value_1, column_name_2 = value_2, ...
        WHERE some_column = some_value;
    
    Important: You need to be careful when you use the UPDATE statement
    without a WHERE clause as every single row will be updated.


DELETE:
    -> To delete data from your database, you would use the DELETE statement.
    Ex:-
        DELETE FROM table_name
        WHERE some_column = some_value;

    Important: Just like the UPDATE statement, if you don't specify a WHERE
    clause, all of the entries from the table will be affected, meaning that all
    of your users will be deleted. So, it is critical to always add a WHERE
    clause when executing a DELETE statement.
    Ex:-
        DELETE FROM table_name;
"""