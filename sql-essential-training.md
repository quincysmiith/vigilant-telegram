# Introduction

## Welcome

The goal of this course is to be able to use SQL effectively within database environments.

This course covers how databases are organised and how relational databases work.

CRUD stands for:
* Create
* Read
* Update
* Delete


# 02. SQL Overview

## About the overview

This chapter will be a quick intro to SQL, it will not be exhaustive.

SQL is a language designed to interact with relational databases.

An example of a statement:

```sql
SELECT * FROM Countries WHERE Continent = 'Europe';
```

SQL statements are terminated with a semi colon ```;```

The 4 fundamental functions of a database are:
* Create
* Read
* Update
* Delete

The SELECT statement is how you retrive data from the database.

The INSERT statement is used to add a row to a table.

```sql
INSERT INTO Customer (name, city, state) 
VALUES ('Jimmy Hendrix', 'Renton', 'WA');
``` 

The UPDATE statement is used to change data that is already present in the database. 
This is often used with a WHERE clause to identify the rows that need changing.

```sql
UPDATE Customer
    SET 
        Address = '123 Music Avenue',
        ZIP = '90210'
    WHERE id = 5;
```

The DELETE statement is used to remove rows from a table in a database.

```sql
DELETE FROM Customer WHERE id = 4;
```

## Database Organisation

The aim of a database is to organise data in a way that can be accessed.

A database is made up of one or more tables.

A single table is made up of rows and columns. A single table has 2 dimensions.

A row is a single line in a table. Also may be reffered to as a record.

A column is like a field.

All tables must have a unique key. The unique key of a table may or may not be hidden.

When a column in the table is used as the unique key, this column is referred to as the primary key.

Keys are used to create relationships between tables.

A foreign key is when there is a column in the table that is the unique key in another table. 
For example the 'Customer ID' field in the Sales table is a foriegn key because the 'Customer ID'
field is the primary key in the Customer table.
 
Foreign keys make it possible to use joined queries.


## The Select Statement

The SELECT statement retrieves data from a database.

```sql
SELECT 'Hello, World';
```

The AS keyword creates an alias for the column

```sql
SELECT 'Hello, World' AS Result;
```

An asterix in the SELECT statement is a wildcard match. In this usage it is saying to return all of the columns 
(ans all of the rows) from the Country table

```sql
SELECT * FROM Country;
```

To sort the results we can add the ORDER BY keywords to the statement.

```sql
SELECT * FROM Country ORDER BY Name;
```

Instead of selecting all of the columns we can just list out the ones we want to just pull those.

```sql
SELECT Name, LifeExpectancy FROM Country ORDER BY Name;
```

We can also change the name of the columns in the results table. Making the LifeExpectancy field more readable

```sql
SELECT Name, LifeExpectancy AS "Life Expectancy" FROM Country ORDER BY Name;
```

In the above example many database systems will allow the use of single quotes instead of double quotes
for the alias identifier.


## Selecting Rows

Use SELECT with a WHERE clause to select specific rows from a table.

The example below looks for rows where the Continent column matches the literal string 'Europe'.

```sql
SELECT Name, Continent, Region FROM Country WHERE Continent = 'Europe';
```

Sorting is still possible when using the WHERE clause

```sql
SELECT Name, Continent, Region FROM Country WHERE Continent = 'Europe' ORDER BY Name;
```

ORDER BY always comes **after** the WHERE clause.

To just return the first n rows of the results the LIMIT clause can be used

```sql
SELECT Name, Continent, Region FROM Country WHERE Continent = 'Europe' ORDER BY Name LIMIT 5;
```

To get the second 5 rows we can use the OFFSET clause

```sql
SELECT Name, Continent, Region FROM Country WHERE Continent = 'Europe' ORDER BY Name LIMIT 5 OFFSET 5;
```

LIMIT and OFFSET are not present in all SQL implementations.


## Selecting Columns

All columns can be returned by using the \*. The following will select all columns from the Country table

```sql
SELECT * from Country;
```

