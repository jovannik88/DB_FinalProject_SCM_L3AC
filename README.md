# Supply Chain Management System

## Brief Introduction

A supply chain refers to the complete network of individuals, organizaƟons, acƟviƟes,
informaƟon, and resources involved in producing and delivering a product or service to
the end customer. It begins with the sourcing of raw materials and conƟnues through
manufacturing, storage, distribuƟon, and final delivery. In modern business
environments, supply chains are no longer simple or local; instead, they are complex
systems that oŌen span mulƟple countries and regions.

With the rapid growth of globalizaƟon and digital transformaƟon, supply chain
management has become a key factor in determining a company's success. Businesses
today must coordinate with suppliers, manage inventories, and ensure Ɵmely delivery
while maintaining cost efficiency. Companies such as Amazon have set high standards by
leveraging advanced logisƟcs systems and data-driven decision-making to deliver
products quickly and reliably.

Moreover, consumer expectaƟons have significantly increased. Customers now demand
faster shipping, beƩer product availability, and lower prices. As a result, companies are
under constant pressure to opƟmize their supply chains. However, while an efficient
supply chain can provide numerous benefits, it also introduces various risks and
challenges that must be carefully managed.

One of the most important advantages of a well-managed supply chain is improved
operaƟonal efficiency. By streamlining processes and eliminaƟng unnecessary steps,
companies can ensure that goods move smoothly from one stage to another. This
reduces delays and allows businesses to operate more effecƟvely.

Another key benefit is cost reducƟon. Efficient supply chains enable companies to
opƟmize inventory levels, reduce storage costs, and minimize waste. Bulk purchasing and
beƩer supplier relaƟonships can also help lower the cost of raw materials. Over Ɵme,
these savings can significantly improve a company's profitability.

Supply chains also contribute to faster delivery and improved customer saƟsfacƟon. With
well-organized logisƟcs and distribuƟon systems, companies can ensure that products
reach customers on Ɵme. This is especially important in compeƟƟve markets where
customers expect quick and reliable service.

In addiƟon, supply chains promote beƩer collaboraƟon and coordinaƟon among
different stakeholders. Suppliers, manufacturers, and distributors must work together
closely, leading to improved communicaƟon and stronger business relaƟonships. This
collaboraƟon helps prevent misunderstandings and ensures smoother operaƟons.

Another advantage is increased flexibility and responsiveness. A strong supply chain
allows companies to quickly adapt to changes in demand, market condiƟons, or
customer preferences. For example, businesses can adjust producƟon levels or switch
suppliers when necessary.

Finally, an effecƟve supply chain provides a significant compeƟƟve advantage.
Companies that can deliver high-quality products quickly and at lower costs are more
likely to aƩract and retain customers. This advantage can help businesses stand out in
crowded markets and achieve long-term success.

Despite its many benefits, supply chain management also has several disadvantages. One
of the major challenges is its complexity. Managing mulƟple suppliers, transportaƟon
routes, and storage faciliƟes requires careful planning and coordinaƟon. Without proper
systems in place, the supply chain can become inefficient and difficult to control.

Another significant disadvantage is the risk of disrupƟons. Supply chains are highly
sensiƟve to external factors, and even a small disrupƟon can have a large impact. Events
such as natural disasters, economic crises, or global pandemics can delay producƟon and
delivery, causing financial losses for businesses.

High implementaƟon and maintenance costs are also a concern. Establishing a supply
chain requires investment in infrastructure such as warehouses, transportaƟon systems,
and technology plaƞorms. In addiƟon, ongoing costs such as labor, maintenance, and
system upgrades can be expensive.

Dependence on suppliers is another issue. Companies oŌen rely on external suppliers for
raw materials or components. If a supplier fails to deliver on Ɵme or provides low-quality
materials, it can disrupt the enƟre producƟon process and damage the company's
reputaƟon.

Lack of transparency can also create problems within the supply chain. When companies
do not have clear visibility into their operaƟons, it becomes difficult to track inventory,
predict demand, or idenƟfy potenƟal issues. This can lead to inefficiencies and poor
decision-making.

Finally, supply chains can have negaƟve environmental impacts. TransportaƟon,
producƟon, and packaging processes oŌen contribute to polluƟon and carbon emissions.
As a result, companies are increasingly expected to adopt sustainable pracƟces, which
can add additional complexity and cost to supply chain management.



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
