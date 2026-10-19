# What is SQL

*SQL* (structured query language) is used to interact with databases to get information from this in a more human readable format.

The thing that is written to get this data is called a *query*.

# SELECT And FROM Statement

When it comes to writing any *query*, the basic format will always use the keywords **SELECT** and **FROM**.

## SELECT

The **SELECT** keyword specifies which columns of data to use from a table. This is done by listing out one or more (comma separated) column names from the table. However, if ALL columns of data are needed from the table then just use the \* symbol in place of column names and it will select them all.

## FROM

The **FROM** keyword specifies which table(s) to use. Multiple tables can be used by comma separating them.

> [!IMPORTANT]
>
> For each query and future ones, there is an order to execution that is done for each keyword. For example, the **FROM** keyword is processed then the **SELECT** is processed.

After writing out a *query*, put a semi-colon at the end; otherwise, if more than one *query* is written then this will cause an error since each *query* is considered new if it has a **SELECT** statement.

> [!TIP]
>
> If a single query is written then no semi-colon is needed or if it is the last query in the list of queries written.

> [!WARNING]
>
> When selecting all the data from the columns of a table, this should not be done because most of the time not all the data will need to be used and this can cause a slow down in performance.

## Performaing Calculations

There is a way to select the same column of data twice, but have the data be collected 

## Examples

### Select all from table

```sql
SELECT *
FROM tableName
```

### Selecting column of data

```sql
SELECT name 
FROM tableName
```

### Selecting multiple things

```sql
SELECT item, item2 FROM tableName
```

### Multiple SELECT statements

```sql
SELECT item, item2 FROM tableName;

/*Last semi-colon is optional*/
SELECT name
FROM tableName;
```

### Multiple table selects

```sql
SELECT *
FROM this, that
```

### Performing calculations

```sql
```

# Order By keyword
