# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_welcome(object):
    def setupUi(self, welcome):
        if not welcome.objectName():
            welcome.setObjectName(u"welcome")
        welcome.resize(540, 464)
        self.label_welcome = QLabel(welcome)
        self.label_welcome.setObjectName(u"label_welcome")
        self.label_welcome.setGeometry(QRect(40, 10, 501, 31))
        font = QFont()
        font.setPointSize(16)
        self.label_welcome.setFont(font)
        self.label_welcome.setTextFormat(Qt.TextFormat.PlainText)
        self.label_username = QLabel(welcome)
        self.label_username.setObjectName(u"label_username")
        self.label_username.setGeometry(QRect(10, 100, 181, 41))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_username.setFont(font1)
        self.label_password = QLabel(welcome)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setGeometry(QRect(10, 160, 181, 41))
        self.label_password.setFont(font1)
        self.pushButton = QPushButton(welcome)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 230, 211, 71))
        self.pushButton.setFont(font)
        self.Textarea_username = QLineEdit(welcome)
        self.Textarea_username.setObjectName(u"Textarea_username")
        self.Textarea_username.setGeometry(QRect(140, 110, 221, 31))
        self.textarea_password = QLineEdit(welcome)
        self.textarea_password.setObjectName(u"textarea_password")
        self.textarea_password.setGeometry(QRect(140, 170, 221, 31))
        self.textarea_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.retranslateUi(welcome)

        QMetaObject.connectSlotsByName(welcome)
    # setupUi

    def retranslateUi(self, welcome):
        welcome.setWindowTitle(QCoreApplication.translate("welcome", u"Dialog", None))
        self.label_welcome.setText(QCoreApplication.translate("welcome", u"Welcome To Supply Chain Management System", None))
        self.label_username.setText(QCoreApplication.translate("welcome", u"Username :", None))
        self.label_password.setText(QCoreApplication.translate("welcome", u"Password  :", None))
        self.pushButton.setText(QCoreApplication.translate("welcome", u"Login", None))
    # retranslateUi

    

