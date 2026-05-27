from PySide6.QtWidgets import (QDialog, QMessageBox, QComboBox, QSpinBox, 
                                QLineEdit, QTableWidgetItem, QHeaderView)
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QDate, Qt
from db_connector import get_connection



from SalesOrders.salesorder_ui import Ui_SalesOrder

#Add New Sales Order
from SalesOrders.new_so_ui import Ui_NewSO

#View Sales Detail
from SalesOrders.view_salesdetail_ui import Ui_ViewSalesDetail

#View Sales Order
from SalesOrders.view_so_ui import Ui_ViewSO

#Cancel Order
from SalesOrders.cancelorder_ui import Ui_CancelOrder

from SalesOrders.so_invoice import SOInvoiceWindow



class SalesOrderWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SalesOrder()
        self.ui.setupUi(self)

        self.ui.pushButton_11.clicked.connect(self.close)
        self.ui.New_SO_Button.clicked.connect(self.create_New_SO_ui)
        self.ui.view_so_button.clicked.connect(self.view_SO_ui)
        self.ui.view_SODetail_button.clicked.connect(self.view_SODetail_ui)
        self.ui.CancelOrder__button.clicked.connect(self.cancel_ui)
        self.ui.CancelOrder__button_2.clicked.connect(self.invoice_ui)

    def create_New_SO_ui(self):
        self.new_so_window = CreateSOWindow()
        self.new_so_window.show()

    def view_SO_ui(self):
        self.view_so_window = ViewSOWindow()
        self.view_so_window.show()

    def view_SODetail_ui(self):
        self.view_soDetail_window = ViewSODetailWindow()
        self.view_soDetail_window.show()

    def cancel_ui(self):
        self.cancel_window = CancelSOWindow()
        self.cancel_window.show()
    
    def invoice_ui(self):
        self.invoice_window = SOInvoiceWindow()
        self.invoice_window.show()


