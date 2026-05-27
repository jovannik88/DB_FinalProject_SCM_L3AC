from PySide6.QtWidgets import QDialog, QMessageBox
from PurchaseOrders.po_invoice_ui import Ui_POInvoice
from db_connector import get_connection
from PurchaseOrders.invoicegenerator import generate_po_invoice

class POInvoiceWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_POInvoice()
        self.ui.setupUi(self)

        self.load_purchase_orders()

        self.ui.SelectPOcomboBox.currentIndexChanged.connect(self.show_po_info)
        self.ui.pushButton.clicked.connect(self.generate_invoice)
        self.ui.pushButton_2.clicked.connect(self.close)

    def load_purchase_orders(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Pass date format as parameter
            cursor.execute("""
                SELECT po.PurchaseID, s.SupplierName,
                       DATE_FORMAT(po.PurchaseDate, %s),
                       po.Status
                FROM PurchaseOrders po
                JOIN Suppliers s ON po.SupplierID = s.SupplierID
                ORDER BY po.PurchaseDate DESC
            """, ('%d/%m/%Y %H:%i:%s',))  # ← format as parameter
            orders = cursor.fetchall()

            self.ui.SelectPOcomboBox.clear()
            for order in orders:
                label = f"PO-{order[0]:04d} | {order[1]} | {order[2]} | {order[3]}"
                self.ui.SelectPOcomboBox.addItem(label, order[0])

            cursor.close()
            conn.close()

            self.show_po_info()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def show_po_info(self):
        po_id = self.ui.SelectPOcomboBox.currentData()
        if not po_id:
            self.ui.label_3.setText("")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Pass date format as parameter
            cursor.execute("""
                SELECT s.SupplierName, po.TotalAmount, po.Status,
                       DATE_FORMAT(po.PurchaseDate, %s),
                       COALESCE(SUM(sp.Amount), 0) as PaidAmount
                FROM PurchaseOrders po
                JOIN Suppliers s ON po.SupplierID = s.SupplierID
                LEFT JOIN SupplierPayments sp ON po.PurchaseID = sp.PurchaseID
                WHERE po.PurchaseID = %s
                GROUP BY s.SupplierName, po.TotalAmount, po.Status, po.PurchaseDate
            """, ('%d/%m/%Y %H:%i:%s', po_id))  # ← format first, then po_id
            result = cursor.fetchone()

            if result:
                remaining = float(result[1]) - float(result[4])
                self.ui.label_3.setText(
                    f"Supplier: {result[0]}  |  Date: {result[3]}  |  "
                    f"Status: {result[2]}  |  Total: Rp. {float(result[1]):,.2f}  |  "
                    f"Paid: Rp. {float(result[4]):,.2f}  |  Remaining: Rp. {remaining:,.2f}"
                )

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def generate_invoice(self):
        po_id = self.ui.SelectPOcomboBox.currentData()
        if not po_id:
            QMessageBox.warning(self, "Error", "Please select a Purchase Order")
            return

        success, result = generate_po_invoice(po_id)

        if success:
            QMessageBox.information(self, "Success", f"Invoice generated!\nSaved to:\n{result}")
        else:
            QMessageBox.critical(self, "Error", f"Failed to generate invoice:\n{result}")