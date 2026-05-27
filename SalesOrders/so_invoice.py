from PySide6.QtWidgets import QDialog, QMessageBox
from SalesOrders.so_invoice_ui import Ui_SOInvoice
from db_connector import get_connection
from SalesOrders.invoicegenerator import generate_so_invoice

class SOInvoiceWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SOInvoice()
        self.ui.setupUi(self)

        self.load_sales_orders()

        self.ui.SelectPOcomboBox.currentIndexChanged.connect(self.show_so_info)
        self.ui.pushButton.clicked.connect(self.generate_invoice)
        self.ui.pushButton_2.clicked.connect(self.close)

    def load_sales_orders(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT so.SalesID, c.CustomerName,
                       DATE_FORMAT(so.SalesDate, %s),
                       so.Status
                FROM SalesOrders so
                JOIN Customers c ON so.CustomerID = c.CustomerID
                WHERE so.Status != 'Cancelled'
                ORDER BY so.SalesDate DESC
            """, ('%d/%m/%Y %H:%i:%s',))
            orders = cursor.fetchall()

            self.ui.SelectPOcomboBox.clear()
            for order in orders:
                label = f"SO-{order[0]:04d} | {order[1]} | {order[2]} | {order[3]}"
                self.ui.SelectPOcomboBox.addItem(label, order[0])

            cursor.close()
            conn.close()

            self.show_so_info()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def show_so_info(self):
        so_id = self.ui.SelectPOcomboBox.currentData()
        if not so_id:
            self.ui.label_3.setText("")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT c.CustomerName, so.TotalAmount, so.Status,
                       DATE_FORMAT(so.SalesDate, %s),
                       COALESCE(SUM(p.Amount), 0) as PaidAmount
                FROM SalesOrders so
                JOIN Customers c ON so.CustomerID = c.CustomerID
                LEFT JOIN Payments p ON so.SalesID = p.SalesID
                WHERE so.SalesID = %s
                GROUP BY c.CustomerName, so.TotalAmount, so.Status, so.SalesDate
            """, ('%d/%m/%Y %H:%i:%s', so_id))
            result = cursor.fetchone()

            if result:
                remaining = float(result[1]) - float(result[4])
                self.ui.label_3.setText(
                    f"Customer: {result[0]}  |  Date: {result[3]}  |  "
                    f"Status: {result[2]}  |  Total: Rp. {float(result[1]):,.2f}  |  "
                    f"Paid: Rp. {float(result[4]):,.2f}  |  Remaining: Rp. {remaining:,.2f}"
                )

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def generate_invoice(self):
        so_id = self.ui.SelectPOcomboBox.currentData()
        if not so_id:
            QMessageBox.warning(self, "Error", "Please select a Sales Order")
            return

        success, result = generate_so_invoice(so_id)

        if success:
            QMessageBox.information(self, "Success", f"Invoice generated!\nSaved to:\n{result}")
        else:
            QMessageBox.critical(self, "Error", f"Failed to generate invoice:\n{result}")