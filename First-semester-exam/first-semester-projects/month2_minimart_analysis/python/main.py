# Entry point for the MiniMart data reporting system
from report_generator import SalesReport

def main():
    try:
        report_generator = SalesReport()
        report = report_generator.generate_report()
        
        print("\n=== MiniMart Sales Report ===")
        print(f"Report Generated: {report['report_date']}")
        print(f"\nTotal Products Sold: {report['total_products_sold']}")
        print(f"Most Popular Product: {report['most_popular_product']}")
        print("\nRevenue by Customer:")
        for customer, revenue in report['revenue_by_customer'].items():
            print(f"  {customer}: ${revenue:,.2f}")
        
        # Save report to file
        report_generator.save_report(report)
        print("\nReport saved to sales_report.json")
        
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        print(f"Error generating report: {e}")

if __name__ == "__main__":
    main()