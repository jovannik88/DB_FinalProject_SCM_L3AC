# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SO_INVOICE.ui'
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
    QPushButton, QSizePolicy, QWidget)

class Ui_SOInvoice(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(510, 497)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 20, 91, 41))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 100, 51, 31))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_2.setFont(font1)
        self.SelectPOcomboBox = QComboBox(Dialog)
        self.SelectPOcomboBox.setObjectName(u"SelectPOcomboBox")
        self.SelectPOcomboBox.setGeometry(QRect(70, 100, 121, 41))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(400, 210, 111, 51))
        font2 = QFont()
        font2.setPointSize(12)
        self.pushButton.setFont(font2)
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(380, 420, 121, 51))
        self.pushButton_2.setFont(font2)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 160, 491, 41))
        self.label_3.setFont(font2)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Invoice", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"SO :", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Generate", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"BACK", None))
        self.label_3.setText("")
    # retranslateUi

