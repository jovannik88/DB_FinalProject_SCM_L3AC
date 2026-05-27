from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QDate, Qt
from db_connector import get_connection


from CustomerPayments.CustomerPayment_ui import Ui_CustomerPayment
from CustomerPayments.record_SOpayment_ui import Ui_RecordSoPayment
from CustomerPayments.view_customerpayment_ui import Ui_viewcustomerpayment

class CustomerPaymentWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui =  Ui_CustomerPayment()
        self.ui.setupUi(self)
        
        self.ui.pushButton_11.clicked.connect(self.close)
        self.ui.Record_Payment_button.clicked.connect(self.create_New_CustomerPayment_ui)
        self.ui.view_payment_Button.clicked.connect(self.view_CustomerPayment_ui)

    def create_New_CustomerPayment_ui(self):
        self.createcustomerpayment_window = RecordSOPaymentWindow()
        self.createcustomerpayment_window.show()
    def view_CustomerPayment_ui(self):
        self.viewcustomerpayment_window = ViewCustomerPaymentWindow()
        self.viewcustomerpayment_window.show()

#Record CustomerPayment
class RecordSOPaymentWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RecordSoPayment()
        self.ui.setupUi(self)

        self.customer_id = None
        self.so_total = 0.0

        self.load_sales_orders()
        self.load_payment_methods()
        self.set_today_date()

        self.ui.selectSO_combobox.currentIndexChanged.connect(self.fill_so_data)
        self.ui.pushButton_11.clicked.connect(self.close)
        self.ui.savePayment_button_12.clicked.connect(self.save_payment)

    def load_sales_orders(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Only show orders that are not fully paid
            cursor.execute("""
                SELECT so.SalesID, c.CustomerName, so.TotalAmount,
                       COALESCE(SUM(p.Amount), 0) as TotalPaid
                FROM SalesOrders so
                JOIN Customers c ON so.CustomerID = c.CustomerID
                LEFT JOIN Payments p ON so.SalesID = p.SalesID
                WHERE so.Status != 'Cancelled'
                GROUP BY so.SalesID, c.CustomerName, so.TotalAmount
                HAVING COALESCE(SUM(p.Amount), 0) < so.TotalAmount
                ORDER BY so.SalesDate DESC
            """)
            orders = cursor.fetchall()

            self.ui.selectSO_combobox.clear()
            for order in orders:
                label = f"SO#{order[0]} - {order[1]}"
                self.ui.selectSO_combobox.addItem(label, order[0])

            cursor.close()
            conn.close()

            self.fill_so_data()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def fill_so_data(self):
        so_id = self.ui.selectSO_combobox.currentData()
        if not so_id:
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT c.CustomerName, so.TotalAmount, so.CustomerID
                FROM SalesOrders so
                JOIN Customers c ON so.CustomerID = c.CustomerID
                WHERE so.SalesID = %s
            """, (so_id,))
            result = cursor.fetchone()

            if result:
                self.customer_id = result[2]
                self.so_total = float(result[1])

                # Get total already paid
                cursor.execute("""
                    SELECT COALESCE(SUM(Amount), 0)
                    FROM Payments
                    WHERE SalesID = %s
                """, (so_id,))
                paid = cursor.fetchone()
                already_paid = float(paid[0]) if paid else 0.0
                remaining = self.so_total - already_paid

                self.ui.customer_label.setText(str(result[0]))
                self.ui.total_amount_label.setText(
                    f"Rp. {self.so_total:,.2f} | Paid: Rp. {already_paid:,.2f} | Remaining: Rp. {remaining:,.2f}"
                )

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def load_payment_methods(self):
        self.ui.Paymentmethod_combobox_2.clear()
        self.ui.Paymentmethod_combobox_2.addItems(['Cash', 'Transfer', 'Cheque'])

    def set_today_date(self):
        self.ui.dateEdit.setDisplayFormat("dd/MM/yyyy")
        self.ui.dateEdit.setDate(QDate.currentDate())

    def save_payment(self):
        so_id = self.ui.selectSO_combobox.currentData()
        amount_text = self.ui.Amount_Payment_textedit.text()
        payment_method = self.ui.Paymentmethod_combobox_2.currentText()

        if not so_id:
            QMessageBox.warning(self, "Error", "Please select a Sales Order")
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
                FROM Payments
                WHERE SalesID = %s
            """, (so_id,))
            paid = cursor.fetchone()
            already_paid = float(paid[0]) if paid else 0.0
            total_paid = already_paid + amount

            # Auto determine status
            if total_paid >= self.so_total:
                status = 'Paid'
            else:
                status = 'Partial'

            # Save payment with NOW() for exact time
            cursor.execute("""
                INSERT INTO Payments 
                (SalesID, PaymentDate, Amount, PaymentMethod, Status)
                VALUES (%s, NOW(), %s, %s, %s)
            """, (so_id, amount, payment_method, status))

            # Update SO status if fully paid
            if total_paid >= self.so_total:
                cursor.execute("""
                    UPDATE SalesOrders 
                    SET Status = 'Completed'
                    WHERE SalesID = %s
                """, (so_id,))

            conn.commit()

            QMessageBox.information(
                self, "Success",
                f"Payment recorded!\nStatus: {status}\nTotal Paid: Rp. {total_paid:,.2f}"
            )

            self.clear_fields()
            self.load_sales_orders()

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def clear_fields(self):
        self.ui.Amount_Payment_textedit.clear()
        self.ui.selectSO_combobox.setCurrentIndex(0)
        self.ui.Paymentmethod_combobox_2.setCurrentIndex(0)
        self.set_today_date()

#View Customer Payment
class ViewCustomerPaymentWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_viewcustomerpayment()
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
                SELECT p.PaymentID, so.SalesID, c.CustomerName,
                       p.PaymentDate, p.Amount, p.PaymentMethod, p.Status
                FROM Payments p
                JOIN SalesOrders so ON p.SalesID = so.SalesID
                JOIN Customers c ON so.CustomerID = c.CustomerID
                ORDER BY p.PaymentDate DESC
            """)
            payments = cursor.fetchall()

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels([
                'Payment ID', 'SO ID', 'Customer',
                'Payment Date', 'Amount', 'Payment Method', 'Status'
            ])

            for row_data in payments:
                row = []
                for item in row_data:
                    cell = QStandardItem(str(item) if item else '')
                    cell.setEditable(False)
                    row.append(cell)
                model.appendRow(row)

            self.ui.viewCustomerpayment_tableView.setModel(model)
            self.ui.viewCustomerpayment_tableView.resizeColumnsToContents()
            self.ui.viewCustomerpayment_tableView.horizontalHeader().setStretchLastSection(True)
            self.ui.viewCustomerpayment_tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            self.ui.viewCustomerpayment_tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))
