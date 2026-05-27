from PySide6.QtWidgets import QDialog
from Main_menu_ui import Ui_Dialog
from users.user import ManageUsersWindow
from categories.category import CategoryWindow
from products.product import ProductWindow
from customers.customer import CustomerWindow
from suppliers.supplier import SupplierWindow
from PurchaseOrders.purchaseorder import PurchaseOrderWindow
from SupplierPayments.supplierpayment import SupplierPaymentWindow
from SalesOrders.salesorder import SalesOrderWindow
from CustomerPayments.CustomerPayment import CustomerPaymentWindow
from dashboard import DashboardWindow

class AdminWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.pushButton_11.clicked.connect(self.close)
        self.ui.User_button.clicked.connect(self.open_manage_users)
        self.ui.category_button.clicked.connect(self.open_category_ui)
        self.ui.product_button.clicked.connect(self.open_product_ui)
        self.ui.customer_button.clicked.connect(self.open_customer_ui)
        self.ui.supplier_button.clicked.connect(self.open_supplier_ui)
        self.ui.po_button.clicked.connect(self.open_purchaseorder_ui)
        self.ui.pushButton_10.clicked.connect(self. open_supplierPayment_ui)
        self.ui.Sales_button.clicked.connect(self.open_salesorder_ui)
        self.ui.pushButton_9.clicked.connect(self.open_CustomerPayment_ui)
        self.ui.Dashboard_Button.clicked.connect(self.open_Dashboard_ui)

    def open_manage_users(self):
        self.manage_users_window = ManageUsersWindow()
        self.manage_users_window.show()

    def open_category_ui(self):
        self.category_window = CategoryWindow()
        self.category_window.show()

    def open_product_ui(self):
        self.product_window = ProductWindow()
        self.product_window.show()

    def open_customer_ui(self):
        self.customer_window = CustomerWindow()
        self.customer_window.show()
    
    def open_supplier_ui(self):
        self.supplier_window = SupplierWindow()
        self.supplier_window.show()
    
    def open_purchaseorder_ui(self):
        self.purchaseorder_window = PurchaseOrderWindow()
        self.purchaseorder_window.show()

    def open_supplierPayment_ui(self):
        self.supplierpayment_window = SupplierPaymentWindow()
        self.supplierpayment_window.show()
    
    def open_salesorder_ui(self):
        self.salesorder_window = SalesOrderWindow()
        self.salesorder_window.show()

    def open_CustomerPayment_ui(self):
        self.customerpayment_window = CustomerPaymentWindow()
        self.customerpayment_window.show()

    def open_Dashboard_ui(self):
        self.dashboard_window = DashboardWindow()
        self.dashboard_window.show()