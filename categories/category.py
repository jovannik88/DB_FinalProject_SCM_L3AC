from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem

#add Category
from categories.add_category_ui import Ui_Catt
#edit category
from categories.edit_category_ui import Ui_editcatt
#Manage Category
from categories.manage_category_ui import Ui_ManageCatt
#Category UI
from categories.ui_category import Ui_Categoryy


from db_connector import get_connection


class CategoryWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Categoryy()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.pushButton_11.clicked.connect(self.close)
        self.ui.add_category_button.clicked.connect(self.add_category)
        self.ui.Edit_category_button.clicked.connect(self.edit_category)
        self.ui.View_Category_Button.clicked.connect(self.manage_category)

    def add_category(self):
        self.add_category_window = AddCategoryWindow()
        self.add_category_window.show()

    def edit_category(self):
        self.add_category_window = EditCategoryWindow()
        self.add_category_window.show()
        

    def manage_category(self):
        self.add_category_window = ViewCategoryWindow()
        self.add_category_window.show()


#Add Category
class AddCategoryWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Catt()
        self.ui.setupUi(self)
        self.ui.save_button.clicked.connect(self.save_category)
        self.ui.Back_button.clicked.connect(self.close)

    def save_category(self):
        category_name = self.ui.username_textarea.text()

        if not category_name:
            QMessageBox.warning(self, "Error", "Category name is required")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Check Existed Category
            cursor.execute("SELECT CategoryID FROM Categories WHERE CategoryName = %s", (category_name,))
            if cursor.fetchone():
                QMessageBox.warning(self, "Error", "Category already exists")
                return

            cursor.execute("INSERT INTO Categories (CategoryName) VALUES (%s)", (category_name,))
            conn.commit()

            QMessageBox.information(self, "Success", "Category added successfully!")
            self.ui.username_textarea.clear()

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

#Edit Category
class EditCategoryWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_editcatt()
        self.ui.setupUi(self)

        # Load categories when form opens
        self.load_categories()

        # Autofill Category Data
        self.ui.Selectuser_combobox.currentIndexChanged.connect(self.fill_category_data)

        self.ui.edituser_button.clicked.connect(self.save_edit)
        self.ui.Back_button.clicked.connect(self.close)

    def load_categories(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT CategoryID, CategoryName FROM Categories")
            categories = cursor.fetchall()

            self.ui.Selectuser_combobox.clear()
            for category in categories:
                self.ui.Selectuser_combobox.addItem(category[1], category[0])

            cursor.close()
            conn.close()

            # Fill data for first category
            self.fill_category_data()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def fill_category_data(self):
        category_id = self.ui.Selectuser_combobox.currentData()
        if not category_id:
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT CategoryName FROM Categories WHERE CategoryID = %s", (category_id,))
            category = cursor.fetchone()

            if category:
                self.ui.username_textarea.setText(category[0])

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def save_edit(self):
        category_id = self.ui.Selectuser_combobox.currentData()
        category_name = self.ui.username_textarea.text()

        if not category_name:
            QMessageBox.warning(self, "Error", "Category name is required")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE Categories 
                SET CategoryName = %s 
                WHERE CategoryID = %s
            """, (category_name, category_id))
            conn.commit()

            QMessageBox.information(self, "Success", "Category updated successfully!")

            # Reload categories in case name changed
            self.load_categories()

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

#Manage Category
class ViewCategoryWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ManageCatt()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.Back_button.clicked.connect(self.close)
        self.ui.delete_button.clicked.connect(self.delete_category)

        # Load data when form opens
        self.load_categories_table()
        self.load_categories_combobox()

    def load_categories_table(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT CategoryID, CategoryName FROM Categories")
            categories = cursor.fetchall()

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(['CategoryID', 'CategoryName'])

            for row_data in categories:
                row = []
                for item in row_data:
                    cell = QStandardItem(str(item) if item else '')
                    cell.setEditable(False)
                    row.append(cell)
                model.appendRow(row)

            self.ui.View_category.setModel(model)
            self.ui.View_category.horizontalHeader().setStretchLastSection(True)

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def load_categories_combobox(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT CategoryID, CategoryName FROM Categories")
            categories = cursor.fetchall()

            self.ui.comboBox_ID.clear()
            for category in categories:
                self.ui.comboBox_ID.addItem(category[1], category[0])

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def delete_category(self):
        category_id = self.ui.comboBox_ID.currentData()
        category_name = self.ui.comboBox_ID.currentText()

        confirm = QMessageBox.question(
            self, "Confirm Delete",
            f"Are you sure you want to delete category '{category_name}'?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            try:
                conn = get_connection()
                cursor = conn.cursor()

                cursor.execute("DELETE FROM Categories WHERE CategoryID = %s", (category_id,))
                conn.commit()

                QMessageBox.information(self, "Success", f"Category '{category_name}' deleted successfully!")

                # Refresh table and combobox
                self.load_categories_table()
                self.load_categories_combobox()

                cursor.close()
                conn.close()

            except Exception as e:
                QMessageBox.critical(self, "Database Error", str(e))
