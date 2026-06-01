from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Catt(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(686, 613)
        self.save_button = QPushButton(Dialog)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(-10, 190, 181, 71))
        font = QFont()
        font.setPointSize(16)
        self.save_button.setFont(font)
        self.Back_button = QPushButton(Dialog)
        self.Back_button.setObjectName(u"Back_button")
        self.Back_button.setGeometry(QRect(490, 520, 191, 71))
        self.Back_button.setFont(font)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 10, 211, 51))
        font1 = QFont()
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.userName_label = QLabel(Dialog)
        self.userName_label.setObjectName(u"userName_label")
        self.userName_label.setGeometry(QRect(0, 100, 151, 51))
        self.userName_label.setFont(font)
        self.username_textarea = QLineEdit(Dialog)
        self.username_textarea.setObjectName(u"username_textarea")
        self.username_textarea.setGeometry(QRect(150, 110, 401, 41))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.save_button.setText(QCoreApplication.translate("Dialog", u"Add category", None))
        self.Back_button.setText(QCoreApplication.translate("Dialog", u"Back ", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Add Categories", None))
        self.userName_label.setText(QCoreApplication.translate("Dialog", u"Category Name :", None))
    # retranslateUi