It is possible to have only certain columns returned by listing out those columns in the SELECT statement.

```sql
SELECT Name, Continent, Region from Country;
```

It is possible to have the columns name changed in the table that is returned to you. This is achieved by using the AS clause.

```sql
SELECT Name AS Country, Continent, Region from Country;
```

Columns can appear in any desired order. Simply list the columns in the SELECT statement as you would like them to 
appear in the table

```sql
SELECT Continent, Region, Name AS Country from Country;
```


## Counting Rows

Counting rows can be done in SQL by using the COUNT function.

```sql
SELECT COUNT(*) FROM Country;
```

The above SQL returns a single row with the number of rows that the Country table has.

How many countries have a population greater than 1 million?

```sql
SELECT COUNT(*) FROM Country WHERE Population > 1000000;
```

Multiple conditions can be used in the WHERE clause by separating them with AND

```sql
SELECT COUNT(*) FROM Country WHERE Population > 100000000 AND Continent = 'Europe' ;
```

Using a Column name in the COUNT function will return the number of rows where that column has a value (not blank). This does not count rows that are NULL

```sql
SELECT COUNT(LifeExpectancy) FROM Country;
```


## Inserting data

INSERT INTO is used to put data into the database.

```sql
INSERT INTO customer (name, address, city, state, zip) VALUES ('Fred Flintstone', '123 Cobblestone Way', 'Bedrock', 'CA', '91234');
```

When inserting data it is not necessary to list all of the columns.

```sql
INSERT INTO customer (name, city, state) VALUES ('Jimi Hendrix', 'Renton', 'WA');
```

Any columns that are not updated will have a NULL placed in them, indicating that no value was entered into that particular row and column.


## Updating data

Using the UPDATE statement it is possible to change already existing data in a database table

```sql
UPDATE customer SET address = '123 Music Avenue', zip = '98056' WHERE id = 5;
```

It is also possible to set existing values to NULL

```sql
UPDATE customer SET address = NULL, zip = NULL WHERE id = 5;
```

Using the WHERE clause in an UPDATE statement allows you to specify which rows you would like to change.


## Deleting data

It is possible to delete rows using the delete statement.

Best preactice is to select the rows you want to delete and inspect them to emsure you are deleting what you mean to.

```sql
SELECT * FROM customer WHERE id = 4;
```

Once happy with the rows to delete, then perform the delete statement

```sql
DELETE FROM customer WHERE id = 4;
```

Using the WHERE clause with a delete statement identifies which rows you would like to delete.


# 03. Fundamental Concepts

## Creating a table

The CREATE statement can be used to create tables within a database.

The below SQL creates a table with 2 columns.

```sql
CREATE TABLE test (
  a INTEGER,
  b TEXT
);
```

Different databases support different datatypes.


## Deleting a table

The DROP TABLE statement is used to delete tables from a database.

```sql
DROP TABLE test;
```

If it is unclear that the table to be deleted is in the database or not then can nest the 
DROP TABLE function in an IF EXISTS clause. If the table is there it will be deleted. This
method is used to help avoid errors.

```sql
DROP TABLE IF EXISTS test;
```


## Inserting data

The INSERT INTO is used to add data to a database table.

```sql
INSERT INTO test VALUES ( 1, 'This', 'Right here!' ); 
INSERT INTO test ( b, c ) VALUES ( 'That', 'Over there!' );
```

To add an empty row use the DEFAULT VALUES clause

```sql
INSERT INTO test DEFAULT VALUES;
```

It is possible to use a select statement to add data into a table. This can insert multiple rows into the table

```sql
INSERT INTO test ( a, b, c ) SELECT id, name, description from item;
```

The example above performs the SELECT statement, then the results from that are placed in test table in columns a, b, and c.


## Deleting rows

It is a good idea to aution the WHERE clause in the delete statement before actually deleting.

```sql
SELECT * FROM test WHERE a = 1;
```

Then once happy can actually delete the data

```sql
DELETE FROM test WHERE a = 1;
```

Deleted rows can not be easily recovered.


