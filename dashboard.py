from PySide6.QtWidgets import QDialog, QMessageBox, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from dashboard_ui import Ui_Dashboard
from db_connector import get_connection


class DashboardWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.close)
        self.load_dashboard()

    def showEvent(self, event):
        super().showEvent(event)
        self.load_dashboard()

    def load_dashboard(self):
        self.load_summary_cards()
        self.load_recent_sales()
        self.load_recent_purchases()
        self.load_unpaid_customers()
        self.load_unpaid_suppliers()
        self.load_low_stock()

    def setup_table(self, table_view, model):
        table_view.setModel(model)
        header = table_view.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        table_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        table_view.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

    def load_summary_cards(self):
        try:  # ← fixed indentation
            conn = get_connection()
            cursor = conn.cursor()

            # Total Sales Today
            cursor.execute("""
                SELECT COALESCE(SUM(Amount), 0)
                FROM Payments
                WHERE DATE(PaymentDate) = CURDATE()
            """)
            total_sales = float(cursor.fetchone()[0])
            self.ui.label_TotalSalesToday.setText(f"Rp. {total_sales:,.2f}")

            # Total Purchases Today
            cursor.execute("""
                SELECT COALESCE(SUM(Amount), 0)
                FROM SupplierPayments
                WHERE DATE(PaymentDate) = CURDATE()
            """)
            total_purchases = float(cursor.fetchone()[0])
            self.ui.totalPurchasetoday_label.setText(f"Rp. {total_purchases:,.2f}")

            # Gross Profit from Sales Today
            cursor.execute("""
                SELECT 
                    COALESCE(SUM(sd.Quantity * sd.UnitPrice - sd.Discount), 0) -
                    COALESCE(SUM(sd.Quantity * p.BuyingPrice), 0)
                FROM SalesDetail sd
                JOIN Products p ON sd.ProductID = p.ProductID
                JOIN SalesOrders so ON sd.SalesID = so.SalesID
                WHERE DATE(so.SalesDate) = CURDATE()
                AND so.Status != 'Cancelled'
            """)
            gross_profit = float(cursor.fetchone()[0])

            # Supplier Payments Today
            cursor.execute("""
                SELECT COALESCE(SUM(Amount), 0)
                FROM SupplierPayments
                WHERE DATE(PaymentDate) = CURDATE()
            """)
            supplier_payments_today = float(cursor.fetchone()[0])

            # Net Profit = Gross Profit - Supplier Payments Today
            net_profit = gross_profit - supplier_payments_today

            if net_profit >= 0:
                self.ui.todayprofitloss_label.setText(f"Net Profit: Rp. {net_profit:,.2f}")
                self.ui.todayprofitloss_label.setStyleSheet("color: green;")
            else:
                self.ui.todayprofitloss_label.setText(f"Net Loss: Rp. {abs(net_profit):,.2f}")
                self.ui.todayprofitloss_label.setStyleSheet("color: red;")

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def load_recent_sales(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT so.SalesID, c.CustomerName,
                       DATE_FORMAT(so.SalesDate, '%d/%m/%Y %H:%i:%s') as SalesDate,
                       so.TotalAmount, so.Status
                FROM SalesOrders so
                JOIN Customers c ON so.CustomerID = c.CustomerID
                ORDER BY so.SalesDate DESC
                LIMIT 5
            """)
            orders = cursor.fetchall()

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels([
                'SO ID', 'Customer', 'Date & Time', 'Total Amount', 'Status'
            ])

            for row_data in orders:
                row = []
                for item in row_data:
                    cell = QStandardItem(str(item) if item else '')
                    cell.setEditable(False)
                    row.append(cell)
                model.appendRow(row)

            self.setup_table(self.ui.RecentSales_Table, model)

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def load_recent_purchases(self):
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
                LIMIT 5
            """)
            orders = cursor.fetchall()

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels([
                'PO ID', 'Supplier', 'Date & Time', 'Total Amount', 'Status'
            ])

            for row_data in orders:
                row = []
                for item in row_data:
                    cell = QStandardItem(str(item) if item else '')
                    cell.setEditable(False)
                    row.append(cell)
                model.appendRow(row)

            self.setup_table(self.ui.RecentPurchase_Table_2, model)

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def load_unpaid_customers(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT 
                    so.SalesID,
                    c.CustomerName,
                    so.TotalAmount,
                    COALESCE(SUM(p.Amount), 0) as PaidAmount,
                    so.TotalAmount - COALESCE(SUM(p.Amount), 0) as RemainingAmount,
                    DATE_FORMAT(so.SalesDate, '%d/%m/%Y %H:%i:%s') as SalesDate
                FROM SalesOrders so
                JOIN Customers c ON so.CustomerID = c.CustomerID
                LEFT JOIN Payments p ON so.SalesID = p.SalesID
                WHERE so.Status != 'Cancelled'
                GROUP BY so.SalesID, c.CustomerName, so.TotalAmount, so.SalesDate
                HAVING COALESCE(SUM(p.Amount), 0) < so.TotalAmount
                ORDER BY RemainingAmount DESC
            """)
            customers = cursor.fetchall()

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels([
                'SO ID', 'Customer', 'Total Amount',
                'Paid Amount', 'Remaining Amount', 'Date & Time'
            ])

            for row_data in customers:
                row = []
                for item in row_data:
                    cell = QStandardItem(str(item) if item else '')
                    cell.setEditable(False)
                    row.append(cell)
                model.appendRow(row)

            self.setup_table(self.ui.unpaidcustomertableview, model)

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def load_unpaid_suppliers(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT 
                    po.PurchaseID,
                    s.SupplierName,
                    po.TotalAmount,
                    COALESCE(SUM(sp.Amount), 0) as PaidAmount,
                    po.TotalAmount - COALESCE(SUM(sp.Amount), 0) as RemainingAmount,
                    DATE_FORMAT(po.PurchaseDate, '%d/%m/%Y %H:%i:%s') as PurchaseDate
                FROM PurchaseOrders po
                JOIN Suppliers s ON po.SupplierID = s.SupplierID
                LEFT JOIN SupplierPayments sp ON po.PurchaseID = sp.PurchaseID
                WHERE po.Status != 'Cancelled'
                GROUP BY po.PurchaseID, s.SupplierName, po.TotalAmount, po.PurchaseDate
                HAVING COALESCE(SUM(sp.Amount), 0) < po.TotalAmount
                ORDER BY RemainingAmount DESC
            """)
            suppliers = cursor.fetchall()

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels([
                'PO ID', 'Supplier', 'Total Amount',
                'Paid Amount', 'Remaining Amount', 'Date & Time'
            ])

            for row_data in suppliers:
                row = []
                for item in row_data:
                    cell = QStandardItem(str(item) if item else '')
                    cell.setEditable(False)
                    row.append(cell)
                model.appendRow(row)

            self.setup_table(self.ui.unpaidsuppliertableview_2, model)

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def load_low_stock(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT p.ProductID, p.ProductName, c.CategoryName,
                       p.Quantity, p.MeasurementUnits,
                       DATE_FORMAT(p.LastUpdated, '%d/%m/%Y %H:%i:%s') as LastUpdated
                FROM Products p
                JOIN Categories c ON p.CategoryID = c.CategoryID
                WHERE p.Quantity < 10
                ORDER BY p.Quantity ASC
            """)
            products = cursor.fetchall()

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels([
                'ID', 'Product Name', 'Category',
                'Stock', 'Unit', 'Last Updated'
            ])

            for row_data in products:
                row = []
                for item in row_data:
                    cell = QStandardItem(str(item) if item else '')
                    cell.setEditable(False)
                    row.append(cell)
                model.appendRow(row)

            self.setup_table(self.ui.lowstocktableview_3, model)

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))