# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_category.ui'
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

class Ui_editcatt(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(686, 613)
        self.edituser_button = QPushButton(Dialog)
        self.edituser_button.setObjectName(u"edituser_button")
        self.edituser_button.setGeometry(QRect(0, 230, 181, 71))
        font = QFont()
        font.setPointSize(16)
        self.edituser_button.setFont(font)
        self.Back_button = QPushButton(Dialog)
        self.Back_button.setObjectName(u"Back_button")
        self.Back_button.setGeometry(QRect(490, 520, 191, 71))
        self.Back_button.setFont(font)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 10, 171, 51))
        font1 = QFont()
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.username_textarea = QLineEdit(Dialog)
        self.username_textarea.setObjectName(u"username_textarea")
        self.username_textarea.setGeometry(QRect(160, 140, 401, 41))
        self.Selectuser_combobox = QComboBox(Dialog)
        self.Selectuser_combobox.setObjectName(u"Selectuser_combobox")
        self.Selectuser_combobox.setGeometry(QRect(160, 90, 161, 26))
        self.selectuser_label = QLabel(Dialog)
        self.selectuser_label.setObjectName(u"selectuser_label")
        self.selectuser_label.setGeometry(QRect(0, 70, 151, 51))
        self.selectuser_label.setFont(font)
        self.password_label_2 = QLabel(Dialog)
        self.password_label_2.setObjectName(u"password_label_2")
        self.password_label_2.setGeometry(QRect(0, 130, 151, 51))
        self.password_label_2.setFont(font)
        

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.edituser_button.setText(QCoreApplication.translate("Dialog", u"Edit Category", None))
        self.Back_button.setText(QCoreApplication.translate("Dialog", u"Back ", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Edit Category", None))
        self.selectuser_label.setText(QCoreApplication.translate("Dialog", u"Select Category", None))
        self.password_label_2.setText(QCoreApplication.translate("Dialog", u"Category Name  :", None))
    # retranslateUi