## The NULL value

NULL is a special state for a result with no value

NULL is the lack of a value.

It is not possible to test for NULL values in the traditional way. The follwong will not return any rows.

```sql
SELECT * FROM test WHERE a = NULL;
```

To test for a NULL value we need to test using a IS NULL clause

```sql
SELECT * FROM test WHERE a IS NULL;
```

To test the inverse ie rows where there is actually a value can test using the IS NOT NULL clause

```sql
SELECT * FROM test WHERE a IS NOT NULL;
```

We can specify in the creation of a table if a column is allowed to accept null values.

```sql
CREATE TABLE test (
  a INTEGER NOT NULL,
  b TEXT NOT NULL,
  c TEXT
);
```

Any attempt to add NULL values into column a or b will result in a failure.

## Constraining Columns

Constraints are used to define certain rules and behaviours on certain columns within a table.

Constraints are set on table creation.

Not accepting NULL values into column c

```sql
CREATE TABLE test ( a TEXT, b TEXT, c TEXT NOT NULL );
```

Constraints can be used to set default values if no value is enrtered

```sql
CREATE TABLE test ( a TEXT, b TEXT, c TEXT DEFAULT 'panda' );
```

If a column needs to contain only unique values this can be set with UNIQUE. NULL values are often
exempted from UNIQUE constraints. That is to say if a column has a unique constraint there can
be multiple rows with NULL in them.

```sql
CREATE TABLE test ( a TEXT UNIQUE, b TEXT, c TEXT DEFAULT 'panda' );
```

Multiple contraints can be used on a single column

```sql
CREATE TABLE test ( a TEXT UNIQUE NOT NULL, b TEXT, c TEXT DEFAULT 'panda' );
```


## Changing a schema

The ALTER TABLE statement can be used to modify a table after it has been created.

Adding a column 'd' to an existing test table

```sql
ALTER TABLE test ADD d TEXT;
```

## ID columns

An ID column is a column that holds a unique value for each row within the table.

Typically ID columns are automatically populated.

Creation of ID column varies between each different database system.

The example below is how setting up an ID column works for SQLite.

```sql
CREATE TABLE test (
  id INTEGER PRIMARY KEY,
  a INTEGER,
  b TEXT
);
```

In SQLite setting the primary key as an integer means the database will handle populating this field 
and auto incrementing the values in this for you.

It is not necessary to insert values into an integer primary key.

Each table may have only one ID column.


## Filtering data

SELECT statements are filtered using the WHERE clause.

The WHERE clause takes a boolean expression (True or False)

```sql
SELECT Name, Continent, Population FROM Country WHERE Population < 100000 ORDER BY Population DESC;
```

Also include rows that have NULL as the population

```sql
SELECT Name, Continent, Population FROM Country WHERE Population < 100000 OR Population IS NULL ORDER BY Population DESC;
```

To filter when both or multiple conditions are true use the AND command in the WHERE clause

```sql
SELECT Name, Continent, Population 
FROM Country 
WHERE Population < 100000 AND Continent = 'Oceania' 
ORDER BY Population DESC;
```

The like operator can be used to perform string matching. 

Percent signs work as a wild card and means any 1 or more characters.

```sql
SELECT Name, Continent, Population FROM Country WHERE Name LIKE '%island%' ORDER BY Name;
```

Underscores can be used in a like, this is used to match a single character

The in operator can be used to identify if row values are in a list of string literals

```sql
SELECT Name, Continent, Population FROM Country WHERE Continent IN ( 'Europe', 'Asia' ) ORDER BY Name;
```


## Removing Duplicates

There are times when you want to know only the range of values contained in a column. SELECT DISTINCT can 
do this for you.

```sql
SELECT DISTINCT Continent FROM Country;
```

SELECT DISTINCT can also be used to get the distinct combinations of 2 columns

```sql
SELECT DISTINCT a, b FROM test;
```

The above query will return all the distinct value pairs that columns a and b have.


## Ordering output

The ORDER BY clause is used to sort results from a query

