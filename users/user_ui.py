# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'User_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QWidget)

class Ui_ManageUsers(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(686, 613)
        self.Registered_users_button = QPushButton(Dialog)
        self.Registered_users_button.setObjectName(u"Registered_users_button")
        self.Registered_users_button.setGeometry(QRect(250, 230, 181, 71))
        font = QFont()
        font.setPointSize(16)
        self.Registered_users_button.setFont(font)
        self.Add_user_Button = QPushButton(Dialog)
        self.Add_user_Button.setObjectName(u"Add_user_Button")
        self.Add_user_Button.setGeometry(QRect(250, 40, 181, 71))
        self.Add_user_Button.setFont(font)
        self.Delete_users_button = QPushButton(Dialog)
        self.Delete_users_button.setObjectName(u"Delete_users_button")
        self.Delete_users_button.setGeometry(QRect(250, 320, 181, 71))
        self.Delete_users_button.setFont(font)
        self.Edit_User_button = QPushButton(Dialog)
        self.Edit_User_button.setObjectName(u"Edit_User_button")
        self.Edit_User_button.setGeometry(QRect(250, 140, 181, 71))
        self.Edit_User_button.setFont(font)
        self.pushButton_11 = QPushButton(Dialog)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(490, 520, 191, 71))
        self.pushButton_11.setFont(font)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Registered_users_button.setText(QCoreApplication.translate("Dialog", u"Registered Users", None))
        self.Add_user_Button.setText(QCoreApplication.translate("Dialog", u"Add Users", None))
        self.Delete_users_button.setText(QCoreApplication.translate("Dialog", u"Delete Users", None))
        self.Edit_User_button.setText(QCoreApplication.translate("Dialog", u"Edit Users", None))
        self.pushButton_11.setText(QCoreApplication.translate("Dialog", u"Back ", None))
    # retranslateUi

