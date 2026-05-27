# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete_user.ui'
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

class Ui_User_Deletee(object):
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
        self.label_deleteUser = QLabel(Dialog)
        self.label_deleteUser.setObjectName(u"label_deleteUser")
        self.label_deleteUser.setGeometry(QRect(260, 10, 151, 51))
        font1 = QFont()
        font1.setPointSize(20)
        self.label_deleteUser.setFont(font1)
        self.View_user = QTableView(Dialog)
        self.View_user.setObjectName(u"View_user")
        self.View_user.setGeometry(QRect(0, 80, 671, 391))
        self.label_select_user = QLabel(Dialog)
        self.label_select_user.setObjectName(u"label_select_user")
        self.label_select_user.setGeometry(QRect(10, 490, 151, 51))
        self.label_select_user.setFont(font)
        self.comboBox_ID = QComboBox(Dialog)
        self.comboBox_ID.setObjectName(u"comboBox_ID")
        self.comboBox_ID.setGeometry(QRect(140, 500, 121, 41))
        self.delete_button = QPushButton(Dialog)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(10, 550, 111, 51))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Back_button.setText(QCoreApplication.translate("Dialog", u"Back ", None))
        self.label_deleteUser.setText(QCoreApplication.translate("Dialog", u"Delete Users", None))
        self.label_select_user.setText(QCoreApplication.translate("Dialog", u"Select Users", None))
        self.delete_button.setText(QCoreApplication.translate("Dialog", u"Delete", None))
    # retranslateUi

