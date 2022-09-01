# ==============================================================================
# working with select statements
"""
Pattern Matching:
    _ matches any single character and 
    % matches an arbitrary number ofcharacters.
    ex:- SELECT * FROM users WHERE username LIKE '%y';
    ex:- SELECT * FROM users WHERE username LIKE '_e';


Formatting:
    \G would format the output ina list rather than a table
    ex:- SELECT * FROM users \G


specific columns only:
    ex:- SELECT username, birthday FROM users;


with no FROM Clause:
    a column can be a literal with no FROM clause
    ex:- SELECT 'Sunil' as username;


with Arithmetic Operations:
    can contain arithmetic expressions involving the operation +, –, *, and /.
    ex:- SELECT username, birthday + 1 FROM users;
         SELECT username, active*5 as new_active FROM users;


LIMIT:
    LIMIT is used to specify the number of rows to return.
    ex:- SELECT * FROM users LIMIT 2;


COUNT:
    COUNT is used to count the number of rows in a table.
    ex:- SELECT COUNT(*) FROM users;


Min, Max, Avg and Sum:
    Min, Max, Avg and Sum are used to find the minimum, maximum, average, and sum of a column.
    ex:- SELECT MIN(id) FROM users;
            SELECT MAX(id) FROM users;
            SELECT AVG(id) FROM users;
            SELECT SUM(id) FROM users;


DISTINCT:
    DISTINCT is used to remove duplicate rows from a table.
    ex:- SELECT DISTINCT username FROM users;
"""

# Where Clause: (used to filter data) (filtering data based on some conditions)
"""
The WHERE clause allows you to specify different conditions so that you
could filter out the data and get a specific result set.
    ex:- SELECT * FROM users WHERE username='bobby';


Operators: 
    =, !=, <, >, <=, >=, LIKE, NOT LIKE, IN, NOT IN, BETWEEN, NOT BETWEEN, IS, IS NOT, EXISTS, NOT EXISTS
    (https://dev.mysql.com/doc/refman/8.0/en/non-typed-operators.html)
    ex:- SELECT * FROM users WHERE username='bobby' AND active=true;


AND keyword:
    AND is used to combine two or more conditions. 
    all conditions should satisfy the AND keyword.
    ex:- SELECT * FROM users WHERE username='bobby' AND active=true;


OR keyword:
    OR is used to combine two or more conditions. 
    any one of the conditions can satisfy the OR keyword.
    ex:- SELECT * FROM users WHERE username='bobby' OR active=true;


LIKE operator (NOT LIKE):
    LIKE is used to match a string with a pattern.
    ex:- SELECT * FROM users WHERE username LIKE '%bobby%';
         SELECT * FROM users WHERE username NOT LIKE '%bobby%';


IN operator (NOT IN):
    IN is used to match a value with a list of values.
    ex:- SELECT * FROM users WHERE username IN ('bobby', 'bobbyiliev');
         SELECT * FROM users WHERE username NOT IN ('bobby', 'bobbyiliev');


IS operator (NOT NULL):
    IS is used to match a value with a value. mostly used to check if a value is NULL.
    ex:- SELECT * FROM users WHERE username IS NULL;
         SELECT * FROM users WHERE about IS NOT NULL;


BETWEEN operator ():
    BETWEEN is used to match a value with a range of values.
    ex:- SELECT * FROM users WHERE id BETWEEN 1 AND 5;
"""

# Order the result set (Group by, order by and having)
# The above clauses should be added after the FROM clause and after the WHERE clause.

"""
ORDER BY: (default sorting is ascending)
    ORDER BY is used to order the result set.
    ex:- SELECT * FROM users ORDER BY username; or ORDER BY username ASC;
         SELECT * FROM users ORDER BY username DESC;


GROUP BY:
    GROUP BY is used to group the result set.
    The GROUP BY statement allows you to use a function like COUNT, MIN, MAX etc., with multiple columns.
    ex:- SELECT username, COUNT(*) FROM users GROUP BY username;

HAVING Clause:
    HAVING is used to filter the result set based on the value of the column.
    The HAVING clause allows you to filter out the results on the groups formed by the GROUP BY clause.
    ex:- SELECT username, COUNT(*) FROM users GROUP BY username HAVING COUNT(*) > 1;

    NOTE :- The WHERE clause places conditions on the selected columns,
            whereas the HAVING clause places conditions on groups created by the
            GROUP BY clause.
"""