#Add New Sales Order
class CreateSOWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_NewSO()
        self.ui.setupUi(self)

        self.load_customers()
        self.set_today_date()

        # Set columns evenly sized
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.ui.pushButton_11.clicked.connect(self.close)
        self.ui.AddProduct_Button_.clicked.connect(self.add_product_row)
        self.ui.DeleteProduct_Button.clicked.connect(self.remove_product_row)
        self.ui.saveqty_button_12.clicked.connect(self.save_order)

    def load_customers(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT CustomerID, CustomerName FROM Customers")
            customers = cursor.fetchall()

            self.ui.selectCust_combobox.clear()
            for customer in customers:
                self.ui.selectCust_combobox.addItem(customer[1], customer[0])

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def set_today_date(self):
        self.ui.SelectDate.setDisplayFormat("dd/MM/yyyy")
        self.ui.SelectDate.setDate(QDate.currentDate())

    def get_products(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT ProductID, ProductName, SellingPrice, Quantity FROM Products")
            products = cursor.fetchall()

            cursor.close()
            conn.close()
            return products

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))
            return []

    def add_product_row(self):
        products = self.get_products()
        if not products:
            QMessageBox.warning(self, "Error", "No products found in database")
            return

        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)

        # Column 0 - Product ComboBox
        product_combo = QComboBox()
        for product in products:
            product_combo.addItem(f"{product[1]} (Stock: {product[3]})", product[0])
        self.ui.tableWidget.setCellWidget(row, 0, product_combo)

        # Column 1 - Quantity SpinBox
        qty_spinbox = QSpinBox()
        qty_spinbox.setMinimum(1)
        qty_spinbox.setMaximum(99999)
        qty_spinbox.setValue(1)
        self.ui.tableWidget.setCellWidget(row, 1, qty_spinbox)

        # Column 2 - Unit Price LineEdit
        unit_price_input = QLineEdit()
        unit_price_input.setPlaceholderText("0.00")

        # Auto fill selling price when product is selected
        def fill_price():
            selected_id = product_combo.currentData()
            for p in products:
                if p[0] == selected_id:
                    unit_price_input.setText(str(p[2]))
                    break

        product_combo.currentIndexChanged.connect(fill_price)
        fill_price()  # fill on first load
        self.ui.tableWidget.setCellWidget(row, 2, unit_price_input)

        # Column 3 - Discount LineEdit
        discount_input = QLineEdit()
        discount_input.setPlaceholderText("0.00")
        discount_input.setText("0")
        self.ui.tableWidget.setCellWidget(row, 3, discount_input)

        # Column 4 - Subtotal (read only)
        subtotal_item = QTableWidgetItem("0.00")
        subtotal_item.setFlags(Qt.ItemIsEnabled)
        self.ui.tableWidget.setItem(row, 4, subtotal_item)

        # Connect changes to update subtotal
        qty_spinbox.valueChanged.connect(lambda: self.update_subtotal(row))
        unit_price_input.textChanged.connect(lambda: self.update_subtotal(row))
        discount_input.textChanged.connect(lambda: self.update_subtotal(row))

    def remove_product_row(self):
        current_row = self.ui.tableWidget.currentRow()
        if current_row >= 0:
            self.ui.tableWidget.removeRow(current_row)
            self.update_total()
        else:
            QMessageBox.warning(self, "Error", "Please select a row to remove")

    def update_subtotal(self, row):
        try:
            qty_widget = self.ui.tableWidget.cellWidget(row, 1)
            price_widget = self.ui.tableWidget.cellWidget(row, 2)
            discount_widget = self.ui.tableWidget.cellWidget(row, 3)

            if qty_widget and price_widget and discount_widget:
                qty = qty_widget.value()
                price_text = price_widget.text()
                discount_text = discount_widget.text()

                if price_text:
                    price = float(price_text)
                    discount = float(discount_text) if discount_text else 0.0
                    subtotal = (qty * price) - discount
                    subtotal = max(0, subtotal)  # prevent negative
                    self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(f"{subtotal:,.2f}"))

            self.update_total()

        except ValueError:
            pass

    def update_total(self):
        total = 0.0
        for row in range(self.ui.tableWidget.rowCount()):
            subtotal_item = self.ui.tableWidget.item(row, 4)
            if subtotal_item and subtotal_item.text():
                try:
                    total += float(subtotal_item.text().replace(',', ''))
                except ValueError:
                    pass

        self.ui.label_amount.setText(f"Rp. {total:,.2f}")

    def save_order(self):
        customer_id = self.ui.selectCust_combobox.currentData()
        sales_date = self.ui.SelectDate.date().toString("yyyy-MM-dd")

        if self.ui.tableWidget.rowCount() == 0:
            QMessageBox.warning(self, "Error", "Please add at least one product")
            return

        order_items = []
        for row in range(self.ui.tableWidget.rowCount()):
            product_combo = self.ui.tableWidget.cellWidget(row, 0)
            qty_spinbox = self.ui.tableWidget.cellWidget(row, 1)
            price_input = self.ui.tableWidget.cellWidget(row, 2)
            discount_input = self.ui.tableWidget.cellWidget(row, 3)

            product_id = product_combo.currentData()
            qty = qty_spinbox.value()
            price_text = price_input.text()
            discount_text = discount_input.text()

            if not price_text:
                QMessageBox.warning(self, "Error", f"Please enter unit price for row {row + 1}")
                return

            try:
                unit_price = float(price_text)
                discount = float(discount_text) if discount_text else 0.0
            except ValueError:
                QMessageBox.warning(self, "Error", f"Invalid price or discount in row {row + 1}")
                return

            subtotal = (qty * unit_price) - discount

            # Check stock availability
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("SELECT Quantity, ProductName FROM Products WHERE ProductID = %s", (product_id,))
                stock = cursor.fetchone()
                cursor.close()
                conn.close()

                if stock and stock[0] < qty:
                    QMessageBox.warning(self, "Error", 
                        f"Insufficient stock for '{stock[1]}'\nAvailable: {stock[0]}, Requested: {qty}")
                    return
            except Exception as e:
                QMessageBox.critical(self, "Database Error", str(e))
                return

            order_items.append((product_id, qty, unit_price, discount, subtotal))

        total = sum(item[4] for item in order_items)

        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Insert into SalesOrders with Pending status
            cursor.execute("""
                INSERT INTO SalesOrders (SalesDate, CustomerID, TotalAmount, Status)
                VALUES (%s, %s, %s, 'Pending')
            """, (sales_date, customer_id, total))

            sales_id = cursor.lastrowid

            for product_id, qty, unit_price, discount, subtotal in order_items:
                # Insert into SalesDetail
                cursor.execute("""
                    INSERT INTO SalesDetail (SalesID, ProductID, Quantity, UnitPrice, Discount, Subtotal)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (sales_id, product_id, qty, unit_price, discount, subtotal))

                # Decrease product quantity
                cursor.execute("""
                    UPDATE Products
                    SET Quantity = Quantity - %s,
                        LastSellPrice = %s,
                        LastSellDate = NOW()
                    WHERE ProductID = %s
                """, (qty, unit_price, product_id))

            conn.commit()

            QMessageBox.information(self, "Success", "Sales Order saved successfully!")
            self.clear_form()

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def clear_form(self):
        self.ui.tableWidget.setRowCount(0)
        self.ui.label_amount.setText("")
        self.ui.selectCust_combobox.setCurrentIndex(0)
        self.set_today_date()


#View Sales Detail
class ViewSODetailWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ViewSalesDetail()
        self.ui.setupUi(self)

        self.ui.pushButton_11.clicked.connect(self.close)
        self.load_sales_details()

    def showEvent(self, event):
        super().showEvent(event)
        self.load_sales_details()

    def load_sales_details(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT sd.SalesID, p.ProductName, sd.Quantity,
                       sd.UnitPrice, sd.Discount, sd.Subtotal
                FROM SalesDetail sd
                JOIN Products p ON sd.ProductID = p.ProductID
                ORDER BY sd.SalesID DESC
            """)
            details = cursor.fetchall()

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels([
                'SO ID', 'Product', 'Quantity',
                'Unit Price', 'Discount', 'Subtotal'
            ])

            for row_data in details:
                row = []
                for item in row_data:
                    cell = QStandardItem(str(item) if item else '')
                    cell.setEditable(False)
                    row.append(cell)
                model.appendRow(row)

            self.ui.viewsalesdetail_tableView.setModel(model)
            self.ui.viewsalesdetail_tableView.resizeColumnsToContents()
            self.ui.viewsalesdetail_tableView.horizontalHeader().setStretchLastSection(True)
            self.ui.viewsalesdetail_tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            self.ui.viewsalesdetail_tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

