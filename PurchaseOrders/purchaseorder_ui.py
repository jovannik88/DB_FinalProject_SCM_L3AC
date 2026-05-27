# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'purchaseorder.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_POmenu(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(748, 714)
        self.view_purchase_button = QPushButton(Dialog)
        self.view_purchase_button.setObjectName(u"view_purchase_button")
        self.view_purchase_button.setGeometry(QRect(490, 130, 211, 101))
        font = QFont()
        font.setPointSize(16)
        self.view_purchase_button.setFont(font)
        self.pushButton_11 = QPushButton(Dialog)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(540, 580, 191, 71))
        self.pushButton_11.setFont(font)
        self.New_PO_Button = QPushButton(Dialog)
        self.New_PO_Button.setObjectName(u"New_PO_Button")
        self.New_PO_Button.setGeometry(QRect(0, 130, 211, 101))
        self.New_PO_Button.setFont(font)
        self.view_po_button = QPushButton(Dialog)
        self.view_po_button.setObjectName(u"view_po_button")
        self.view_po_button.setGeometry(QRect(250, 130, 211, 101))
        self.view_po_button.setFont(font)
        self.label_title = QLabel(Dialog)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(250, 10, 281, 61))
        font1 = QFont()
        font1.setPointSize(28)
        self.label_title.setFont(font1)
        self.status__button = QPushButton(Dialog)
        self.status__button.setObjectName(u"status__button")
        self.status__button.setGeometry(QRect(0, 270, 211, 101))
        self.status__button.setFont(font)
        self.Receive_Qty_Button = QPushButton(Dialog)
        self.Receive_Qty_Button.setObjectName(u"Receive_Qty_Button")
        self.Receive_Qty_Button.setGeometry(QRect(250, 270, 211, 101))
        self.Receive_Qty_Button.setFont(font)
        self.Invoice_Button = QPushButton(Dialog)
        self.Invoice_Button.setObjectName(u"Invoice_Button")
        self.Invoice_Button.setGeometry(QRect(490, 270, 211, 101))
        self.Invoice_Button.setFont(font)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.view_purchase_button.setText(QCoreApplication.translate("Dialog", u"View Purchase Detail", None))
        self.pushButton_11.setText(QCoreApplication.translate("Dialog", u"Back ", None))
        self.New_PO_Button.setText(QCoreApplication.translate("Dialog", u"New Purchase Order", None))
        self.view_po_button.setText(QCoreApplication.translate("Dialog", u"View Purchase Order", None))
        self.label_title.setText(QCoreApplication.translate("Dialog", u"Purchase Order", None))
        self.status__button.setText(QCoreApplication.translate("Dialog", u"Update Status", None))
        self.Receive_Qty_Button.setText(QCoreApplication.translate("Dialog", u"Receive Qty Update", None))
        self.Invoice_Button.setText(QCoreApplication.translate("Dialog", u"Invoice", None))
    # retranslateUi

