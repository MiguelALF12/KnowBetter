# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
    QHBoxLayout, QLabel, QListView, QListWidget,
    QListWidgetItem, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import logo-header_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1150, 806)
        MainWindow.setMinimumSize(QSize(1150, 800))
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	padding: 8px 8px 8px 8px;\n"
"	background: #f9f9f9;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Header = QFrame(self.centralwidget)
        self.Header.setObjectName(u"Header")
        self.Header.setEnabled(True)
        self.Header.setMinimumSize(QSize(0, 150))
        self.Header.setStyleSheet(u"\n"
"	padding: 8px 8px 8px 8px;\n"
"	background: #bbbc3b;\n"
"	border-color: #000000;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 15px 15px 15px 15px;\n"
"")
        self.Header.setFrameShape(QFrame.StyledPanel)
        self.Header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.Header)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_16 = QLabel(self.Header)
        self.label_16.setObjectName(u"label_16")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setStyleSheet(u"border:0px;")
        self.label_16.setPixmap(QPixmap(u":/newPrefix/IMAGES/header-utp-logo.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.horizontalLayout_13.addWidget(self.label_16)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_17 = QLabel(self.Header)
        self.label_17.setObjectName(u"label_17")
        font = QFont()
        font.setPointSize(42)
        font.setBold(True)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(u"border:0px;")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_17)

        self.label_18 = QLabel(self.Header)
        self.label_18.setObjectName(u"label_18")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(False)
        self.label_18.setFont(font1)
        self.label_18.setStyleSheet(u"border:0px;")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_18.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.label_18)


        self.horizontalLayout_13.addLayout(self.verticalLayout_12)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_13)


        self.verticalLayout_2.addWidget(self.Header)

        self.Body = QFrame(self.centralwidget)
        self.Body.setObjectName(u"Body")
        self.Body.setMinimumSize(QSize(0, 520))
        self.Body.setFrameShape(QFrame.NoFrame)
        self.Body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Body)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.Input_text_frame = QFrame(self.Body)
        self.Input_text_frame.setObjectName(u"Input_text_frame")
        self.Input_text_frame.setMinimumSize(QSize(360, 0))
        self.Input_text_frame.setMaximumSize(QSize(350, 16777215))
        self.Input_text_frame.setStyleSheet(u"\n"
"	padding: 8px 8px 8px 8px;\n"
"	opacity: 85%;\n"
"	background: #f7b744;\n"
"	border-color: #000000;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 15px 15px 15px 15px;\n"
"")
        self.Input_text_frame.setFrameShape(QFrame.StyledPanel)
        self.Input_text_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Input_text_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 60, -1, 40)
        self.label = QLabel(self.Input_text_frame)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(False)
        font2.setKerning(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"QLabel {\n"
"	border: 0px;\n"
"}")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setLineWidth(0)
        self.label.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label)

        self.plainTextEdit = QPlainTextEdit(self.Input_text_frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMaximumSize(QSize(410, 16777215))
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

        self.verticalLayout_4.addWidget(self.plainTextEdit)


        self.horizontalLayout_3.addWidget(self.Input_text_frame)

        self.Category_and_search = QFrame(self.Body)
        self.Category_and_search.setObjectName(u"Category_and_search")
        self.Category_and_search.setMinimumSize(QSize(100, 0))
        self.Category_and_search.setMaximumSize(QSize(250, 16777215))
        self.Category_and_search.setFrameShape(QFrame.NoFrame)
        self.Category_and_search.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.Category_and_search)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.frame = QFrame(self.Category_and_search)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(0, 10))
        font4 = QFont()
        font4.setPointSize(18)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"")
        self.label_2.setWordWrap(True)
        self.label_2.setMargin(0)
        self.label_2.setIndent(0)

        self.verticalLayout_3.addWidget(self.label_2)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setMinimumSize(QSize(0, 0))
        self.comboBox.setFont(font4)
        self.comboBox.setStyleSheet(u"")
        self.comboBox.setMaxVisibleItems(15)
        self.comboBox.setInsertPolicy(QComboBox.InsertAtCurrent)

        self.verticalLayout_3.addWidget(self.comboBox)


        self.verticalLayout_5.addWidget(self.frame)

        self.verticalSpacer_2 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.pushButton = QPushButton(self.Category_and_search)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(130, 40))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    border: 1px rounded #555;\n"
