# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ABOUTv3.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import logo_header_rc
import logo_header_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1300, 870)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(1300, 870))
        Form.setMaximumSize(QSize(1300, 870))
        Form.setStyleSheet(u"background: #2f244c;")
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 1302, 802))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(175, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frame = QFrame(self.layoutWidget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(950, 800))
        self.frame.setMaximumSize(QSize(950, 800))
        self.frame.setStyleSheet(u"\n"
"background: #4b3fdd;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(0, 400))
        self.frame_2.setMaximumSize(QSize(16777215, 400))
        self.frame_2.setStyleSheet(u"/*border: 2px solid;\n"
"border-color: rgb(255, 255, 255);*/\n"
"border:0px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(470, 70))
        self.label.setMaximumSize(QSize(470, 70))
        font = QFont()
        font.setFamilies([u"Bayon"])
        font.setPointSize(60)
        self.label.setFont(font)
        self.label.setStyleSheet(u"	color: #ffffff;\n"
"	font-family: \"Bayon\";\n"
"	text-align: left;\n"
"")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(800, 230))
        self.label_2.setMaximumSize(QSize(800, 230))
        font1 = QFont()
        font1.setFamilies([u"Basic"])
        font1.setPointSize(25)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: #ffffff;\n"
"font-family: \"Basic\";\n"
"margin-left:100px;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(0, 300))
        self.frame_3.setStyleSheet(u"/*border: 2px solid;\n"
"border-color: rgb(255, 255, 255);*/")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(35, -1, -1, -1)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Basic"])
        font2.setPointSize(25)
        font2.setBold(False)
        font2.setStrikeOut(False)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: #232323;\n"
"font-family: \"Basic\";\n"
"")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.label_3)


        self.verticalLayout_7.addLayout(self.verticalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_12)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(230, 200))
        self.label_6.setMaximumSize(QSize(220, 200))
        self.label_6.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0)")
        self.label_6.setPixmap(QPixmap(u":/newPrefix/IMAGES/header-utp-logo-blanco.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_6)

        self.horizontalSpacer_13 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_13)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 2, -1, 2)
        self.horizontalSpacer_5 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamilies([u"Basic"])
        font3.setPointSize(25)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);\n"
"margin: 4px;\n"
"	color: #232323;\n"
"	font-family: \"Basic\";\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.horizontalSpacer_6 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(250, 200))
        self.label_7.setMaximumSize(QSize(220, 200))
        self.label_7.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0)")
        self.label_7.setPixmap(QPixmap(u":/newPrefix/IMAGES/header-utp-logo-blanco.png"))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_9 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)

        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);\n"
