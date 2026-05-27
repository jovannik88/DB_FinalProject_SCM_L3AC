from PySide6.QtWidgets import (QDialog, QMessageBox, QComboBox, QSpinBox, QLineEdit, QTableWidgetItem, QHeaderView)
from PySide6.QtGui import QFont, QStandardItemModel, QStandardItem
from PySide6.QtCore import QDate, Qt
from PurchaseOrders.purchaseorder_ui import Ui_POmenu
from db_connector import get_connection

# Add PO
from PurchaseOrders.newpo_ui import Ui_NewPurchaseorder
# View PO
from PurchaseOrders.view_po_ui import Ui_ViewPO
# View Purchase Detail
from PurchaseOrders.view_purchasedetail_ui import Ui_viewpurchasedetail
# Update Status
from PurchaseOrders.update_status_ui import Ui_UpdateStatus
# Update QTY
from PurchaseOrders.updatepoqty_ui import Ui_updatepoqty
#UI Invoice
from PurchaseOrders.po_invoice import POInvoiceWindow

class PurchaseOrderWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_POmenu()
        self.ui.setupUi(self)

        self.ui.pushButton_11.clicked.connect(self.close)
        self.ui.New_PO_Button.clicked.connect(self.create_New_PO_ui)
        self.ui.view_po_button.clicked.connect(self.view_PO_ui)
        self.ui.view_purchase_button.clicked.connect(self.view_Purchase_ui)
        self.ui.status__button.clicked.connect(self.status_ui)
        self.ui.Receive_Qty_Button.clicked.connect(self.receive_qty_ui)
        self.ui.Invoice_Button.clicked.connect(self.invoice_ui)

    def create_New_PO_ui(self):
        self.new_po_window = CreatePOWindow()
        self.new_po_window.show()

    def view_PO_ui(self):
        self.view_po_window = ViewPOWindow()
        self.view_po_window.show()

    def view_Purchase_ui(self):
        self.view_purchasedetail_window = ViewPODetailWindow()
        self.view_purchasedetail_window.show()

    def status_ui(self):
        self.view_updatestatus_window = UpdateStatusWindow()
        self.view_updatestatus_window.show()

    def receive_qty_ui(self):
        self.view_updatereceiveqty_window = UpdateQtyWindow()
        self.view_updatereceiveqty_window.show()
    
    def invoice_ui(self):
        self.view_invoiceui_window = POInvoiceWindow()
        self.view_invoiceui_window.show()


class CreatePOWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_NewPurchaseorder()
        self.ui.setupUi(self)

        self.load_suppliers()
        self.set_today_date() 

        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.ui.pushButton_11.clicked.connect(self.close)
        self.ui.addproduct_button.clicked.connect(self.add_product_row)
        self.ui.removeproduct_button.clicked.connect(self.remove_product_row)
        self.ui.saveorder_button_12.clicked.connect(self.save_order)

    def load_suppliers(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT SupplierID, SupplierName FROM Suppliers")
            suppliers = cursor.fetchall()

            self.ui.selectsupplier_combobox.clear()
            for supplier in suppliers:
                self.ui.selectsupplier_combobox.addItem(supplier[1], supplier[0])

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def set_today_date(self):  
        self.ui.dateEdit_combobox.setDisplayFormat("dd/MM/yyyy")
        self.ui.dateEdit_combobox.setDate(QDate.currentDate())

    def get_products(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT ProductID, ProductName FROM Products")
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

        product_combo = QComboBox()
        for product in products:
            product_combo.addItem(product[1], product[0])
        self.ui.tableWidget.setCellWidget(row, 0, product_combo)

        qty_spinbox = QSpinBox()
        qty_spinbox.setMinimum(1)
        qty_spinbox.setMaximum(99999)
        qty_spinbox.setValue(1)
        self.ui.tableWidget.setCellWidget(row, 1, qty_spinbox)

        unit_price_input = QLineEdit()
        unit_price_input.setPlaceholderText("0.00")
        self.ui.tableWidget.setCellWidget(row, 2, unit_price_input)

        subtotal_item = QTableWidgetItem("0.00")
        subtotal_item.setFlags(Qt.ItemIsEnabled)
        self.ui.tableWidget.setItem(row, 3, subtotal_item)

        qty_spinbox.valueChanged.connect(lambda: self.update_subtotal(row))
        unit_price_input.textChanged.connect(lambda: self.update_subtotal(row))

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

            if qty_widget and price_widget:
                qty = qty_widget.value()
                price_text = price_widget.text()

                if price_text:
                    price = float(price_text)
                    subtotal = qty * price
                    self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(f"{subtotal:,.2f}"))

            self.update_total()

        except ValueError:
            pass

    def update_total(self):
        total = 0.0
        for row in range(self.ui.tableWidget.rowCount()):
            subtotal_item = self.ui.tableWidget.item(row, 3)
            if subtotal_item and subtotal_item.text():
                try:
                    total += float(subtotal_item.text().replace(',', ''))
                except ValueError:
                    pass

        self.ui.TotalAmount_label.setText(f"Rp. {total:,.2f}")

    def save_order(self):
        supplier_id = self.ui.selectsupplier_combobox.currentData()

        if self.ui.tableWidget.rowCount() == 0:
            QMessageBox.warning(self, "Error", "Please add at least one product")
            return

        order_items = []
        for row in range(self.ui.tableWidget.rowCount()):
            product_combo = self.ui.tableWidget.cellWidget(row, 0)
            qty_spinbox = self.ui.tableWidget.cellWidget(row, 1)
            price_input = self.ui.tableWidget.cellWidget(row, 2)

            product_id = product_combo.currentData()
            qty = qty_spinbox.value()
            price_text = price_input.text()

            if not price_text:
                QMessageBox.warning(self, "Error", f"Please enter unit price for row {row + 1}")
                return

            try:
                unit_price = float(price_text)
            except ValueError:
                QMessageBox.warning(self, "Error", f"Invalid price in row {row + 1}")
                return

            order_items.append((product_id, qty, unit_price))

        total = sum(qty * price for _, qty, price in order_items)

        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Use NOW() for exact date and time
            cursor.execute("""
                INSERT INTO PurchaseOrders (PurchaseDate, SupplierID, TotalAmount, Status)
                VALUES (NOW(), %s, %s, 'Pending')
            """, (supplier_id, total))

            purchase_id = cursor.lastrowid

            for product_id, qty, unit_price in order_items:
                cursor.execute("""
                    INSERT INTO PurchaseDetail (PurchaseID, ProductID, Quantity, UnitPrice, ReceivedQty)
                    VALUES (%s, %s, %s, %s, %s)
                """, (purchase_id, product_id, qty, unit_price, 0))

            conn.commit()

            QMessageBox.information(self, "Success", "Purchase Order saved successfully!")
            self.clear_form()

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def clear_form(self):
        self.ui.tableWidget.setRowCount(0)
        self.ui.TotalAmount_label.setText("")
        self.ui.selectsupplier_combobox.setCurrentIndex(0)
        self.set_today_date()


class ViewPOWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ViewPO()
        self.ui.setupUi(self)

        self.ui.pushButton_11.clicked.connect(self.close)
        self.load_purchase_orders()

    def showEvent(self, event):
        super().showEvent(event)
        self.load_purchase_orders()

    def load_purchase_orders(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT po.PurchaseID, s.SupplierName,
                       DATE_FORMAT(po.PurchaseDate, '%d/%m/%Y %H:%i:%s') as PurchaseDate,
                       po.TotalAmount, po.Status
                FROM PurchaseOrders po
                JOIN Suppliers s ON po.SupplierID = s.SupplierID
                ORDER BY po.PurchaseDate DESC
            """)
            orders = cursor.fetchall()

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels([
                'PO ID', 'Supplier', 'Date', 'Total Amount', 'Status'
            ])

            for row_data in orders:
                row = []
                for item in row_data:
                    cell = QStandardItem(str(item) if item else '')
                    cell.setEditable(False)
                    row.append(cell)
                model.appendRow(row)

            self.ui.viewpo_tableView.setModel(model)
            self.ui.viewpo_tableView.resizeColumnsToContents()
            self.ui.viewpo_tableView.horizontalHeader().setStretchLastSection(True)
            self.ui.viewpo_tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            self.ui.viewpo_tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))


class ViewPODetailWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_viewpurchasedetail()
        self.ui.setupUi(self)

        self.ui.pushButton_11.clicked.connect(self.close)
        self.load_purchase_details()

    def showEvent(self, event):
        super().showEvent(event)
        self.load_purchase_details()

    def load_purchase_details(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT pd.PurchaseID, p.ProductName, pd.Quantity,
                       pd.UnitPrice, pd.ReceivedQty,
                       (pd.Quantity * pd.UnitPrice) as Subtotal
                FROM PurchaseDetail pd
                JOIN Products p ON pd.ProductID = p.ProductID
                JOIN PurchaseOrders po ON pd.PurchaseID = po.PurchaseID
                ORDER BY pd.PurchaseID DESC
            """)
            details = cursor.fetchall()

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels([
                'PO ID', 'Product', 'Ordered Qty',
                'Unit Price', 'Received Qty', 'Subtotal'
            ])

            for row_data in details:
                row = []
                for item in row_data:
                    cell = QStandardItem(str(item) if item else '')
                    cell.setEditable(False)
                    row.append(cell)
                model.appendRow(row)

            self.ui.viewpurchasedetail_tableView.setModel(model)
            self.ui.viewpurchasedetail_tableView.resizeColumnsToContents()
            self.ui.viewpurchasedetail_tableView.horizontalHeader().setStretchLastSection(True)
            self.ui.viewpurchasedetail_tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            self.ui.viewpurchasedetail_tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))


class UpdateStatusWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_UpdateStatus()
        self.ui.setupUi(self)

        self.load_purchase_orders()

        self.ui.PONO_comboBox.currentIndexChanged.connect(self.show_current_status)
        self.ui.pushButton_11.clicked.connect(self.close)
        self.ui.Update_button.clicked.connect(self.cancel_order)

        self.ui.Status_comboBox.clear()
        self.ui.Status_comboBox.addItems(['Cancelled'])
        self.ui.Update_button.setText("Cancel Order")

    def load_purchase_orders(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT po.PurchaseID, s.SupplierName,
                       DATE_FORMAT(po.PurchaseDate, '%d/%m/%Y %H:%i:%s'), po.Status
                FROM PurchaseOrders po
                JOIN Suppliers s ON po.SupplierID = s.SupplierID
                WHERE po.Status = 'Pending'
                ORDER BY po.PurchaseDate DESC
            """)
            orders = cursor.fetchall()

            self.ui.PONO_comboBox.clear()
            for order in orders:
                label = f"PO#{order[0]} - {order[1]} ({order[2]})"
                self.ui.PONO_comboBox.addItem(label, order[0])

            cursor.close()
            conn.close()

            self.show_current_status()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def show_current_status(self):
        po_id = self.ui.PONO_comboBox.currentData()
        if not po_id:
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT po.Status, s.SupplierName, po.TotalAmount
                FROM PurchaseOrders po
                JOIN Suppliers s ON po.SupplierID = s.SupplierID
                WHERE po.PurchaseID = %s
            """, (po_id,))
            result = cursor.fetchone()

            if result:
                self.ui.TotalAmount_label.setText(
                    f"Status: {result[0]} | Supplier: {result[1]} | Total: Rp. {result[2]:,.2f}"
                )

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def cancel_order(self):
        po_id = self.ui.PONO_comboBox.currentData()

        if not po_id:
            QMessageBox.warning(self, "Error", "Please select a Purchase Order")
            return

        confirm = QMessageBox.question(
            self, "Confirm Cancellation",
            f"Are you sure you want to cancel PO#{po_id}?\nThis cannot be undone.",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            try:
                conn = get_connection()
                cursor = conn.cursor()

                cursor.execute("""
                    UPDATE PurchaseOrders 
                    SET Status = 'Cancelled'
                    WHERE PurchaseID = %s
                """, (po_id,))
                conn.commit()

                QMessageBox.information(self, "Success", f"PO#{po_id} has been cancelled!")
                self.load_purchase_orders()

                cursor.close()
                conn.close()

            except Exception as e:
                QMessageBox.critical(self, "Database Error", str(e))


class UpdateQtyWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_updatepoqty()
        self.ui.setupUi(self)

        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.ui.selectPO_combobox.currentIndexChanged.connect(self.load_products)
        self.ui.pushButton_11.clicked.connect(self.close)
        self.ui.saveorde_button_12.clicked.connect(self.save_qty)

        self.load_purchase_orders()

    def load_purchase_orders(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT po.PurchaseID, s.SupplierName,
                       DATE_FORMAT(po.PurchaseDate, '%d/%m/%Y %H:%i:%s')
                FROM PurchaseOrders po
                JOIN Suppliers s ON po.SupplierID = s.SupplierID
                WHERE po.Status = 'Pending'
                ORDER BY po.PurchaseDate DESC
            """)
            orders = cursor.fetchall()

            self.ui.selectPO_combobox.currentIndexChanged.disconnect(self.load_products)

            self.ui.selectPO_combobox.clear()
            for order in orders:
                label = f"PO#{order[0]} - {order[1]} ({order[2]})"
                self.ui.selectPO_combobox.addItem(label, order[0])

            self.ui.selectPO_combobox.currentIndexChanged.connect(self.load_products)

            cursor.close()
            conn.close()

            self.load_products()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def load_products(self):
        po_id = self.ui.selectPO_combobox.currentData()
        if not po_id:
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT pd.ProductID, p.ProductName, pd.Quantity, pd.ReceivedQty
                FROM PurchaseDetail pd
                JOIN Products p ON pd.ProductID = p.ProductID
                WHERE pd.PurchaseID = %s
            """, (po_id,))
            details = cursor.fetchall()

            self.ui.tableWidget.setRowCount(0)

            for row_data in details:
                row = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(row)

                product_item = QTableWidgetItem(str(row_data[1]))
                product_item.setFlags(Qt.ItemIsEnabled)
                product_item.setData(Qt.UserRole, row_data[0])
                self.ui.tableWidget.setItem(row, 0, product_item)

                ordered_item = QTableWidgetItem(str(row_data[2]))
                ordered_item.setFlags(Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(row, 1, ordered_item)

                qty_spinbox = QSpinBox()
                qty_spinbox.setMinimum(0)
                qty_spinbox.setMaximum(99999)
                qty_spinbox.setValue(row_data[3] if row_data[3] else 0)
                self.ui.tableWidget.setCellWidget(row, 2, qty_spinbox)

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def save_qty(self):
        po_id = self.ui.selectPO_combobox.currentData()

        if not po_id:
            QMessageBox.warning(self, "Error", "Please select a Purchase Order")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            for row in range(self.ui.tableWidget.rowCount()):
                product_item = self.ui.tableWidget.item(row, 0)
                qty_spinbox = self.ui.tableWidget.cellWidget(row, 2)

                product_id = product_item.data(Qt.UserRole)
                received_qty = qty_spinbox.value()

                cursor.execute("""
                    SELECT pd.UnitPrice, pd.ReceivedQty
                    FROM PurchaseDetail pd
                    WHERE pd.PurchaseID = %s AND pd.ProductID = %s
                """, (po_id, product_id))
                detail = cursor.fetchone()

                if detail:
                    old_received_qty = detail[1] if detail[1] else 0
                    qty_difference = received_qty - old_received_qty

                    cursor.execute("""
                        UPDATE PurchaseDetail 
                        SET ReceivedQty = %s
                        WHERE PurchaseID = %s AND ProductID = %s
                    """, (received_qty, po_id, product_id))

                    if qty_difference != 0:
                        cursor.execute("""
                            UPDATE Products
                            SET Quantity = Quantity + %s,
                                LastPurchasePrice = %s,
                                LastPurchaseDate = NOW()
                            WHERE ProductID = %s
                        """, (qty_difference, detail[0], product_id))

            # Auto update PO status
            cursor.execute("""
                SELECT COUNT(*) FROM PurchaseDetail
                WHERE PurchaseID = %s AND ReceivedQty < Quantity
            """, (po_id,))
            not_received = cursor.fetchone()[0]

            if not_received == 0:
                cursor.execute("""
                    UPDATE PurchaseOrders 
                    SET Status = 'Completed'
                    WHERE PurchaseID = %s
                """, (po_id,))
            else:
                cursor.execute("""
                    UPDATE PurchaseOrders 
                    SET Status = 'Pending'
                    WHERE PurchaseID = %s
                """, (po_id,))

            conn.commit()

            QMessageBox.information(self, "Success", "Received quantities updated successfully!")
            self.load_purchase_orders()

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))