-- SQL script to insert sample data
INSERT INTO customers (name, email, join_date) VALUES
('Adam Tare', 'adamtare45@gmail.com', '2025-01-15'),
('Henry Hart', 'henry567@gmail.com', '2025-03-22'),
('David Gold', 'davidg@yahoo.com', '2025-05-10'),
('Ben Graham', 'bendboss@gmail.com', '2025-06-05'),
('Danielle River', 'danielle@hotmail.com', '2025-07-12');

INSERT INTO products (product_name, category, price) VALUES
('Coca-Cola', 'drinks', 200),
('Pepsi', 'drinks', 250),
('Munch it', 'snacks', 2000),
('Oreo Cookies', 'snacks', 1500),
('Kopiko', 'sweets', 100);

INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES
(1, 1, 2, '2024-04-01 10:00:00'),
(1, 3, 1, '2024-04-01 10:05:00'),
(2, 2, 3, '2024-04-02 11:00:00'),
(2, 4, 2, '2024-04-02 11:10:00'),
(3, 5, 5, '2024-06-10 09:30:00');
