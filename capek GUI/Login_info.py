# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Intro(object):
    def setupUi(self, Intro):
        Intro.setObjectName("Intro")
        Intro.resize(332, 437)
        Intro.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Intro)
        self.centralwidget.setMaximumSize(QtCore.QSize(450, 600))
        self.centralwidget.setStyleSheet("border-radius: 20px;")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(-1, 9, -1, -1)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setStyleSheet("QWidget#Register_page{\n"
"border-image: url(:/newPrefix/14546211_rm127-tang-16b-japaneseframe.jpg);\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.Login_page = QtWidgets.QWidget()
        self.Login_page.setStyleSheet("QWidget#Login_page{\n"
"border-image: url(:/newPrefix/14546211_rm127-tang-16b-japaneseframe.jpg);\n"
"}")
        self.Login_page.setObjectName("Login_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Login_page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.Login_page)
        self.frame_3.setStyleSheet("background-color:rgba(0,0,0,0.3);\n"
"border-radius:20px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setStyleSheet("background-color : rgba(0,0,0,0);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_3.setStyleSheet("color : rgba(255,255,255,0.7);\n"
"background-color : rgba(0,0,0,0);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.gotoRegister = QtWidgets.QPushButton(self.frame_4)
        self.gotoRegister.setStyleSheet("QPushButton#gotoRegister{\n"
"color : rgba(255,255,255,0.7);\n"
"background-color: rgba(255, 255, 255,0);\n"
"}\n"
"\n"
"QPushButton#gotoRegister:hover{\n"
"border: none;\n"
"border-bottom: 0.5px solid rgba(255,255,255,1);\n"
"}\n"
"\n"
"")
        self.gotoRegister.setObjectName("gotoRegister")
        self.horizontalLayout_4.addWidget(self.gotoRegister)
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_3.raise_()
        self.gotoRegister.raise_()
        self.gridLayout.addWidget(self.frame_4, 9, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color : rgba(0,0,0,0);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.inputPassword = QtWidgets.QLineEdit(self.frame_3)
        self.inputPassword.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"border : none;\n"
"border-bottom : 3px solid rgba(243, 243, 243,0.8);\n"
"color : rgba(255,255,255,1);\n"
"padding-bottom : 7px;")
        self.inputPassword.setText("")
        self.inputPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassword.setObjectName("inputPassword")
        self.gridLayout.addWidget(self.inputPassword, 5, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 1)
        self.inputUsername = QtWidgets.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.inputUsername.setFont(font)
        self.inputUsername.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"border : none;\n"
"border-bottom : 3px solid rgba(243, 243, 243,0.8);\n"
"color : rgba(255,255,255,1);\n"
"padding-bottom : 7px;")
        self.inputUsername.setText("")
        self.inputUsername.setDragEnabled(True)
        self.inputUsername.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.inputUsername.setClearButtonEnabled(True)
        self.inputUsername.setObjectName("inputUsername")
        self.gridLayout.addWidget(self.inputUsername, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color : rgba(0,0,0,0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.Login_button = QtWidgets.QPushButton(self.frame_3)
        self.Login_button.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Login_button.setFont(font)
        self.Login_button.setStyleSheet("QPushButton#Login_button {\n"
"    color: rgba(0, 0, 0, 0.7);  /* Warna teks dengan transparansi 70% */\n"
"    border: none;  /* Menghilangkan border */\n"
"    background-color: rgb(240, 240, 240);  /* Warna latar belakang */\n"
"    border-radius: 15px;  /* Membuat sudut tombol melengkung */\n"
"    padding: 10px 20px;  /* Tambahkan padding untuk menambah ruang di dalam tombol */\n"
"}\n"
"\n"
"QPushButton#Login_button:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.477, y1:0, x2:0.5, y2:1, \n"
"    stop:0 rgba(0, 0, 0, 0.2), stop:1 rgba(255, 255, 255, 0.9));\n"
"    /* Mengubah warna latar belakang saat tombol di-hover */\n"
"}\n"
"\n"
"QPushButton#Login_button:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(105, 118, 132, 1);  /* Mengubah warna latar belakang saat tombol ditekan */\n"
"    color: white;  /* Ubah warna teks menjadi putih saat tombol ditekan */\n"
"    /* Mengurangi padding untuk memberikan efek \"tekan\" */\n"
"}\n"
"")
        self.Login_button.setObjectName("Login_button")
        self.gridLayout.addWidget(self.Login_button, 7, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.frame_3)
        self.widget.setStyleSheet("background-color : rgba(0,0,0,0);")
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.Google = QtWidgets.QPushButton(self.widget)
        self.Google.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(22)
        self.Google.setFont(font)
        self.Google.setStyleSheet("QPushButton#Google{\n"
"color : rgba(0,0,0,1);\n"
"background-color : rgba(255,255,255,0);\n"
"}\n"
"\n"
"QPushButton#Google:hover{\n"
"color:rgba(240,240,240,1);\n"
"}")
        self.Google.setObjectName("Google")
        self.horizontalLayout_3.addWidget(self.Google)
        self.WA = QtWidgets.QPushButton(self.widget)
        self.WA.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(20)
        self.WA.setFont(font)
        self.WA.setStyleSheet("QPushButton#WA{\n"
"color : rgba(0,0,0,1);\n"
"background-color : rgba(255,255,255,0);\n"
"}\n"
"\n"
"QPushButton#WA:hover{\n"
"color:rgba(240,240,240,1);\n"
"}")
        self.WA.setObjectName("WA")
        self.horizontalLayout_3.addWidget(self.WA)
        self.Youtube = QtWidgets.QPushButton(self.widget)
        self.Youtube.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(20)
        self.Youtube.setFont(font)
        self.Youtube.setStyleSheet("QPushButton#Youtube{\n"
"color : rgba(0,0,0,1);\n"
"background-color : rgba(255,255,255,0);\n"
"}\n"
"\n"
"QPushButton#Youtube:hover{\n"
"color:rgba(240,240,240,1);\n"
"}")
        self.Youtube.setObjectName("Youtube")
        self.horizontalLayout_3.addWidget(self.Youtube)
        self.Discord = QtWidgets.QPushButton(self.widget)
        self.Discord.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(20)
        self.Discord.setFont(font)
        self.Discord.setStyleSheet("QPushButton#Discord{\n"
"color : rgba(0,0,0,1);\n"
"background-color : rgba(255,255,255,0);\n"
"}\n"
"\n"
"QPushButton#Discord:hover{\n"
"color:rgba(240,240,240,1);\n"
"}")
        self.Discord.setObjectName("Discord")
        self.horizontalLayout_3.addWidget(self.Discord)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.gridLayout.addWidget(self.widget, 10, 0, 1, 1)
        self.Error = QtWidgets.QLabel(self.frame_3)
        self.Error.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color:rgb(255, 19, 34);\n"
"padding-left:15px;")
        self.Error.setText("")
        self.Error.setObjectName("Error")
        self.gridLayout.addWidget(self.Error, 8, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.Login_page)
        self.Register_page = QtWidgets.QWidget()
        self.Register_page.setStyleSheet("QWidget#Register_page{\n"
"border-image: url(:/newPrefix/14546211_rm127-tang-16b-japaneseframe.jpg);\n"
"}")
        self.Register_page.setObjectName("Register_page")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Register_page)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.Register_page)
        self.frame_5.setStyleSheet("background-color:rgba(0,0,0,0.3);\n"
"border-radius:20px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setMinimumSize(QtCore.QSize(0, 30))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(25)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(0,0,0,0);\n"
"\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(26)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgba(255,255,255,0);\n"
"color : rgba(255,255,255,210)")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.inputUsername_2 = QtWidgets.QLineEdit(self.frame_5)
        self.inputUsername_2.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"border : none;\n"
"border-bottom : 3px solid rgba(243, 243, 243,0.8);\n"
"color : rgba(255,255,255,1);\n"
"padding-bottom : 7px;")
        self.inputUsername_2.setObjectName("inputUsername_2")
        self.verticalLayout.addWidget(self.inputUsername_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem5)
        self.InputPassword = QtWidgets.QLineEdit(self.frame_5)
        self.InputPassword.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"border : none;\n"
"border-bottom : 3px solid rgba(243, 243, 243,0.8);\n"
"color : rgba(255,255,255,1);\n"
"padding-bottom : 7px;")
        self.InputPassword.setObjectName("InputPassword")
        self.verticalLayout.addWidget(self.InputPassword)
        spacerItem6 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem6)
        self.ReInputPassword = QtWidgets.QLineEdit(self.frame_5)
        self.ReInputPassword.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"border : none;\n"