```sql
SELECT Name FROM Country ORDER BY Name;
```

The order can be specified by passing either ASC or DESC to enforce whether the column being sorted on is 
in ascending or descending order

```sql
SELECT Name FROM Country ORDER BY Name ASC;

SELECT Name FROM Country ORDER BY Name DESC;
```

Passing multiple columns to the ORDER BY clause nests the ordering according to the order in which they were passed.

The following example sorts on continent and then within each continent sorts by name.

```sql
SELECT Name, Continent FROM Country ORDER BY Continent, Name;
```

It is possible to specify whether each column passed to the ORDER BY clause is in ascending or descending order independently.

In the below example Continent is sorted in a descending order while Region and Name are both in ascending order.

```sql
SELECT Name, Continent, Region FROM Country ORDER BY Continent DESC, Region, Name;
```


## Conditional expressions

conditional expressions in sql are cumbersome.

In SQL:
* 1 is considered true
* 0 is considered false
* anything non zero considered true
* empty string considered false
* any string considered true

The below example is testing if a and b themselves are true or false.

```sql
SELECT
    CASE WHEN a THEN 'true' ELSE 'false' END as boolA,
    CASE WHEN b THEN 'true' ELSE 'false' END as boolB
    FROM booltest
;
```

The example below is comparing a and b to the integer 1

```sql
SELECT
  CASE a WHEN 1 THEN 'true' ELSE 'false' END AS boolA,
  CASE b WHEN 1 THEN 'true' ELSE 'false' END AS boolB 
  FROM booltest
;
```


# Relationships

## Understanding join

Some tables contain information relating to other tables.

JOINs can be used to combine data from multiple tables in a simple query.

ID columns are usually used in joins to match rows across tables.

The INNER JOIN is the most common form of a JOIN and is the default.

The result of an INNER JOIN will return results from both tables where the join condition is met.

LEFT OUTER JOIN includes rows from both tables where the JOIN condition is met **plus** the remaining rows 
from the left table.

RIGHT OUTER JOIN includes rows from both tables where the JOIN condition is met **plus** the remaining rows 
from the right table.

Many databases don't support right joins.

A right join can be re-written as a left join by changing the order of the tables being joined on.

A FULL OUTER JOIN combines the effects of left and right outer joins.

https://www.codeproject.com/KB/database/Visual_SQL_Joins/Visual_SQL_JOINS_V2.png


## Accessing related tables

Example query

```sql
SELECT l.description AS left, r.description AS right
  FROM left AS l
  JOIN right AS r ON l.id = r.id
  ;
```

'l.description' is the description column from the left table. 'r.description' is the description column from the right table.

the left table is aliases as 'l'. This allows us to use the shorthand 'l' to refer to that table.

Another JOIN example

```sql
SELECT s.id AS sale, s.date, i.name, i.description, s.price 
  FROM sale AS s
  JOIN item AS i ON s.item_id = i.id
  ;
```

## Relating multiple tables

In database tables it is common to have many to many relationships.

A single customer may buy multiple products, and a single product may be bought by multiple customers.

This is often handled by making use of a junction table.

In the below example the sale table is the junction table as it has in it the id for both customers and items


```sql
SELECT i.name AS Item, c.name AS Cust, s.price AS Price
  FROM sale AS s
  JOIN item AS i ON s.item_id = i.id
  JOIN customer AS c ON s.customer_id = c.id
  ORDER BY Cust, Item
```


# Strings

## About SQL strings

SQL has a number of operators to handle strings.

Strings in SQL are typically enclosed in single quotes.

To represent a single quote within a string is achieved with double single quotes.

Concatenating strings is achieved with double pipes as standard ||.

Different database systems have different concatanation functions.


## Finding the length of a string

Most database systems have a function to determine the length of strings.

Typically this is a function called LENGTH.

```sql
SELECT LENGTH('string');
```

or in an actual query

```sql
SELECT Name, LENGTH(Name) AS Len FROM City ORDER BY Len DESC;
```

# Selecting part of a string

SQL standard does not include a substring function, however all major database systems support a substring operation.

