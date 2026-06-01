from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QWidget)

class Ui_CashierMenu(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(602, 459)
        self.So_button = QPushButton(Dialog)
        self.So_button.setObjectName(u"So_button")
        self.So_button.setGeometry(QRect(210, 30, 191, 71))
        font = QFont()
        font.setPointSize(16)
        self.So_button.setFont(font)
        self.payment_button = QPushButton(Dialog)
        self.payment_button.setObjectName(u"payment_button")
        self.payment_button.setGeometry(QRect(210, 140, 191, 71))
        self.payment_button.setFont(font)
        self.pushButton_11 = QPushButton(Dialog)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(400, 350, 191, 71))
        self.pushButton_11.setFont(font)
        self.payment_button_2 = QPushButton(Dialog)
        self.payment_button_2.setObjectName(u"payment_button_2")
        self.payment_button_2.setGeometry(QRect(210, 250, 191, 71))
        self.payment_button_2.setFont(font)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.So_button.setText(QCoreApplication.translate("Dialog", u"Sales Order", None))
        self.payment_button.setText(QCoreApplication.translate("Dialog", u"Payments", None))
        self.pushButton_11.setText(QCoreApplication.translate("Dialog", u"Exit", None))
        self.payment_button_2.setText(QCoreApplication.translate("Dialog", u"Customers", None))
    # retranslateUi

