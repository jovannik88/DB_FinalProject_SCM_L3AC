from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_supplier(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(686, 613)
        self.manage_supplier_button = QPushButton(Dialog)
        self.manage_supplier_button.setObjectName(u"manage_supplier_button")
        self.manage_supplier_button.setGeometry(QRect(230, 350, 211, 101))
        font = QFont()
        font.setPointSize(16)
        self.manage_supplier_button.setFont(font)
        self.pushButton_11 = QPushButton(Dialog)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(490, 520, 191, 71))
        self.pushButton_11.setFont(font)
        self.add_SupplierButton = QPushButton(Dialog)
        self.add_SupplierButton.setObjectName(u"add_SupplierButton")
        self.add_SupplierButton.setGeometry(QRect(230, 100, 211, 101))
        self.add_SupplierButton.setFont(font)
        self.Edit_supplier_button = QPushButton(Dialog)
        self.Edit_supplier_button.setObjectName(u"Edit_supplier_button")
        self.Edit_supplier_button.setGeometry(QRect(230, 220, 211, 101))
        self.Edit_supplier_button.setFont(font)
        self.label_customer = QLabel(Dialog)
        self.label_customer.setObjectName(u"label_customer")
        self.label_customer.setGeometry(QRect(260, 10, 211, 61))
        font1 = QFont()
        font1.setPointSize(28)
        self.label_customer.setFont(font1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.manage_supplier_button.setText(QCoreApplication.translate("Dialog", u"Manage Supplier", None))
        self.pushButton_11.setText(QCoreApplication.translate("Dialog", u"Back ", None))
        self.add_SupplierButton.setText(QCoreApplication.translate("Dialog", u"Add Supplier", None))
        self.Edit_supplier_button.setText(QCoreApplication.translate("Dialog", u"Edit Supplier", None))
        self.label_customer.setText(QCoreApplication.translate("Dialog", u"Supplier", None))
    # retranslateUi

