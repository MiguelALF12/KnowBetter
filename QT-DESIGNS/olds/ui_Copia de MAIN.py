# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Copia de MAIN.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)
import logo-header_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1306, 870)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1306, 870))
        MainWindow.setMaximumSize(QSize(1306, 870))
        MainWindow.setStyleSheet(u"padding:0px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(1306, 849))
        self.centralwidget.setMaximumSize(QSize(1306, 849))
        self.centralwidget.setStyleSheet(u"padding:0px;\n"
"margin:0px;")
        self.verticalLayout_15 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.genera_verticalLayout_2 = QVBoxLayout()
        self.genera_verticalLayout_2.setSpacing(0)
        self.genera_verticalLayout_2.setObjectName(u"genera_verticalLayout_2")
        self.body_layout = QVBoxLayout()
        self.body_layout.setObjectName(u"body_layout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(1280, 750))
        self.frame.setMaximumSize(QSize(1280, 750))
        self.frame.setStyleSheet(u"background-image: url(:/newPrefix/IMAGES/background image.png);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.frame)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMinimumSize(QSize(0, 150))
        self.header_frame.setMaximumSize(QSize(16777215, 150))
        self.header_frame.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);")
        self.header_frame.setFrameShape(QFrame.Panel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(140, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.header_frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(220, 100))
        self.label.setMaximumSize(QSize(220, 200))
        self.label.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0)")
        self.label.setPixmap(QPixmap(u":/newPrefix/IMAGES/header-utp-logo-blanco.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(520, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.header_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 100))
        self.label_2.setMaximumSize(QSize(16777215, 200))
        font = QFont()
        font.setFamilies([u"Bayon"])
        font.setPointSize(60)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(False)

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer_4 = QSpacerItem(240, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addWidget(self.header_frame)

        self.body_frame = QFrame(self.frame)
        self.body_frame.setObjectName(u"body_frame")
        self.body_frame.setMinimumSize(QSize(0, 590))
        self.body_frame.setMaximumSize(QSize(16777215, 590))
        self.body_frame.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"")
        self.body_frame.setFrameShape(QFrame.NoFrame)
        self.body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.body_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_2 = QFrame(self.body_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(640, 572))
        self.frame_2.setMaximumSize(QSize(640, 572))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"    background: #55c5bf;\n"
"    border-color: #000000;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-radius: 32px 32px 32px 32px;")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)

        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(250, 40))
        self.pushButton_2.setMaximumSize(QSize(250, 40))
        font1 = QFont()
        font1.setFamilies([u"Helvetica"])
        font1.setPointSize(19)
        font1.setBold(True)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"   color: #333;\n"
"    border: 2px rounded ;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: #fefb64;\n"
"	padding: 5 px;\n"
"font-family: \"Helvetica\";\n"
"font-weight: bold;\n"
"text-align: center;\n"
"\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(253, 130, 127);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(214, 218, 218)\n"
"    }\n"
"\n"
"")

        self.horizontalLayout_10.addWidget(self.pushButton_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, -1, 20, 8)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamilies([u"Devanagari Sangam MN"])
        font2.setPointSize(21)
        font2.setBold(False)
        font2.setStrikeOut(False)
        font2.setKerning(False)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"border:0px;")
        self.label_3.setWordWrap(True)
        self.label_3.setIndent(0)

        self.verticalLayout.addWidget(self.label_3)

        self.plainTextEdit = QPlainTextEdit(self.frame_4)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy2)
        self.plainTextEdit.setMinimumSize(QSize(300, 0))
        self.plainTextEdit.setMaximumSize(QSize(300, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Helvetica"])
        font3.setBold(False)
        self.plainTextEdit.setFont(font3)
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit{\n"
"	padding: 4px 8px 4px 8px;\n"
"    background: #ffffff;\n"
"    color: #00000;\n"
"    border-color: #232323;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-radius: 8px 8px 8px 8px;\n"
"    font-family: \"Helvetica\";\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"    line-height: 1.3;\n"
"    text-align: left;\n"
"}")
        self.plainTextEdit.setReadOnly(False)
        self.plainTextEdit.setOverwriteMode(False)
        self.plainTextEdit.setBackgroundVisible(True)

        self.verticalLayout.addWidget(self.plainTextEdit)


        self.horizontalLayout_8.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, -1, 5, -1)
        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setFamilies([u"Devanagari Sangam MN"])
        font4.setPointSize(21)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"border:0px;")
        self.label_4.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_4)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QSize(200, 0))
        self.comboBox.setMaximumSize(QSize(200, 16777215))
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(False)
        self.comboBox.setFont(font5)
        self.comboBox.setStyleSheet(u"background:rgb(244, 239, 255);\n"
"border:2px solid #000000;\n"
"placeholder: \"Seleccione...\";\n"
"")

        self.horizontalLayout_9.addWidget(self.comboBox)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_2 = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QSize(180, 0))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"   color: #ffffff;\n"
