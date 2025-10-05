# 🛠️ First Semester Projects

## 📚 Project 1 – Student Management System (Python)

A beginner-level Python project to practice core programming concepts.

### 🎯 Objectives

- Use Python lists and dictionaries
- Write and use functions
- Accept user input
- Perform basic calculations (e.g., averages)
- Organize readable and maintainable code

### 🧩 Tasks

1. In `student_data.py`, complete:
   - `add_student()`: Collects student name, age, and grade.
   - `view_students()`: Displays all added students.
   - `get_average_grade()`: Calculates the average of all grades.
2. In `main.py`, call the functions using a simple menu system.

### ▶️ Run the App

```bash
cd month1_student_management
python main.py
```

# 🛒 Month 2 – MiniMart Sales System (SQL + Python)

A practical project to combine **SQL** and **Python** for building and analyzing a retail data workflow.

## 🎯 Objectives

- Create and manage SQL tables
- Insert and query relational data
- Perform SQL aggregations and joins
- Use Python for reporting and basic analytics

## 🧩 SQL Tasks

### 1. Create 3 Tables: `customers`, `products`, `orders`

Define each table with the following columns:

- **`customers`**

  - `customer_id` (Primary Key)
  - `name`
  - `email`
  - `join_date`
- **`products`**

  - `product_id` (Primary Key)
  - `product_name`
  - `category`
  - `price`
- **`orders`**

  - `order_id` (Primary Key)
  - `customer_id` (Foreign Key → customers)
  - `product_id` (Foreign Key → products)
  - `quantity`
  - `order_date`

### 2. Insert Sample Data

Insert at least **5 rows** into each table with realistic sample values.

### 3. Practice the Following SQL Queries

* **Basic Queries**

  * Use `SELECT` to retrieve all customers or all products.
  * Use `WHERE` to filter products by category (e.g., `"Drinks"`).
  * Use `ORDER BY` to list recent orders by date.
* **Aggregation**

  * Use `COUNT()` to find the number of total orders.
  * Use `SUM()` to calculate revenue per product (price × quantity).
  * Use `AVG()` to find the average product price.
* **Joins**

  * Use `INNER JOIN` to get detailed order information (with customer and product details).
  * Use `LEFT JOIN` to list all customers and include their orders (if any).
  * Use `LEFT JOIN` to show products even if they haven’t been ordered.

#### 🧩 Python Tasks

- Simulate new orders using `lists` or `dictionaries`
- Use conditionals to flag **large orders** (e.g., total > $100)
- Convert product prices to another currency and apply conditional discounts
- Generate a dictionary report including:
  - ✅ Total products sold
  - ✅ Most popular product
  - ✅ Revenue per customer

> 💡 Bonus: Save the report to a `.json` file or print a nicely formatted summary.

## ▶️ Run the Python Analysis

```bash
cd month2_minimart_analysis/python
python main.py
```

## 🚀 Submission Instructions

1. **Fork** this repository to your GitHub.
2. **Clone** it locally:

   ```bash
   git clone https://github.com/SamDewriter/first-semester-projects.git
   cd first-semester-projects
   ```
3. Complete all tasks inside `month1_student_management/` and `month2_minimart_analysis/`.
4. **Commit and Push**:

   ```bash
   git add .
   git commit -m "Completed Month 1 & 2 projects"
   git push origin main
   ```
5. **Submit your GitHub repo link**.

---

## ✅ Tools Used

- Python 3.x
- PostgreSQL (recommended for Month 2)
- Any text editor or IDE (VSCode, PyCharm, etc.)

Happy coding! 🎉
