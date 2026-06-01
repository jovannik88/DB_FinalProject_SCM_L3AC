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

class Ui_ManageCatt(object):
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
        self.label_ManageCategoties = QLabel(Dialog)
        self.label_ManageCategoties.setObjectName(u"label_ManageCategoties")
        self.label_ManageCategoties.setGeometry(QRect(230, 10, 261, 51))
        font1 = QFont()
        font1.setPointSize(20)
        self.label_ManageCategoties.setFont(font1)
        self.View_category = QTableView(Dialog)
        self.View_category.setObjectName(u"View_category")
        self.View_category.setGeometry(QRect(0, 80, 671, 391))
        self.label_select_category = QLabel(Dialog)
        self.label_select_category.setObjectName(u"label_select_category")
        self.label_select_category.setGeometry(QRect(10, 490, 171, 51))
        self.label_select_category.setFont(font)
        self.comboBox_ID = QComboBox(Dialog)
        self.comboBox_ID.setObjectName(u"comboBox_ID")
        self.comboBox_ID.setGeometry(QRect(180, 500, 121, 41))
        self.delete_button = QPushButton(Dialog)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(10, 550, 111, 51))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Back_button.setText(QCoreApplication.translate("Dialog", u"Back ", None))
        self.label_ManageCategoties.setText(QCoreApplication.translate("Dialog", u" Manage Categories", None))
        self.label_select_category.setText(QCoreApplication.translate("Dialog", u"Select Categories", None))
        self.delete_button.setText(QCoreApplication.translate("Dialog", u"Delete", None))
    # retranslateUi

