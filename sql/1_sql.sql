select * from superstore;

select * from superstore limit 10;   -- show only top 10 records

select count('Order ID') from superstore;


select count('Order ID') as total_num_of_records from superstore;

select count(*) as total_records from superstore;

/* count with distinct */


select * from superstore;

select city from superstore;

select distinct(city) from superstore;

select count( distinct(city)) as unique_city from superstore;    


select * from superstore as su; -- here we are giving table name alias as su


-- Debuging SQL>>
select * from super	  ;


-- for this we got error>> 00:17:53	select * from super LIMIT 0, 1000	Error Code: 1146. Table 'ds_sql.super' doesn't exist	0.000 sec



-- SQL FORMATTING

select * from superstore;

select 'Order Date', 'Customer Name', City
from superstore 
limit 5;



