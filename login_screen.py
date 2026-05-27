from PySide6.QtWidgets import QDialog, QMessageBox
from login_screenUI import Ui_welcome
from db_connector import get_connection

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_welcome()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.ui.Textarea_username.text()
        password = self.ui.textarea_password.text()

        if not username or not password:
            QMessageBox.warning(self, "Error", "Please enter username and password")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
                SELECT Users.UserID, Users.Username, Roles.RoleName 
                FROM Users 
                JOIN Roles ON Users.RoleID = Roles.RoleID
                WHERE Users.Username = %s AND Users.Password = %s
            """
            cursor.execute(query, (username, password))
            user = cursor.fetchone()

            if user:
                user_id, username, role = user
                self.open_dashboard(role)
            else:
                QMessageBox.warning(self, "Error", "Invalid username or password")

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def open_dashboard(self, role):
        from Main_menu import AdminWindow
        from purchasingmenu import PurchasingWindow
        from cashiermenu import CashierWindow

        if role == "Admin":
            self.window = AdminWindow()
        elif role == "Purchasing":
            self.window = PurchasingWindow()
        elif role == "Cashier":
            self.window = CashierWindow()
        else:
            QMessageBox.warning(self, "Error", f"Unknown role: {role}")
            return

        self.window.show()
        self.close()