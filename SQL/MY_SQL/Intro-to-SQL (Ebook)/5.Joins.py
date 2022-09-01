# ==============================================================================
# Joins (The JOIN clause allows you to combine the data from 2 or more tables into one result set.)
"""
CROSS Join
INNER Join
LEFT Join
RIGHT Join

CROSS JOIN:
    -> It is used to combine the results of two or more queries into one result set.
    -> The CROSS join allows you to put the result of two tables next to each
        other without specifying any WHERE conditions. This makes the CROSS
        join the simplest one, but it is also not of much use in a real-life scenario.
    Ex:-
        SELECT *
        FROM table_name_1
        CROSS JOIN table_name_2;

INNER JOIN:
    -> The INNER join is used to join two tables. However, unlike the CROSS
        join, by convention, it is based on a condition. By using an INNER join,
        you can match the first table to the second one.
    Ex:-
        SELECT *
        FROM table_name_1
        INNER JOIN table_name_2
        ON table_name_1.column_name_1 = table_name_2.column_name_1;

    Note:- With the inner join, the NULL values are discarded. For example, if you
           have a user who does not have a post associated with it, the user with
           NULL posts will not be displayed when running the above INNER join query.
    -> To get the null values as well, you would need to use an outer join.


LEFT JOIN:
"""