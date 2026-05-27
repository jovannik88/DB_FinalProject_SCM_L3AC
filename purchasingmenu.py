from PySide6.QtWidgets import QDialog
from purchasingmenu_ui import Ui_purchasingmenu
from products.product import ProductWindow
from categories.category import CategoryWindow
from suppliers.supplier import SupplierWindow
from PurchaseOrders.purchaseorder import PurchaseOrderWindow
from SupplierPayments.supplierpayment import SupplierPaymentWindow

class PurchasingWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_purchasingmenu()
        self.ui.setupUi(self)

        self.ui.pushButton_11.clicked.connect(self.close)
        self.ui.product_button.clicked.connect(self.open_product)
        self.ui.category_button.clicked.connect(self.open_category)
        self.ui.supplier_button.clicked.connect(self.open_supplier)
        self.ui.Sales_button.clicked.connect(self.open_po)
        self.ui.supplierpaymentbutton.clicked.connect(self.open_supplier_payment)

    def open_product(self):
        self.product_window = ProductWindow()
        self.product_window.show()

    def open_category(self):
        self.category_window = CategoryWindow()
        self.category_window.show()

    def open_supplier(self):
        self.supplier_window = SupplierWindow()
        self.supplier_window.show()

    def open_po(self):
        self.po_window = PurchaseOrderWindow()
        self.po_window.show()

    def open_supplier_payment(self):
        self.supplier_payment_window = SupplierPaymentWindow()
        self.supplier_payment_window.show()