"margin: 4px;\n"
"	color: #232323;\n"
"	font-family: \"Basic\";\n"
"")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_9)

        self.horizontalSpacer_11 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_14 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_14)

        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QSize(250, 200))
        self.label_10.setMaximumSize(QSize(220, 200))
        self.label_10.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0)")
        self.label_10.setPixmap(QPixmap(u":/newPrefix/IMAGES/header-utp-logo-blanco.png"))
        self.label_10.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_10)

        self.horizontalSpacer_15 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_15)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_3.addLayout(self.verticalLayout_9)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setMinimumSize(QSize(0, 60))
        self.frame_4.setMaximumSize(QSize(16777215, 60))
        self.frame_4.setStyleSheet(u"/*border: 2px solid;\n"
"border-color: rgb(255, 255, 255);*/\n"
"border:0px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        font4 = QFont()
        font4.setFamilies([u"Basic"])
        font4.setPointSize(20)
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"\n"
"	color: #e5e5e5;\n"
"	font-family: \"Basic\";\n"
"	text-align: left;\n"
"")

        self.horizontalLayout_12.addWidget(self.label_5)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(60, 36))
        self.label_8.setMaximumSize(QSize(60, 36))
        self.label_8.setPixmap(QPixmap(u":/newPrefix/IMAGES/moqupsapp.png"))
        self.label_8.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_8)

        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMaximumSize(QSize(51, 51))
        self.label_11.setPixmap(QPixmap(u":/newPrefix/IMAGES/vexels.png"))
        self.label_11.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QSize(60, 45))
        self.label_12.setMaximumSize(QSize(64, 45))
        self.label_12.setPixmap(QPixmap(u":/newPrefix/IMAGES/qt-design.png"))
        self.label_12.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_12)

        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QSize(47, 47))
        self.label_14.setMaximumSize(QSize(47, 47))
        self.label_14.setPixmap(QPixmap(u":/newPrefix/IMAGES/python-logo.png"))
        self.label_14.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_14)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)

        self.horizontalSpacer_16 = QSpacerItem(532, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_16)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.horizontalLayout.addWidget(self.frame)

        self.horizontalSpacer_2 = QSpacerItem(175, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 800, 1300, 72))
        self.Footer_layout = QHBoxLayout(self.layoutWidget1)
        self.Footer_layout.setSpacing(0)
        self.Footer_layout.setObjectName(u"Footer_layout")
        self.Footer_layout.setContentsMargins(0, 0, 0, 0)
        self.back_page_pushButton = QPushButton(self.layoutWidget1)
        self.back_page_pushButton.setObjectName(u"back_page_pushButton")
        sizePolicy.setHeightForWidth(self.back_page_pushButton.sizePolicy().hasHeightForWidth())
        self.back_page_pushButton.setSizePolicy(sizePolicy)
        self.back_page_pushButton.setMinimumSize(QSize(161, 70))
        self.back_page_pushButton.setMaximumSize(QSize(160, 70))
        self.back_page_pushButton.setStyleSheet(u"QPushButton {\n"
"   color: #333;\n"
"    border: 2px rounded #555;\n"
"	border-bottom-left-radius: 10px;\n"
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
        icon.addFile(u":/newPrefix/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_page_pushButton.setIcon(icon)
        self.back_page_pushButton.setIconSize(QSize(95, 40))
        self.back_page_pushButton.setCheckable(False)
        self.back_page_pushButton.setAutoExclusive(False)
        self.back_page_pushButton.setAutoDefault(False)

        self.Footer_layout.addWidget(self.back_page_pushButton)

        self.Spacer_between_buttons = QSpacerItem(976, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.Footer_layout.addItem(self.Spacer_between_buttons)

        self.front_page_pushButton = QPushButton(self.layoutWidget1)
        self.front_page_pushButton.setObjectName(u"front_page_pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.front_page_pushButton.sizePolicy().hasHeightForWidth())
        self.front_page_pushButton.setSizePolicy(sizePolicy2)
        self.front_page_pushButton.setMinimumSize(QSize(161, 70))
        self.front_page_pushButton.setMaximumSize(QSize(160, 70))
        self.front_page_pushButton.setStyleSheet(u"QPushButton {\n"
"   color: #333;\n"
"    border: 2px rounded #555;\n"
"    border-style: outset;\n"
"	border-bottom-right-radius: 10px;\n"
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
        icon1.addFile(u":/newPrefix/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.front_page_pushButton.setIcon(icon1)
        self.front_page_pushButton.setIconSize(QSize(100, 40))

        self.Footer_layout.addWidget(self.front_page_pushButton)


        self.retranslateUi(Form)
        self.back_page_pushButton.clicked.connect(Form.close)

        self.back_page_pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"SOBRE KNOW BETTER", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Es un aplicativo que ayuda en la comprensi\u00f3n de peque\u00f1os textos (generalmente en forma de ejercicios) guiados prinicipalmente en el tema de programaci\u00f3n.\n"
"\n"
"Funciona mediante la lectura de un conjunto de mas 20 ejercicios de programaci\u00f3n analizados de manera individual separando las ideas principales de cada uno.", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Desarrollado por:", None))
        self.label_6.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"EN: ", None))
        self.label_7.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"PARA:", None))
        self.label_10.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Herramientas:", None))
        self.label_8.setText("")
        self.label_11.setText("")
        self.label_12.setText("")
        self.label_14.setText("")
        self.back_page_pushButton.setText("")
        self.front_page_pushButton.setText("")
    # retranslateUi

