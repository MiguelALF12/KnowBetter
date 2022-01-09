from PyQt5 import QtCore, QtGui, QtWidgets
# import IMAGES
from BACKEND.read_analize_CSV import open_csv
from BACKEND.showInfo import describe
from FRONTEND import mainInterfaceV3

class AboutUiForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1300, 870)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(1270, 850))
        Form.setMaximumSize(QtCore.QSize(1270, 850))
        Form.setStyleSheet("background: #2f244c;")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(950, 800))
        self.frame.setMaximumSize(QtCore.QSize(950, 800))
        self.frame.setStyleSheet("\n"
"background: #4b3fdd;")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 400))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 400))
        self.frame_2.setStyleSheet("/*border: 2px solid;\n"
"border-color: rgb(255, 255, 255);*/\n"
"border:0px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(470, 70))
        self.label.setMaximumSize(QtCore.QSize(470, 70))
        font = QtGui.QFont()
        font.setFamily("Bayon")
        font.setPointSize(60)
        self.label.setFont(font)
        self.label.setStyleSheet("    color: #ffffff;\n"
"    font-family: \"Bayon\";\n"
"    text-align: left;\n"
"")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(800, 230))
        self.label_2.setMaximumSize(QtCore.QSize(800, 230))
        font = QtGui.QFont()
        font.setFamily("Basic")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"    color: #ffffff;\n"
"    font-family: \"Basic\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_3.setStyleSheet("/*border: 2px solid;\n"
"border-color: rgb(255, 255, 255);*/")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Basic")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: #232323;\n"
"font-family: \"Basic\";\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_10.addWidget(self.label_3)
        self.verticalLayout_7.addLayout(self.verticalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(230, 200))
        self.label_6.setMaximumSize(QtCore.QSize(220, 200))
        self.label_6.setStyleSheet("padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0)")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("FRONTEND/IMAGES/header-utp-logo-blanco.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, 2, -1, 2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Basic")
        font.setPointSize(25)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"margin: 4px;\n"
