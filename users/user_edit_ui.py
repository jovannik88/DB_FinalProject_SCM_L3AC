# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_user.ui'
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

class Ui_User_edit(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(686, 613)
        self.edituser_button = QPushButton(Dialog)
        self.edituser_button.setObjectName(u"edituser_button")
        self.edituser_button.setGeometry(QRect(30, 300, 181, 71))
        font = QFont()
        font.setPointSize(16)
        self.edituser_button.setFont(font)
        self.Back_button = QPushButton(Dialog)
        self.Back_button.setObjectName(u"Back_button")
        self.Back_button.setGeometry(QRect(490, 520, 191, 71))
        self.Back_button.setFont(font)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 10, 151, 51))
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
        self.username_textarea = QLineEdit(Dialog)
        self.username_textarea.setObjectName(u"username_textarea")
        self.username_textarea.setGeometry(QRect(140, 130, 401, 41))
        self.password_textareea = QLineEdit(Dialog)
        self.password_textareea.setObjectName(u"password_textareea")
        self.password_textareea.setGeometry(QRect(140, 190, 401, 41))
        self.roles_combobox = QComboBox(Dialog)
        self.roles_combobox.setObjectName(u"roles_combobox")
        self.roles_combobox.setGeometry(QRect(140, 250, 141, 31))
        self.roles_label = QLabel(Dialog)
        self.roles_label.setObjectName(u"roles_label")
        self.roles_label.setGeometry(QRect(10, 240, 151, 51))
        self.roles_label.setFont(font)
        self.Selectuser_combobox = QComboBox(Dialog)
        self.Selectuser_combobox.setObjectName(u"Selectuser_combobox")
        self.Selectuser_combobox.setGeometry(QRect(140, 80, 161, 26))
        self.selectuser_label = QLabel(Dialog)
        self.selectuser_label.setObjectName(u"selectuser_label")
        self.selectuser_label.setGeometry(QRect(0, 70, 151, 51))
        self.selectuser_label.setFont(font)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.edituser_button.setText(QCoreApplication.translate("Dialog", u"Edit User", None))
        self.Back_button.setText(QCoreApplication.translate("Dialog", u"Back ", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Edit Users", None))
        self.userName_label.setText(QCoreApplication.translate("Dialog", u"Username :", None))
        self.password_label.setText(QCoreApplication.translate("Dialog", u"Password :", None))
        self.roles_label.setText(QCoreApplication.translate("Dialog", u"Roles :", None))
        self.selectuser_label.setText(QCoreApplication.translate("Dialog", u"Select Users", None))
    # retranslateUi

