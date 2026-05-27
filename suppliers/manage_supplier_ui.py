# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view_supplier.ui'
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

class Ui_Managesupplier(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(686, 613)
        self.Back_button = QPushButton(Dialog)
        self.Back_button.setObjectName(u"Back_button")
        self.Back_button.setGeometry(QRect(490, 520, 191, 71))
        font = QFont()
        font.setPointSize(16)
        self.Back_button.setFont(font)
        self.label_viewUser = QLabel(Dialog)
        self.label_viewUser.setObjectName(u"label_viewUser")
        self.label_viewUser.setGeometry(QRect(260, 10, 191, 51))
        font1 = QFont()
        font1.setPointSize(20)
        self.label_viewUser.setFont(font1)
        self.View_Customer = QTableView(Dialog)
        self.View_Customer.setObjectName(u"View_Customer")
        self.View_Customer.setGeometry(QRect(0, 80, 671, 391))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 490, 161, 31))
        self.label.setFont(font)
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(160, 500, 141, 26))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 540, 131, 51))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Back_button.setText(QCoreApplication.translate("Dialog", u"Back ", None))
        self.label_viewUser.setText(QCoreApplication.translate("Dialog", u"View Supplier", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Select Supplier", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Delete", None))
    # retranslateUi

