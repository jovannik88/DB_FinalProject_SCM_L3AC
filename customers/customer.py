from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from db_connector import get_connection

from customers.customer_ui import Ui_customer
#Add Customer
from customers.add_customer_ui import add_users_ui
#Edit Customer
from customers.edit_customer_ui import Ui_EditCustomer
#view_customer
from customers.view_customer_ui import Ui_viewcustomer


class CustomerWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_customer()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.pushButton_11.clicked.connect(self.close)
        self.ui.add_CustomerButton.clicked.connect(self.add_customer)
        self.ui.Edit_customer_button.clicked.connect(self.edit_customer)
        self.ui.manage_customer_button.clicked.connect(self.manage_customer)

    def add_customer(self):
        self.add_customer_window = AddCustomerWindow()
        self.add_customer_window.show()

    def edit_customer(self):
        self.edit_customer_window = EditCustomerWindow()
        self.edit_customer_window.show()

    def manage_customer(self):
        self.edit_customer_window = ViewCustomerWindow()
        self.edit_customer_window.show()

#Add Customer 
class AddCustomerWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = add_users_ui()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.save_button.clicked.connect(self.save_customer)
        self.ui.Back_button.clicked.connect(self.close)

    def save_customer(self):
        name = self.ui.Name_textarea.text()
        phone = self.ui.Phone_textarea.text()
        email = self.ui.Email_textarea.text()
        address = self.ui.address_textarea.text()

        # Validate fields
        if not name:
            QMessageBox.warning(self, "Error", "Customer name is required")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO Customers (CustomerName, Phone, Email, Address)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (name, phone, email, address))
            conn.commit()

            QMessageBox.information(self, "Success", "Customer added successfully!")
            self.clear_fields()

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def clear_fields(self):
        self.ui.Name_textarea.clear()
        self.ui.Phone_textarea.clear()
        self.ui.Email_textarea.clear()
        self.ui.address_textarea.clear()

#Edit Customer
class EditCustomerWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_EditCustomer()
        self.ui.setupUi(self)

        # Load customers when form opens
        self.load_customers()

        # When customer is selected, auto fill fields
        self.ui.Selectcustomer_combobox.currentIndexChanged.connect(self.fill_customer_data)

        # Connect buttons
        self.ui.editcustomer_button.clicked.connect(self.save_edit)
        self.ui.Back_button.clicked.connect(self.close)

    def load_customers(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT CustomerID, CustomerName FROM Customers")
            customers = cursor.fetchall()

            self.ui.Selectcustomer_combobox.clear()
            for customer in customers:
                self.ui.Selectcustomer_combobox.addItem(customer[1], customer[0])

            cursor.close()
            conn.close()

            # Fill data for first customer
            self.fill_customer_data()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def fill_customer_data(self):
        customer_id = self.ui.Selectcustomer_combobox.currentData()
        if not customer_id:
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT CustomerName, Phone, Email, Address 
                FROM Customers WHERE CustomerID = %s
            """, (customer_id,))
            customer = cursor.fetchone()

            if customer:
                self.ui.name_textarea.setText(str(customer[0]) if customer[0] else '')
                self.ui.phone_textareea.setText(str(customer[1]) if customer[1] else '')
                self.ui.email_textareea_2.setText(str(customer[2]) if customer[2] else '')
                self.ui.address_textareea_3.setText(str(customer[3]) if customer[3] else '')

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def save_edit(self):
        customer_id = self.ui.Selectcustomer_combobox.currentData()
        name = self.ui.name_textarea.text()
        phone = self.ui.phone_textareea.text()
        email = self.ui.email_textareea_2.text()
        address = self.ui.address_textareea_3.text()

        if not name:
            QMessageBox.warning(self, "Error", "Customer name is required")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE Customers 
                SET CustomerName = %s, Phone = %s, Email = %s, Address = %s
                WHERE CustomerID = %s
            """, (name, phone, email, address, customer_id))
            conn.commit()

            QMessageBox.information(self, "Success", "Customer updated successfully!")
            self.load_customers()

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

#View Customer
class ViewCustomerWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_viewcustomer()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.Back_button.clicked.connect(self.close)
        self.ui.pushButton.clicked.connect(self.delete_customer)

        # Load data when form opens
        self.load_customers_table()
        self.load_customers_combobox()

    def load_customers_table(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT CustomerID, CustomerName, Phone, Email, Address
                FROM Customers
            """)
            customers = cursor.fetchall()

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels([
                'ID', 'Customer Name', 'Phone', 'Email', 'Address'
            ])

            for row_data in customers:
                row = []
                for item in row_data:
                    cell = QStandardItem(str(item) if item else '')
                    cell.setEditable(False)
                    row.append(cell)
                model.appendRow(row)

            self.ui.View_Customer.setModel(model)
            self.ui.View_Customer.resizeColumnsToContents()
            self.ui.View_Customer.horizontalHeader().setStretchLastSection(True)
            self.ui.View_Customer.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            self.ui.View_Customer.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def load_customers_combobox(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT CustomerID, CustomerName FROM Customers")
            customers = cursor.fetchall()

            self.ui.comboBox.clear()
            for customer in customers:
                self.ui.comboBox.addItem(customer[1], customer[0])

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def delete_customer(self):
        customer_id = self.ui.comboBox.currentData()
        customer_name = self.ui.comboBox.currentText()

        confirm = QMessageBox.question(
            self, "Confirm Delete",
            f"Are you sure you want to delete customer '{customer_name}'?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            try:
                conn = get_connection()
                cursor = conn.cursor()

                cursor.execute("DELETE FROM Customers WHERE CustomerID = %s", (customer_id,))
                conn.commit()

                QMessageBox.information(self, "Success", f"Customer '{customer_name}' deleted successfully!")

                self.load_customers_table()
                self.load_customers_combobox()

                cursor.close()
                conn.close()

            except Exception as e:
                QMessageBox.critical(self, "Database Error", str(e))
