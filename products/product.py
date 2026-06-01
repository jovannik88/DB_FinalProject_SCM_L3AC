from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from db_connector import get_connection

#Import Product UI
from products.product_ui import Ui_Product
#add product
from products.add_product_ui import Ui_AddProduct
#edit Product
from products.edit_product_ui import Ui_EditProduct
# Manage Product
from products.manage_product_ui import Ui_manageproduct


class ProductWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Product()
        self.ui.setupUi(self)

        self.ui.pushButton_11.clicked.connect(self.close)
        self.ui.add_Product_button.clicked.connect(self.add_product)
        self.ui.Edit_Product_button.clicked.connect(self.edit_product)
        self.ui.View_Product_Button.clicked.connect(self.view_product)

    def add_product(self):
        self.add_user_window = AddProductWindow()
        self.add_user_window.show()

    def edit_product(self):
        self.edit_product_window = EditProductWindow()
        self.edit_product_window.show()

    def view_product(self):
        self.view_product_window = ViewProductWindow()
        self.view_product_window.show()


class AddProductWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AddProduct()
        self.ui.setupUi(self)

        self.load_categories()
        self.load_units()

        self.ui.save_button.clicked.connect(self.save_product)
        self.ui.Back_button.clicked.connect(self.close)

    def load_categories(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT CategoryID, CategoryName FROM Categories")
            categories = cursor.fetchall()

            self.ui.ID_combobox.clear()
            for category in categories:
                self.ui.ID_combobox.addItem(category[1], category[0])

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def load_units(self):
        units = ['Pcs', 'Kg', 'G', 'L', 'ML', 'Bottle', 'Box', 'Pack', 'Dozen', 'Meter']
        self.ui.Units_combobox_2.clear()
        for unit in units:
            self.ui.Units_combobox_2.addItem(unit)

    def save_product(self):
        product_name = self.ui.productname_textarea.text()
        description = self.ui.Description_textareea.text()
        category_id = self.ui.ID_combobox.currentData()
        buying_price = self.ui.BuyingPrice_textareea_2.text()
        selling_price = self.ui.BuyingPrice_textareea_3.text()
        units = self.ui.Units_combobox_2.currentText()
        quantity = self.ui.Quantity_textareea_5.text()

        if not product_name:
            QMessageBox.warning(self, "Error", "Product name is required")
            return
        if not buying_price:
            QMessageBox.warning(self, "Error", "Buying price is required")
            return
        if not selling_price:
            QMessageBox.warning(self, "Error", "Selling price is required")
            return
        if not quantity:
            QMessageBox.warning(self, "Error", "Quantity is required")
            return

        try:
            buying_price = float(buying_price)
            selling_price = float(selling_price)
            quantity = int(quantity)
        except ValueError:
            QMessageBox.warning(self, "Error", "Price and quantity must be numbers")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO Products 
                (ProductName, Description, CategoryID, BuyingPrice, SellingPrice, MeasurementUnits, Quantity, LastUpdated)
                VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())
            """, (product_name, description, category_id, buying_price, selling_price, units, quantity))
            conn.commit()

            QMessageBox.information(self, "Success", "Product added successfully!")
            self.clear_fields()

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def clear_fields(self):
        self.ui.productname_textarea.clear()
        self.ui.Description_textareea.clear()
        self.ui.BuyingPrice_textareea_2.clear()
        self.ui.BuyingPrice_textareea_3.clear()
        self.ui.Quantity_textareea_5.clear()
        self.ui.ID_combobox.setCurrentIndex(0)
        self.ui.Units_combobox_2.setCurrentIndex(0)


class EditProductWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_EditProduct()
        self.ui.setupUi(self)

        self.load_products()
        self.load_categories()
        self.load_units()

        self.ui.ID_combobox_2.currentIndexChanged.connect(self.fill_product_data)
        self.ui.save_button.clicked.connect(self.save_edit)
        self.ui.Back_button.clicked.connect(self.close)

    def load_products(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT ProductID, ProductName FROM Products")
            products = cursor.fetchall()

            self.ui.ID_combobox_2.clear()
            for product in products:
                self.ui.ID_combobox_2.addItem(product[1], product[0])

            cursor.close()
            conn.close()

            self.fill_product_data()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def load_categories(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT CategoryID, CategoryName FROM Categories")
            categories = cursor.fetchall()

            self.ui.ID_combobox.clear()
            for category in categories:
                self.ui.ID_combobox.addItem(category[1], category[0])

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def load_units(self):
        units = ['Pcs', 'Kg', 'G', 'L', 'ML', 'Bottle', 'Box', 'Pack', 'Dozen', 'Meter']
        self.ui.Units_combobox_2.clear()
        for unit in units:
            self.ui.Units_combobox_2.addItem(unit)

    def fill_product_data(self):
        product_id = self.ui.ID_combobox_2.currentData()
        if not product_id:
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT ProductName, Description, CategoryID, BuyingPrice,
                       SellingPrice, MeasurementUnits, Quantity 
                FROM Products WHERE ProductID = %s
            """, (product_id,))
            product = cursor.fetchone()

            if product:
                self.ui.productname_textarea.setText(str(product[0]) if product[0] else '')
                self.ui.Description_textareea.setText(str(product[1]) if product[1] else '')

                index = self.ui.ID_combobox.findData(product[2])
                if index >= 0:
                    self.ui.ID_combobox.setCurrentIndex(index)

                self.ui.BuyingPrice_textareea_2.setText(str(product[3]) if product[3] else '')
                self.ui.BuyingPrice_textareea_3.setText(str(product[4]) if product[4] else '')

                unit_index = self.ui.Units_combobox_2.findText(str(product[5]) if product[5] else '')
                if unit_index >= 0:
                    self.ui.Units_combobox_2.setCurrentIndex(unit_index)

                self.ui.Quantity_textareea_5.setText(str(product[6]) if product[6] else '')

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def save_edit(self):
        product_id = self.ui.ID_combobox_2.currentData()
        product_name = self.ui.productname_textarea.text()
        description = self.ui.Description_textareea.text()
        category_id = self.ui.ID_combobox.currentData()
        buying_price = self.ui.BuyingPrice_textareea_2.text()
        selling_price = self.ui.BuyingPrice_textareea_3.text()
        units = self.ui.Units_combobox_2.currentText()
        quantity = self.ui.Quantity_textareea_5.text()

        if not product_name:
            QMessageBox.warning(self, "Error", "Product name is required")
            return
        if not buying_price:
            QMessageBox.warning(self, "Error", "Buying price is required")
            return
        if not selling_price:
            QMessageBox.warning(self, "Error", "Selling price is required")
            return

        try:
            buying_price = float(buying_price)
            selling_price = float(selling_price)
            quantity = int(quantity)
        except ValueError:
            QMessageBox.warning(self, "Error", "Price and quantity must be numbers")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE Products 
                SET ProductName = %s, Description = %s, CategoryID = %s,
                    BuyingPrice = %s, SellingPrice = %s, MeasurementUnits = %s,
                    Quantity = %s, LastUpdated = NOW()
                WHERE ProductID = %s
            """, (product_name, description, category_id, buying_price,
                  selling_price, units, quantity, product_id))
            conn.commit()

            QMessageBox.information(self, "Success", "Product updated successfully!")
            self.load_products()

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))


class ViewProductWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_manageproduct()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.delete_product)
        self.ui.pushButton_2.clicked.connect(self.close)

        self.load_products_table()
        self.load_products_combobox()

    def showEvent(self, event):
        super().showEvent(event)
        self.load_products_table()
        self.load_products_combobox()

    def load_products_table(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT p.ProductID, p.ProductName, p.Description, 
                       c.CategoryName, p.MeasurementUnits, p.Quantity,
                       p.LastUpdated, p.LastPurchasePrice, p.LastPurchaseDate,
                       p.LastSellPrice, p.LastSellDate
                FROM Products p
                JOIN Categories c ON p.CategoryID = c.CategoryID
            """)
            products = cursor.fetchall()

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels([
                'ID', 'Product Name', 'Description', 'Category',
                'Units', 'Quantity', 'Last Updated',
                'Last Purchase Price', 'Last Purchase Date',
                'Last Sell Price', 'Last Sell Date'
            ])

            for row_data in products:
                row = []
                for item in row_data:
                    cell = QStandardItem(str(item) if item else '')
                    cell.setEditable(False)
                    row.append(cell)
                model.appendRow(row)

            self.ui.ProducrView.setModel(model)
            self.ui.ProducrView.resizeColumnsToContents()
            self.ui.ProducrView.horizontalHeader().setStretchLastSection(True)
            self.ui.ProducrView.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            self.ui.ProducrView.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def load_products_combobox(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT ProductID, ProductName FROM Products")
            products = cursor.fetchall()

            self.ui.comboBox.clear()
            for product in products:
                self.ui.comboBox.addItem(product[1], product[0])

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def delete_product(self):
        product_id = self.ui.comboBox.currentData()
        product_name = self.ui.comboBox.currentText()

        confirm = QMessageBox.question(
            self, "Confirm Delete",
            f"Are you sure you want to delete product '{product_name}'?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            try:
                conn = get_connection()
                cursor = conn.cursor()

                cursor.execute("DELETE FROM Products WHERE ProductID = %s", (product_id,))
                conn.commit()

                QMessageBox.information(self, "Success", f"Product '{product_name}' deleted successfully!")

                self.load_products_table()
                self.load_products_combobox()

                cursor.close()
                conn.close()

            except Exception as e:
                QMessageBox.critical(self, "Database Error", str(e))