A substring function allows you to select parts of a string depending on the position of the characters.

```sql
SELECT SUBSTR('this string', 6);
SELECT released,
    SUBSTR(released, 1, 4) AS year,
    SUBSTR(released, 6, 2) AS month,
    SUBSTR(released, 9, 2) AS day
  FROM album
  ORDER BY released
```

The second argument to the substring function is the starting string.

The third argument to the substring function us the number of characters to select.


## Removing spaces

Often with strings it may be necessary to remove leading or trailing whitespace.

This can be achieved with the TRIM function.

TRIM will remove spaces from the beginning and the end, not from the middle.

TRIM and its variants example

```sql
-- remove both leading and trailing whitespace
SELECT TRIM('   string   ');

-- remove leading whitespace
SELECT LTRIM('   string   ');

-- remove trailing whitespace
SELECT RTRIM('   string   ');

-- remove trailing or leading characters that isn't whitespace
SELECT TRIM('...string...', '.');
```


## Forcing case

There are cases where it may be necessary to force strings to be either upper case or lower case.

In SQL there are the UPPER and LOWER functions to achieve this.

Examples

```sql
-- the upper function
SELECT UPPER(Name) FROM City ORDER BY Name;

-- the lower function
SELECT LOWER(Name) FROM City ORDER BY Name;
```

SQLite only forces to uppercase and lowercase for asci characters. 

Characters with an accent for example are not converted.

Different databases may implement in a different way to achive transitioning non asci characters.


# Numbers

## Numeric types

Data types are almost never the same across different database systems.

There are 2 basic categories of numeric types.

Fundamental numeric types are:
* Integer
* Real

Integer types will fall into the following types
* Integer(precision)
* Decimal(precision, scale)
* Money(precision, scale)

Decimals are normally integer values scaled up.

Real types fall in the following types:
* Real (precision)
* Float (precision)

Real types sacrifice accuracy for scale. This is to say they are capable of representing very large or very small numbers but only to a limited number of significant figures.

The following SQL query will determine A as not equal to B.

```sql
SELECT A, B, A = B FROM 
  ( SELECT 
    ( ( .1 + .2 ) * 10 ) as A,
    ( 1.0 + 2.0 ) as B
  );
```

## What type is that value

The TYPEOF function is used to find the type of an expression.

TYPEOF function usage example:

```sql
SELECT TYPEOF( 1 + 1 );
```

Not all database systems support the TYPEOF function.


## Integer division

When dividing one integer by another the result will always be another integer.

```sql
-- integer division
SELECT 1 / 2;
```

The above will give the answer 0.

To get a decimal answer one of the numbers needs to be converted into a real number

```sql
SELECT 1.0 / 2;

-- or
SELECT CAST(1 AS REAL) / 2;
```


## Rounding numbers

Many database systems support the ROUND function.

With a single argument the ROUND function will round to the nearest whole number

```sql
SELECT ROUND(2.55555);
```

The second argument to the ROUND function specifies the decimal places.

```sql
SELECT ROUND(2.55555, 3);
```


# Dates and times

## Dates and times

Dates are typically represented in databases with most significant components of the dates first ie Year.

'2018-03-28 15:32:43'

This allows for faster sorting within the database.

Within databases dates and times are normally represented in UTC. 

UTC is easily converted to local timezones for reporting and display purposes.

Common data types for dates and times within database systems include:
* DATE
* TIME
* DATETIME
* YEAR
* INTERVAL


## Date and time related functions

Date and time functions that work with SQLite

```sql
SELECT DATETIME('now');
SELECT DATE('now');
SELECT TIME('now');
SELECT DATETIME('now', '+1 day');
SELECT DATETIME('now', '+3 days');
SELECT DATETIME('now', '-1 month');
SELECT DATETIME('now', '+1 year');
SELECT DATETIME('now', '+3 hours', '+27 minutes', '-1 day', '+3 years');
```


# Aggregates

## What are aggregates

SQL has powerful features for dealing with aggregate data.

