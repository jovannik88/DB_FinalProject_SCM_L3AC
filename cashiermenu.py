from PySide6.QtWidgets import QDialog
from cashiermenu_ui import Ui_CashierMenu
from SalesOrders.salesorder import SalesOrderWindow
from CustomerPayments.CustomerPayment import CustomerPaymentWindow
from customers.customer import CustomerWindow

class CashierWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CashierMenu()
        self.ui.setupUi(self)

        self.ui.pushButton_11.clicked.connect(self.close)
        self.ui.So_button.clicked.connect(self.open_sales)
        self.ui.payment_button.clicked.connect(self.open_payment)
        self.ui.payment_button_2.clicked.connect(self.open_customers)

    def open_sales(self):
        self.sales_window = SalesOrderWindow()
        self.sales_window.show()

    def open_payment(self):
        self.payment_window = CustomerPaymentWindow()
        self.payment_window.show()

    def open_customers(self):
        self.customer_window = CustomerWindow()
        self.customer_window.show()