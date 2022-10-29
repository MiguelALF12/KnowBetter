# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MAINv3.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import logo_header_rc
import logo_header_rc
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
        Form.setStyleSheet(u"padding:0px;")
        self.body_horizontalFrame = QFrame(Form)
        self.body_horizontalFrame.setObjectName(u"body_horizontalFrame")
        self.body_horizontalFrame.setGeometry(QRect(0, 0, 1300, 870))
        sizePolicy.setHeightForWidth(self.body_horizontalFrame.sizePolicy().hasHeightForWidth())
        self.body_horizontalFrame.setSizePolicy(sizePolicy)
        self.body_horizontalFrame.setMinimumSize(QSize(1300, 870))
        self.body_horizontalFrame.setMaximumSize(QSize(1280, 870))
        self.body_horizontalFrame.setStyleSheet(u"background-image: url(:/newPrefix/IMAGES/background image.png);")
        self.body_horizontalFrame.setFrameShape(QFrame.NoFrame)
        self.body_horizontalFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.body_horizontalFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.body_header_frame = QFrame(self.body_horizontalFrame)
        self.body_header_frame.setObjectName(u"body_header_frame")
        self.body_header_frame.setMinimumSize(QSize(0, 200))
        self.body_header_frame.setMaximumSize(QSize(16777215, 150))
        self.body_header_frame.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);")
        self.body_header_frame.setFrameShape(QFrame.Panel)
        self.body_header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.body_header_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(140, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.UTP_logo = QLabel(self.body_header_frame)
        self.UTP_logo.setObjectName(u"UTP_logo")
        self.UTP_logo.setMinimumSize(QSize(220, 150))
        self.UTP_logo.setMaximumSize(QSize(220, 200))
        self.UTP_logo.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0)")
        self.UTP_logo.setPixmap(QPixmap(u":/newPrefix/IMAGES/header-utp-logo-blanco.png"))
        self.UTP_logo.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.UTP_logo)

        self.horizontalSpacer_5 = QSpacerItem(480, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.appTitle_label = QLabel(self.body_header_frame)
        self.appTitle_label.setObjectName(u"appTitle_label")
        self.appTitle_label.setMinimumSize(QSize(0, 100))
        self.appTitle_label.setMaximumSize(QSize(16777215, 200))
        font = QFont()
        font.setFamilies([u"Bayon"])
        font.setPointSize(78)
        font.setBold(True)
        self.appTitle_label.setFont(font)
        self.appTitle_label.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")
        self.appTitle_label.setAlignment(Qt.AlignCenter)
        self.appTitle_label.setWordWrap(False)

        self.horizontalLayout_3.addWidget(self.appTitle_label)

        self.horizontalSpacer_6 = QSpacerItem(140, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addWidget(self.body_header_frame)

        self.body_input_show_frame = QFrame(self.body_horizontalFrame)
        self.body_input_show_frame.setObjectName(u"body_input_show_frame")
        self.body_input_show_frame.setMinimumSize(QSize(0, 600))
        self.body_input_show_frame.setMaximumSize(QSize(16777215, 590))
        self.body_input_show_frame.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"")
        self.body_input_show_frame.setFrameShape(QFrame.NoFrame)
        self.body_input_show_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.body_input_show_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.body_input_show_horizontalLayout = QHBoxLayout()
        self.body_input_show_horizontalLayout.setSpacing(0)
        self.body_input_show_horizontalLayout.setObjectName(u"body_input_show_horizontalLayout")
        self.body_input_left_side_frame = QFrame(self.body_input_show_frame)
        self.body_input_left_side_frame.setObjectName(u"body_input_left_side_frame")
        self.body_input_left_side_frame.setMinimumSize(QSize(560, 572))
        self.body_input_left_side_frame.setMaximumSize(QSize(550, 572))
        self.body_input_left_side_frame.setFrameShape(QFrame.StyledPanel)
        self.body_input_left_side_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.body_input_left_side_frame)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 25)
        self.input_info_frame = QFrame(self.body_input_left_side_frame)
        self.input_info_frame.setObjectName(u"input_info_frame")
        self.input_info_frame.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"    background: #55c5bf;\n"
