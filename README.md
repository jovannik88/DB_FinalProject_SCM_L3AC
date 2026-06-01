# Supply Chain Management System

## ERD

![ERD Diagram](<SCM FInallll.drawio.png>)


## Steps to run the app :

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/scm-sejahtera.git
cd scm-sejahtera
```

### 2. Install Dependencies
```bash
pip install PySide6 mysql-connector-python python-dotenv reportlab
```

### 3. Upload SQL Script to MySQL Workbench
- Open **MySQL Workbench**
- Connect to your MySQL server
- Go to **File** → **Open SQL Script**
- Open the provided `SQL SCRIPT VMS.sql` file
- Click the  **Execute** button to run the script
- This will create the `scm` database and all required tables

---

## 🔧 Configuration

### 1. Create `.env` File
Copy `.env.example` and fill in your database credentials:

```bash
cp .env.example .env
```

### 2. Edit `.env`
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=mydb
```

### 3. `.env.example` Template
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=mydb
```


---

## Running the App

```bash
python main.py
```

---

## User Roles

| Role | Access |
|---|---|
| **Admin** | Full access — Dashboard, Users, Products, Categories, Suppliers, Customers, Purchase Orders, Sales Orders, Payments, Supplier Payments, Invoices |
| **Cashier** | Sales Orders, Customer Payments, Manage Customers |
| **Purchasing** | Products, Categories, Suppliers, Purchase Orders, Supplier Payments |

### Default Login Credentials

| Username | Password | Role |
|---|---|---|
| `admin` | `admin` | Admin |
| `cashier` | `cashier` | Cashier |
| `purchasing` | `purchasing` | Purchasing |



---
