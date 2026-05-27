# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'update_status.ui'
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

class Ui_UpdateStatus(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(743, 536)
        self.pushButton_11 = QPushButton(Dialog)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(510, 370, 191, 71))
        font = QFont()
        font.setPointSize(16)
        self.pushButton_11.setFont(font)
        self.label_title = QLabel(Dialog)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(250, 10, 371, 61))
        font1 = QFont()
        font1.setPointSize(28)
        self.label_title.setFont(font1)
        self.TotalAmount_label = QLabel(Dialog)
        self.TotalAmount_label.setObjectName(u"TotalAmount_label")
        self.TotalAmount_label.setGeometry(QRect(140, 730, 581, 31))
        font2 = QFont()
        font2.setPointSize(14)
        self.TotalAmount_label.setFont(font2)
        self.label_title_2 = QLabel(Dialog)
        self.label_title_2.setObjectName(u"label_title_2")
        self.label_title_2.setGeometry(QRect(0, 130, 191, 61))
        font3 = QFont()
        font3.setPointSize(20)
        self.label_title_2.setFont(font3)
        self.Status_comboBox = QComboBox(Dialog)
        self.Status_comboBox.setObjectName(u"Status_comboBox")
        self.Status_comboBox.setGeometry(QRect(190, 150, 411, 31))
        self.Update_button = QPushButton(Dialog)
        self.Update_button.setObjectName(u"Update_button")
        self.Update_button.setGeometry(QRect(0, 270, 191, 71))
        self.Update_button.setFont(font)
        self.label_title_3 = QLabel(Dialog)
        self.label_title_3.setObjectName(u"label_title_3")
        self.label_title_3.setGeometry(QRect(0, 80, 191, 61))
        self.label_title_3.setFont(font3)
        self.PONO_comboBox = QComboBox(Dialog)
        self.PONO_comboBox.setObjectName(u"PONO_comboBox")
        self.PONO_comboBox.setGeometry(QRect(190, 90, 411, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_11.setText(QCoreApplication.translate("Dialog", u"Back ", None))
        self.label_title.setText(QCoreApplication.translate("Dialog", u"Update Status", None))
        self.TotalAmount_label.setText("")
        self.label_title_2.setText(QCoreApplication.translate("Dialog", u"Current Status :", None))
        self.Update_button.setText(QCoreApplication.translate("Dialog", u"Update", None))
        self.label_title_3.setText(QCoreApplication.translate("Dialog", u"PO NO :", None))
    # retranslateUi

