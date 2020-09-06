/*

This chapter provides a brief introduction to working with relational databases. You'll learn about their structure, how to talk about them using database lingo, and how to begin an analysis using simple SQL commands to select and summarize columns from database tables.

*/


/*

Welcome to the Course!
- Video

*/


/*

Onboarding | Tables
---
If you've used DataCamp to learn R or Python, you'll be familiar with the interface. For SQL, however, there are a few new features you should be aware of.

For this course, you'll be using a database containing information on almost 5000 films. To the right, underneath the editor, you can see the data in this database by clicking through the tabs.

From looking at the tabs, who is the first person listed in the people table?
---
Instructions - 50 XP

##Possible Answers

# Kanye West
# Biggie Smalls
# 50 Cent <------- Correct
# Jay Z

*/

/*

Onboarding | Query Result
---
Notice the query result tab in the bottom right corner of your screen. This is where the results of your SQL queries will be displayed.

Run this query in the editor and check out the resulting table in the query result tab!

  SELECT name FROM people;

Who is the second person listed in the query result?
---
Instructions - 50 XP

##Possible Answers

# Kanye West
# A. Michael Baldwin <------- Correct
# 50 Cent
# Jay Z

*/

/*

Onboarding | Errors
---
If you submit the code to the right, you'll see that you get two types of errors.

SQL errors are shown below the editor. These are errors returned by the SQL engine. You should see:

  syntax error at or near "'DataCamp <3 SQL'" LINE 2: 'DataCamp <3 SQL' ^

DataCamp errors are shown in the Instructions box. These will let you know in plain English where you went wrong in your code! You should see:

  You need to add SELECT at the start of line 2!
---
Instructions - 100 XP
-Submit the code to the right, check out the errors, then fix them!

-- Try running me!
SELECT 'DataCamp <3 SQL'
AS result;

*/


/*

Onboarding | Bullet Exercises
---
Another new feature we're introducing is the bullet exercise, which allows you to easily practice a new concept through repetition. Check it out below!
---
Instructions 1/3 - 35 XP
-Submit the query in the editor! Don't worry, you'll learn how it works soon.

SELECT 'SQL'
AS result;

Instructions 2/3
-Now change 'SQL' to 'SQL is' and click Submit!

SELECT 'SQL is'
AS result;

Instructions 3/3
-Finally, change 'SQL is' to 'SQL is cool!' and click Submit!

SELECT 'SQL is cool!'
AS result;

*/


/*

Beginning your SQL journey
---
Now that you're familiar with the interface, let's get straight into it.

SQL, which stands for Structured Query Language, is a language for interacting with data stored in something called a relational database.

You can think of a relational database as a collection of tables. A table is just a set of rows and columns, like a spreadsheet, which represents exactly one type of entity. For example, a table might represent employees in a company or purchases made, but not both.

Each row, or record, of a table contains information about a single entity. For example, in a table representing employees, each row represents a single person. Each column, or field, of a table contains a single attribute for all rows in the table. For example, in a table representing employees, we might have a column containing first and last names for all employees.

The table of employees might look something like this:

id	name	age	nationality
1	Jessica	22	Ireland
2	Gabriel	48	France
3	Laura	36	USA

How many fields does the employees table above contain?

Answer the question - 50 XP
---
##Possible Answers

# 1
# 2
# 3
# 4 <------- Correct

*/


/*

SELECTing single columns
---
While SQL can be used to create and modify databases, the focus of this course will be querying databases. A query is a request for data from a database table (or combination of tables). Querying is an essential skill for a data scientist, since the data you need for your analyses will often live in databases.

In SQL, you can select data from a table using a SELECT statement. For example, the following query selects the name column from the people table:

  SELECT name
  FROM people;
  
In this query, SELECT and FROM are called keywords. In SQL, keywords are not case-sensitive, which means you can write the same query as:

  select name
  from people;
  
That said, it's good practice to make SQL keywords uppercase to distinguish them from other parts of your query, like column and table names.

It's also good practice (but not necessary for the exercises in this course) to include a semicolon at the end of your query. This tells SQL where the end of your query is!

Remember, you can see the results of executing your query in the query result tab to the right!
---
Instructions 1/3 - 35 XP
-Select the title column from the films table.

SELECT title
FROM films;

Instructions 2/3
-Select the release_year column from the films table.

SELECT release_year
FROM films;

Instructions 3/3
-Select the name of each person in the people table.

SELECT name
FROM people;

*/


