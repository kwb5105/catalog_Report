# Kyle's Catalog reporting Project

This is a project to display 3 different reports using python and a postgres database.
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?


## Install

Create 2 views in the database 
- logDateCount --Create view for the total count by date.

`
create view logDateCount as 
select count(*), CAST(time as DATE)  from log Group By CAST(time as DATE)
order by count(*) desc;`

- failedCount --Create view for failure count by date.

`
create view failedCount as 
select count(*),CAST(time as DATE) 
from log 
where status != '200 OK'
Group By CAST(time as DATE)
order by count(*) desc;`
