# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_customer.ui'
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

class Ui_EditCustomer(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(686, 613)
        self.editcustomer_button = QPushButton(Dialog)
        self.editcustomer_button.setObjectName(u"editcustomer_button")
        self.editcustomer_button.setGeometry(QRect(-10, 420, 181, 71))
        font = QFont()
        font.setPointSize(16)
        self.editcustomer_button.setFont(font)
        self.Back_button = QPushButton(Dialog)
        self.Back_button.setObjectName(u"Back_button")
        self.Back_button.setGeometry(QRect(490, 520, 191, 71))
        self.Back_button.setFont(font)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 10, 181, 51))
        font1 = QFont()
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.userName_label = QLabel(Dialog)
        self.userName_label.setObjectName(u"userName_label")
        self.userName_label.setGeometry(QRect(10, 120, 151, 51))
        self.userName_label.setFont(font)
        self.password_label = QLabel(Dialog)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(10, 180, 151, 51))
        self.password_label.setFont(font)
        self.name_textarea = QLineEdit(Dialog)
        self.name_textarea.setObjectName(u"name_textarea")
        self.name_textarea.setGeometry(QRect(160, 130, 401, 41))
        self.phone_textareea = QLineEdit(Dialog)
        self.phone_textareea.setObjectName(u"phone_textareea")
        self.phone_textareea.setGeometry(QRect(160, 190, 401, 41))
        self.roles_label = QLabel(Dialog)
        self.roles_label.setObjectName(u"roles_label")
        self.roles_label.setGeometry(QRect(10, 240, 61, 51))
        self.roles_label.setFont(font)
        self.Selectcustomer_combobox = QComboBox(Dialog)
        self.Selectcustomer_combobox.setObjectName(u"Selectcustomer_combobox")
        self.Selectcustomer_combobox.setGeometry(QRect(160, 90, 161, 26))
        self.selectuser_label = QLabel(Dialog)
        self.selectuser_label.setObjectName(u"selectuser_label")
        self.selectuser_label.setGeometry(QRect(0, 70, 151, 51))
        self.selectuser_label.setFont(font)
        self.email_textareea_2 = QLineEdit(Dialog)
        self.email_textareea_2.setObjectName(u"email_textareea_2")
        self.email_textareea_2.setGeometry(QRect(160, 250, 401, 41))
        self.roles_label_2 = QLabel(Dialog)
        self.roles_label_2.setObjectName(u"roles_label_2")
        self.roles_label_2.setGeometry(QRect(10, 300, 81, 51))
        self.roles_label_2.setFont(font)
        self.address_textareea_3 = QLineEdit(Dialog)
        self.address_textareea_3.setObjectName(u"address_textareea_3")
        self.address_textareea_3.setGeometry(QRect(160, 310, 401, 41))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.editcustomer_button.setText(QCoreApplication.translate("Dialog", u"Edit Customer", None))
        self.Back_button.setText(QCoreApplication.translate("Dialog", u"Back ", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Edit Customer", None))
        self.userName_label.setText(QCoreApplication.translate("Dialog", u"Name ", None))
        self.password_label.setText(QCoreApplication.translate("Dialog", u"Phone", None))
        self.roles_label.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.selectuser_label.setText(QCoreApplication.translate("Dialog", u"Select Customer", None))
        self.roles_label_2.setText(QCoreApplication.translate("Dialog", u"Address", None))
    # retranslateUi

