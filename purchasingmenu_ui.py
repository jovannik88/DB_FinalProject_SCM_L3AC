from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QWidget)

class Ui_purchasingmenu(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(686, 613)
        self.product_button = QPushButton(Dialog)
        self.product_button.setObjectName(u"product_button")
        self.product_button.setGeometry(QRect(10, 30, 181, 71))
        font = QFont()
        font.setPointSize(16)
        self.product_button.setFont(font)
        self.category_button = QPushButton(Dialog)
        self.category_button.setObjectName(u"category_button")
        self.category_button.setGeometry(QRect(240, 30, 181, 71))
        self.category_button.setFont(font)
        self.supplier_button = QPushButton(Dialog)
        self.supplier_button.setObjectName(u"supplier_button")
        self.supplier_button.setGeometry(QRect(470, 30, 181, 71))
        self.supplier_button.setFont(font)
        self.Sales_button = QPushButton(Dialog)
        self.Sales_button.setObjectName(u"Sales_button")
        self.Sales_button.setGeometry(QRect(0, 140, 191, 71))
        self.Sales_button.setFont(font)
        self.supplierpaymentbutton = QPushButton(Dialog)
        self.supplierpaymentbutton.setObjectName(u"supplierpaymentbutton")
        self.supplierpaymentbutton.setGeometry(QRect(230, 140, 191, 71))
        self.supplierpaymentbutton.setFont(font)
        self.pushButton_11 = QPushButton(Dialog)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(490, 520, 191, 71))
        self.pushButton_11.setFont(font)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.product_button.setText(QCoreApplication.translate("Dialog", u"Manage Product", None))
        self.category_button.setText(QCoreApplication.translate("Dialog", u"Manage Category", None))
        self.supplier_button.setText(QCoreApplication.translate("Dialog", u"Manage Supplier", None))
        self.Sales_button.setText(QCoreApplication.translate("Dialog", u"Sales Order", None))
        self.supplierpaymentbutton.setText(QCoreApplication.translate("Dialog", u"Supplier Payment", None))
        self.pushButton_11.setText(QCoreApplication.translate("Dialog", u"Exit", None))
    # retranslateUi

