from PyQt5 import QtCore, QtGui, QtWidgets
from FRONTEND import aboutInterfaceV3
from BACKEND.read_analize_CSV import open_csv
from BACKEND.showInfo import describe


class MainUIForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1300, 855)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(1270, 850))
        Form.setMaximumSize(QtCore.QSize(1270, 850))
        Form.setStyleSheet("padding:0px;")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.body_horizontalFrame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body_horizontalFrame.sizePolicy().hasHeightForWidth())
        self.body_horizontalFrame.setSizePolicy(sizePolicy)
        self.body_horizontalFrame.setMinimumSize(QtCore.QSize(1300, 790))
        self.body_horizontalFrame.setMaximumSize(QtCore.QSize(1300, 790))
        self.body_horizontalFrame.setStyleSheet("background-image: url(FRONTEND/IMAGES/background image.png);")
        self.body_horizontalFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.body_horizontalFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body_horizontalFrame.setObjectName("body_horizontalFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.body_horizontalFrame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.body_header_frame = QtWidgets.QFrame(self.body_horizontalFrame)
        self.body_header_frame.setMinimumSize(QtCore.QSize(0, 200))
        self.body_header_frame.setMaximumSize(QtCore.QSize(16777215, 150))
        self.body_header_frame.setStyleSheet("padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);")
        self.body_header_frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.body_header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body_header_frame.setObjectName("body_header_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.body_header_frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(140, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.UTP_logo = QtWidgets.QLabel(self.body_header_frame)
        self.UTP_logo.setMinimumSize(QtCore.QSize(220, 150))
        self.UTP_logo.setMaximumSize(QtCore.QSize(220, 200))
        self.UTP_logo.setStyleSheet("padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0)")
        self.UTP_logo.setText("")
        self.UTP_logo.setPixmap(QtGui.QPixmap("FRONTEND/IMAGES/header-utp-logo-blanco.png"))
        self.UTP_logo.setScaledContents(True)
        self.UTP_logo.setObjectName("UTP_logo")
        self.horizontalLayout_3.addWidget(self.UTP_logo)
        spacerItem1 = QtWidgets.QSpacerItem(480, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.appTitle_label = QtWidgets.QLabel(self.body_header_frame)
        self.appTitle_label.setMinimumSize(QtCore.QSize(0, 100))
        self.appTitle_label.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily("Bayon")
        font.setPointSize(78)
        font.setBold(True)
        font.setWeight(75)
        self.appTitle_label.setFont(font)
        self.appTitle_label.setStyleSheet("padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")
        self.appTitle_label.setAlignment(QtCore.Qt.AlignCenter)
        self.appTitle_label.setWordWrap(False)
        self.appTitle_label.setObjectName("appTitle_label")
        self.horizontalLayout_3.addWidget(self.appTitle_label)
        spacerItem2 = QtWidgets.QSpacerItem(140, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.body_header_frame)
        self.body_input_show_frame = QtWidgets.QFrame(self.body_horizontalFrame)
        self.body_input_show_frame.setMinimumSize(QtCore.QSize(0, 590))
        self.body_input_show_frame.setMaximumSize(QtCore.QSize(16777215, 590))
        self.body_input_show_frame.setStyleSheet("padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"")
        self.body_input_show_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.body_input_show_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body_input_show_frame.setObjectName("body_input_show_frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.body_input_show_frame)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.body_input_show_horizontalLayout = QtWidgets.QHBoxLayout()
        self.body_input_show_horizontalLayout.setSpacing(0)
        self.body_input_show_horizontalLayout.setObjectName("body_input_show_horizontalLayout")
        self.body_input_left_side_frame = QtWidgets.QFrame(self.body_input_show_frame)
        self.body_input_left_side_frame.setMinimumSize(QtCore.QSize(560, 572))
        self.body_input_left_side_frame.setMaximumSize(QtCore.QSize(550, 572))
        self.body_input_left_side_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body_input_left_side_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body_input_left_side_frame.setObjectName("body_input_left_side_frame")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.body_input_left_side_frame)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 25)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.input_info_frame = QtWidgets.QFrame(self.body_input_left_side_frame)
        self.input_info_frame.setStyleSheet("padding: 8px 8px 8px 8px;\n"
"    background: #55c5bf;\n"
"    border-color: #000000;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-radius: 32px 32px 32px 32px;")
        self.input_info_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.input_info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_info_frame.setObjectName("input_info_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.input_info_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.bodyInputInfoTitle_label = QtWidgets.QLabel(self.input_info_frame)
        font = QtGui.QFont()
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        self.bodyInputInfoTitle_label.setFont(font)
        self.bodyInputInfoTitle_label.setStyleSheet("border:0px;")
        self.bodyInputInfoTitle_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bodyInputInfoTitle_label.setObjectName("bodyInputInfoTitle_label")
        self.verticalLayout_4.addWidget(self.bodyInputInfoTitle_label)
        self.input_info_internal_layout = QtWidgets.QHBoxLayout()
        self.input_info_internal_layout.setObjectName("input_info_internal_layout")
        self.left_side_input_info_layout = QtWidgets.QVBoxLayout()
        self.left_side_input_info_layout.setObjectName("left_side_input_info_layout")
        spacerItem3 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.left_side_input_info_layout.addItem(spacerItem3)
        self.typeTheTextTitle_label = QtWidgets.QLabel(self.input_info_frame)
        font = QtGui.QFont()
        font.setFamily("Devanagari Sangam MN")
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.typeTheTextTitle_label.setFont(font)
        self.typeTheTextTitle_label.setStyleSheet("border:0px;")
        self.typeTheTextTitle_label.setAlignment(QtCore.Qt.AlignCenter)
        self.typeTheTextTitle_label.setWordWrap(True)
        self.typeTheTextTitle_label.setIndent(0)
        self.typeTheTextTitle_label.setObjectName("typeTheTextTitle_label")
        self.left_side_input_info_layout.addWidget(self.typeTheTextTitle_label)
        self.analize_button_horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.analize_button_horizontalLayout_2.setSpacing(0)
        self.analize_button_horizontalLayout_2.setObjectName("analize_button_horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.analize_button_horizontalLayout_2.addItem(spacerItem4)

        #-------analize_pushButton-------
        self.analize_pushButton = QtWidgets.QPushButton(self.input_info_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analize_pushButton.sizePolicy().hasHeightForWidth())
        self.analize_pushButton.setSizePolicy(sizePolicy)
        self.analize_pushButton.setMinimumSize(QtCore.QSize(180, 0))
        self.analize_pushButton.setStyleSheet("QPushButton {\n"
"   color: #ffffff;\n"
"    border: 2px rounded #555;\n"
"    border-radius: 11px;\n"
"    border-style: outset;\n"
"    background: #af3a11;\n"
"    padding: 5 px;\n"
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
        self.analize_pushButton.setObjectName("analize_pushButton")

        #-----Obtain excercise from input area---
        self.analize_pushButton.clicked.connect(self.getAndSendExcercise)

        #--------analize PushButton---------



        self.analize_button_horizontalLayout_2.addWidget(self.analize_pushButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.analize_button_horizontalLayout_2.addItem(spacerItem5)
        self.left_side_input_info_layout.addLayout(self.analize_button_horizontalLayout_2)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.HowToUseTheAPP_pushButton_4 = QtWidgets.QPushButton(self.input_info_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HowToUseTheAPP_pushButton_4.sizePolicy().hasHeightForWidth())
        self.HowToUseTheAPP_pushButton_4.setSizePolicy(sizePolicy)
        self.HowToUseTheAPP_pushButton_4.setMinimumSize(QtCore.QSize(150, 40))
        self.HowToUseTheAPP_pushButton_4.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.HowToUseTheAPP_pushButton_4.setFont(font)
        self.HowToUseTheAPP_pushButton_4.setStyleSheet("QPushButton {\n"
"   color: #333;\n"
"    border: 2px rounded ;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: #fefb64;\n"
"    padding: 5 px;\n"
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
        self.HowToUseTheAPP_pushButton_4.setObjectName("HowToUseTheAPP_pushButton_4")
        self.horizontalLayout_11.addWidget(self.HowToUseTheAPP_pushButton_4)
        self.left_side_input_info_layout.addLayout(self.horizontalLayout_11)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.left_side_input_info_layout.addItem(spacerItem6)
        self.input_info_internal_layout.addLayout(self.left_side_input_info_layout)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(5, -1, 5, -1)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.typeTextArea_PlainTextEdit = QtWidgets.QPlainTextEdit(self.input_info_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typeTextArea_PlainTextEdit.sizePolicy().hasHeightForWidth())
        self.typeTextArea_PlainTextEdit.setSizePolicy(sizePolicy)
        self.typeTextArea_PlainTextEdit.setMinimumSize(QtCore.QSize(250, 400))
        self.typeTextArea_PlainTextEdit.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.typeTextArea_PlainTextEdit.setFont(font)
        self.typeTextArea_PlainTextEdit.setStyleSheet("QPlainTextEdit{\n"
"    padding: 4px 8px 4px 8px;\n"
"    background: #ffffff;\n"
"    color: #000000;\n"
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
        self.typeTextArea_PlainTextEdit.setPlainText("")
        self.typeTextArea_PlainTextEdit.setOverwriteMode(False)
        self.typeTextArea_PlainTextEdit.setBackgroundVisible(True)
        self.typeTextArea_PlainTextEdit.setObjectName("typeTextArea_PlainTextEdit")
        self.verticalLayout_8.addWidget(self.typeTextArea_PlainTextEdit)
        self.input_info_internal_layout.addLayout(self.verticalLayout_8)
        self.verticalLayout_4.addLayout(self.input_info_internal_layout)
        self.verticalLayout_14.addWidget(self.input_info_frame)
        self.body_input_show_horizontalLayout.addWidget(self.body_input_left_side_frame)
        self.body_input_right_side_frame = QtWidgets.QFrame(self.body_input_show_frame)
        self.body_input_right_side_frame.setMinimumSize(QtCore.QSize(590, 0))
        self.body_input_right_side_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body_input_right_side_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body_input_right_side_frame.setObjectName("body_input_right_side_frame")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.body_input_right_side_frame)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(18)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.generalInfo_layout = QtWidgets.QHBoxLayout()
        self.generalInfo_layout.setObjectName("generalInfo_layout")
        self.generalInfo_label = QtWidgets.QLabel(self.body_input_right_side_frame)
        font = QtGui.QFont()
        font.setFamily("Bayon")
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.generalInfo_label.setFont(font)
        self.generalInfo_label.setStyleSheet("padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")
        self.generalInfo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.generalInfo_label.setObjectName("generalInfo_label")
        self.generalInfo_layout.addWidget(self.generalInfo_label)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.ToDo_label = QtWidgets.QLabel(self.body_input_right_side_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToDo_label.sizePolicy().hasHeightForWidth())
        self.ToDo_label.setSizePolicy(sizePolicy)
        self.ToDo_label.setMinimumSize(QtCore.QSize(0, 29))
        self.ToDo_label.setMaximumSize(QtCore.QSize(16777215, 29))
        font = QtGui.QFont()
        font.setFamily("Bayon")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.ToDo_label.setFont(font)
        self.ToDo_label.setStyleSheet("padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")
        self.ToDo_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ToDo_label.setObjectName("ToDo_label")
        self.verticalLayout_10.addWidget(self.ToDo_label)
        self.ToDoList_QListWidget = QtWidgets.QListWidget(self.body_input_right_side_frame)
        self.ToDoList_QListWidget.setStyleSheet("QListWidget\n"
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
        self.ToDoList_QListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ToDoList_QListWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ToDoList_QListWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.SelectedClicked)
        self.ToDoList_QListWidget.setProperty("showDropIndicator", False)
        self.ToDoList_QListWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.ToDoList_QListWidget.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.ToDoList_QListWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.ToDoList_QListWidget.setMovement(QtWidgets.QListView.Free)
        self.ToDoList_QListWidget.setProperty("isWrapping", False)
        self.ToDoList_QListWidget.setResizeMode(QtWidgets.QListView.Adjust)
        self.ToDoList_QListWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.ToDoList_QListWidget.setUniformItemSizes(False)
        self.ToDoList_QListWidget.setWordWrap(True)
        self.ToDoList_QListWidget.setObjectName("ToDoList_QListWidget")
        self.verticalLayout_10.addWidget(self.ToDoList_QListWidget)
        self.givenInfo_label = QtWidgets.QLabel(self.body_input_right_side_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.givenInfo_label.sizePolicy().hasHeightForWidth())
        self.givenInfo_label.setSizePolicy(sizePolicy)
        self.givenInfo_label.setMinimumSize(QtCore.QSize(0, 29))
        self.givenInfo_label.setMaximumSize(QtCore.QSize(16777215, 29))
        font = QtGui.QFont()
        font.setFamily("Bayon")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.givenInfo_label.setFont(font)
        self.givenInfo_label.setStyleSheet("padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")
        self.givenInfo_label.setObjectName("givenInfo_label")
        self.verticalLayout_10.addWidget(self.givenInfo_label)
        self.givenInfo_QListWidget = QtWidgets.QListWidget(self.body_input_right_side_frame)
        self.givenInfo_QListWidget.setStyleSheet("QListWidget\n"
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
        self.givenInfo_QListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.givenInfo_QListWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.givenInfo_QListWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.SelectedClicked)
        self.givenInfo_QListWidget.setProperty("showDropIndicator", False)
        self.givenInfo_QListWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.givenInfo_QListWidget.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.givenInfo_QListWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.givenInfo_QListWidget.setMovement(QtWidgets.QListView.Free)
        self.givenInfo_QListWidget.setProperty("isWrapping", False)
        self.givenInfo_QListWidget.setResizeMode(QtWidgets.QListView.Adjust)
        self.givenInfo_QListWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.givenInfo_QListWidget.setUniformItemSizes(False)
        self.givenInfo_QListWidget.setWordWrap(True)
        self.givenInfo_QListWidget.setObjectName("givenInfo_QListWidget")
        self.verticalLayout_10.addWidget(self.givenInfo_QListWidget)
        self.generalInfo_layout.addLayout(self.verticalLayout_10)
        self.verticalLayout_15.addLayout(self.generalInfo_layout)
        self.specifications_layout = QtWidgets.QHBoxLayout()
        self.specifications_layout.setObjectName("specifications_layout")
        self.specifications_label = QtWidgets.QLabel(self.body_input_right_side_frame)
        font = QtGui.QFont()
        font.setFamily("Bayon")
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.specifications_label.setFont(font)
        self.specifications_label.setStyleSheet("padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")
        self.specifications_label.setAlignment(QtCore.Qt.AlignCenter)
        self.specifications_label.setObjectName("specifications_label")
        self.specifications_layout.addWidget(self.specifications_label)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.input_label = QtWidgets.QLabel(self.body_input_right_side_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_label.sizePolicy().hasHeightForWidth())
        self.input_label.setSizePolicy(sizePolicy)
        self.input_label.setMinimumSize(QtCore.QSize(0, 29))
        self.input_label.setMaximumSize(QtCore.QSize(16777215, 29))
        font = QtGui.QFont()
        font.setFamily("Bayon")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.input_label.setFont(font)
        self.input_label.setStyleSheet("padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")
        self.input_label.setObjectName("input_label")
        self.verticalLayout_17.addWidget(self.input_label)
        self.input_QLineEdit = QtWidgets.QLineEdit(self.body_input_right_side_frame)
        self.input_QLineEdit.setMinimumSize(QtCore.QSize(0, 36))
        self.input_QLineEdit.setMaximumSize(QtCore.QSize(16777215, 36))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.input_QLineEdit.setFont(font)
        self.input_QLineEdit.setStyleSheet("color: rgb(255, 255, 255)")
        self.input_QLineEdit.setText("")
        self.input_QLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_QLineEdit.setClearButtonEnabled(False)
        self.input_QLineEdit.setObjectName("input_QLineEdit")
        self.verticalLayout_17.addWidget(self.input_QLineEdit)
        self.condition_label = QtWidgets.QLabel(self.body_input_right_side_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.condition_label.sizePolicy().hasHeightForWidth())
        self.condition_label.setSizePolicy(sizePolicy)
        self.condition_label.setMinimumSize(QtCore.QSize(0, 29))
        self.condition_label.setMaximumSize(QtCore.QSize(16777215, 29))
        font = QtGui.QFont()
        font.setFamily("Bayon")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.condition_label.setFont(font)
        self.condition_label.setStyleSheet("padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")
        self.condition_label.setObjectName("condition_label")
        self.verticalLayout_17.addWidget(self.condition_label)
        self.conditions_QLineEdit = QtWidgets.QLineEdit(self.body_input_right_side_frame)
        self.conditions_QLineEdit.setMinimumSize(QtCore.QSize(0, 36))
        self.conditions_QLineEdit.setMaximumSize(QtCore.QSize(16777215, 36))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.conditions_QLineEdit.setFont(font)
        self.conditions_QLineEdit.setStyleSheet("color: rgb(255, 255, 255)")
        self.conditions_QLineEdit.setText("")
        self.conditions_QLineEdit.setObjectName("conditions_QLineEdit")
        self.verticalLayout_17.addWidget(self.conditions_QLineEdit)
        self.output_label = QtWidgets.QLabel(self.body_input_right_side_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_label.sizePolicy().hasHeightForWidth())
        self.output_label.setSizePolicy(sizePolicy)
        self.output_label.setMinimumSize(QtCore.QSize(0, 29))
        self.output_label.setMaximumSize(QtCore.QSize(16777215, 29))
        font = QtGui.QFont()
        font.setFamily("Bayon")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.output_label.setFont(font)
        self.output_label.setStyleSheet("padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")
        self.output_label.setObjectName("output_label")
        self.verticalLayout_17.addWidget(self.output_label)
        self.output_QLineEdit = QtWidgets.QLineEdit(self.body_input_right_side_frame)
        self.output_QLineEdit.setMinimumSize(QtCore.QSize(0, 36))
        self.output_QLineEdit.setMaximumSize(QtCore.QSize(16777215, 36))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.output_QLineEdit.setFont(font)
        self.output_QLineEdit.setStyleSheet("color: rgb(255, 255, 255)")
        self.output_QLineEdit.setText("")
        self.output_QLineEdit.setObjectName("output_QLineEdit")
        self.verticalLayout_17.addWidget(self.output_QLineEdit)
        self.specifications_layout.addLayout(self.verticalLayout_17)
        self.verticalLayout_15.addLayout(self.specifications_layout)
        self.pseudocode_layout = QtWidgets.QHBoxLayout()
        self.pseudocode_layout.setObjectName("pseudocode_layout")
        self.pseudocode_label = QtWidgets.QLabel(self.body_input_right_side_frame)
        font = QtGui.QFont()
        font.setFamily("Bayon")
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pseudocode_label.setFont(font)
        self.pseudocode_label.setStyleSheet("padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;")
        self.pseudocode_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pseudocode_label.setObjectName("pseudocode_label")
        self.pseudocode_layout.addWidget(self.pseudocode_label)
        self.pseudocode_QListWidget = QtWidgets.QListWidget(self.body_input_right_side_frame)
        self.pseudocode_QListWidget.setStyleSheet("QListWidget\n"
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
        self.pseudocode_QListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pseudocode_QListWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.pseudocode_QListWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.SelectedClicked)
        self.pseudocode_QListWidget.setProperty("showDropIndicator", False)
        self.pseudocode_QListWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.pseudocode_QListWidget.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.pseudocode_QListWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.pseudocode_QListWidget.setMovement(QtWidgets.QListView.Free)
        self.pseudocode_QListWidget.setProperty("isWrapping", False)
        self.pseudocode_QListWidget.setResizeMode(QtWidgets.QListView.Adjust)
        self.pseudocode_QListWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.pseudocode_QListWidget.setUniformItemSizes(False)
        self.pseudocode_QListWidget.setWordWrap(True)
        self.pseudocode_QListWidget.setObjectName("pseudocode_QListWidget")
        self.pseudocode_layout.addWidget(self.pseudocode_QListWidget)
        self.verticalLayout_15.addLayout(self.pseudocode_layout)
        self.body_input_show_horizontalLayout.addWidget(self.body_input_right_side_frame)
        self.horizontalLayout_9.addLayout(self.body_input_show_horizontalLayout)
        self.verticalLayout_2.addWidget(self.body_input_show_frame)
        self.verticalLayout.addWidget(self.body_horizontalFrame)

#         #----------Footer layout---------- First version
#         self.footer_Layout = QtWidgets.QHBoxLayout()
#         self.footer_Layout.setSpacing(0)
#         self.footer_Layout.setObjectName("footer_Layout")
#
#         #----------Back page button -----------
#         self.back_page_pushButton = QtWidgets.QPushButton(Form)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.back_page_pushButton.sizePolicy().hasHeightForWidth())
#         self.back_page_pushButton.setSizePolicy(sizePolicy)
#         self.back_page_pushButton.setMinimumSize(QtCore.QSize(180, 70))
#         self.back_page_pushButton.setMaximumSize(QtCore.QSize(180, 70))
#         self.back_page_pushButton.setStyleSheet("QPushButton {\n"
# "   color: #333;\n"
# "    border: 1px rounded #555;\n"
# "    border-style: outset;\n"
# "    border-bottom-left-radius: 10px;\n"
# "    background: rgb(72, 187, 177);\n"
# "    padding: 5 px;\n"
# "    }\n"
# "\n"
# "QPushButton:hover {\n"
# "    background: rgb(195, 255, 187)\n"
# "    }\n"
# "\n"
# "QPushButton:pressed {\n"
# "    border-style: inset;\n"
# "    background: rgb(214, 218, 218)\n"
# "    }\n"
# "\n"
# "")
#         self.back_page_pushButton.setText("")
#         icon = QtGui.QIcon("FRONTEND/IMAGES/buttonsBehind.png")
#         # icon = QtGui.QIcon.fromTheme("PageBefore")
#         self.back_page_pushButton.setIcon(icon)
#         self.back_page_pushButton.setIconSize(QtCore.QSize(40, 40))
#         self.back_page_pushButton.setCheckable(False)
#         self.back_page_pushButton.setAutoExclusive(False)
#         self.back_page_pushButton.setAutoDefault(False)
#         self.back_page_pushButton.setDefault(False)
#         self.back_page_pushButton.setObjectName("back_page_pushButton")
#         #----------Back page button -----------
#
#         # ----------Front page button----------
#         self.front_page_pushButton = QtWidgets.QPushButton(Form)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.front_page_pushButton.sizePolicy().hasHeightForWidth())
#         self.front_page_pushButton.setSizePolicy(sizePolicy)
#         self.front_page_pushButton.setMinimumSize(QtCore.QSize(180, 70))
#         self.front_page_pushButton.setMaximumSize(QtCore.QSize(180, 70))
#         self.front_page_pushButton.setAutoFillBackground(False)
#         self.front_page_pushButton.setStyleSheet("QPushButton {\n"
#                                                  "   color: #333;\n"
#                                                  "    border: 1px rounded #555;\n"
#                                                  "    border-style: outset;\n"
#                                                  "    border-bottom-right-radius: 10px;\n"
#                                                  "    background: rgb(72, 187, 177);\n"
#                                                  "    padding: 5 px;\n"
#                                                  "    }\n"
#                                                  "\n"
#                                                  "QPushButton:hover {\n"
#                                                  "    background: rgb(195, 255, 187)\n"
#                                                  "    }\n"
#                                                  "\n"
#                                                  "QPushButton:pressed {\n"
#                                                  "    border-style: inset;\n"
#                                                  "    background: rgb(214, 218, 218)\n"
#                                                  "    }\n"
#                                                  "\n"
#                                                  "")
#         self.front_page_pushButton.setText("")
#         icon = QtGui.QIcon("FRONTEND/IMAGES/buttonsAfter.png")
#         # icon = QtGui.QIcon.fromTheme("PageAfter")
#         self.front_page_pushButton.setIcon(icon)
#         self.front_page_pushButton.setIconSize(QtCore.QSize(40, 40))
#         self.front_page_pushButton.setObjectName("front_page_pushButton")
#         self.footer_Layout.addWidget(self.front_page_pushButton)
#         self.verticalLayout.addLayout(self.footer_Layout)
#
#         # connection to about
#         self.front_page_pushButton.clicked.connect(self.launchAbout)
#         self.front_page_pushButton.clicked.connect(Form.close)
#         # ----------Front page button----------
#
#         self.footer_Layout.addWidget(self.back_page_pushButton)
#         self.Home_About_LabelsFrame = QtWidgets.QFrame(Form)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.Home_About_LabelsFrame.sizePolicy().hasHeightForWidth())
#         self.Home_About_LabelsFrame.setSizePolicy(sizePolicy)
#         self.Home_About_LabelsFrame.setMinimumSize(QtCore.QSize(945, 70))
#         self.Home_About_LabelsFrame.setMaximumSize(QtCore.QSize(945, 70))
#         self.Home_About_LabelsFrame.setStyleSheet(
# "    background: #ffffff;\n"
# "    margin:0px;\n"
# "\n"
# "")
#         self.Home_About_LabelsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.Home_About_LabelsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.Home_About_LabelsFrame.setObjectName("Home_About_LabelsFrame")
#         self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.Home_About_LabelsFrame)
#         self.horizontalLayout_7.setContentsMargins(12,7,12,7)
#         self.horizontalLayout_7.setSpacing(5)
#         self.horizontalLayout_7.setObjectName("horizontalLayout_7")
#         self.HomeFooter_Label = QtWidgets.QLabel(self.Home_About_LabelsFrame)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.HomeFooter_Label.sizePolicy().hasHeightForWidth())
#         self.HomeFooter_Label.setSizePolicy(sizePolicy)
#         self.HomeFooter_Label.setMinimumSize(QtCore.QSize(101, 40))
#         self.HomeFooter_Label.setMaximumSize(QtCore.QSize(101, 40))
#         font = QtGui.QFont()
#         font.setFamily("Helvetica")
#         font.setPointSize(30)
#         font.setBold(True)
#         font.setWeight(75)
#         self.HomeFooter_Label.setFont(font)
#         self.HomeFooter_Label.setStyleSheet("padding: 5 px;\n"
# "font-family: \"Helvetica\";\n"
# "font-weight: bold;\n"
# "text-align: center;\n"
# "border:0px;\n"
# "")
#         self.HomeFooter_Label.setObjectName("HomeFooter_Label")
#         self.horizontalLayout_7.addWidget(self.HomeFooter_Label)
#         spacerItem7 = QtWidgets.QSpacerItem(689, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
#         self.horizontalLayout_7.addItem(spacerItem7)
#         self.AboutFooter_Label = QtWidgets.QLabel(self.Home_About_LabelsFrame)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.AboutFooter_Label.sizePolicy().hasHeightForWidth())
#         self.AboutFooter_Label.setSizePolicy(sizePolicy)
#         self.AboutFooter_Label.setMinimumSize(QtCore.QSize(121, 40))
#         self.AboutFooter_Label.setMaximumSize(QtCore.QSize(121, 40))
#         font = QtGui.QFont()
#         font.setFamily("Helvetica")
#         font.setPointSize(30)
#         font.setBold(True)
#         font.setWeight(75)
#         self.AboutFooter_Label.setFont(font)
#         self.AboutFooter_Label.setStyleSheet("padding: 5 px;\n"
# "font-family: \"Helvetica\";\n"
# "font-weight: bold;\n"
# "text-align: center;\n"
# "border:0px;")
#         self.AboutFooter_Label.setObjectName("AboutFooter_Label")
#         self.horizontalLayout_7.addWidget(self.AboutFooter_Label)
#         self.footer_Layout.addWidget(self.Home_About_LabelsFrame)
#         self.footer_Layout.addWidget(self.front_page_pushButton)
#         # ----------Footer layout----------

        # ----------Footer layout---------- Second version
        self.footer_Layout = QtWidgets.QHBoxLayout()
        self.footer_Layout.setContentsMargins(0, 0, 0, 0)
        self.footer_Layout.setSpacing(0)
        self.footer_Layout.setObjectName("footer_Layout")

        # ----------Back page button----------
        self.back_page_pushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_page_pushButton.sizePolicy().hasHeightForWidth())
        self.back_page_pushButton.setSizePolicy(sizePolicy)
        self.back_page_pushButton.setMinimumSize(QtCore.QSize(161, 70))
        self.back_page_pushButton.setMaximumSize(QtCore.QSize(160, 70))
        self.back_page_pushButton.setStyleSheet("QPushButton {\n"
                                                "   color: #333;\n"
                                                "    border: 2px rounded #555;\n"
                                                "    border-bottom-left-radius: 10px;\n"
                                                "    border-style: outset;\n"
                                                "    background: rgb(72, 187, 177);\n"
                                                "    padding: 5 px;\n"
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
        self.back_page_pushButton.setText("")
        icon = QtGui.QIcon("FRONTEND/IMAGES/buttonsBehind.png")
        # icon = QtGui.QIcon.fromTheme("PageBefore")
        self.back_page_pushButton.setIcon(icon)
        self.back_page_pushButton.setIconSize(QtCore.QSize(40, 40))
        self.back_page_pushButton.setCheckable(False)
        self.back_page_pushButton.setAutoExclusive(False)
        self.back_page_pushButton.setAutoDefault(False)
        self.back_page_pushButton.setDefault(False)
        self.back_page_pushButton.setObjectName("back_page_pushButton")

        # ----------Back page button----------

        self.footer_Layout.addWidget(self.back_page_pushButton)
        # self.Home_About_LabelsFrame = QtWidgets.QFrame(Form)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.Home_About_LabelsFrame.sizePolicy().hasHeightForWidth())
        # self.Home_About_LabelsFrame.setSizePolicy(sizePolicy)
        # self.Home_About_LabelsFrame.setMinimumSize(QtCore.QSize(950, 67))
        # self.Home_About_LabelsFrame.setMaximumSize(QtCore.QSize(950, 67))
        # self.Home_About_LabelsFrame.setStyleSheet("padding: 8px 8px 8px 8px;\n"
        #                                           "    background: #ffffff;\n"
        #                                           "    border-color: #000000;\n"
        #                                           "    border-top: 2px solid;\n"
        #                                           "    border-bottom: 1px solid;\n"
        #                                           "\n"
        #                                           "")
        # self.Home_About_LabelsFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.Home_About_LabelsFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        # self.Home_About_LabelsFrame.setObjectName("Home_About_LabelsFrame")
        # self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.Home_About_LabelsFrame)
        # self.horizontalLayout_7.setContentsMargins(12, 3, 12, 3)
        # self.horizontalLayout_7.setSpacing(5)
        # self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        # self.HomeFooter_Label = QtWidgets.QLabel(self.Home_About_LabelsFrame)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.HomeFooter_Label.sizePolicy().hasHeightForWidth())
        # self.HomeFooter_Label.setSizePolicy(sizePolicy)
        # self.HomeFooter_Label.setMinimumSize(QtCore.QSize(101, 40))
        # self.HomeFooter_Label.setMaximumSize(QtCore.QSize(101, 40))
        # font = QtGui.QFont()
        # font.setFamily("Helvetica")
        # font.setPointSize(30)
        # font.setBold(True)
        # font.setWeight(75)
        # self.HomeFooter_Label.setFont(font)
        # self.HomeFooter_Label.setStyleSheet("padding: 5 px;\n"
        #                                     "font-family: \"Helvetica\";\n"
        #                                     "font-weight: bold;\n"
        #                                     "text-align: center;\n"
        #                                     "border:0px;\n"
        #                                     "")
        # self.HomeFooter_Label.setObjectName("HomeFooter_Label")
        # self.horizontalLayout_7.addWidget(self.HomeFooter_Label)
        # spacerItem15 = QtWidgets.QSpacerItem(689, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_7.addItem(spacerItem15)
        # self.AboutFooter_Label = QtWidgets.QLabel(self.Home_About_LabelsFrame)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(41)
        # sizePolicy.setVerticalStretch(121)
        # sizePolicy.setHeightForWidth(self.AboutFooter_Label.sizePolicy().hasHeightForWidth())
        # self.AboutFooter_Label.setSizePolicy(sizePolicy)
        # self.AboutFooter_Label.setMinimumSize(QtCore.QSize(121, 40))
        # self.AboutFooter_Label.setMaximumSize(QtCore.QSize(121, 40))
        # font = QtGui.QFont()
        # font.setFamily("Helvetica")
        # font.setPointSize(30)
        # font.setBold(True)
        # font.setWeight(75)
        # self.AboutFooter_Label.setFont(font)
        # self.AboutFooter_Label.setStyleSheet("padding: 5 px;\n"
        #                                      "font-family: \"Helvetica\";\n"
        #                                      "font-weight: bold;\n"
        #                                      "text-align: center;\n"
        #                                      "border:0px;")
        # self.AboutFooter_Label.setObjectName("AboutFooter_Label")
        # self.horizontalLayout_7.addWidget(self.AboutFooter_Label)
        # self.footer_Layout.addWidget(self.Home_About_LabelsFrame)

        # ----------Footer Layout----------

        # ----------Front page button----------
        self.front_page_pushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.front_page_pushButton.sizePolicy().hasHeightForWidth())
        self.front_page_pushButton.setSizePolicy(sizePolicy)
        self.front_page_pushButton.setMinimumSize(QtCore.QSize(161, 70))
        self.front_page_pushButton.setMaximumSize(QtCore.QSize(160, 70))
        self.front_page_pushButton.setStyleSheet("QPushButton {\n"
                                                 "   color: #333;\n"
                                                 "    border: 2px rounded #555;\n"
                                                 "    border-style: outset;\n"
                                                 "    border-bottom-right-radius: 10px;\n"
                                                 "    background: rgb(72, 187, 177);\n"
                                                 "    padding: 5 px;\n"
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
        self.front_page_pushButton.setText("")
        icon = QtGui.QIcon("FRONTEND/IMAGES/buttonsAfter.png")
        # icon = QtGui.QIcon.fromTheme("PageAfter")
        self.front_page_pushButton.setIcon(icon)
        self.front_page_pushButton.setIconSize(QtCore.QSize(40, 40))
        self.front_page_pushButton.setObjectName("front_page_pushButton")
        self.footer_Layout.addWidget(self.front_page_pushButton)
        self.verticalLayout.addLayout(self.footer_Layout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        # connection to about
        self.front_page_pushButton.clicked.connect(self.launchAbout)
        self.front_page_pushButton.clicked.connect(Form.close)
        # ----------Front page button----------


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def launchAbout(self):
        self.AboutWindows = aboutInterfaceV3.AboutUiForm()
        self.AboutWindows.show_about_window()

    def show_main_windows(self):
        self.mainWindows = QtWidgets.QWidget()
        self.setupUi(self.mainWindows)
        self.mainWindows.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.appTitle_label.setText(_translate("Form", "KNOW BETTER"))
        self.bodyInputInfoTitle_label.setText(_translate("Form", "INGRESO DE INFORMACIÓN"))
        self.typeTheTextTitle_label.setText(_translate("Form", "Digite en este campo el texto a analizar:"))
        self.analize_pushButton.setText(_translate("Form", "ANALIZAR"))
        self.HowToUseTheAPP_pushButton_4.setText(_translate("Form", "COMO USAR LA APP?"))
        self.typeTextArea_PlainTextEdit.setPlaceholderText(_translate("Form", "Digite el enunciado a ser analizado"))
        self.generalInfo_label.setText(_translate("Form", "INFORMACIÓN\n"
"GENERAL"))
        self.ToDo_label.setText(_translate("Form", "QUE DEBES HACER?"))
        self.ToDoList_QListWidget.setSortingEnabled(True)
        __sortingEnabled = self.ToDoList_QListWidget.isSortingEnabled()
        self.ToDoList_QListWidget.setSortingEnabled(__sortingEnabled)
        self.givenInfo_label.setText(_translate("Form", "QUE INFORMACIÓN TE BRINDAN?"))
        self.givenInfo_QListWidget.setSortingEnabled(True)
        __sortingEnabled = self.givenInfo_QListWidget.isSortingEnabled()
        self.givenInfo_QListWidget.setSortingEnabled(False)
        self.givenInfo_QListWidget.setSortingEnabled(__sortingEnabled)
        self.specifications_label.setText(_translate("Form", "ESPECIFICACIONES"))
        self.input_label.setText(_translate("Form", "ENTRADA"))
        self.condition_label.setText(_translate("Form", "CONDICIONES"))
        self.output_label.setText(_translate("Form", "SALIDA"))
        self.pseudocode_label.setText(_translate("Form", "PSEUDOCÓDIGO"))
        self.pseudocode_QListWidget.setSortingEnabled(True)
        __sortingEnabled = self.pseudocode_QListWidget.isSortingEnabled()
        self.pseudocode_QListWidget.setSortingEnabled(False)
        self.pseudocode_QListWidget.setSortingEnabled(__sortingEnabled)
        # self.HomeFooter_Label.setText(_translate("Form", "HOME"))
        # self.AboutFooter_Label.setText(_translate("Form", "ABOUT"))

    def listItems(self,excercise):
        #before do somtehing, we need to kepp clen the list items areas
        self.ToDoList_QListWidget.clear()
        self.givenInfo_QListWidget.clear()
        self.pseudocode_QListWidget.clear()
        given_input = ""
        #creating item for ToDoList
        for element in excercise['hacer']:
            self.ToDoList_QListWidget.addItem(element)
        # creating item for givenInfo
        for element in excercise['info']:
            self.givenInfo_QListWidget.addItem(element)

        # putting text in input
        if len(excercise['entrada']) > 1:
            for element in excercise['entrada']:
                given_input += element + " - "
            self.input_QLineEdit.setText(given_input[:len(given_input) - 2])
        else:
            self.input_QLineEdit.setText(excercise['entrada'][0])

        # putting text in conditions
        self.conditions_QLineEdit.setText(excercise['condiciones'])

        # putting text in output
        if len(excercise['salida']) > 1:
            for element in excercise['salida']:
                given_input += element + " - "
            self.output_QLineEdit.setText(given_input[:len(given_input) - 2])
        else:
            self.output_QLineEdit.setText(excercise['salida'][0])

        #PSEUDOCODE will be here soon
        counter = 1
        #temporary
        if len(excercise['pseudocodigo']) != 0 or len(excercise['pseudocodigo']) != None:
                for element in excercise['pseudocodigo']:
                    self.pseudocode_QListWidget.addItem(str(counter)+"."+element)
                    counter+=1

    def getAndSendExcercise(self):
        saved_excercises = open_csv()  # Read CSV
        text = self.typeTextArea_PlainTextEdit.toPlainText()
        excercise_description = describe(text,saved_excercises)
        self.listItems(excercise_description)
