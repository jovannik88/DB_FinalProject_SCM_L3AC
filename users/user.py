from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem
#For User menu UI
from users.user_ui import Ui_ManageUsers
#for add user
from users.User_add_ui import Ui_add_user
#for edit user
from users.user_edit_ui import Ui_User_edit
#for view user
from users.user_view_ui import Ui_userview
#for Delete User
from users.user_delete_ui import Ui_User_Deletee

from db_connector import get_connection

#User Ui functionality
class ManageUsersWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ManageUsers()
        self.ui.setupUi(self)

        self.ui.pushButton_11.clicked.connect(self.close)
        self.ui.Add_user_Button.clicked.connect(self.add_user)
        self.ui.Edit_User_button.clicked.connect(self.edit_user)
        self.ui.Delete_users_button.clicked.connect(self.delete_user)
        self.ui.Registered_users_button.clicked.connect(self.view_users)

    def add_user(self):
        self.add_user_window = AddUserWindow()
        self.add_user_window.show()

    def edit_user(self):
        self.edit_user_window = EditUserWindow()
        self.edit_user_window.show()

    def delete_user(self):
        self.edit_user_window = DeleteUserWindow()
        self.edit_user_window.show()

    def view_users(self):
        self.edit_user_window = ViewUsersWindow()
        self.edit_user_window.show()

