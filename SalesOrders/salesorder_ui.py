from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_SalesOrder(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(748, 714)
        self.view_SODetail_button = QPushButton(Dialog)
        self.view_SODetail_button.setObjectName(u"view_SODetail_button")
        self.view_SODetail_button.setGeometry(QRect(490, 130, 211, 101))
        font = QFont()
        font.setPointSize(16)
        self.view_SODetail_button.setFont(font)
        self.pushButton_11 = QPushButton(Dialog)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(540, 580, 191, 71))
        self.pushButton_11.setFont(font)
        self.New_SO_Button = QPushButton(Dialog)
        self.New_SO_Button.setObjectName(u"New_SO_Button")
        self.New_SO_Button.setGeometry(QRect(0, 130, 211, 101))
        self.New_SO_Button.setFont(font)
        self.view_so_button = QPushButton(Dialog)
        self.view_so_button.setObjectName(u"view_so_button")
        self.view_so_button.setGeometry(QRect(250, 130, 211, 101))
        self.view_so_button.setFont(font)
        self.label_title = QLabel(Dialog)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(250, 10, 281, 61))
        font1 = QFont()
        font1.setPointSize(28)
        self.label_title.setFont(font1)
        self.CancelOrder__button = QPushButton(Dialog)
        self.CancelOrder__button.setObjectName(u"CancelOrder__button")
        self.CancelOrder__button.setGeometry(QRect(0, 270, 211, 101))
        self.CancelOrder__button.setFont(font)
        self.CancelOrder__button_2 = QPushButton(Dialog)
        self.CancelOrder__button_2.setObjectName(u"CancelOrder__button_2")
        self.CancelOrder__button_2.setGeometry(QRect(250, 270, 211, 101))
        self.CancelOrder__button_2.setFont(font)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.view_SODetail_button.setText(QCoreApplication.translate("Dialog", u"View Sales Detail", None))
        self.pushButton_11.setText(QCoreApplication.translate("Dialog", u"Back ", None))
        self.New_SO_Button.setText(QCoreApplication.translate("Dialog", u"New Sales Order", None))
        self.view_so_button.setText(QCoreApplication.translate("Dialog", u"View Sales Order", None))
        self.label_title.setText(QCoreApplication.translate("Dialog", u"Sales Order", None))
        self.CancelOrder__button.setText(QCoreApplication.translate("Dialog", u"Cancel Order", None))
        self.CancelOrder__button_2.setText(QCoreApplication.translate("Dialog", u"Invoice", None))
    # retranslateUi

