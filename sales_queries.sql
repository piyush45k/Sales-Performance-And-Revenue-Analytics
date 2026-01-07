-- Total Revenue
SELECT SUM(Sales) AS Total_Revenue
FROM sales_data;

-- Revenue by Region
SELECT Region, SUM(Sales) AS Revenue
FROM sales_data
GROUP BY Region;

-- Top 5 Products
SELECT Product_Name, SUM(Sales) AS Revenue
FROM sales_data
GROUP BY Product_Name
ORDER BY Revenue DESC
LIMIT 5;

-- Monthly Revenue
SELECT DATE_FORMAT(Order_Date, '%Y-%m') AS Month,
       SUM(Sales) AS Revenue
FROM sales_data
GROUP BY Month;
