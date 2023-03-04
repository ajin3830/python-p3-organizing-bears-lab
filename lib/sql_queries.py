# DIFF WAYS TO WRITE, THEY ALL WORK

# select_all_female_bears_return_name_and_age = """
#     SELECT
#         bears.name,
#         bears.age
#     FROM bears
#     WHERE sex='F';
# """
select_all_female_bears_return_name_and_age = """
    SELECT name, age
    FROM bears
    WHERE sex = 'F'
"""

select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT name FROM bears ORDER BY name ASC; 
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT name,age
    FROM bears 
    WHERE alive = 1 
    ORDER BY age ASC;
"""
# LIMIT 1 is to grab top row from table, 
# name w a value takes precedence over NULL,
# also when both have same age value bc primary keys dont change, 
# it'll grab the name with smaller primary key number 
# select_oldest_bear_and_returns_name_and_age = """
#     SELECT name,age
#     FROM bears
#     WHERE
#         age = (SELECT max(age) FROM bears)
#     LIMIT 1;
# """
# select_oldest_bear_and_returns_name_and_age = """
#     SELECT name,age
#     FROM bears
#     ORDER BY age DESC
#     LIMIT 1;
# """
select_oldest_bear_and_returns_name_and_age = """
    SELECT name, max(age)
    FROM bears
"""


# select_youngest_bear_and_returns_name_and_age = """
#     SELECT name,age
#     FROM bears
#     WHERE
#         age = (SELECT min(age) FROM bears);
# """
# select_youngest_bear_and_returns_name_and_age = """
#     SELECT name,age
#     FROM bears
#     ORDER BY age ASC
#     LIMIT 1
# """
select_youngest_bear_and_returns_name_and_age = """
    SELECT name, min(age) 
    FROM bears
"""