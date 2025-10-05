-- SQL queries for retrieving insights
SELECT * FROM customers;

SELECT * FROM products 
WHERE category = 'Drinks';

SELECT * FROM orders 
ORDER BY order_date DESC;

SELECT COUNT(*) FROM orders;

SELECT p.product_name, SUM(o.quantity * p.price) AS revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name;

SELECT o.order_id, c.name, p.product_name, o.quantity, o.order_date
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN products p ON o.product_id = p.product_id;
