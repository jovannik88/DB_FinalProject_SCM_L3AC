# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableView,
    QWidget)

class Ui_manageproduct(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1088, 899)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(460, 0, 221, 51))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.ProducrView = QTableView(Dialog)
        self.ProducrView.setObjectName(u"ProducrView")
        self.ProducrView.setGeometry(QRect(0, 50, 1081, 591))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 680, 41, 31))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_2.setFont(font1)
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(60, 680, 161, 41))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 740, 121, 51))
        font2 = QFont()
        font2.setPointSize(16)
        self.pushButton.setFont(font2)
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(930, 770, 121, 51))
        self.pushButton_2.setFont(font1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Manage Product", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"ID :", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Delete", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Exit", None))
    # retranslateUi

