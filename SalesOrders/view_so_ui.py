# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view_so.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableView, QWidget)

class Ui_ViewSO(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(743, 977)
        self.pushButton_11 = QPushButton(Dialog)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(550, 880, 191, 71))
        font = QFont()
        font.setPointSize(16)
        self.pushButton_11.setFont(font)
        self.label_title = QLabel(Dialog)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(200, 10, 371, 61))
        font1 = QFont()
        font1.setPointSize(28)
        self.label_title.setFont(font1)
        self.TotalAmount_label = QLabel(Dialog)
        self.TotalAmount_label.setObjectName(u"TotalAmount_label")
        self.TotalAmount_label.setGeometry(QRect(140, 730, 581, 31))
        font2 = QFont()
        font2.setPointSize(14)
        self.TotalAmount_label.setFont(font2)
        self.viewso_tableView = QTableView(Dialog)
        self.viewso_tableView.setObjectName(u"viewso_tableView")
        self.viewso_tableView.setGeometry(QRect(0, 90, 731, 731))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_11.setText(QCoreApplication.translate("Dialog", u"Back ", None))
        self.label_title.setText(QCoreApplication.translate("Dialog", u"View Sales Order", None))
        self.TotalAmount_label.setText("")
    # retranslateUi

