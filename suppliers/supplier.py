from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from suppliers.ui_supplier import Ui_supplier
from db_connector import get_connection

#Add supplier
from suppliers.add_supplier_ui import Ui_addsupplier
#Edit Supplier
from suppliers.edit_supplier_ui import Ui_editsupplier
#Manage Supplier
from suppliers.manage_supplier_ui import Ui_Managesupplier

class SupplierWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_supplier()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.pushButton_11.clicked.connect(self.close)
        self.ui.add_SupplierButton.clicked.connect(self.add_supplier)
        self.ui.Edit_supplier_button.clicked.connect(self.edit_supplier)
        self.ui.manage_supplier_button.clicked.connect(self.manage_supplier)

    def add_supplier(self):
        self.add_customer_window = AddSupplierWindow()
        self.add_customer_window.show()

    def edit_supplier(self):
        self.edit_supplier_window = EditSupplierWindow()
        self.edit_supplier_window.show()

    def manage_supplier(self):
        self.manage_supplier_window = ViewSupplierWindow()
        self.manage_supplier_window.show()

#Add Supplier
class AddSupplierWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_addsupplier()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.save_button.clicked.connect(self.save_supplier)
        self.ui.Back_button.clicked.connect(self.close)

    def save_supplier(self):
        name = self.ui.Name_textarea.text()
        phone = self.ui.Phone_TextArea_2.text()
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
                INSERT INTO Suppliers (SupplierName, Phone, Email, Address)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (name, phone, email, address))
            conn.commit()

            QMessageBox.information(self, "Success", "Supplier added successfully!")
            self.clear_fields()

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def clear_fields(self):
        self.ui.Name_textarea.clear()
        self.ui.Phone_TextArea_2.clear()
        self.ui.Email_textarea.clear()
        self.ui.address_textarea.clear()

#Edit Supplier
class EditSupplierWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_editsupplier()
        self.ui.setupUi(self)

        self.load_suppliers()
        self.ui.Selectsupplier_combobox.currentIndexChanged.connect(self.fill_supplier_data)
        self.ui.editsupplier_button.clicked.connect(self.save_edit)
        self.ui.Back_button.clicked.connect(self.close)

    def load_suppliers(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT SupplierID, SupplierName FROM Suppliers")
            suppliers = cursor.fetchall()  # ← was "customers", fixed to "suppliers"

            self.ui.Selectsupplier_combobox.clear()
            for supplier in suppliers:  # ← was "for supplier in supplier", fixed
                self.ui.Selectsupplier_combobox.addItem(supplier[1], supplier[0])

            cursor.close()
            conn.close()

            self.fill_supplier_data()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def fill_supplier_data(self):
        supplier_id = self.ui.Selectsupplier_combobox.currentData()
        if not supplier_id:
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT SupplierName, Phone, Email, Address 
                FROM Suppliers WHERE SupplierID = %s
            """, (supplier_id,))
            supplier = cursor.fetchone()

            if supplier:
                self.ui.name_textarea.setText(str(supplier[0]) if supplier[0] else '')
                self.ui.phone_textareea.setText(str(supplier[1]) if supplier[1] else '')
                self.ui.email_textareea_2.setText(str(supplier[2]) if supplier[2] else '')
                self.ui.address_textareea_3.setText(str(supplier[3]) if supplier[3] else '')

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def save_edit(self):
        supplier_id = self.ui.Selectsupplier_combobox.currentData()  # ← was Selectcustomer_combobox
        name = self.ui.name_textarea.text()
        phone = self.ui.phone_textareea.text()
        email = self.ui.email_textareea_2.text()
        address = self.ui.address_textareea_3.text()

        if not name:
            QMessageBox.warning(self, "Error", "Supplier name is required")  # ← was "Customer"
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE Suppliers 
                SET SupplierName = %s, Phone = %s, Email = %s, Address = %s
                WHERE SupplierID = %s
            """, (name, phone, email, address, supplier_id))
            conn.commit()

            QMessageBox.information(self, "Success", "Supplier updated successfully!")  # ← was "Customer"
            self.load_suppliers()  # ← was load_customers()

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

#manage supplier
class ViewSupplierWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Managesupplier()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.Back_button.clicked.connect(self.close)
        self.ui.pushButton.clicked.connect(self.delete_supplier)

        # Load data when form opens
        self.load_suppliers_table()
        self.load_suppliers_combobox()

    def load_suppliers_table(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT SupplierID, SupplierName, Phone, Email, Address
                FROM Suppliers
            """)
            suppliers = cursor.fetchall()

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels([
                'ID', 'Supplier Name', 'Phone', 'Email', 'Address'
            ])

            for row_data in suppliers:
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

    def load_suppliers_combobox(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT SupplierID, SupplierName FROM suppliers")
            suppliers = cursor.fetchall()

            self.ui.comboBox.clear()
            for supplier in suppliers:
                self.ui.comboBox.addItem(supplier[1], supplier[0])

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def delete_supplier(self):
        supplier_id = self.ui.comboBox.currentData()
        supplier_name = self.ui.comboBox.currentText()

        confirm = QMessageBox.question(
            self, "Confirm Delete",
            f"Are you sure you want to delete customer '{supplier_name}'?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            try:
                conn = get_connection()
                cursor = conn.cursor()

                cursor.execute("DELETE FROM Suppliers WHERE SupplierID = %s", (supplier_id,))
                conn.commit()

                QMessageBox.information(self, "Success", f"Supplier '{supplier_name}' deleted successfully!")

                self.load_suppliers_table()
                self.load_suppliers_combobox()

                cursor.close()
                conn.close()

            except Exception as e:
                QMessageBox.critical(self, "Database Error", str(e))