#Add User Code
class AddUserWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_add_user()
        self.ui.setupUi(self)

        # Load roles from database into combobox
        self.load_roles()

        # Connect buttons
        self.ui.save_button.clicked.connect(self.save_user)
        self.ui.Back_button.clicked.connect(self.close)

    def load_roles(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT RoleID, RoleName FROM Roles")
            roles = cursor.fetchall()

            for role in roles:
                self.ui.roles_combobox.addItem(role[1], role[0])  # display name, store ID

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def save_user(self):
        username = self.ui.username_textarea.text()
        password = self.ui.password_textareea.text()
        role_id = self.ui.roles_combobox.currentData()  # gets the RoleID

        # Validate fields
        if not username:
            QMessageBox.warning(self, "Error", "Username is required")
            return
        if not password:
            QMessageBox.warning(self, "Error", "Password is required")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Check if username already exists
            cursor.execute("SELECT UserID FROM Users WHERE Username = %s", (username,))
            if cursor.fetchone():
                QMessageBox.warning(self, "Error", "Username already exists")
                return

            query = """
                INSERT INTO Users (Username, Password, RoleID, CreatedAt)
                VALUES (%s, %s, %s, NOW())
            """
            cursor.execute(query, (username, password, role_id))
            conn.commit()

            QMessageBox.information(self, "Success", "User added successfully!")
            self.clear_fields()

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def clear_fields(self):
        self.ui.username_textarea.clear()
        self.ui.password_textareea.clear()
        self.ui.roles_combobox.setCurrentIndex(0)

#Edit User
class EditUserWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_User_edit()
        self.ui.setupUi(self)

        # Load users and roles when form opens
        self.load_users()
        self.load_roles()

        # When user selects a different user, auto fill fields
        self.ui.Selectuser_combobox.currentIndexChanged.connect(self.fill_user_data)

        # Connect buttons
        self.ui.edituser_button.clicked.connect(self.save_edit)
        self.ui.Back_button.clicked.connect(self.close)

    def load_users(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT UserID, Username FROM Users")
            users = cursor.fetchall()

            self.ui.Selectuser_combobox.clear()
            for user in users:
                self.ui.Selectuser_combobox.addItem(user[1], user[0])  # display username, store UserID

            cursor.close()
            conn.close()

            # Fill data for first user
            self.fill_user_data()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def load_roles(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT RoleID, RoleName FROM Roles")
            roles = cursor.fetchall()

            self.ui.roles_combobox.clear()
            for role in roles:
                self.ui.roles_combobox.addItem(role[1], role[0])

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def fill_user_data(self):
        user_id = self.ui.Selectuser_combobox.currentData()
        if not user_id:
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT Username, Password, RoleID FROM Users WHERE UserID = %s", (user_id,))
            user = cursor.fetchone()

            if user:
                self.ui.username_textarea.setText(user[0])
                self.ui.password_textareea.setText(user[1])

                # Set the correct role in combobox
                index = self.ui.roles_combobox.findData(user[2])
                if index >= 0:
                    self.ui.roles_combobox.setCurrentIndex(index)

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def save_edit(self):
        user_id = self.ui.Selectuser_combobox.currentData()
        username = self.ui.username_textarea.text()
        password = self.ui.password_textareea.text()
        role_id = self.ui.roles_combobox.currentData()

        if not username:
            QMessageBox.warning(self, "Error", "Username is required")
            return
        if not password:
            QMessageBox.warning(self, "Error", "Password is required")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
                UPDATE Users 
                SET Username = %s, Password = %s, RoleID = %s
                WHERE UserID = %s
            """
            cursor.execute(query, (username, password, role_id, user_id))
            conn.commit()

            QMessageBox.information(self, "Success", "User updated successfully!")

            # Reload users in case username changed
            self.load_users()

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

#View User Functionality
class ViewUsersWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_userview()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.Back_button.clicked.connect(self.close)

        # Load users when form opens
        self.load_users()

    def load_users(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
                SELECT Users.UserID, Users.Username, Roles.RoleName, Users.CreatedAt
                FROM Users
                JOIN Roles ON Users.RoleID = Roles.RoleID
            """
            cursor.execute(query)
            users = cursor.fetchall()

            # Set up table model
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(['UserID', 'Username', 'Role', 'Created At'])

            for row_data in users:
                row = []
                for item in row_data:
                    cell = QStandardItem(str(item) if item else '')
                    cell.setEditable(False)  # make cells read only
                    row.append(cell)
                model.appendRow(row)

            self.ui.View_user.setModel(model)

            # Stretch columns to fit the table width
            self.ui.View_user.horizontalHeader().setStretchLastSection(True)

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

#Delete User
class DeleteUserWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_User_Deletee()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.Back_button.clicked.connect(self.close)
        self.ui.delete_button.clicked.connect(self.delete_user)

        # Load data when form opens
        self.load_users_table()
        self.load_users_combobox()

    def load_users_table(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
                SELECT Users.UserID, Users.Username, Roles.RoleName, Users.CreatedAt
                FROM Users
                JOIN Roles ON Users.RoleID = Roles.RoleID
            """
            cursor.execute(query)
            users = cursor.fetchall()

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(['UserID', 'Username', 'Role', 'Created At'])

            for row_data in users:
                row = []
                for item in row_data:
                    cell = QStandardItem(str(item) if item else '')
                    cell.setEditable(False)
                    row.append(cell)
                model.appendRow(row)

            self.ui.View_user.setModel(model)
            self.ui.View_user.horizontalHeader().setStretchLastSection(True)

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def load_users_combobox(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT UserID, Username FROM Users")
            users = cursor.fetchall()

            self.ui.comboBox_ID.clear()
            for user in users:
                self.ui.comboBox_ID.addItem(user[1], user[0])  # display username, store UserID

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def delete_user(self):
        user_id = self.ui.comboBox_ID.currentData()
        username = self.ui.comboBox_ID.currentText()

        # Confirm before deleting
        confirm = QMessageBox.question(
            self, "Confirm Delete",
            f"Are you sure you want to delete user '{username}'?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            try:
                conn = get_connection()
                cursor = conn.cursor()

                cursor.execute("DELETE FROM Users WHERE UserID = %s", (user_id,))
                conn.commit()

                QMessageBox.information(self, "Success", f"User '{username}' deleted successfully!")

                # Refresh table and combobox
                self.load_users_table()
                self.load_users_combobox()

                cursor.close()
                conn.close()

            except Exception as e:
                QMessageBox.critical(self, "Database Error", str(e))