"    border-color: #000000;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-radius: 32px 32px 32px 32px;")
        self.input_info_frame.setFrameShape(QFrame.NoFrame)
        self.input_info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.input_info_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.bodyInputInfoTitle_label = QLabel(self.input_info_frame)
        self.bodyInputInfoTitle_label.setObjectName(u"bodyInputInfoTitle_label")
        font1 = QFont()
        font1.setPointSize(34)
        font1.setBold(True)
        self.bodyInputInfoTitle_label.setFont(font1)
        self.bodyInputInfoTitle_label.setStyleSheet(u"border:0px;")
        self.bodyInputInfoTitle_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.bodyInputInfoTitle_label)

        self.input_info_internal_layout = QHBoxLayout()
        self.input_info_internal_layout.setObjectName(u"input_info_internal_layout")
        self.left_side_input_info_layout = QVBoxLayout()
        self.left_side_input_info_layout.setObjectName(u"left_side_input_info_layout")
        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.left_side_input_info_layout.addItem(self.verticalSpacer)

        self.typeTheTextTitle_label = QLabel(self.input_info_frame)
        self.typeTheTextTitle_label.setObjectName(u"typeTheTextTitle_label")
        font2 = QFont()
        font2.setFamilies([u"Devanagari Sangam MN"])
        font2.setPointSize(21)
        font2.setBold(False)
        font2.setStrikeOut(False)
        font2.setKerning(False)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.typeTheTextTitle_label.setFont(font2)
        self.typeTheTextTitle_label.setStyleSheet(u"border:0px;")
        self.typeTheTextTitle_label.setAlignment(Qt.AlignCenter)
        self.typeTheTextTitle_label.setWordWrap(True)
        self.typeTheTextTitle_label.setIndent(0)

        self.left_side_input_info_layout.addWidget(self.typeTheTextTitle_label)

        self.analize_button_horizontalLayout_2 = QHBoxLayout()
        self.analize_button_horizontalLayout_2.setSpacing(0)
        self.analize_button_horizontalLayout_2.setObjectName(u"analize_button_horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.analize_button_horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.analize_pushButton = QPushButton(self.input_info_frame)
        self.analize_pushButton.setObjectName(u"analize_pushButton")
        sizePolicy.setHeightForWidth(self.analize_pushButton.sizePolicy().hasHeightForWidth())
        self.analize_pushButton.setSizePolicy(sizePolicy)
        self.analize_pushButton.setMinimumSize(QSize(180, 0))
        self.analize_pushButton.setStyleSheet(u"QPushButton {\n"
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

        self.analize_button_horizontalLayout_2.addWidget(self.analize_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.analize_button_horizontalLayout_2.addItem(self.horizontalSpacer)


        self.left_side_input_info_layout.addLayout(self.analize_button_horizontalLayout_2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.HowToUseTheAPP_pushButton_4 = QPushButton(self.input_info_frame)
        self.HowToUseTheAPP_pushButton_4.setObjectName(u"HowToUseTheAPP_pushButton_4")
        sizePolicy.setHeightForWidth(self.HowToUseTheAPP_pushButton_4.sizePolicy().hasHeightForWidth())
        self.HowToUseTheAPP_pushButton_4.setSizePolicy(sizePolicy)
        self.HowToUseTheAPP_pushButton_4.setMinimumSize(QSize(150, 40))
        self.HowToUseTheAPP_pushButton_4.setMaximumSize(QSize(150, 40))
        font3 = QFont()
        font3.setFamilies([u"Helvetica"])
        font3.setPointSize(13)
        font3.setBold(True)
        self.HowToUseTheAPP_pushButton_4.setFont(font3)
        self.HowToUseTheAPP_pushButton_4.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_11.addWidget(self.HowToUseTheAPP_pushButton_4)


        self.left_side_input_info_layout.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.left_side_input_info_layout.addItem(self.verticalSpacer_2)


        self.input_info_internal_layout.addLayout(self.left_side_input_info_layout)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, -1, 5, -1)
        self.typeTextArea_PlainTextEdit = QPlainTextEdit(self.input_info_frame)
        self.typeTextArea_PlainTextEdit.setObjectName(u"typeTextArea_PlainTextEdit")
        sizePolicy.setHeightForWidth(self.typeTextArea_PlainTextEdit.sizePolicy().hasHeightForWidth())
        self.typeTextArea_PlainTextEdit.setSizePolicy(sizePolicy)
        self.typeTextArea_PlainTextEdit.setMinimumSize(QSize(250, 400))
        self.typeTextArea_PlainTextEdit.setMaximumSize(QSize(250, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Helvetica"])
        font4.setBold(False)
        self.typeTextArea_PlainTextEdit.setFont(font4)
        self.typeTextArea_PlainTextEdit.setStyleSheet(u"QPlainTextEdit{\n"
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
        self.typeTextArea_PlainTextEdit.setReadOnly(False)
        self.typeTextArea_PlainTextEdit.setOverwriteMode(False)
        self.typeTextArea_PlainTextEdit.setBackgroundVisible(True)

        self.verticalLayout_8.addWidget(self.typeTextArea_PlainTextEdit)


        self.input_info_internal_layout.addLayout(self.verticalLayout_8)


        self.verticalLayout_4.addLayout(self.input_info_internal_layout)


        self.verticalLayout_14.addWidget(self.input_info_frame)


        self.body_input_show_horizontalLayout.addWidget(self.body_input_left_side_frame)

        self.body_input_right_side_frame = QFrame(self.body_input_show_frame)
        self.body_input_right_side_frame.setObjectName(u"body_input_right_side_frame")
        self.body_input_right_side_frame.setMinimumSize(QSize(590, 0))
        self.body_input_right_side_frame.setFrameShape(QFrame.StyledPanel)
        self.body_input_right_side_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.body_input_right_side_frame)
        self.verticalLayout_15.setSpacing(18)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.generalInfo_layout = QHBoxLayout()
        self.generalInfo_layout.setObjectName(u"generalInfo_layout")
        self.generalInfo_label = QLabel(self.body_input_right_side_frame)
        self.generalInfo_label.setObjectName(u"generalInfo_label")
        font5 = QFont()
        font5.setFamilies([u"Bayon"])
        font5.setPointSize(18)
        font5.setBold(True)
        font5.setUnderline(True)
        self.generalInfo_label.setFont(font5)
        self.generalInfo_label.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")
        self.generalInfo_label.setAlignment(Qt.AlignCenter)

        self.generalInfo_layout.addWidget(self.generalInfo_label)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.ToDo_label = QLabel(self.body_input_right_side_frame)
        self.ToDo_label.setObjectName(u"ToDo_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ToDo_label.sizePolicy().hasHeightForWidth())
        self.ToDo_label.setSizePolicy(sizePolicy1)
        self.ToDo_label.setMinimumSize(QSize(0, 29))
        self.ToDo_label.setMaximumSize(QSize(16777215, 29))
        font6 = QFont()
        font6.setFamilies([u"Bayon"])
        font6.setPointSize(15)
        font6.setBold(True)
        self.ToDo_label.setFont(font6)
        self.ToDo_label.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")
        self.ToDo_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_10.addWidget(self.ToDo_label)

        self.ToDoList_QListWidget = QListWidget(self.body_input_right_side_frame)
        QListWidgetItem(self.ToDoList_QListWidget)
        QListWidgetItem(self.ToDoList_QListWidget)
        QListWidgetItem(self.ToDoList_QListWidget)
        QListWidgetItem(self.ToDoList_QListWidget)
        QListWidgetItem(self.ToDoList_QListWidget)
        QListWidgetItem(self.ToDoList_QListWidget)
        QListWidgetItem(self.ToDoList_QListWidget)
        QListWidgetItem(self.ToDoList_QListWidget)
        QListWidgetItem(self.ToDoList_QListWidget)
        QListWidgetItem(self.ToDoList_QListWidget)
        QListWidgetItem(self.ToDoList_QListWidget)
        QListWidgetItem(self.ToDoList_QListWidget)
        QListWidgetItem(self.ToDoList_QListWidget)
        QListWidgetItem(self.ToDoList_QListWidget)
        QListWidgetItem(self.ToDoList_QListWidget)
        QListWidgetItem(self.ToDoList_QListWidget)
        QListWidgetItem(self.ToDoList_QListWidget)
        brush = QBrush(QColor(212, 248, 255, 255))
        brush.setStyle(Qt.NoBrush)
        font7 = QFont()
        font7.setPointSize(14)
        __qlistwidgetitem = QListWidgetItem(self.ToDoList_QListWidget)
        __qlistwidgetitem.setFont(font7);
        __qlistwidgetitem.setBackground(brush);
        brush1 = QBrush(QColor(212, 248, 255, 255))
        brush1.setStyle(Qt.NoBrush)
        __qlistwidgetitem1 = QListWidgetItem(self.ToDoList_QListWidget)
        __qlistwidgetitem1.setFont(font7);
        __qlistwidgetitem1.setBackground(brush1);
        __qlistwidgetitem2 = QListWidgetItem(self.ToDoList_QListWidget)
        __qlistwidgetitem2.setFont(font7);
        QListWidgetItem(self.ToDoList_QListWidget)
        QListWidgetItem(self.ToDoList_QListWidget)
        QListWidgetItem(self.ToDoList_QListWidget)
        QListWidgetItem(self.ToDoList_QListWidget)
        QListWidgetItem(self.ToDoList_QListWidget)
        self.ToDoList_QListWidget.setObjectName(u"ToDoList_QListWidget")
        self.ToDoList_QListWidget.setStyleSheet(u"QListWidget\n"
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
        self.ToDoList_QListWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ToDoList_QListWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.ToDoList_QListWidget.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.SelectedClicked)
        self.ToDoList_QListWidget.setProperty("showDropIndicator", False)
        self.ToDoList_QListWidget.setDragDropMode(QAbstractItemView.DragOnly)
        self.ToDoList_QListWidget.setDefaultDropAction(Qt.IgnoreAction)
        self.ToDoList_QListWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.ToDoList_QListWidget.setMovement(QListView.Free)
        self.ToDoList_QListWidget.setProperty("isWrapping", False)
        self.ToDoList_QListWidget.setResizeMode(QListView.Adjust)
        self.ToDoList_QListWidget.setSpacing(4)
        self.ToDoList_QListWidget.setViewMode(QListView.ListMode)
        self.ToDoList_QListWidget.setUniformItemSizes(False)
        self.ToDoList_QListWidget.setWordWrap(True)
        self.ToDoList_QListWidget.setSortingEnabled(True)

        self.verticalLayout_10.addWidget(self.ToDoList_QListWidget)

        self.givenInfo_label = QLabel(self.body_input_right_side_frame)
        self.givenInfo_label.setObjectName(u"givenInfo_label")
        sizePolicy1.setHeightForWidth(self.givenInfo_label.sizePolicy().hasHeightForWidth())
        self.givenInfo_label.setSizePolicy(sizePolicy1)
        self.givenInfo_label.setMinimumSize(QSize(0, 29))
        self.givenInfo_label.setMaximumSize(QSize(16777215, 29))
        self.givenInfo_label.setFont(font6)
        self.givenInfo_label.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")

        self.verticalLayout_10.addWidget(self.givenInfo_label)

        self.givenInfo_QListWidget = QListWidget(self.body_input_right_side_frame)
        QListWidgetItem(self.givenInfo_QListWidget)
        QListWidgetItem(self.givenInfo_QListWidget)
        QListWidgetItem(self.givenInfo_QListWidget)
        QListWidgetItem(self.givenInfo_QListWidget)
        QListWidgetItem(self.givenInfo_QListWidget)
        QListWidgetItem(self.givenInfo_QListWidget)
        QListWidgetItem(self.givenInfo_QListWidget)
        QListWidgetItem(self.givenInfo_QListWidget)
        QListWidgetItem(self.givenInfo_QListWidget)
        QListWidgetItem(self.givenInfo_QListWidget)
        QListWidgetItem(self.givenInfo_QListWidget)
        QListWidgetItem(self.givenInfo_QListWidget)
        QListWidgetItem(self.givenInfo_QListWidget)
        QListWidgetItem(self.givenInfo_QListWidget)
        QListWidgetItem(self.givenInfo_QListWidget)
        QListWidgetItem(self.givenInfo_QListWidget)
        QListWidgetItem(self.givenInfo_QListWidget)
        brush2 = QBrush(QColor(212, 248, 255, 255))
        brush2.setStyle(Qt.NoBrush)
        __qlistwidgetitem3 = QListWidgetItem(self.givenInfo_QListWidget)
        __qlistwidgetitem3.setFont(font7);
        __qlistwidgetitem3.setBackground(brush2);
        brush3 = QBrush(QColor(212, 248, 255, 255))
        brush3.setStyle(Qt.NoBrush)
        __qlistwidgetitem4 = QListWidgetItem(self.givenInfo_QListWidget)
        __qlistwidgetitem4.setFont(font7);
        __qlistwidgetitem4.setBackground(brush3);
        __qlistwidgetitem5 = QListWidgetItem(self.givenInfo_QListWidget)
        __qlistwidgetitem5.setFont(font7);
        QListWidgetItem(self.givenInfo_QListWidget)
        QListWidgetItem(self.givenInfo_QListWidget)
        QListWidgetItem(self.givenInfo_QListWidget)
        QListWidgetItem(self.givenInfo_QListWidget)
        QListWidgetItem(self.givenInfo_QListWidget)
        self.givenInfo_QListWidget.setObjectName(u"givenInfo_QListWidget")
        self.givenInfo_QListWidget.setStyleSheet(u"QListWidget\n"
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
        self.givenInfo_QListWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.givenInfo_QListWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.givenInfo_QListWidget.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.SelectedClicked)
        self.givenInfo_QListWidget.setProperty("showDropIndicator", False)
        self.givenInfo_QListWidget.setDragDropMode(QAbstractItemView.DragOnly)
        self.givenInfo_QListWidget.setDefaultDropAction(Qt.IgnoreAction)
        self.givenInfo_QListWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.givenInfo_QListWidget.setMovement(QListView.Free)
        self.givenInfo_QListWidget.setProperty("isWrapping", False)
        self.givenInfo_QListWidget.setResizeMode(QListView.Adjust)
        self.givenInfo_QListWidget.setSpacing(4)
        self.givenInfo_QListWidget.setViewMode(QListView.ListMode)
        self.givenInfo_QListWidget.setUniformItemSizes(False)
        self.givenInfo_QListWidget.setWordWrap(True)
        self.givenInfo_QListWidget.setSortingEnabled(True)

        self.verticalLayout_10.addWidget(self.givenInfo_QListWidget)


        self.generalInfo_layout.addLayout(self.verticalLayout_10)


        self.verticalLayout_15.addLayout(self.generalInfo_layout)

        self.specifications_layout = QHBoxLayout()
        self.specifications_layout.setObjectName(u"specifications_layout")
        self.specifications_label = QLabel(self.body_input_right_side_frame)
        self.specifications_label.setObjectName(u"specifications_label")
        self.specifications_label.setFont(font5)
        self.specifications_label.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")
        self.specifications_label.setAlignment(Qt.AlignCenter)

        self.specifications_layout.addWidget(self.specifications_label)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.input_label = QLabel(self.body_input_right_side_frame)
        self.input_label.setObjectName(u"input_label")
        sizePolicy1.setHeightForWidth(self.input_label.sizePolicy().hasHeightForWidth())
        self.input_label.setSizePolicy(sizePolicy1)
        self.input_label.setMinimumSize(QSize(0, 29))
        self.input_label.setMaximumSize(QSize(16777215, 29))
        self.input_label.setFont(font6)
        self.input_label.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")

        self.verticalLayout_17.addWidget(self.input_label)

        self.input_QLineEdit = QLineEdit(self.body_input_right_side_frame)
        self.input_QLineEdit.setObjectName(u"input_QLineEdit")
        self.input_QLineEdit.setMinimumSize(QSize(0, 36))
        self.input_QLineEdit.setMaximumSize(QSize(16777215, 36))
        font8 = QFont()
        font8.setPointSize(18)
        self.input_QLineEdit.setFont(font8)
        self.input_QLineEdit.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.input_QLineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.input_QLineEdit.setClearButtonEnabled(False)

        self.verticalLayout_17.addWidget(self.input_QLineEdit)

        self.condition_label = QLabel(self.body_input_right_side_frame)
        self.condition_label.setObjectName(u"condition_label")
        sizePolicy1.setHeightForWidth(self.condition_label.sizePolicy().hasHeightForWidth())
        self.condition_label.setSizePolicy(sizePolicy1)
        self.condition_label.setMinimumSize(QSize(0, 29))
        self.condition_label.setMaximumSize(QSize(16777215, 29))
        self.condition_label.setFont(font6)
        self.condition_label.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")

        self.verticalLayout_17.addWidget(self.condition_label)

        self.conditions_QLineEdit = QLineEdit(self.body_input_right_side_frame)
        self.conditions_QLineEdit.setObjectName(u"conditions_QLineEdit")
        self.conditions_QLineEdit.setMinimumSize(QSize(0, 36))
        self.conditions_QLineEdit.setMaximumSize(QSize(16777215, 36))
        self.conditions_QLineEdit.setFont(font8)
        self.conditions_QLineEdit.setStyleSheet(u"color: rgb(255, 255, 255)")

        self.verticalLayout_17.addWidget(self.conditions_QLineEdit)

        self.output_label = QLabel(self.body_input_right_side_frame)
        self.output_label.setObjectName(u"output_label")
        sizePolicy1.setHeightForWidth(self.output_label.sizePolicy().hasHeightForWidth())
        self.output_label.setSizePolicy(sizePolicy1)
        self.output_label.setMinimumSize(QSize(0, 29))
        self.output_label.setMaximumSize(QSize(16777215, 29))
        self.output_label.setFont(font6)
        self.output_label.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")

        self.verticalLayout_17.addWidget(self.output_label)

        self.output_QLineEdit = QLineEdit(self.body_input_right_side_frame)
        self.output_QLineEdit.setObjectName(u"output_QLineEdit")
        self.output_QLineEdit.setMinimumSize(QSize(0, 36))
        self.output_QLineEdit.setMaximumSize(QSize(16777215, 36))
        self.output_QLineEdit.setFont(font8)
        self.output_QLineEdit.setStyleSheet(u"color: rgb(255, 255, 255)")

        self.verticalLayout_17.addWidget(self.output_QLineEdit)


        self.specifications_layout.addLayout(self.verticalLayout_17)


        self.verticalLayout_15.addLayout(self.specifications_layout)

        self.pseudocode_layout = QHBoxLayout()
        self.pseudocode_layout.setObjectName(u"pseudocode_layout")
        self.pseudocode_label = QLabel(self.body_input_right_side_frame)
        self.pseudocode_label.setObjectName(u"pseudocode_label")
        self.pseudocode_label.setFont(font5)
        self.pseudocode_label.setStyleSheet(u"padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")
        self.pseudocode_label.setAlignment(Qt.AlignCenter)

        self.pseudocode_layout.addWidget(self.pseudocode_label)

        self.pseudocode_QListWidget = QListWidget(self.body_input_right_side_frame)
        QListWidgetItem(self.pseudocode_QListWidget)
        QListWidgetItem(self.pseudocode_QListWidget)
        QListWidgetItem(self.pseudocode_QListWidget)
        QListWidgetItem(self.pseudocode_QListWidget)
        QListWidgetItem(self.pseudocode_QListWidget)
        QListWidgetItem(self.pseudocode_QListWidget)
        QListWidgetItem(self.pseudocode_QListWidget)
        QListWidgetItem(self.pseudocode_QListWidget)
        QListWidgetItem(self.pseudocode_QListWidget)
        QListWidgetItem(self.pseudocode_QListWidget)
        QListWidgetItem(self.pseudocode_QListWidget)
        QListWidgetItem(self.pseudocode_QListWidget)
        QListWidgetItem(self.pseudocode_QListWidget)
        QListWidgetItem(self.pseudocode_QListWidget)
        QListWidgetItem(self.pseudocode_QListWidget)
        QListWidgetItem(self.pseudocode_QListWidget)
        QListWidgetItem(self.pseudocode_QListWidget)
        brush4 = QBrush(QColor(212, 248, 255, 255))
        brush4.setStyle(Qt.NoBrush)
        __qlistwidgetitem6 = QListWidgetItem(self.pseudocode_QListWidget)
        __qlistwidgetitem6.setFont(font7);
        __qlistwidgetitem6.setBackground(brush4);
        brush5 = QBrush(QColor(212, 248, 255, 255))
        brush5.setStyle(Qt.NoBrush)
        __qlistwidgetitem7 = QListWidgetItem(self.pseudocode_QListWidget)
        __qlistwidgetitem7.setFont(font7);
        __qlistwidgetitem7.setBackground(brush5);
        __qlistwidgetitem8 = QListWidgetItem(self.pseudocode_QListWidget)
        __qlistwidgetitem8.setFont(font7);
        QListWidgetItem(self.pseudocode_QListWidget)
        QListWidgetItem(self.pseudocode_QListWidget)
        QListWidgetItem(self.pseudocode_QListWidget)
        QListWidgetItem(self.pseudocode_QListWidget)
        QListWidgetItem(self.pseudocode_QListWidget)
        self.pseudocode_QListWidget.setObjectName(u"pseudocode_QListWidget")
        self.pseudocode_QListWidget.setStyleSheet(u"QListWidget\n"
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
        self.pseudocode_QListWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pseudocode_QListWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.pseudocode_QListWidget.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.SelectedClicked)
        self.pseudocode_QListWidget.setProperty("showDropIndicator", False)
        self.pseudocode_QListWidget.setDragDropMode(QAbstractItemView.DragOnly)
        self.pseudocode_QListWidget.setDefaultDropAction(Qt.IgnoreAction)
        self.pseudocode_QListWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.pseudocode_QListWidget.setMovement(QListView.Free)
        self.pseudocode_QListWidget.setProperty("isWrapping", False)
        self.pseudocode_QListWidget.setResizeMode(QListView.Adjust)
        self.pseudocode_QListWidget.setSpacing(4)
        self.pseudocode_QListWidget.setViewMode(QListView.ListMode)
        self.pseudocode_QListWidget.setUniformItemSizes(False)
        self.pseudocode_QListWidget.setWordWrap(True)
        self.pseudocode_QListWidget.setSortingEnabled(True)

        self.pseudocode_layout.addWidget(self.pseudocode_QListWidget)


        self.verticalLayout_15.addLayout(self.pseudocode_layout)


        self.body_input_show_horizontalLayout.addWidget(self.body_input_right_side_frame)


        self.horizontalLayout_9.addLayout(self.body_input_show_horizontalLayout)


        self.verticalLayout_2.addWidget(self.body_input_show_frame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.back_page_pushButton = QPushButton(self.body_horizontalFrame)
        self.back_page_pushButton.setObjectName(u"back_page_pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.back_page_pushButton.sizePolicy().hasHeightForWidth())
        self.back_page_pushButton.setSizePolicy(sizePolicy2)
        self.back_page_pushButton.setMinimumSize(QSize(161, 70))
        self.back_page_pushButton.setMaximumSize(QSize(160, 70))
        self.back_page_pushButton.setStyleSheet(u"QPushButton {\n"
"   color: #333;\n"
"    border: 2px rounded #555;\n"
"    border-style: outset;\n"
"    border-bottom-left-radius: 10px;\n"
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

        self.horizontalLayout.addWidget(self.back_page_pushButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.front_page_pushButton = QPushButton(self.body_horizontalFrame)
        self.front_page_pushButton.setObjectName(u"front_page_pushButton")
        sizePolicy2.setHeightForWidth(self.front_page_pushButton.sizePolicy().hasHeightForWidth())
        self.front_page_pushButton.setSizePolicy(sizePolicy2)
        self.front_page_pushButton.setMinimumSize(QSize(161, 70))
        self.front_page_pushButton.setMaximumSize(QSize(160, 70))
        self.front_page_pushButton.setAutoFillBackground(False)
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

        self.horizontalLayout.addWidget(self.front_page_pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)
        self.front_page_pushButton.clicked.connect(Form.close)

        self.back_page_pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.UTP_logo.setText("")
        self.appTitle_label.setText(QCoreApplication.translate("Form", u"KNOW BETTER", None))
        self.bodyInputInfoTitle_label.setText(QCoreApplication.translate("Form", u"INGRESO DE INFORMACI\u00d3N", None))
        self.typeTheTextTitle_label.setText(QCoreApplication.translate("Form", u"Digite en este campo el texto a analizar:", None))
        self.analize_pushButton.setText(QCoreApplication.translate("Form", u"ANALIZAR", None))
        self.HowToUseTheAPP_pushButton_4.setText(QCoreApplication.translate("Form", u"COMO USAR LA APP?", None))
        self.typeTextArea_PlainTextEdit.setPlainText("")
        self.typeTextArea_PlainTextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Digite el enunciado a ser analizado", None))
        self.generalInfo_label.setText(QCoreApplication.translate("Form", u"INFORMACI\u00d3N\n"
"GENERAL", None))
        self.ToDo_label.setText(QCoreApplication.translate("Form", u"QUE DEBES HACER?", None))

        __sortingEnabled = self.ToDoList_QListWidget.isSortingEnabled()
        self.ToDoList_QListWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.ToDoList_QListWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"1", None));
        ___qlistwidgetitem1 = self.ToDoList_QListWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"2", None));
        ___qlistwidgetitem2 = self.ToDoList_QListWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Form", u"3", None));
        ___qlistwidgetitem3 = self.ToDoList_QListWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Form", u"4", None));
        ___qlistwidgetitem4 = self.ToDoList_QListWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Form", u"5", None));
        ___qlistwidgetitem5 = self.ToDoList_QListWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("Form", u"6", None));
        ___qlistwidgetitem6 = self.ToDoList_QListWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("Form", u"7", None));
        ___qlistwidgetitem7 = self.ToDoList_QListWidget.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("Form", u"89", None));
        ___qlistwidgetitem8 = self.ToDoList_QListWidget.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("Form", u"a", None));
        ___qlistwidgetitem9 = self.ToDoList_QListWidget.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("Form", u"b", None));
        ___qlistwidgetitem10 = self.ToDoList_QListWidget.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("Form", u"c", None));
        ___qlistwidgetitem11 = self.ToDoList_QListWidget.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("Form", u"d", None));
        ___qlistwidgetitem12 = self.ToDoList_QListWidget.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("Form", u"e", None));
        ___qlistwidgetitem13 = self.ToDoList_QListWidget.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("Form", u"f", None));
        ___qlistwidgetitem14 = self.ToDoList_QListWidget.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("Form", u"h", None));
        ___qlistwidgetitem15 = self.ToDoList_QListWidget.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("Form", u"k", None));
        ___qlistwidgetitem16 = self.ToDoList_QListWidget.item(16)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("Form", u"l", None));
        ___qlistwidgetitem17 = self.ToDoList_QListWidget.item(17)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("Form", u"PASO 1: ....", None));
        ___qlistwidgetitem18 = self.ToDoList_QListWidget.item(18)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("Form", u"PASO 2: .....", None));
        ___qlistwidgetitem19 = self.ToDoList_QListWidget.item(19)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("Form", u"PASO 3: ...", None));
        ___qlistwidgetitem20 = self.ToDoList_QListWidget.item(20)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("Form", u"s", None));
        ___qlistwidgetitem21 = self.ToDoList_QListWidget.item(21)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("Form", u"v", None));
        ___qlistwidgetitem22 = self.ToDoList_QListWidget.item(22)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("Form", u"w", None));
        ___qlistwidgetitem23 = self.ToDoList_QListWidget.item(23)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("Form", u"y", None));
        ___qlistwidgetitem24 = self.ToDoList_QListWidget.item(24)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("Form", u"z", None));
        self.ToDoList_QListWidget.setSortingEnabled(__sortingEnabled)

        self.givenInfo_label.setText(QCoreApplication.translate("Form", u"QUE INFORMACI\u00d3N TE BRINDAN?", None))

        __sortingEnabled1 = self.givenInfo_QListWidget.isSortingEnabled()
        self.givenInfo_QListWidget.setSortingEnabled(False)
        ___qlistwidgetitem25 = self.givenInfo_QListWidget.item(0)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("Form", u"1", None));
        ___qlistwidgetitem26 = self.givenInfo_QListWidget.item(1)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("Form", u"2", None));
        ___qlistwidgetitem27 = self.givenInfo_QListWidget.item(2)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("Form", u"3", None));
        ___qlistwidgetitem28 = self.givenInfo_QListWidget.item(3)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("Form", u"4", None));
        ___qlistwidgetitem29 = self.givenInfo_QListWidget.item(4)
        ___qlistwidgetitem29.setText(QCoreApplication.translate("Form", u"5", None));
        ___qlistwidgetitem30 = self.givenInfo_QListWidget.item(5)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("Form", u"6", None));
        ___qlistwidgetitem31 = self.givenInfo_QListWidget.item(6)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("Form", u"7", None));
        ___qlistwidgetitem32 = self.givenInfo_QListWidget.item(7)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("Form", u"89", None));
        ___qlistwidgetitem33 = self.givenInfo_QListWidget.item(8)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("Form", u"a", None));
        ___qlistwidgetitem34 = self.givenInfo_QListWidget.item(9)
        ___qlistwidgetitem34.setText(QCoreApplication.translate("Form", u"b", None));
        ___qlistwidgetitem35 = self.givenInfo_QListWidget.item(10)
        ___qlistwidgetitem35.setText(QCoreApplication.translate("Form", u"c", None));
        ___qlistwidgetitem36 = self.givenInfo_QListWidget.item(11)
        ___qlistwidgetitem36.setText(QCoreApplication.translate("Form", u"d", None));
        ___qlistwidgetitem37 = self.givenInfo_QListWidget.item(12)
        ___qlistwidgetitem37.setText(QCoreApplication.translate("Form", u"e", None));
        ___qlistwidgetitem38 = self.givenInfo_QListWidget.item(13)
        ___qlistwidgetitem38.setText(QCoreApplication.translate("Form", u"f", None));
        ___qlistwidgetitem39 = self.givenInfo_QListWidget.item(14)
        ___qlistwidgetitem39.setText(QCoreApplication.translate("Form", u"h", None));
        ___qlistwidgetitem40 = self.givenInfo_QListWidget.item(15)
        ___qlistwidgetitem40.setText(QCoreApplication.translate("Form", u"k", None));
        ___qlistwidgetitem41 = self.givenInfo_QListWidget.item(16)
        ___qlistwidgetitem41.setText(QCoreApplication.translate("Form", u"l", None));
        ___qlistwidgetitem42 = self.givenInfo_QListWidget.item(17)
        ___qlistwidgetitem42.setText(QCoreApplication.translate("Form", u"PASO 1: ....", None));
        ___qlistwidgetitem43 = self.givenInfo_QListWidget.item(18)
        ___qlistwidgetitem43.setText(QCoreApplication.translate("Form", u"PASO 2: .....", None));
        ___qlistwidgetitem44 = self.givenInfo_QListWidget.item(19)
        ___qlistwidgetitem44.setText(QCoreApplication.translate("Form", u"PASO 3: ...", None));
        ___qlistwidgetitem45 = self.givenInfo_QListWidget.item(20)
        ___qlistwidgetitem45.setText(QCoreApplication.translate("Form", u"s", None));
        ___qlistwidgetitem46 = self.givenInfo_QListWidget.item(21)
        ___qlistwidgetitem46.setText(QCoreApplication.translate("Form", u"v", None));
        ___qlistwidgetitem47 = self.givenInfo_QListWidget.item(22)
        ___qlistwidgetitem47.setText(QCoreApplication.translate("Form", u"w", None));
        ___qlistwidgetitem48 = self.givenInfo_QListWidget.item(23)
        ___qlistwidgetitem48.setText(QCoreApplication.translate("Form", u"y", None));
        ___qlistwidgetitem49 = self.givenInfo_QListWidget.item(24)
        ___qlistwidgetitem49.setText(QCoreApplication.translate("Form", u"z", None));
        self.givenInfo_QListWidget.setSortingEnabled(__sortingEnabled1)

        self.specifications_label.setText(QCoreApplication.translate("Form", u"ESPECIFICACIONES", None))
        self.input_label.setText(QCoreApplication.translate("Form", u"ENTRADA", None))
        self.input_QLineEdit.setText("")
        self.condition_label.setText(QCoreApplication.translate("Form", u"CONDICIONES", None))
        self.conditions_QLineEdit.setText("")
        self.output_label.setText(QCoreApplication.translate("Form", u"SALIDA", None))
        self.output_QLineEdit.setText("")
        self.pseudocode_label.setText(QCoreApplication.translate("Form", u"PSEUDOC\u00d3DIGO", None))

        __sortingEnabled2 = self.pseudocode_QListWidget.isSortingEnabled()
        self.pseudocode_QListWidget.setSortingEnabled(False)
        ___qlistwidgetitem50 = self.pseudocode_QListWidget.item(0)
        ___qlistwidgetitem50.setText(QCoreApplication.translate("Form", u"1", None));
        ___qlistwidgetitem51 = self.pseudocode_QListWidget.item(1)
        ___qlistwidgetitem51.setText(QCoreApplication.translate("Form", u"2", None));
        ___qlistwidgetitem52 = self.pseudocode_QListWidget.item(2)
        ___qlistwidgetitem52.setText(QCoreApplication.translate("Form", u"3", None));
        ___qlistwidgetitem53 = self.pseudocode_QListWidget.item(3)
        ___qlistwidgetitem53.setText(QCoreApplication.translate("Form", u"4", None));
        ___qlistwidgetitem54 = self.pseudocode_QListWidget.item(4)
        ___qlistwidgetitem54.setText(QCoreApplication.translate("Form", u"5", None));
        ___qlistwidgetitem55 = self.pseudocode_QListWidget.item(5)
        ___qlistwidgetitem55.setText(QCoreApplication.translate("Form", u"6", None));
        ___qlistwidgetitem56 = self.pseudocode_QListWidget.item(6)
        ___qlistwidgetitem56.setText(QCoreApplication.translate("Form", u"7", None));
        ___qlistwidgetitem57 = self.pseudocode_QListWidget.item(7)
        ___qlistwidgetitem57.setText(QCoreApplication.translate("Form", u"89", None));
        ___qlistwidgetitem58 = self.pseudocode_QListWidget.item(8)
        ___qlistwidgetitem58.setText(QCoreApplication.translate("Form", u"a", None));
        ___qlistwidgetitem59 = self.pseudocode_QListWidget.item(9)
        ___qlistwidgetitem59.setText(QCoreApplication.translate("Form", u"b", None));
        ___qlistwidgetitem60 = self.pseudocode_QListWidget.item(10)
        ___qlistwidgetitem60.setText(QCoreApplication.translate("Form", u"c", None));
        ___qlistwidgetitem61 = self.pseudocode_QListWidget.item(11)
        ___qlistwidgetitem61.setText(QCoreApplication.translate("Form", u"d", None));
        ___qlistwidgetitem62 = self.pseudocode_QListWidget.item(12)
        ___qlistwidgetitem62.setText(QCoreApplication.translate("Form", u"e", None));
        ___qlistwidgetitem63 = self.pseudocode_QListWidget.item(13)
        ___qlistwidgetitem63.setText(QCoreApplication.translate("Form", u"f", None));
        ___qlistwidgetitem64 = self.pseudocode_QListWidget.item(14)
        ___qlistwidgetitem64.setText(QCoreApplication.translate("Form", u"h", None));
        ___qlistwidgetitem65 = self.pseudocode_QListWidget.item(15)
        ___qlistwidgetitem65.setText(QCoreApplication.translate("Form", u"k", None));
        ___qlistwidgetitem66 = self.pseudocode_QListWidget.item(16)
        ___qlistwidgetitem66.setText(QCoreApplication.translate("Form", u"l", None));
        ___qlistwidgetitem67 = self.pseudocode_QListWidget.item(17)
        ___qlistwidgetitem67.setText(QCoreApplication.translate("Form", u"PASO 1: ....", None));
        ___qlistwidgetitem68 = self.pseudocode_QListWidget.item(18)
        ___qlistwidgetitem68.setText(QCoreApplication.translate("Form", u"PASO 2: .....", None));
        ___qlistwidgetitem69 = self.pseudocode_QListWidget.item(19)
        ___qlistwidgetitem69.setText(QCoreApplication.translate("Form", u"PASO 3: ...", None));
        ___qlistwidgetitem70 = self.pseudocode_QListWidget.item(20)
        ___qlistwidgetitem70.setText(QCoreApplication.translate("Form", u"s", None));
        ___qlistwidgetitem71 = self.pseudocode_QListWidget.item(21)
        ___qlistwidgetitem71.setText(QCoreApplication.translate("Form", u"v", None));
        ___qlistwidgetitem72 = self.pseudocode_QListWidget.item(22)
        ___qlistwidgetitem72.setText(QCoreApplication.translate("Form", u"w", None));
        ___qlistwidgetitem73 = self.pseudocode_QListWidget.item(23)
        ___qlistwidgetitem73.setText(QCoreApplication.translate("Form", u"y", None));
        ___qlistwidgetitem74 = self.pseudocode_QListWidget.item(24)
        ___qlistwidgetitem74.setText(QCoreApplication.translate("Form", u"z", None));
        self.pseudocode_QListWidget.setSortingEnabled(__sortingEnabled2)

        self.back_page_pushButton.setText("")
        self.front_page_pushButton.setText("")
    # retranslateUi

