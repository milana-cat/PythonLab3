# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'function_calc.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDoubleSpinBox, QGridLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 490)
        MainWindow.setMinimumSize(QSize(600, 490))
        MainWindow.setMaximumSize(QSize(600, 490))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Result = QTextEdit(self.centralwidget)
        self.Result.setObjectName(u"Result")
        self.Result.setGeometry(QRect(10, 10, 231, 111))
        font = QFont()
        font.setPointSize(12)
        self.Result.setFont(font)
        self.Result.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.Result.setReadOnly(True)
        self.Calculate = QPushButton(self.centralwidget)
        self.Calculate.setObjectName(u"Calculate")
        self.Calculate.setGeometry(QRect(10, 130, 231, 41))
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(260, 10, 321, 161))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 2)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.SpinBoxA = QDoubleSpinBox(self.gridLayoutWidget)
        self.SpinBoxA.setObjectName(u"SpinBoxA")

        self.gridLayout.addWidget(self.SpinBoxA, 0, 1, 1, 1)

        self.SpinBoxB = QDoubleSpinBox(self.gridLayoutWidget)
        self.SpinBoxB.setObjectName(u"SpinBoxB")

        self.gridLayout.addWidget(self.SpinBoxB, 1, 1, 1, 1)

        self.SpinBoxH = QDoubleSpinBox(self.gridLayoutWidget)
        self.SpinBoxH.setObjectName(u"SpinBoxH")

        self.gridLayout.addWidget(self.SpinBoxH, 2, 1, 1, 1)

        self.SpinBoxK = QDoubleSpinBox(self.gridLayoutWidget)
        self.SpinBoxK.setObjectName(u"SpinBoxK")

        self.gridLayout.addWidget(self.SpinBoxK, 3, 1, 1, 1)


        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 180, 571, 281))
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 40, 211, 61))
        self.label_7.setAutoFillBackground(False)
        self.label_7.setPixmap(QPixmap(u"UI/FunctionPic.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(Qt.AlignCenter)
        MainWindow.centralWidget = self.centralwidget
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.statusBar = self.statusbar

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0438 \u0432 \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u0435", None))
        self.Calculate.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u044c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0444\u0443\u043d\u043a\u0446\u0438\u044f: f(x)=x^3+m*sin(x)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0435\u0446 \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u0430(b)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u0430(a)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f(m)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433(h)", None))
        self.label_7.setText("")
    # retranslateUi

