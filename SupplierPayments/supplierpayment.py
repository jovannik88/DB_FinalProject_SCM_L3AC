from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QDate, Qt
from db_connector import get_connection

from SupplierPayments.supplierpayment_ui import Ui_SupplierPayment
from SupplierPayments.record_supplyerpayment_ui import Ui_recordsupplierpayment
from SupplierPayments.view_supplierpayment_ui import Ui_view_supplierPayment


class SupplierPaymentWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SupplierPayment()
        self.ui.setupUi(self)
        
        self.ui.pushButton_11.clicked.connect(self.close)
        self.ui.Record_Payment_button.clicked.connect(self.create_New_SupplierPayment_ui)
        self.ui.view_payment_Button.clicked.connect(self.view_SupplierPayment_ui)

    def create_New_SupplierPayment_ui(self):
        self.recordsupplierpayment_window = RecordSupplierPaymentWindow()
        self.recordsupplierpayment_window.show()

    def view_SupplierPayment_ui(self):
        self.viewsupplierpayment_window = ViewSupplierPaymentWindow()
        self.viewsupplierpayment_window.show()

#Record Supplier Payment
class RecordSupplierPaymentWindow(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_recordsupplierpayment()
        self.ui.setupUi(self)

        self.supplier_id = None
        self.po_total = 0.0

        self.load_purchase_orders()
        self.load_payment_methods()
        self.set_today_date()

        self.ui.selectPO_combobox.currentIndexChanged.connect(self.fill_po_data)
        self.ui.pushButton_11.clicked.connect(self.close)
        self.ui.savePayment_button_12.clicked.connect(self.save_payment)

    def load_purchase_orders(self):

        try:
            conn = get_connection()
            cursor = conn.cursor()


        # Only load POs that are not fully paid
            cursor.execute("""
                           
                            SELECT po.PurchaseID, s.SupplierName, po.TotalAmount,
                            COALESCE(SUM(sp.Amount), 0) as TotalPaid
                            FROM PurchaseOrders po
                            JOIN Suppliers s ON po.SupplierID = s.SupplierID
                            LEFT JOIN SupplierPayments sp ON po.PurchaseID = sp.PurchaseID
                            GROUP BY po.PurchaseID, s.SupplierName, po.TotalAmount
                            HAVING COALESCE(SUM(sp.Amount), 0) < po.TotalAmount
                            ORDER BY po.PurchaseDate DESC
                            """)
            
            orders = cursor.fetchall()


            self.ui.selectPO_combobox.clear()
            for order in orders:
                label = f"PO#{order[0]} - {order[1]}"
                self.ui.selectPO_combobox.addItem(label, order[0])

            cursor.close()
            conn.close()

            self.fill_po_data()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def fill_po_data(self):
        po_id = self.ui.selectPO_combobox.currentData()
        if not po_id:
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT s.SupplierName, po.TotalAmount, po.SupplierID
                FROM PurchaseOrders po
                JOIN Suppliers s ON po.SupplierID = s.SupplierID
                WHERE po.PurchaseID = %s
            """, (po_id,))
            result = cursor.fetchone()

            if result:
                self.supplier_id = result[2]
                self.po_total = float(result[1])

                # Get total already paid for this PO
                cursor.execute("""
                    SELECT COALESCE(SUM(Amount), 0)
                    FROM SupplierPayments
                    WHERE PurchaseID = %s
                """, (po_id,))
                paid = cursor.fetchone()
                already_paid = float(paid[0]) if paid else 0.0
                remaining = self.po_total - already_paid

                self.ui.supplier_label.setText(str(result[0]))
                self.ui.total_amount_label.setText(
                    f"Rp. {self.po_total:,.2f} | Paid: Rp. {already_paid:,.2f} | Remaining: Rp. {remaining:,.2f}"
                )

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def load_payment_methods(self):
        self.ui.Paymentmethod_combobox_2.clear()
        self.ui.Paymentmethod_combobox_2.addItems(['Cash', 'Transfer', 'Cheque'])

    def set_today_date(self):
        self.ui.dateEdit.setDate(QDate.currentDate())

    def save_payment(self):
        po_id = self.ui.selectPO_combobox.currentData()
        amount_text = self.ui.lineEdit.text()
        payment_method = self.ui.Paymentmethod_combobox_2.currentText()

        if not po_id:
            QMessageBox.warning(self, "Error", "Please select a Purchase Order")
            return
        if not amount_text:
            QMessageBox.warning(self, "Error", "Please enter payment amount")
            return

        try:
            amount = float(amount_text)
        except ValueError:
            QMessageBox.warning(self, "Error", "Amount must be a number")
            return

        if amount <= 0:
            QMessageBox.warning(self, "Error", "Amount must be greater than 0")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Get total already paid
            cursor.execute("""
                SELECT COALESCE(SUM(Amount), 0)
                FROM SupplierPayments
                WHERE PurchaseID = %s
            """, (po_id,))
            paid = cursor.fetchone()
            already_paid = float(paid[0]) if paid else 0.0
            total_paid = already_paid + amount

            # Auto determine status
            if total_paid >= self.po_total:
                status = 'Paid'
            else:
                status = 'Partial'

            # Save payment with NOW() for exact time
            cursor.execute("""
                INSERT INTO SupplierPayments 
                (PurchaseID, SupplierID, PaymentDate, Amount, PaymentMethod, Status)
                VALUES (%s, %s, NOW(), %s, %s, %s)
            """, (po_id, self.supplier_id, amount, payment_method, status))

            conn.commit()

            QMessageBox.information(
                self, "Success",
                f"Payment recorded!\nStatus: {status}\nTotal Paid: Rp. {total_paid:,.2f}"
            )

            self.clear_fields()
            self.load_purchase_orders()

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def clear_fields(self):
        self.ui.lineEdit.clear()
        self.ui.selectPO_combobox.setCurrentIndex(0)
        self.ui.Paymentmethod_combobox_2.setCurrentIndex(0)
        self.set_today_date()

#View Supplier Payment
class ViewSupplierPaymentWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_view_supplierPayment()
        self.ui.setupUi(self)

        self.ui.pushButton_11.clicked.connect(self.close)
        self.load_payments()

    def showEvent(self, event):
        super().showEvent(event)
        self.load_payments()

    def load_payments(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT sp.SupplierPaymentsID, po.PurchaseID, s.SupplierName,
                       sp.PaymentDate, sp.Amount, sp.PaymentMethod, sp.Status
                FROM SupplierPayments sp
                JOIN PurchaseOrders po ON sp.PurchaseID = po.PurchaseID
                JOIN Suppliers s ON sp.SupplierID = s.SupplierID
                ORDER BY sp.PaymentDate DESC
            """)
            payments = cursor.fetchall()

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels([
                'Payment ID', 'PO ID', 'Supplier',
                'Payment Date', 'Amount', 'Payment Method', 'Status'
            ])

            for row_data in payments:
                row = []
                for item in row_data:
                    cell = QStandardItem(str(item) if item else '')
                    cell.setEditable(False)
                    row.append(cell)
                model.appendRow(row)

            self.ui.viewsupplyerpayment_tableView.setModel(model)
            self.ui.viewsupplyerpayment_tableView.resizeColumnsToContents()
            self.ui.viewsupplyerpayment_tableView.horizontalHeader().setStretchLastSection(True)
            self.ui.viewsupplyerpayment_tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            self.ui.viewsupplyerpayment_tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))
