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

A row is a single line in a table. Also may be refeered to as a record.

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