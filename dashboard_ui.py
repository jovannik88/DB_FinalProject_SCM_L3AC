# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dashboard.ui'
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

class Ui_Dashboard(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(770, 1156)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 10, 181, 41))
        font = QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 100, 211, 41))
        font1 = QFont()
        font1.setPointSize(20)
        self.label_2.setFont(font1)
        self.label_TotalSalesToday = QLabel(Dialog)
        self.label_TotalSalesToday.setObjectName(u"label_TotalSalesToday")
        self.label_TotalSalesToday.setGeometry(QRect(0, 150, 211, 41))
        font2 = QFont()
        font2.setPointSize(16)
        self.label_TotalSalesToday.setFont(font2)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 100, 251, 41))
        self.label_3.setFont(font1)
        self.totalPurchasetoday_label = QLabel(Dialog)
        self.totalPurchasetoday_label.setObjectName(u"totalPurchasetoday_label")
        self.totalPurchasetoday_label.setGeometry(QRect(230, 150, 251, 41))
        self.totalPurchasetoday_label.setFont(font2)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(500, 100, 221, 41))
        self.label_5.setFont(font1)
        self.todayprofitloss_label = QLabel(Dialog)
        self.todayprofitloss_label.setObjectName(u"todayprofitloss_label")
        self.todayprofitloss_label.setGeometry(QRect(500, 150, 221, 41))
        self.todayprofitloss_label.setFont(font2)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(270, 200, 201, 41))
        self.label_4.setFont(font)
        self.RecentSales_Table = QTableView(Dialog)
        self.RecentSales_Table.setObjectName(u"RecentSales_Table")
        self.RecentSales_Table.setGeometry(QRect(0, 250, 761, 101))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(250, 360, 261, 41))
        self.label_6.setFont(font)
        self.RecentPurchase_Table_2 = QTableView(Dialog)
        self.RecentPurchase_Table_2.setObjectName(u"RecentPurchase_Table_2")
        self.RecentPurchase_Table_2.setGeometry(QRect(0, 410, 761, 101))
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(240, 530, 291, 41))
        self.label_7.setFont(font)
        self.unpaidcustomertableview = QTableView(Dialog)
        self.unpaidcustomertableview.setObjectName(u"unpaidcustomertableview")
        self.unpaidcustomertableview.setGeometry(QRect(0, 590, 761, 101))
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(250, 710, 291, 41))
        self.label_8.setFont(font)
        self.unpaidsuppliertableview_2 = QTableView(Dialog)
        self.unpaidsuppliertableview_2.setObjectName(u"unpaidsuppliertableview_2")
        self.unpaidsuppliertableview_2.setGeometry(QRect(0, 760, 761, 101))
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(290, 870, 291, 41))
        self.label_9.setFont(font)
        self.lowstocktableview_3 = QTableView(Dialog)
        self.lowstocktableview_3.setObjectName(u"lowstocktableview_3")
        self.lowstocktableview_3.setGeometry(QRect(0, 920, 761, 101))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(580, 1050, 171, 61))
        font3 = QFont()
        font3.setPointSize(14)
        self.pushButton.setFont(font3)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Dashboard ", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Total Sales Today", None))
        self.label_TotalSalesToday.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Total Purchase Today", None))
        self.totalPurchasetoday_label.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Today's Profit/loss", None))
        self.todayprofitloss_label.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Recent Sales", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Recent Purchase", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Unpaid Customer", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Unpaid Supplier", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Low Stock", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Back", None))
    # retranslateUi

