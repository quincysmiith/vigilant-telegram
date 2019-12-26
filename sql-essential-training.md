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