"    border-radius: 8px;\n"
"    border-style: outset;\n"
"    background: rgb(97, 205, 255);\n"
"	padding: 5 px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: rgba(75, 141, 255, 219)\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(214, 218, 218)\n"
"    }\n"
"")

        self.verticalLayout_5.addWidget(self.pushButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)


        self.horizontalLayout_3.addWidget(self.Category_and_search)

        self.Show_analysis_frame = QFrame(self.Body)
        self.Show_analysis_frame.setObjectName(u"Show_analysis_frame")
        self.Show_analysis_frame.setStyleSheet(u"\n"
"	padding: 8px 8px 8px 8px;\n"
"	opacity: 85%;\n"
"	background: #f7b744;\n"
"	border-color: #000000;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 15px 15px 15px 15px;\n"
"")
        self.Show_analysis_frame.setFrameShape(QFrame.StyledPanel)
        self.Show_analysis_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.Show_analysis_frame)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, 0, 0)
        self.frame_2 = QFrame(self.Show_analysis_frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMaximumSize(QSize(16777215, 135))
        self.frame_2.setStyleSheet(u"border: 0px;")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setMaximumSize(QSize(150, 55))
        self.label_3.setFrameShape(QFrame.Box)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy3.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy3)
        self.frame_5.setStyleSheet(u"QPlainTextEdit{\n"
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
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
#ifndef Q_OS_MAC
        self.verticalLayout_6.setSpacing(-1)
#endif
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setWordWrap(False)

        self.horizontalLayout_6.addWidget(self.label_11)

        self.plainTextEdit_3 = QPlainTextEdit(self.frame_5)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.plainTextEdit_3.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_3.setSizePolicy(sizePolicy4)
        self.plainTextEdit_3.setMinimumSize(QSize(0, 40))
        self.plainTextEdit_3.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_3.setStyleSheet(u"padding-top: 1px;\n"
"padding-bottom: 1px;\n"
"padding-right: 15px;\n"
"\n"
"\n"
"")
        self.plainTextEdit_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.plainTextEdit_3.setOverwriteMode(False)

        self.horizontalLayout_6.addWidget(self.plainTextEdit_3)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setWordWrap(False)

        self.horizontalLayout_7.addWidget(self.label_12)

        self.plainTextEdit_4 = QPlainTextEdit(self.frame_5)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        sizePolicy4.setHeightForWidth(self.plainTextEdit_4.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_4.setSizePolicy(sizePolicy4)
        self.plainTextEdit_4.setMinimumSize(QSize(0, 40))
        self.plainTextEdit_4.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_4.setStyleSheet(u"padding-top: 1px;\n"
"padding-bottom: 1px;\n"
"padding-right: 15px;\n"
"\n"
"\n"
"")
        self.plainTextEdit_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_7.addWidget(self.plainTextEdit_4)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.verticalLayout_6.addLayout(self.verticalLayout)


        self.horizontalLayout_5.addWidget(self.frame_5)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.Show_analysis_frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy4.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy4)
        self.frame_3.setMaximumSize(QSize(16777215, 185))
        self.frame_3.setStyleSheet(u"border: 0px;")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setMaximumSize(QSize(150, 55))
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_4)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QPlainTextEdit{\n"
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
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
#ifndef Q_OS_MAC
        self.verticalLayout_9.setSpacing(-1)
#endif
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_8.addWidget(self.label_13)

        self.horizontalSpacer_3 = QSpacerItem(10, 15, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.plainTextEdit_5 = QPlainTextEdit(self.frame_6)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        sizePolicy4.setHeightForWidth(self.plainTextEdit_5.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_5.setSizePolicy(sizePolicy4)
        self.plainTextEdit_5.setMinimumSize(QSize(0, 40))
        self.plainTextEdit_5.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_5.setStyleSheet(u"padding-top: 1px;\n"
"padding-bottom: 1px;\n"
"padding-right: 15px;\n"
"\n"
"\n"
"")
        self.plainTextEdit_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_8.addWidget(self.plainTextEdit_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_14 = QLabel(self.frame_6)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_9.addWidget(self.label_14)

        self.horizontalSpacer_4 = QSpacerItem(25, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.plainTextEdit_6 = QPlainTextEdit(self.frame_6)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")
        sizePolicy4.setHeightForWidth(self.plainTextEdit_6.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_6.setSizePolicy(sizePolicy4)
        self.plainTextEdit_6.setMinimumSize(QSize(0, 40))
        self.plainTextEdit_6.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_6.setStyleSheet(u"padding-top: 1px;\n"
"padding-bottom: 1px;\n"
"padding-right: 15px;\n"
"\n"
"\n"
"")
        self.plainTextEdit_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_6.setCenterOnScroll(False)

        self.horizontalLayout_9.addWidget(self.plainTextEdit_6)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_10.addWidget(self.label_15)

        self.plainTextEdit_7 = QPlainTextEdit(self.frame_6)
        self.plainTextEdit_7.setObjectName(u"plainTextEdit_7")
        sizePolicy4.setHeightForWidth(self.plainTextEdit_7.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_7.setSizePolicy(sizePolicy4)
        self.plainTextEdit_7.setMinimumSize(QSize(0, 40))
        self.plainTextEdit_7.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_7.setStyleSheet(u"padding-top: 1px;\n"
"padding-bottom: 1px;\n"
"padding-right: 15px;\n"
"\n"
"\n"
"")
        self.plainTextEdit_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_10.addWidget(self.plainTextEdit_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)


        self.horizontalLayout.addWidget(self.frame_6)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.Show_analysis_frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setStyleSheet(u"border: 0px;")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setMaximumSize(QSize(150, 55))
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self.frame_7)
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
        font5 = QFont()
        font5.setPointSize(14)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setFont(font5);
        __qlistwidgetitem.setBackground(brush);
        brush1 = QBrush(QColor(212, 248, 255, 255))
        brush1.setStyle(Qt.NoBrush)
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setFont(font5);
        __qlistwidgetitem1.setBackground(brush1);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem2.setFont(font5);
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
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setResizeMode(QListView.Adjust)
        self.listWidget.setSpacing(2)
        self.listWidget.setViewMode(QListView.ListMode)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setWordWrap(True)
        self.listWidget.setSortingEnabled(True)

        self.verticalLayout_11.addWidget(self.listWidget)


        self.horizontalLayout_4.addWidget(self.frame_7)


        self.verticalLayout_7.addWidget(self.frame_4)


        self.horizontalLayout_3.addWidget(self.Show_analysis_frame)


        self.verticalLayout_2.addWidget(self.Body)

        self.Footer = QFrame(self.centralwidget)
        self.Footer.setObjectName(u"Footer")
        self.Footer.setMinimumSize(QSize(0, 50))
        self.Footer.setStyleSheet(u"QFrame{\n"
"\n"
"	padding: 8px 8px 8px 8px;\n"
"	background: #bbbc3b;\n"
"	border-color: #000000;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 15px 15px 15px 15px;\n"
"\n"
"}")
        self.Footer.setFrameShape(QFrame.StyledPanel)
        self.Footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Footer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_2.addWidget(self.Footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.comboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_16.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"KNOW BETTER", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"SOFTWARE ACAD\u00c9MICO PARA AYUDAR EN LA COMPRENSI\u00d3N DE TEXTOS", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Digite en este campo el texto a analizar:", None))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite el enunciado a ser analizado", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Seleccione el tema del cual se habla en el texto:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Seleccionar...", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"ANALIZAR", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"INFORMACI\u00d3N GENERAL", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"QUE DEBES HACER?", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"QUE INFORMACI\u00d3N TE \n"
"BRINDA EL EJERCICIO?", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"ESPECIFICACIONES", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"ENTRADAS", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"SALIDAS", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"CONDICIONES", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PSEUDOC\u00d3DIGO", None))

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

    # retranslateUi

