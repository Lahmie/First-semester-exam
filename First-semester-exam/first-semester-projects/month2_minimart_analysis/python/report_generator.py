# Code to generate dictionary summary reports
import json
from datetime import datetime
from utils import DatabaseOperations


from utils import OrderSimulator

class SalesReport:
    def __init__(self):
        self.db = DatabaseOperations()
        self.simulator = OrderSimulator(self.db)

    def generate_report(self):
        if not self.db.connect():
            raise Exception("Failed to connect to database")
            
        try:
            # Simulate new order
            customer_id, product_id, quantity = self.simulator.simulate_order()
            order_id = self.db.add_simulated_order(customer_id, product_id, quantity)
            
            # Get order total and check if it's large
            order_total = self.db.get_order_total(order_id)
            is_large = self.simulator.is_large_order(order_total)
            
            # Apply discounts and currency conversion
            discounted_total = self.simulator.apply_discount(order_total)
            euro_total = self.simulator.convert_currency(discounted_total, 'EUR')

            report = {
                "report_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "total_products_sold": self.db.get_total_products_sold(),
                "most_popular_product": self.db.get_popular_product(),
                "revenue_by_customer": self.db.get_revenue_by_customer(),
                "latest_order": {
                    "order_id": order_id,
                    "total_usd": float(order_total),
                    "is_large_order": is_large,
                    "discounted_total": float(discounted_total),
                    "total_eur": float(euro_total)
                }
            }
            return report
        finally:
            self.db.close()

    def save_report(self, report, filename="../sales_report.json"):
        try:
            with open(filename, 'w') as f:
                json.dump(report, f, indent=4)
        except Exception as e:
            print(f"Error saving report: {e}")