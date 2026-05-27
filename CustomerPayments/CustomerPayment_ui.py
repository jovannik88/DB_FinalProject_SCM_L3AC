# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CustomerPayment.ui'
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

class Ui_CustomerPayment(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(748, 714)
        self.pushButton_11 = QPushButton(Dialog)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(540, 580, 191, 71))
        font = QFont()
        font.setPointSize(16)
        self.pushButton_11.setFont(font)
        self.view_payment_Button = QPushButton(Dialog)
        self.view_payment_Button.setObjectName(u"view_payment_Button")
        self.view_payment_Button.setGeometry(QRect(250, 290, 211, 101))
        self.view_payment_Button.setFont(font)
        self.Record_Payment_button = QPushButton(Dialog)
        self.Record_Payment_button.setObjectName(u"Record_Payment_button")
        self.Record_Payment_button.setGeometry(QRect(250, 150, 211, 101))
        self.Record_Payment_button.setFont(font)
        self.label_title = QLabel(Dialog)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(190, 10, 321, 61))
        font1 = QFont()
        font1.setPointSize(28)
        self.label_title.setFont(font1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_11.setText(QCoreApplication.translate("Dialog", u"Back ", None))
        self.view_payment_Button.setText(QCoreApplication.translate("Dialog", u"View Payment", None))
        self.Record_Payment_button.setText(QCoreApplication.translate("Dialog", u"Record Payment", None))
        self.label_title.setText(QCoreApplication.translate("Dialog", u"Customer Payment", None))
    # retranslateUi

