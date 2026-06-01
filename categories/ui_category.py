from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Categoryy(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(686, 613)
        self.View_Category_Button = QPushButton(Dialog)
        self.View_Category_Button.setObjectName(u"View_Category_Button")
        self.View_Category_Button.setGeometry(QRect(230, 350, 211, 101))
        font = QFont()
        font.setPointSize(16)
        self.View_Category_Button.setFont(font)
        self.pushButton_11 = QPushButton(Dialog)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(490, 520, 191, 71))
        self.pushButton_11.setFont(font)
        self.add_category_button = QPushButton(Dialog)
        self.add_category_button.setObjectName(u"add_category_button")
        self.add_category_button.setGeometry(QRect(230, 100, 211, 101))
        self.add_category_button.setFont(font)
        self.Edit_category_button = QPushButton(Dialog)
        self.Edit_category_button.setObjectName(u"Edit_category_button")
        self.Edit_category_button.setGeometry(QRect(230, 220, 211, 101))
        self.Edit_category_button.setFont(font)
        self.label_category = QLabel(Dialog)
        self.label_category.setObjectName(u"label_category")
        self.label_category.setGeometry(QRect(250, 10, 211, 61))
        font1 = QFont()
        font1.setPointSize(28)
        self.label_category.setFont(font1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.View_Category_Button.setText(QCoreApplication.translate("Dialog", u"View Category", None))
        self.pushButton_11.setText(QCoreApplication.translate("Dialog", u"Back ", None))
        self.add_category_button.setText(QCoreApplication.translate("Dialog", u"Add Category", None))
        self.Edit_category_button.setText(QCoreApplication.translate("Dialog", u"Edit Category", None))
        self.label_category.setText(QCoreApplication.translate("Dialog", u"Category", None))
    # retranslateUi

