# Utility functions for data conversion and filtering
import psycopg2
from psycopg2 import Error
import random
from decimal import Decimal
from datetime import datetime


class OrderSimulator:
    def __init__(self, db):
        self.db = db
        self.exchange_rates = {
            'EUR': Decimal('0.85'),
            'GBP': Decimal('0.73'),
        }

    def simulate_order(self):
        """Simulates a random order"""
        customer_id = random.randint(1, 5)  # Assuming 5 customers
        product_id = random.randint(1, 5)   # Assuming 5 products
        quantity = random.randint(1, 10)
        return (customer_id, product_id, quantity)

    def is_large_order(self, total_amount):
        """Flags orders over $100"""
        return total_amount > Decimal('100.0')

    def apply_discount(self, amount):
        """Applies tiered discounts"""
        if amount >= Decimal('100.0'):
            return amount * Decimal('0.90')  # 10% discount
        elif amount >= Decimal('50.0'):
            return amount * Decimal('0.95')  # 5% discount
        return amount

    def convert_currency(self, amount_usd, target_currency='EUR'):
        """Converts USD to target currency"""
        if target_currency not in self.exchange_rates:
            raise ValueError(f"Unsupported currency: {target_currency}")
        return amount_usd * self.exchange_rates[target_currency]        
    

class DatabaseOperations:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                database="minimart_db2",
                user="postgres",
                password="postgres",
                host="localhost",
                port="5432"
            )
            self.cur = self.conn.cursor()
            return True
        except Error as e:
            print(f"Error connecting to PostgreSQL: {e}")
            return False

    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

    def get_total_products_sold(self):
        try:
            self.cur.execute("SELECT SUM(quantity) FROM orders")
            result = self.cur.fetchone()
            return result[0] if result[0] else 0
        except Error as e:
            print(f"Query error: {e}")
            return 0

    def get_popular_product(self):
        try:
            query = """
            SELECT p.product_name, SUM(o.quantity) as total_sold
            FROM products p
            JOIN orders o ON p.product_id = o.product_id
            GROUP BY p.product_name
            ORDER BY total_sold DESC
            LIMIT 1
            """
            self.cur.execute(query)
            result = self.cur.fetchone()
            return result[0] if result else "No products sold"
        except Error as e:
            print(f"Query error: {e}")
            return "Error retrieving popular product"

    def get_revenue_by_customer(self):
        try:
            query = """
            SELECT c.name, SUM(p.price * o.quantity) as revenue
            FROM customers c
            JOIN orders o ON c.customer_id = o.customer_id
            JOIN products p ON o.product_id = p.product_id
            GROUP BY c.name
            ORDER BY revenue DESC
            """
            self.cur.execute(query)
            return {row[0]: float(row[1]) for row in self.cur.fetchall()}
        except Error as e:
            print(f"Query error: {e}")
            return {}    
        
    def add_simulated_order(self, customer_id, product_id, quantity):
        try:
            query = """
            INSERT INTO orders (customer_id, product_id, quantity, order_date)
            VALUES (%s, %s, %s, %s) RETURNING order_id
            """
            self.cur.execute(query, (customer_id, product_id, quantity, datetime.now()))
            self.conn.commit()
            return self.cur.fetchone()[0]
        except Exception as e:
            self.conn.rollback()
            print(f"Error adding order: {e}")
            return None

    def get_order_total(self, order_id):
        query = """
        SELECT SUM(p.price * o.quantity)
        FROM orders o
        JOIN products p ON o.product_id = p.product_id
        WHERE o.order_id = %s
        """
        self.cur.execute(query, (order_id,))
        result = self.cur.fetchone()[0]
        return Decimal(str(result)) if result else Decimal('0')    