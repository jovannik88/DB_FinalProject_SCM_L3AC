# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(686, 613)
        self.Dashboard_Button = QPushButton(Dialog)
        self.Dashboard_Button.setObjectName(u"Dashboard_Button")
        self.Dashboard_Button.setGeometry(QRect(20, 40, 181, 71))
        font = QFont()
        font.setPointSize(16)
        self.Dashboard_Button.setFont(font)
        self.User_button = QPushButton(Dialog)
        self.User_button.setObjectName(u"User_button")
        self.User_button.setGeometry(QRect(250, 40, 181, 71))
        self.User_button.setFont(font)
        self.product_button = QPushButton(Dialog)
        self.product_button.setObjectName(u"product_button")
        self.product_button.setGeometry(QRect(470, 40, 181, 71))
        self.product_button.setFont(font)
        self.category_button = QPushButton(Dialog)
        self.category_button.setObjectName(u"category_button")
        self.category_button.setGeometry(QRect(20, 140, 181, 71))
        self.category_button.setFont(font)
        self.supplier_button = QPushButton(Dialog)
        self.supplier_button.setObjectName(u"supplier_button")
        self.supplier_button.setGeometry(QRect(250, 140, 181, 71))
        self.supplier_button.setFont(font)
        self.customer_button = QPushButton(Dialog)
        self.customer_button.setObjectName(u"customer_button")
        self.customer_button.setGeometry(QRect(470, 140, 191, 71))
        self.customer_button.setFont(font)
        self.Sales_button = QPushButton(Dialog)
        self.Sales_button.setObjectName(u"Sales_button")
        self.Sales_button.setGeometry(QRect(10, 230, 191, 71))
        self.Sales_button.setFont(font)
        self.po_button = QPushButton(Dialog)
        self.po_button.setObjectName(u"po_button")
        self.po_button.setGeometry(QRect(240, 230, 191, 71))
        self.po_button.setFont(font)
        self.pushButton_9 = QPushButton(Dialog)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(470, 230, 191, 71))
        self.pushButton_9.setFont(font)
        self.pushButton_10 = QPushButton(Dialog)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(10, 320, 191, 71))
        self.pushButton_10.setFont(font)
        self.pushButton_11 = QPushButton(Dialog)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(490, 520, 191, 71))
        self.pushButton_11.setFont(font)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Dashboard_Button.setText(QCoreApplication.translate("Dialog", u"DashBoard", None))
        self.User_button.setText(QCoreApplication.translate("Dialog", u"Users", None))
        self.product_button.setText(QCoreApplication.translate("Dialog", u"Product", None))
        self.category_button.setText(QCoreApplication.translate("Dialog", u"Category", None))
        self.supplier_button.setText(QCoreApplication.translate("Dialog", u"Supplier", None))
        self.customer_button.setText(QCoreApplication.translate("Dialog", u"Customers", None))
        self.Sales_button.setText(QCoreApplication.translate("Dialog", u"Sales Order", None))
        self.po_button.setText(QCoreApplication.translate("Dialog", u"Purchase Order", None))
        self.pushButton_9.setText(QCoreApplication.translate("Dialog", u"Payments", None))
        self.pushButton_10.setText(QCoreApplication.translate("Dialog", u"Supplier Payment", None))
        self.pushButton_11.setText(QCoreApplication.translate("Dialog", u"Exit", None))
    # retranslateUi

