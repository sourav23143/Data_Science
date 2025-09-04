use ds_sql;


-- Aggerate fn:

select * from superstore;

select avg(Sales) from superstore;

select avg(Sales) as avg_sales from superstore;

select sum(Sales) as sum_sales from superstore;


select min(Profit) as min_profit from superstore;


select max(Profit) as max_profit from superstore;

-- where with aggregate function

select avg(Sales) as avg_sales_south from superstore
where Region = "South";

select * from superstore;

select count(profit) as Pro
from superstore
where Profit >200;


-- round function

select avg(Sales) as avg_sales_south from superstore
where Region = "South";

select round(avg(Sales), 2) as avg_sales_south from superstore
where Region = "South";

select round(avg(Sales), 3) as avg_sales_south from superstore
where Region = "South";

select round(avg(Sales)) as avg_sales_south from superstore
where Region = "South";


-- Aliasing with arithmetic

-- sorting and grouping 

-- ORDER BY clause>>

select * from superstore;

select Sales from superstore order by Sales;  -- by default it will sort in accending order

-- for in decending order>>
select Sales from superstore order by Sales desc;

select Sales, 'Customer Name' from superstore order by 'Customer Name'; 


-- Groupingh

-- Group by single field>>

select Region, sum(Sales) as total_sales
from superstore
group by Region;


select Region, sum(Sales) as total_sales
from superstore
group by Region
order by total_sales;


select Region, round(sum(Sales)) as total_sales
from superstore
group by Region
order by total_sales;


-- GROUP BY multipal feilds>>

select Region , State, count(Sales)
from superstore
group by Region, State;

-- GRoup by with order by>>
select Region, round(sum(Sales)) as total_sales
from superstore
group by Region
order by total_sales desc;

