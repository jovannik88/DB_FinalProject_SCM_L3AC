from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableView, QWidget)

class Ui_userview(object):
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
        self.label_viewUser = QLabel(Dialog)
        self.label_viewUser.setObjectName(u"label_viewUser")
        self.label_viewUser.setGeometry(QRect(260, 10, 151, 51))
        font1 = QFont()
        font1.setPointSize(20)
        self.label_viewUser.setFont(font1)
        self.View_user = QTableView(Dialog)
        self.View_user.setObjectName(u"View_user")
        self.View_user.setGeometry(QRect(0, 80, 671, 391))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Back_button.setText(QCoreApplication.translate("Dialog", u"Back ", None))
        self.label_viewUser.setText(QCoreApplication.translate("Dialog", u"View Users", None))
    # retranslateUi