"    color: #232323;\n"
"    font-family: \"Basic\";\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        spacerItem6 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(250, 200))
        self.label_7.setMaximumSize(QtCore.QSize(220, 200))
        self.label_7.setStyleSheet("padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0)")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("FRONTEND/IMAGES/header-utp-logo-blanco.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem9 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem9)
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Basic")
        font.setPointSize(25)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"margin: 4px;\n"
"    color: #232323;\n"
"    font-family: \"Basic\";\n"
"")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        spacerItem10 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem10)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem11)
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(250, 200))
        self.label_10.setMaximumSize(QtCore.QSize(220, 200))
        self.label_10.setStyleSheet("padding: 8px 8px 8px 8px;\n"
"background: rgba(255, 255, 255, 0)")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("FRONTEND/IMAGES/header-utp-logo-blanco.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        spacerItem12 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem12)
        self.verticalLayout_9.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_4.setStyleSheet("/*border: 2px solid;\n"
"border-color: rgb(255, 255, 255);*/\n"
"border:0px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Basic")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("\n"
"    color: #e5e5e5;\n"
"    font-family: \"Basic\";\n"
"    text-align: left;\n"
"")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_12.addWidget(self.label_5)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(60, 36))
        self.label_8.setMaximumSize(QtCore.QSize(60, 36))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("FRONTEND/IMAGES/moqupsapp.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_11.addWidget(self.label_8)
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMaximumSize(QtCore.QSize(51, 51))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("FRONTEND/IMAGES/vexels.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(60, 45))
        self.label_12.setMaximumSize(QtCore.QSize(64, 45))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("FRONTEND/IMAGES/qt-design.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_11.addWidget(self.label_12)
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(47, 47))
        self.label_14.setMaximumSize(QtCore.QSize(47, 47))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("FRONTEND/IMAGES/python-logo.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_11.addWidget(self.label_14)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)
        spacerItem13 = QtWidgets.QSpacerItem(532, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem13)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addWidget(self.frame)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem14)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # ----------Footer layout----------
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

        # connection to main interface
        self.back_page_pushButton.clicked.connect(self.launchMain)
        self.back_page_pushButton.clicked.connect(Form.close)
        # ----------Back page button----------


        self.footer_Layout.addWidget(self.back_page_pushButton)
        self.Home_About_LabelsFrame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Home_About_LabelsFrame.sizePolicy().hasHeightForWidth())
        self.Home_About_LabelsFrame.setSizePolicy(sizePolicy)
        self.Home_About_LabelsFrame.setMinimumSize(QtCore.QSize(950,67))
        self.Home_About_LabelsFrame.setMaximumSize(QtCore.QSize(950,67))
        self.Home_About_LabelsFrame.setStyleSheet("padding: 8px 8px 8px 8px;\n"
"    background: #ffffff;\n"
"    border-color: #000000;\n"
"    border-top: 2px solid;\n"
"    border-bottom: 1px solid;\n"
"\n"
"")
        self.Home_About_LabelsFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Home_About_LabelsFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Home_About_LabelsFrame.setObjectName("Home_About_LabelsFrame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.Home_About_LabelsFrame)
        self.horizontalLayout_7.setContentsMargins(12, 3, 12, 3)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.HomeFooter_Label = QtWidgets.QLabel(self.Home_About_LabelsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HomeFooter_Label.sizePolicy().hasHeightForWidth())
        self.HomeFooter_Label.setSizePolicy(sizePolicy)
        self.HomeFooter_Label.setMinimumSize(QtCore.QSize(101, 40))
        self.HomeFooter_Label.setMaximumSize(QtCore.QSize(101, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.HomeFooter_Label.setFont(font)
        self.HomeFooter_Label.setStyleSheet("padding: 5 px;\n"
"font-family: \"Helvetica\";\n"
"font-weight: bold;\n"
"text-align: center;\n"
"border:0px;\n"
"")
        self.HomeFooter_Label.setObjectName("HomeFooter_Label")
        self.horizontalLayout_7.addWidget(self.HomeFooter_Label)
        spacerItem15 = QtWidgets.QSpacerItem(689, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem15)
        self.AboutFooter_Label = QtWidgets.QLabel(self.Home_About_LabelsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(41)
        sizePolicy.setVerticalStretch(121)
        sizePolicy.setHeightForWidth(self.AboutFooter_Label.sizePolicy().hasHeightForWidth())
        self.AboutFooter_Label.setSizePolicy(sizePolicy)
        self.AboutFooter_Label.setMinimumSize(QtCore.QSize(121, 40))
        self.AboutFooter_Label.setMaximumSize(QtCore.QSize(121, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.AboutFooter_Label.setFont(font)
        self.AboutFooter_Label.setStyleSheet("padding: 5 px;\n"
"font-family: \"Helvetica\";\n"
"font-weight: bold;\n"
"text-align: center;\n"
"border:0px;")
        self.AboutFooter_Label.setObjectName("AboutFooter_Label")
        self.horizontalLayout_7.addWidget(self.AboutFooter_Label)
        self.footer_Layout.addWidget(self.Home_About_LabelsFrame)

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
        # ----------Front page button----------


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def launchMain(self):
        self.mainWindows = mainInterfaceV3.MainUIForm()
        self.mainWindows.show_main_windows()


    def show_about_window(self):
        self.aboutWindows = QtWidgets.QWidget()
        self.setupUi(self.aboutWindows)
        self.aboutWindows.show()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "SOBRE KNOW BETTER"))
        self.label_2.setText(_translate("Form", "Es un aplicativo que ayuda en la comprensión de pequeños textos (generalmente en forma de ejercicios) guiados prinicipalmente en el tema de programación.\n"
"\n"
"Funciona mediante la lectura de un conjunto de mas 20 ejercicios de programación analizados de manera individual separando las ideas principales de cada uno."))
        self.label_3.setText(_translate("Form", "Desarrollado por:"))
        self.label_4.setText(_translate("Form", "EN: "))
        self.label_9.setText(_translate("Form", "PARA:"))
        self.label_5.setText(_translate("Form", "Herramientas:"))
        self.HomeFooter_Label.setText(_translate("Form", "HOME"))
        self.AboutFooter_Label.setText(_translate("Form", "ABOUT"))