#View Sales Detail
class ViewSOWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ViewSO()
        self.ui.setupUi(self)

        self.ui.pushButton_11.clicked.connect(self.close)
        self.load_sales_orders()

    def showEvent(self, event):
        super().showEvent(event)
        self.load_sales_orders()

    def load_sales_orders(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT so.SalesID, c.CustomerName, so.SalesDate,
                       so.TotalAmount, so.Status
                FROM SalesOrders so
                JOIN Customers c ON so.CustomerID = c.CustomerID
                ORDER BY so.SalesDate DESC
            """)
            orders = cursor.fetchall()

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels([
                'SO ID', 'Customer', 'Date', 'Total Amount', 'Status'
            ])

            for row_data in orders:
                row = []
                for item in row_data:
                    cell = QStandardItem(str(item) if item else '')
                    cell.setEditable(False)
                    row.append(cell)
                model.appendRow(row)

            self.ui.viewso_tableView.setModel(model)
            self.ui.viewso_tableView.resizeColumnsToContents()
            self.ui.viewso_tableView.horizontalHeader().setStretchLastSection(True)
            self.ui.viewso_tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            self.ui.viewso_tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

#Cancel Order
class CancelSOWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CancelOrder()
        self.ui.setupUi(self)

        self.load_sales_orders()

        self.ui.PONO_comboBox.currentIndexChanged.connect(self.show_order_info)
        self.ui.pushButton_11.clicked.connect(self.close)
        self.ui.Update_button.clicked.connect(self.cancel_order)

    def load_sales_orders(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Only show Pending orders
            cursor.execute("""
                SELECT so.SalesID, c.CustomerName, so.SalesDate, so.TotalAmount
                FROM SalesOrders so
                JOIN Customers c ON so.CustomerID = c.CustomerID
                WHERE so.Status = 'Pending'
                ORDER BY so.SalesDate DESC
            """)
            orders = cursor.fetchall()

            self.ui.PONO_comboBox.clear()
            for order in orders:
                label = f"SO#{order[0]} - {order[1]} ({order[2]})"
                self.ui.PONO_comboBox.addItem(label, order[0])

            cursor.close()
            conn.close()

            self.show_order_info()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def show_order_info(self):
        so_id = self.ui.PONO_comboBox.currentData()
        if not so_id:
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT so.Status, c.CustomerName, so.TotalAmount
                FROM SalesOrders so
                JOIN Customers c ON so.CustomerID = c.CustomerID
                WHERE so.SalesID = %s
            """, (so_id,))
            result = cursor.fetchone()

            if result:
                self.ui.TotalAmount_label.setText(
                    f"Status: {result[0]} | Customer: {result[1]} | Total: Rp. {result[2]:,.2f}"
                )

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def cancel_order(self):
        so_id = self.ui.PONO_comboBox.currentData()

        if not so_id:
            QMessageBox.warning(self, "Error", "Please select a Sales Order")
            return

        confirm = QMessageBox.question(
            self, "Confirm Cancellation",
            f"Are you sure you want to cancel SO#{so_id}?\nThis will restore product quantities.",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            try:
                conn = get_connection()
                cursor = conn.cursor()

                # Restore product quantities
                cursor.execute("""
                    SELECT ProductID, Quantity FROM SalesDetail
                    WHERE SalesID = %s
                """, (so_id,))
                items = cursor.fetchall()

                for item in items:
                    cursor.execute("""
                        UPDATE Products
                        SET Quantity = Quantity + %s
                        WHERE ProductID = %s
                    """, (item[1], item[0]))

                # Cancel the order
                cursor.execute("""
                    UPDATE SalesOrders 
                    SET Status = 'Cancelled'
                    WHERE SalesID = %s
                """, (so_id,))

                conn.commit()

                QMessageBox.information(self, "Success", 
                    f"SO#{so_id} cancelled and product quantities restored!")
                self.load_sales_orders()

                cursor.close()
                conn.close()

            except Exception as e:
                QMessageBox.critical(self, "Database Error", str(e))