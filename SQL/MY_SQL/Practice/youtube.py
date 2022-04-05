# crack-concepts

# 1)
"""
query a list of city names from a table
that donot start with vowels and donot end with vowels
your results cannot contain duplicates
"""
# substring(column_name/string, starting value, lenght)
"""
select distinct(city_name)
from cities
where substring(city_name, 1, 1) not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U') and
      substring(city_name, -1, 1) not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

"""



# 2)
"""
create a table from already existing table
"""

"""
select * 
into new_table
from old_table 
where 1=0;
"""



# 3)
"""
query to find highest salary in  a department 
"""

"""
select dept_id, max(salary) from employes
groupby dept_id;
"""


# 4)
"""


"""
