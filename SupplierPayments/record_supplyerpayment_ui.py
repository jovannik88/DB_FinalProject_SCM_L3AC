# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'record_payment.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_recordsupplierpayment(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(743, 687)
        self.pushButton_11 = QPushButton(Dialog)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(530, 590, 191, 71))
        font = QFont()
        font.setPointSize(16)
        self.pushButton_11.setFont(font)
        self.label_title = QLabel(Dialog)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(250, 10, 281, 61))
        font1 = QFont()
        font1.setPointSize(28)
        self.label_title.setFont(font1)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 100, 141, 31))
        font2 = QFont()
        font2.setPointSize(14)
        self.label.setFont(font2)
        self.selectPO_combobox = QComboBox(Dialog)
        self.selectPO_combobox.setObjectName(u"selectPO_combobox")
        self.selectPO_combobox.setGeometry(QRect(140, 110, 481, 21))
        self.TotalAmount_label = QLabel(Dialog)
        self.TotalAmount_label.setObjectName(u"TotalAmount_label")
        self.TotalAmount_label.setGeometry(QRect(140, 730, 581, 31))
        self.TotalAmount_label.setFont(font2)
        self.savePayment_button_12 = QPushButton(Dialog)
        self.savePayment_button_12.setObjectName(u"savePayment_button_12")
        self.savePayment_button_12.setGeometry(QRect(0, 410, 351, 91))
        self.savePayment_button_12.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 150, 81, 31))
        self.label_2.setFont(font2)
        self.supplier_label = QLabel(Dialog)
        self.supplier_label.setObjectName(u"supplier_label")
        self.supplier_label.setGeometry(QRect(140, 150, 501, 31))
        self.supplier_label.setFont(font2)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 200, 121, 31))
        self.label_3.setFont(font2)
        self.total_amount_label = QLabel(Dialog)
        self.total_amount_label.setObjectName(u"total_amount_label")
        self.total_amount_label.setGeometry(QRect(140, 200, 601, 31))
        font3 = QFont()
        font3.setPointSize(11)
        self.total_amount_label.setFont(font3)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 250, 131, 31))
        self.label_4.setFont(font2)
        self.dateEdit = QDateEdit(Dialog)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(130, 250, 491, 31))
        self.dateEdit.setCalendarPopup(True)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 300, 81, 31))
        self.label_5.setFont(font2)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(130, 300, 481, 31))
        font4 = QFont()
        font4.setPointSize(9)
        self.lineEdit.setFont(font4)
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 350, 151, 31))
        self.label_6.setFont(font2)
        self.Paymentmethod_combobox_2 = QComboBox(Dialog)
        self.Paymentmethod_combobox_2.setObjectName(u"Paymentmethod_combobox_2")
        self.Paymentmethod_combobox_2.setGeometry(QRect(150, 360, 481, 21))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_11.setText(QCoreApplication.translate("Dialog", u"Back ", None))
        self.label_title.setText(QCoreApplication.translate("Dialog", u"Record Payment", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Select PO :", None))
        self.TotalAmount_label.setText("")
        self.savePayment_button_12.setText(QCoreApplication.translate("Dialog", u"Save Payment", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Supplier :", None))
        self.supplier_label.setText(QCoreApplication.translate("Dialog", u"d", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Total Amount :", None))
        self.total_amount_label.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Payment Date :", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("Dialog", u"dd/MM/yyyy", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Amount :", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Payment Method", None))
    # retranslateUi

