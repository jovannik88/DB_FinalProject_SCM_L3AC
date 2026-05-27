# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editproduct.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_EditProduct(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(753, 814)
        self.save_button = QPushButton(Dialog)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(0, 640, 181, 71))
        font = QFont()
        font.setPointSize(16)
        self.save_button.setFont(font)
        self.Back_button = QPushButton(Dialog)
        self.Back_button.setObjectName(u"Back_button")
        self.Back_button.setGeometry(QRect(520, 670, 191, 71))
        self.Back_button.setFont(font)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 10, 151, 51))
        font1 = QFont()
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.ProductName_label = QLabel(Dialog)
        self.ProductName_label.setObjectName(u"ProductName_label")
        self.ProductName_label.setGeometry(QRect(0, 100, 141, 51))
        self.ProductName_label.setFont(font)
        self.password_label = QLabel(Dialog)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(0, 170, 151, 51))
        self.password_label.setFont(font)
        self.productname_textarea = QLineEdit(Dialog)
        self.productname_textarea.setObjectName(u"productname_textarea")
        self.productname_textarea.setGeometry(QRect(170, 110, 401, 41))
        self.Description_textareea = QLineEdit(Dialog)
        self.Description_textareea.setObjectName(u"Description_textareea")
        self.Description_textareea.setGeometry(QRect(170, 180, 401, 41))
        self.ID_combobox = QComboBox(Dialog)
        self.ID_combobox.setObjectName(u"ID_combobox")
        self.ID_combobox.setGeometry(QRect(170, 250, 141, 31))
        self.ID_label = QLabel(Dialog)
        self.ID_label.setObjectName(u"ID_label")
        self.ID_label.setGeometry(QRect(0, 240, 151, 51))
        self.ID_label.setFont(font)
        self.BP_label_2 = QLabel(Dialog)
        self.BP_label_2.setObjectName(u"BP_label_2")
        self.BP_label_2.setGeometry(QRect(0, 310, 161, 51))
        self.BP_label_2.setFont(font)
        self.BuyingPrice_textareea_2 = QLineEdit(Dialog)
        self.BuyingPrice_textareea_2.setObjectName(u"BuyingPrice_textareea_2")
        self.BuyingPrice_textareea_2.setGeometry(QRect(170, 320, 401, 41))
        self.BP_label_3 = QLabel(Dialog)
        self.BP_label_3.setObjectName(u"BP_label_3")
        self.BP_label_3.setGeometry(QRect(0, 380, 161, 51))
        self.BP_label_3.setFont(font)
        self.BuyingPrice_textareea_3 = QLineEdit(Dialog)
        self.BuyingPrice_textareea_3.setObjectName(u"BuyingPrice_textareea_3")
        self.BuyingPrice_textareea_3.setGeometry(QRect(170, 390, 401, 41))
        self.BP_label_4 = QLabel(Dialog)
        self.BP_label_4.setObjectName(u"BP_label_4")
        self.BP_label_4.setGeometry(QRect(0, 450, 61, 51))
        self.BP_label_4.setFont(font)
        self.BP_label_5 = QLabel(Dialog)
        self.BP_label_5.setObjectName(u"BP_label_5")
        self.BP_label_5.setGeometry(QRect(0, 510, 91, 51))
        self.BP_label_5.setFont(font)
        self.Quantity_textareea_5 = QLineEdit(Dialog)
        self.Quantity_textareea_5.setObjectName(u"Quantity_textareea_5")
        self.Quantity_textareea_5.setGeometry(QRect(170, 520, 401, 41))
        self.Units_combobox_2 = QComboBox(Dialog)
        self.Units_combobox_2.setObjectName(u"Units_combobox_2")
        self.Units_combobox_2.setGeometry(QRect(170, 470, 141, 31))
        self.ProductName_label_2 = QLabel(Dialog)
        self.ProductName_label_2.setObjectName(u"ProductName_label_2")
        self.ProductName_label_2.setGeometry(QRect(0, 50, 31, 51))
        self.ProductName_label_2.setFont(font)
        self.ID_combobox_2 = QComboBox(Dialog)
        self.ID_combobox_2.setObjectName(u"ID_combobox_2")
        self.ID_combobox_2.setGeometry(QRect(170, 60, 141, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.save_button.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.Back_button.setText(QCoreApplication.translate("Dialog", u"Back ", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Edit Product", None))
        self.ProductName_label.setText(QCoreApplication.translate("Dialog", u"Product Name", None))
        self.password_label.setText(QCoreApplication.translate("Dialog", u"Description", None))
        self.ID_label.setText(QCoreApplication.translate("Dialog", u"Category ID", None))
        self.BP_label_2.setText(QCoreApplication.translate("Dialog", u"Buying Price (RP)", None))
        self.BP_label_3.setText(QCoreApplication.translate("Dialog", u"Selling Price (RP)", None))
        self.BP_label_4.setText(QCoreApplication.translate("Dialog", u"Units", None))
        self.BP_label_5.setText(QCoreApplication.translate("Dialog", u"Quantity", None))
        self.ProductName_label_2.setText(QCoreApplication.translate("Dialog", u"ID :", None))
    # retranslateUi