"border-bottom : 3px solid rgba(243, 243, 243,0.8);\n"
"color : rgba(255,255,255,1);\n"
"padding-bottom : 7px;")
        self.ReInputPassword.setObjectName("ReInputPassword")
        self.verticalLayout.addWidget(self.ReInputPassword)
        self.Error_2 = QtWidgets.QLabel(self.frame_5)
        self.Error_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"")
        self.Error_2.setText("")
        self.Error_2.setObjectName("Error_2")
        self.verticalLayout.addWidget(self.Error_2)
        self.RegisterButton = QtWidgets.QPushButton(self.frame_5)
        self.RegisterButton.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.RegisterButton.setFont(font)
        self.RegisterButton.setStyleSheet("QPushButton#RegisterButton{\n"
"    color: rgba(0, 0, 0, 0.7);  /* Warna teks dengan transparansi 70% */\n"
"    border: none;  /* Menghilangkan border */\n"
"    background-color: rgb(240, 240, 240);  /* Warna latar belakang */\n"
"    border-radius: 15px;  /* Membuat sudut tombol melengkung */\n"
"    padding: 10px 20px;  /* Tambahkan padding untuk menambah ruang di dalam tombol */\n"
"    font-size : 18px;\n"
"}\n"
"\n"
"QPushButton#RegisterButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.477, y1:0, x2:0.5, y2:1, \n"
"    stop:0 rgba(0, 0, 0, 0.2), stop:1 rgba(255, 255, 255, 0.9));\n"
"}\n"
"\n"
"QPushButton#RegisterButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(105, 118, 132, 1);  /* Mengubah warna latar belakang saat tombol ditekan */\n"
"    color: white;  /* Ubah warna teks menjadi putih saat tombol ditekan */\n"
"    /* Mengurangi padding untuk memberikan efek \"tekan\" */\n"
"}\n"
"")
        self.RegisterButton.setObjectName("RegisterButton")
        self.verticalLayout.addWidget(self.RegisterButton)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Google_1 = QtWidgets.QPushButton(self.frame_6)
        self.Google_1.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(22)
        self.Google_1.setFont(font)
        self.Google_1.setStyleSheet("QPushButton#Google_1{\n"
"color : rgba(0,0,0,1);\n"
"background-color : rgba(255,255,255,0);\n"
"}\n"
"\n"
"QPushButton#Google_1:hover{\n"
"color:rgba(240,240,240,1);\n"
"}")
        self.Google_1.setObjectName("Google_1")
        self.horizontalLayout_5.addWidget(self.Google_1)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.WA_1 = QtWidgets.QPushButton(self.frame_6)
        self.WA_1.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(22)
        self.WA_1.setFont(font)
        self.WA_1.setStyleSheet("QPushButton#WA_1{\n"
"color : rgba(0,0,0,1);\n"
"background-color : rgba(255,255,255,0);\n"
"}\n"
"\n"
"QPushButton#WA_1:hover{\n"
"color:rgba(240,240,240,1);\n"
"}")
        self.WA_1.setObjectName("WA_1")
        self.horizontalLayout_6.addWidget(self.WA_1)
        self.YT_1 = QtWidgets.QPushButton(self.frame_6)
        self.YT_1.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(22)
        self.YT_1.setFont(font)
        self.YT_1.setStyleSheet("QPushButton#YT_1{\n"
"color : rgba(0,0,0,1);\n"
"background-color : rgba(255,255,255,0);\n"
"}\n"
"\n"
"QPushButton#YT_1:hover{\n"
"color:rgba(240,240,240,1);\n"
"}")
        self.YT_1.setObjectName("YT_1")
        self.horizontalLayout_6.addWidget(self.YT_1)
        self.DC_1 = QtWidgets.QPushButton(self.frame_6)
        self.DC_1.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(22)
        self.DC_1.setFont(font)
        self.DC_1.setStyleSheet("QPushButton#DC_1{\n"
"color : rgba(0,0,0,1);\n"
"background-color : rgba(255,255,255,0);\n"
"}\n"
"\n"
"QPushButton#DC_1:hover{\n"
"color:rgba(240,240,240,1);\n"
"}")
        self.DC_1.setObjectName("DC_1")
        self.horizontalLayout_6.addWidget(self.DC_1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.verticalLayout.addWidget(self.frame_6)
        self.gridLayout_4.addWidget(self.frame_5, 9, 0, 1, 1)
        self.stackedWidget.addWidget(self.Register_page)
        self.Information_page = QtWidgets.QWidget()
        self.Information_page.setStyleSheet("QWidget#Information_page{\n"
"border-image: url(:/newPrefix/14546211_rm127-tang-16b-japaneseframe.jpg);\n"
"}")
        self.Information_page.setObjectName("Information_page")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.Information_page)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_7 = QtWidgets.QFrame(self.Information_page)
        self.frame_7.setStyleSheet("background-color:rgba(0,0,0,0.3);\n"
"border-radius:20px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(17)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color: rgba(255,255,255,1);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setStyleSheet("background-color:rgba(0,0,0,0);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setStyleSheet("background-color:rgba(255,255,255,1);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_6.setContentsMargins(9, 1, -1, -1)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.Dicky = QtWidgets.QPushButton(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.Dicky.setFont(font)
        self.Dicky.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Dicky.setStyleSheet("background-image: url(:/newPrefix/angle-small-down.png);\n"
"background-color:rgba(0,0,0,0);\n"
"padding-left:1px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/angle-small-down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/angle-small-up.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.Dicky.setIcon(icon)
        self.Dicky.setIconSize(QtCore.QSize(25, 25))
        self.Dicky.setCheckable(True)
        self.Dicky.setChecked(False)
        self.Dicky.setAutoRepeat(False)
        self.Dicky.setObjectName("Dicky")
        self.gridLayout_6.addWidget(self.Dicky, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setStyleSheet("background-color: rgb(205, 185, 186);\n"
"color : rgba(255,255,255,1);\n"
"border-radius:20px")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.frame_10)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.frame_10)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.gridLayout_6.addWidget(self.frame_10, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_9)
        self.frame_11 = QtWidgets.QFrame(self.frame_8)
        self.frame_11.setStyleSheet("background-color:rgba(255,255,255,1);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_7.setContentsMargins(-1, 1, -1, -1)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"padding-left:1px;")
        self.pushButton_10.setIcon(icon)
        self.pushButton_10.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_7.addWidget(self.pushButton_10, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.frame_13 = QtWidgets.QFrame(self.frame_11)
        self.frame_13.setStyleSheet("background-color: rgb(205, 185, 186);\n"
"color : rgba(255,255,255,1);\n"
"border-radius:20px")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.frame_13)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_8.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.frame_13)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_8.addWidget(self.label_10)
        self.gridLayout_7.addWidget(self.frame_13, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_8)
        self.frame_12.setStyleSheet("background-color:rgba(255,255,255,1);")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_12)
        self.gridLayout_8.setContentsMargins(-1, 1, -1, -1)
        self.gridLayout_8.setVerticalSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_12)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"padding-left : 1px;")
        self.pushButton_11.setIcon(icon)
        self.pushButton_11.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_8.addWidget(self.pushButton_11, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.frame_14 = QtWidgets.QFrame(self.frame_12)
        self.frame_14.setStyleSheet("background-color: rgb(205, 185, 186);\n"
"color : rgba(255,255,255,1);\n"
"border-radius:20px")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_9.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.frame_14)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_9.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.frame_14)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_9.addWidget(self.label_12)
        self.gridLayout_8.addWidget(self.frame_14, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_12)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.gridLayout_5.addWidget(self.frame_7, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.Information_page)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_15 = QtWidgets.QFrame(self.page)
        self.frame_15.setStyleSheet("QFrame#frame_15{\n"
"border-image: url(:/newPrefix/12158592_Cute_couple_Barista_in_apron_feeling_sorry_and_apologize_cartoon_character_illustration.jpg);\n"
"}")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_15)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_13 = QtWidgets.QLabel(self.frame_15)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color:rgba(0,0,0,0)\n"
"")
        self.label_13.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_13.setObjectName("label_13")
        self.gridLayout_10.addWidget(self.label_13, 2, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_10.addItem(spacerItem9, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame_15)
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(15)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color:rgba(0,0,0,0);")
        self.label_14.setObjectName("label_14")
        self.gridLayout_10.addWidget(self.label_14, 3, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.verticalLayout_4.addWidget(self.frame_15)
        self.stackedWidget.addWidget(self.page)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_2.setStyleSheet("background-color: rgb(133, 133, 133);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.GoToHome = QtWidgets.QPushButton(self.frame_2)
        self.GoToHome.setMinimumSize(QtCore.QSize(0, 0))
        self.GoToHome.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.GoToHome.setFont(font)
        self.GoToHome.setStyleSheet("border-image: url(:/newPrefix/home.png);")
        self.GoToHome.setText("")
        self.GoToHome.setIconSize(QtCore.QSize(15, 15))
        self.GoToHome.setObjectName("GoToHome")
        self.horizontalLayout_2.addWidget(self.GoToHome)
        self.GoToInfo = QtWidgets.QPushButton(self.frame_2)
        self.GoToInfo.setMinimumSize(QtCore.QSize(0, 0))
        self.GoToInfo.setMaximumSize(QtCore.QSize(20, 20))
        self.GoToInfo.setStyleSheet("border-image: url(:/newPrefix/info.png);")
        self.GoToInfo.setText("")
        self.GoToInfo.setObjectName("GoToInfo")
        self.horizontalLayout_2.addWidget(self.GoToInfo)
        spacerItem10 = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)
        Intro.setCentralWidget(self.centralwidget)

        self.retranslateUi(Intro)
        self.stackedWidget.setCurrentIndex(1)
        self.pushButton_11.toggled['bool'].connect(self.frame_14.setHidden) # type: ignore
        self.Dicky.toggled['bool'].connect(self.frame_10.setHidden) # type: ignore
        self.pushButton_10.toggled['bool'].connect(self.frame_13.setHidden) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Intro)

    def retranslateUi(self, Intro):
        _translate = QtCore.QCoreApplication.translate
        Intro.setWindowTitle(_translate("Intro", "MainWindow"))
        self.label_3.setText(_translate("Intro", "Don\'t have an account yet?"))
        self.gotoRegister.setText(_translate("Intro", "Create One"))
        self.label_2.setText(_translate("Intro", "OCR"))
        self.inputPassword.setPlaceholderText(_translate("Intro", "Password"))
        self.inputUsername.setPlaceholderText(_translate("Intro", "Username"))
        self.label.setText(_translate("Intro", "Log In"))
        self.Login_button.setText(_translate("Intro", "L o g  I n"))
        self.Google.setText(_translate("Intro", "H"))
        self.WA.setText(_translate("Intro", "L"))
        self.Youtube.setText(_translate("Intro", "M"))
        self.Discord.setText(_translate("Intro", "Y"))
        self.label_4.setText(_translate("Intro", "OCR"))
        self.label_5.setText(_translate("Intro", "REGISTER"))
        self.inputUsername_2.setPlaceholderText(_translate("Intro", "User Name"))
        self.InputPassword.setPlaceholderText(_translate("Intro", "Password"))
        self.ReInputPassword.setPlaceholderText(_translate("Intro", "Re-Enter Password"))
        self.RegisterButton.setText(_translate("Intro", "R e g i s t e r"))
        self.Google_1.setText(_translate("Intro", "H"))
        self.WA_1.setText(_translate("Intro", "L"))
        self.YT_1.setText(_translate("Intro", "M"))
        self.DC_1.setText(_translate("Intro", "Y"))
        self.label_6.setText(_translate("Intro", "JOB DESC INFORMATION"))
        self.Dicky.setText(_translate("Intro", "Dicky Osmond"))
        self.label_7.setText(_translate("Intro", "Coba"))
        self.label_8.setText(_translate("Intro", "Coba"))
        self.pushButton_10.setText(_translate("Intro", "Fadhli Ammar T.H."))
        self.label_9.setText(_translate("Intro", "Coba"))
        self.label_10.setText(_translate("Intro", "Coba"))
        self.pushButton_11.setText(_translate("Intro", "Stanislaus David "))
        self.label_11.setText(_translate("Intro", "Coba"))
        self.label_12.setText(_translate("Intro", "Coba"))
        self.label_13.setText(_translate("Intro", "MOHON MAAF KAMI "))
        self.label_14.setText(_translate("Intro", "TIDAK PUBLIK"))
import Resources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Intro = QtWidgets.QMainWindow()
    ui = Ui_Intro()
    ui.setupUi(Intro)
    Intro.show()
    sys.exit(app.exec_())