"    border: 2px rounded #555;\n"
"    border-radius: 11px;\n"
"    border-style: outset;\n"
"    background: #af3a11;\n"
"	padding: 5 px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(253, 146, 113);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(214, 218, 218)\n"
"    }\n"
"")

        self.horizontalLayout_6.addWidget(self.pushButton_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_8.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)


        self.verticalLayout_13.addWidget(self.frame_4)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.body_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(550, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        font6 = QFont()
        font6.setFamilies([u"Bayon"])
        font6.setPointSize(18)
        font6.setBold(True)
        font6.setUnderline(True)
        self.label_5.setFont(font6)
        self.label_5.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_5)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        self.label_8.setMinimumSize(QSize(0, 29))
        self.label_8.setMaximumSize(QSize(16777215, 29))
        font7 = QFont()
        font7.setFamilies([u"Bayon"])
        font7.setPointSize(15)
        font7.setBold(True)
        self.label_8.setFont(font7)
        self.label_8.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")

        self.verticalLayout_6.addWidget(self.label_8)

        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 40))
        self.lineEdit.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_6.addWidget(self.lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setMinimumSize(QSize(0, 29))
        self.label_9.setMaximumSize(QSize(16777215, 29))
        self.label_9.setFont(font7)
        self.label_9.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")

        self.verticalLayout_7.addWidget(self.label_9)

        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 40))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_7.addWidget(self.lineEdit_2)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)


        self.horizontalLayout_11.addLayout(self.verticalLayout_8)


        self.verticalLayout_14.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font6)
        self.label_6.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_6)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)
        self.label_10.setMinimumSize(QSize(0, 29))
        self.label_10.setMaximumSize(QSize(16777215, 29))
        self.label_10.setFont(font7)
        self.label_10.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")

        self.verticalLayout_10.addWidget(self.label_10)

        self.lineEdit_3 = QLineEdit(self.frame_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 40))
        self.lineEdit_3.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_10.addWidget(self.lineEdit_3)


        self.verticalLayout_9.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)
        self.label_11.setMinimumSize(QSize(0, 29))
        self.label_11.setMaximumSize(QSize(16777215, 29))
        self.label_11.setFont(font7)
        self.label_11.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")

        self.verticalLayout_11.addWidget(self.label_11)

        self.lineEdit_4 = QLineEdit(self.frame_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 40))
        self.lineEdit_4.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_11.addWidget(self.lineEdit_4)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        sizePolicy3.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy3)
        self.label_12.setMinimumSize(QSize(0, 29))
        self.label_12.setMaximumSize(QSize(16777215, 29))
        self.label_12.setFont(font7)
        self.label_12.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")

        self.verticalLayout_12.addWidget(self.label_12)

        self.lineEdit_5 = QLineEdit(self.frame_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(0, 40))
        self.lineEdit_5.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_12.addWidget(self.lineEdit_5)


        self.verticalLayout_11.addLayout(self.verticalLayout_12)


        self.verticalLayout_9.addLayout(self.verticalLayout_11)


        self.horizontalLayout_12.addLayout(self.verticalLayout_9)


        self.verticalLayout_14.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font6)
        self.label_7.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_7)

        self.listWidget = QListWidget(self.frame_3)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        brush = QBrush(QColor(212, 248, 255, 255))
        brush.setStyle(Qt.NoBrush)
        font8 = QFont()
        font8.setPointSize(14)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setFont(font8);
        __qlistwidgetitem.setBackground(brush);
        brush1 = QBrush(QColor(212, 248, 255, 255))
        brush1.setStyle(Qt.NoBrush)
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setFont(font8);
        __qlistwidgetitem1.setBackground(brush1);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem2.setFont(font8);
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"QListWidget\n"
"{\n"
"border : 1px solid black;\n"
"border-radius: 8px;\n"
"background : rgb(241, 255, 182);\n"
"}\n"
"\n"
" QListWidget::item:selected\n"
"{\n"
"border : 1px solid black;\n"
"border-radius: 8px;\n"
"background : rgb(224, 90, 84);\n"
"}")
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.listWidget.setMovement(QListView.Free)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setResizeMode(QListView.Adjust)
        self.listWidget.setSpacing(4)
        self.listWidget.setViewMode(QListView.ListMode)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setWordWrap(True)
        self.listWidget.setSortingEnabled(True)

        self.horizontalLayout_5.addWidget(self.listWidget)


        self.verticalLayout_14.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_3.addWidget(self.frame_3)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_4.addWidget(self.body_frame)


        self.body_layout.addWidget(self.frame)


        self.genera_verticalLayout_2.addLayout(self.body_layout)

        self.footer_Layout = QHBoxLayout()
        self.footer_Layout.setSpacing(0)
        self.footer_Layout.setObjectName(u"footer_Layout")
        self.footer_Layout.setContentsMargins(1, -1, -1, -1)
        self.back_page_pushButton = QPushButton(self.centralwidget)
        self.back_page_pushButton.setObjectName(u"back_page_pushButton")
        sizePolicy1.setHeightForWidth(self.back_page_pushButton.sizePolicy().hasHeightForWidth())
        self.back_page_pushButton.setSizePolicy(sizePolicy1)
        self.back_page_pushButton.setMinimumSize(QSize(161, 70))
        self.back_page_pushButton.setMaximumSize(QSize(160, 70))
        self.back_page_pushButton.setStyleSheet(u"QPushButton {\n"
"   color: #333;\n"
"    border: 2px rounded #555;\n"
"    border-style: outset;\n"
"    background: rgb(72, 187, 177);\n"
"	padding: 5 px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(195, 255, 187)\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(214, 218, 218)\n"
"    }\n"
"\n"
"")
        icon = QIcon()
        iconThemeName = u"PageBefore"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u":/newPrefix/IMAGES/buttons behind ( activated) .png", QSize(), QIcon.Normal, QIcon.On)
            icon.addFile(u":/newPrefix/IMAGES/buttons behind ( activated) .png", QSize(), QIcon.Disabled, QIcon.Off)
            icon.addFile(u":/newPrefix/IMAGES/buttons behind(desactivated) .png", QSize(), QIcon.Disabled, QIcon.On)
        
        self.back_page_pushButton.setIcon(icon)
        self.back_page_pushButton.setIconSize(QSize(40, 40))
        self.back_page_pushButton.setCheckable(False)
        self.back_page_pushButton.setAutoExclusive(False)
        self.back_page_pushButton.setAutoDefault(False)

        self.footer_Layout.addWidget(self.back_page_pushButton)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy4)
        self.frame_5.setMinimumSize(QSize(161, 70))
        self.frame_5.setMaximumSize(QSize(16777215, 70))
        self.frame_5.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"    background: #ffffff;\n"
