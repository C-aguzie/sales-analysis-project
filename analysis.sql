--SALES DATA ANALYSIS (SQL)

--1. Total Sales
SELECT sum(sales) as total_sales from sales;

--2. Sales by Region
SELECT region, sum(sales) as total_sales from sales group by region
ORDER BY total_sales DESC;

--3. Sales by Year
select strftime('%Y', order_date) as year, sum(sales) as total_sales from sales
group by year
order by year;

--4. Sales by Category
select category, sum(sales) as total_sales from sales
group by category
order by total_sales DESC;

--5. Top 10 Customers by Sales
select customer_name, sum(sales) as total_sales from sales
group by customer_name
order by total_sales DESC
LIMIT 10;

--6. Sales by Segment
SELECT segment, sum(sales) as total_sales from sales
group by segment;
