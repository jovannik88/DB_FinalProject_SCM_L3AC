from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Product(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(686, 613)
        self.View_Product_Button = QPushButton(Dialog)
        self.View_Product_Button.setObjectName(u"View_Product_Button")
        self.View_Product_Button.setGeometry(QRect(230, 350, 211, 101))
        font = QFont()
        font.setPointSize(16)
        self.View_Product_Button.setFont(font)
        self.pushButton_11 = QPushButton(Dialog)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(490, 520, 191, 71))
        self.pushButton_11.setFont(font)
        self.add_Product_button = QPushButton(Dialog)
        self.add_Product_button.setObjectName(u"add_Product_button")
        self.add_Product_button.setGeometry(QRect(230, 100, 211, 101))
        self.add_Product_button.setFont(font)
        self.Edit_Product_button = QPushButton(Dialog)
        self.Edit_Product_button.setObjectName(u"Edit_Product_button")
        self.Edit_Product_button.setGeometry(QRect(230, 220, 211, 101))
        self.Edit_Product_button.setFont(font)
        self.label_product = QLabel(Dialog)
        self.label_product.setObjectName(u"label_product")
        self.label_product.setGeometry(QRect(270, 0, 211, 61))
        font1 = QFont()
        font1.setPointSize(28)
        self.label_product.setFont(font1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.View_Product_Button.setText(QCoreApplication.translate("Dialog", u"View Product", None))
        self.pushButton_11.setText(QCoreApplication.translate("Dialog", u"Back ", None))
        self.add_Product_button.setText(QCoreApplication.translate("Dialog", u"Add Product", None))
        self.Edit_Product_button.setText(QCoreApplication.translate("Dialog", u"Edit Product", None))
        self.label_product.setText(QCoreApplication.translate("Dialog", u"Product", None))
    # retranslateUi