"	border-color: #00000;\n"
"	border-top: 2px solid;\n"
"	border-bottom: 1px solid;\n"
"\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 7, -1, 7)
        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QSize(101, 40))
        self.label_13.setMaximumSize(QSize(101, 40))
        font9 = QFont()
        font9.setFamilies([u"Helvetica"])
        font9.setPointSize(30)
        font9.setBold(True)
        self.label_13.setFont(font9)
        self.label_13.setStyleSheet(u"padding: 5 px;\n"
"font-family: \"Helvetica\";\n"
"font-weight: bold;\n"
"text-align: center;\n"
"border:0px;\n"
"")

        self.horizontalLayout_7.addWidget(self.label_13)

        self.horizontalSpacer_10 = QSpacerItem(689, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_10)

        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(41)
        sizePolicy5.setVerticalStretch(121)
        sizePolicy5.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy5)
        self.label_15.setMinimumSize(QSize(121, 40))
        self.label_15.setMaximumSize(QSize(121, 40))
        self.label_15.setFont(font9)
        self.label_15.setStyleSheet(u"padding: 5 px;\n"
"font-family: \"Helvetica\";\n"
"font-weight: bold;\n"
"text-align: center;\n"
"border:0px;")

        self.horizontalLayout_7.addWidget(self.label_15)


        self.footer_Layout.addWidget(self.frame_5)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(161, 70))
        self.pushButton.setMaximumSize(QSize(160, 70))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"   color: #333;\n"
