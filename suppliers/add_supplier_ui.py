from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_addsupplier(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(686, 613)
        self.save_button = QPushButton(Dialog)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(80, 380, 181, 71))
        font = QFont()
        font.setPointSize(16)
        self.save_button.setFont(font)
        self.Back_button = QPushButton(Dialog)
        self.Back_button.setObjectName(u"Back_button")
        self.Back_button.setGeometry(QRect(490, 520, 191, 71))
        self.Back_button.setFont(font)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 0, 161, 51))
        font1 = QFont()
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.Name_label = QLabel(Dialog)
        self.Name_label.setObjectName(u"Name_label")
        self.Name_label.setGeometry(QRect(0, 100, 151, 51))
        self.Name_label.setFont(font)
        self.Phone_label = QLabel(Dialog)
        self.Phone_label.setObjectName(u"Phone_label")
        self.Phone_label.setGeometry(QRect(0, 170, 151, 51))
        self.Phone_label.setFont(font)
        self.Email_label = QLabel(Dialog)
        self.Email_label.setObjectName(u"Email_label")
        self.Email_label.setGeometry(QRect(0, 240, 151, 51))
        self.Email_label.setFont(font)
        self.address_label = QLabel(Dialog)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setGeometry(QRect(0, 310, 151, 51))
        self.address_label.setFont(font)
        self.Name_textarea = QLineEdit(Dialog)
        self.Name_textarea.setObjectName(u"Name_textarea")
        self.Name_textarea.setGeometry(QRect(90, 110, 401, 41))
        self.Phone_TextArea_2 = QLineEdit(Dialog)
        self.Phone_TextArea_2.setObjectName(u"Phone_TextArea_2")
        self.Phone_TextArea_2.setGeometry(QRect(90, 180, 401, 41))
        self.Email_textarea = QLineEdit(Dialog)
        self.Email_textarea.setObjectName(u"Email_textarea")
        self.Email_textarea.setGeometry(QRect(90, 250, 401, 41))
        self.address_textarea = QLineEdit(Dialog)
        self.address_textarea.setObjectName(u"address_textarea")
        self.address_textarea.setGeometry(QRect(90, 310, 401, 41))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.save_button.setText(QCoreApplication.translate("Dialog", u"Save Supplier", None))
        self.Back_button.setText(QCoreApplication.translate("Dialog", u"Back ", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Add Supplier", None))
        self.Name_label.setText(QCoreApplication.translate("Dialog", u"Name :", None))
        self.Phone_label.setText(QCoreApplication.translate("Dialog", u"Phone :", None))
        self.Email_label.setText(QCoreApplication.translate("Dialog", u"E-Mail :", None))
        self.address_label.setText(QCoreApplication.translate("Dialog", u"Address :", None))
    # retranslateUi

