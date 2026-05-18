# 🍽️ Restaurant POS System

A Command-Line Interface (CLI) based Restaurant Point of Sale (POS) System built with **Python** and **PostgreSQL**, designed to manage all core restaurant operations from a terminal interface.

---

## 👤 Author

| Field | Details |
|---|---|
| **Name** | Pratiksha Dilip Kamble |
| **Student ID** | 541015583 |
| **Tutorial** | 15 |
| **Tutor** | Abbey Lin |
| **Date** | April 24, 2026 |

---

## 📋 Overview

This project simulates real-world restaurant workflows through a fully functional CLI-based POS system. It handles order processing, billing, inventory tracking, customer management, employee management, and analytics — all backed by a PostgreSQL database.

---

## 🎯 Objectives

1. Build a fully functional CLI-based POS system
2. Implement database operations using PostgreSQL
3. Apply programming concepts (OOP, loops, conditionals, functions)
4. Simulate real-world restaurant workflows
5. Ensure efficient and structured data handling

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| PostgreSQL | Persistent data storage |
| psycopg2 | Python-PostgreSQL database connector |
| matplotlib | Analytics graphs and charts |
| pandas | Data export and CSV generation |
| CLI | User interface (terminal-based) |

---

## 📁 Project Structure

```
restaurant-pos/
│
├── main.py          # Entry point — main menu
├── db.py            # Database connection setup
├── menu.py          # Menu item management
├── customer.py      # Customer management
├── employee.py      # Employee management
├── inventory.py     # Inventory / stock management
├── order.py         # Order creation and management
├── billing.py       # Billing, receipts, and sales reports
├── reports.py       # CSV report exports
└── analytics.py     # Analytics graphs and dashboard
```

---

## ✨ Features

### 🍴 Menu Management (`menu.py`)
- Add, update, and delete menu items
- View the full categorized menu
- Search items by name or category

### 👤 Customer Management (`customer.py`)
- Add new customers with name and phone number
- View, search, update, and delete customer records
- View complete order history per customer

### 👷 Employee Management (`employee.py`)
- Add employees with name, role, and salary
- View, search, update, and delete employee records
- Filter employees by role (Manager / Chef / Waiter / Cashier)

### 📦 Inventory Management (`inventory.py`)
- View current stock levels for all menu items
- Update, add to, or reduce stock quantities
- View items below a specified low-stock threshold

### 🪑 Table & Order Management (`order.py`)
- Create new orders linked to customers and tables
- Add multiple menu items with quantity selection
- Automatic stock deduction on order creation
- View all orders and detailed order breakdowns
- Complete or cancel orders (with stock restoration and table release)

### 💳 Billing System (`billing.py`)
- Generate itemised bills with discount and 10% tax calculation
- Save receipts to `.txt` files
- View daily and monthly sales summaries

### 📊 Reports Management (`reports.py`)
- Export CSV reports for: Menu, Customers, Employees, Orders, Inventory

### 📈 Analytics Dashboard (`analytics.py`)
- Daily sales line graph
- Monthly revenue bar chart
- Inventory stock levels bar chart
- Top 5 selling items pie chart
- Top customers by order count bar chart
- Employee salary distribution bar chart
- Order status distribution pie chart
- Export full sales report as CSV

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.8+
- PostgreSQL database access
- pip

### Install Dependencies

```bash
pip install psycopg2-binary matplotlib pandas
```

### Database Configuration

Update the connection details in `db.py`:

```python
import psycopg2

conn = psycopg2.connect(
    host="your_host",
    database="your_database",
    user="your_username",
    password="your_password"
)

cursor = conn.cursor()
```

### Database Tables Required

Ensure the following tables exist in your PostgreSQL database:

```sql
-- Menu items
CREATE TABLE menu_items (
    item_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(50),
    price NUMERIC(10, 2),
    stock INT
);

-- Customers
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
);

-- Employees
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    role VARCHAR(50),
    salary NUMERIC(10, 2)
);

-- Restaurant tables
CREATE TABLE restaurant_tables (
    table_id SERIAL PRIMARY KEY,
    capacity INT,
    status VARCHAR(20) DEFAULT 'Available'
);

-- Orders
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    table_id INT REFERENCES restaurant_tables(table_id),
    status VARCHAR(20),
    total NUMERIC(10, 2),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Order items
CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(order_id),
    item_id INT REFERENCES menu_items(item_id),
    quantity INT,
    subtotal NUMERIC(10, 2)
);
```

### Run the Application

```bash
python main.py
```

---

## 🖥️ Main Menu

```
============================================================
         RESTAURANT POS SYSTEM
============================================================
1. Menu Management
2. Customer Management
3. Employee Management
4. Inventory Management
5. Table Management
6. Order Management
7. Billing Management
8. Reports Management
9. Analytics Dashboard
10. Exit
============================================================
```

---

## 🔄 System Flowchart

```
Start
  └─> Connect to Database
        └─> Display Main Menu
              └─> Enter Choice
                    ├─> Valid? ──No──> Show Error ──> Back to Menu
                    └─> Yes
                          └─> Process Option
                                └─> Exit / Back to Menu
```

---

## 📌 Notes

- All monetary values use USD ($) format
- Tax rate is fixed at **10%**
- Discounts are applied before tax during billing
- Cancelling an order automatically restores stock and frees the table
- Receipt files are saved as `receipt_order_<id>.txt`
- CSV exports are saved in the current working directory

---

## 📄 License

This project was created for academic purposes as part of a university coursework assignment.