"    border: 2px rounded #555;\n"
"    border-style: outset;\n"
"    background: rgb(72, 187, 177);\n"
"	padding: 5 px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(195, 255, 187)\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(214, 218, 218)\n"
"    }\n"
"\n"
"")
        icon1 = QIcon()
        iconThemeName = u"PageAfter"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u":/newPrefix/IMAGES/ buttons after( activated) .png", QSize(), QIcon.Normal, QIcon.On)
            icon1.addFile(u":/newPrefix/IMAGES/ buttons after( activated) .png", QSize(), QIcon.Disabled, QIcon.Off)
            icon1.addFile(u":/newPrefix/IMAGES/ buttons after( desactivated) .png", QSize(), QIcon.Disabled, QIcon.On)
        
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(40, 40))

        self.footer_Layout.addWidget(self.pushButton)


        self.genera_verticalLayout_2.addLayout(self.footer_Layout)


        self.verticalLayout_15.addLayout(self.genera_verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.back_page_pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"KNOW BETTER", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"COMO USAR LA APP?", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Digite en este campo el texto a analizar:", None))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite el enunciado a ser analizado", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Seleccione el tema del cual  se habla en el texto:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Seleccionar", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"Seleccionar", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"ANALIZAR", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"INFORMACI\u00d3N\n"
"GENERAL", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"QUE DEBES HACER?", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"QUE INFORMACI\u00d3N TE BRINDAN?", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ESPECIFICACIONES", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"ENTRADA", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"SALIDA", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"CONDICIONES", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"PSEUDOC\u00d3DIGO", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qlistwidgetitem5 = self.listWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qlistwidgetitem6 = self.listWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qlistwidgetitem7 = self.listWidget.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"89", None));
        ___qlistwidgetitem8 = self.listWidget.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"a", None));
        ___qlistwidgetitem9 = self.listWidget.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"b", None));
        ___qlistwidgetitem10 = self.listWidget.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"c", None));
        ___qlistwidgetitem11 = self.listWidget.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"d", None));
        ___qlistwidgetitem12 = self.listWidget.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"e", None));
        ___qlistwidgetitem13 = self.listWidget.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"f", None));
        ___qlistwidgetitem14 = self.listWidget.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"h", None));
        ___qlistwidgetitem15 = self.listWidget.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"k", None));
        ___qlistwidgetitem16 = self.listWidget.item(16)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("MainWindow", u"l", None));
        ___qlistwidgetitem17 = self.listWidget.item(17)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("MainWindow", u"PASO 1: ....", None));
        ___qlistwidgetitem18 = self.listWidget.item(18)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("MainWindow", u"PASO 2: .....", None));
        ___qlistwidgetitem19 = self.listWidget.item(19)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("MainWindow", u"PASO 3: ...", None));
        ___qlistwidgetitem20 = self.listWidget.item(20)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("MainWindow", u"s", None));
        ___qlistwidgetitem21 = self.listWidget.item(21)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("MainWindow", u"v", None));
        ___qlistwidgetitem22 = self.listWidget.item(22)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("MainWindow", u"w", None));
        ___qlistwidgetitem23 = self.listWidget.item(23)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("MainWindow", u"y", None));
        ___qlistwidgetitem24 = self.listWidget.item(24)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("MainWindow", u"z", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.back_page_pushButton.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"ABOUT", None))
        self.pushButton.setText("")
    # retranslateUi