/*

SELECTing multiple columns
---
Well done! Now you know how to select single columns.

In the real world, you will often want to select multiple columns. Luckily, SQL makes this really easy. To select multiple columns from a table, simply separate the column names with commas!

For example, this query selects two columns, name and birthdate, from the people table:

  SELECT name, birthdate
  FROM people;
  
Sometimes, you may want to select all columns from a table. Typing out every column name would be a pain, so there's a handy shortcut:

  SELECT *
  FROM people;

If you only want to return a certain number of results, you can use the LIMIT keyword to limit the number of rows returned:

  SELECT *
  FROM people
  LIMIT 10;

Before getting started with the instructions below, check out the column names in the films table by clicking on the films tab to the right!
---
Instructions 1/4 - 25 XP
-Get the title of every film from the films table.

SELECT title
FROM films;

Instructions 2/4
-Get the title and release year for every film.

SELECT title, release_year
FROM films;

Instructions 3/4
-Get the title, release year and country for every film.

SELECT title, release_year, country
FROM films;

Instructions 4/4
-Get all columns from the films table.

SELECT *
FROM films;

*/

SELECT DISTINCT
---
Often your results will include many duplicate values. If you want to select all the unique values from a column, you can use the DISTINCT keyword.

This might be useful if, for example, you're interested in knowing which languages are represented in the films table:

  SELECT DISTINCT language
  FROM films;
  
Remember, you can check out the data in the tables by clicking on the tabs to the right under the editor!
---
Instructions 1/3 - 35 XP
-Get all the unique countries represented in the films table.

SELECT DISTINCT country
FROM films;

Instructions 2/3
-Get all the different film certifications from the films table.

SELECT DISTINCT certification
FROM films;

Instructions 3/3
-Get the different types of film roles from the roles table.

SELECT DISTINCT role
FROM roles;

*/


/*

Learning to COUNT
---
What if you want to count the number of employees in your employees table? The COUNT statement lets you do this by returning the number of rows in one or more columns.

For example, this code gives the number of rows in the people table:

  SELECT COUNT(*)
  FROM people;
  
How many records are contained in the reviews table?
---
Instructions - 50 XP

##Possible Answers

# 9,468
# 8,397
# 4,968 <------- Correct
# 9,837
# 9,864

*/


/*

Practice with COUNT
---
As you've seen, COUNT(*) tells you how many rows are in a table. However, if you want to count the number of non-missing values in a particular column, you can call COUNT on just that column.

For example, to count the number of birth dates present in the people table:

  SELECT COUNT(birthdate)
  FROM people;
  
It's also common to combine COUNT with DISTINCT to count the number of distinct values in a column.

For example, this query counts the number of distinct birth dates contained in the people table:

  SELECT COUNT(DISTINCT birthdate)
  FROM people;
  
Let's get some practice with COUNT!
---
Instructions 1/5 -20 XP
-Count the number of rows in the people table.

SELECT COUNT(id)
FROM people;

Instructions 2/5
-Count the number of (non-missing) birth dates in the people table.

SELECT COUNT(birthdate)
FROM people;

Instructions 3/5
-Count the number of unique birth dates in the people table.

SELECT COUNT(DISTINCT birthdate)
FROM people;

Instructions 4/5
-Count the number of unique languages in the films table.

SELECT COUNT(DISTINCT language)
FROM films;

Instructions 5/5
-Count the number of unique countries in the films table.

SELECT COUNT(DISTINCT country)
FROM films;

*/
