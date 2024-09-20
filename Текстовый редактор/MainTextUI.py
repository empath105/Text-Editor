from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import resic


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1132, 950)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 10, 1111, 920))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.icon_only_widget = QtWidgets.QWidget(self.widget)
        self.icon_only_widget.setMinimumSize(QtCore.QSize(71, 0))
        self.icon_only_widget.setMaximumSize(QtCore.QSize(71, 16777215))
        self.icon_only_widget.setStyleSheet("QWidget{\n"
"    background-color: rgb(255, 170, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:checked{\n"
"    background-color:white;\n"
"    border-radius:3px;\n"
"}")
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_14.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_17 = QtWidgets.QPushButton(self.icon_only_widget)
        self.pushButton_17.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/фото для редактора/назад.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_17.setIcon(icon)
        self.pushButton_17.setCheckable(True)
        self.pushButton_17.setAutoExclusive(True)
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_2.addWidget(self.pushButton_17)
        spacerItem1 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_14.addLayout(self.horizontalLayout_2)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSpacing(8)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.file_Button_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.file_Button_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/фото для редактора/файл.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.file_Button_1.setIcon(icon1)
        self.file_Button_1.setCheckable(True)
        self.file_Button_1.setAutoExclusive(True)
        self.file_Button_1.setObjectName("file_Button_1")
        self.verticalLayout_11.addWidget(self.file_Button_1)
        self.allcheck_Button_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.allcheck_Button_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/фото для редактора/выделение всего текста.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.allcheck_Button_1.setIcon(icon2)
        self.allcheck_Button_1.setCheckable(True)
        self.allcheck_Button_1.setAutoExclusive(True)
        self.allcheck_Button_1.setObjectName("allcheck_Button_1")
        self.verticalLayout_11.addWidget(self.allcheck_Button_1)
        self.copy_Button_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.copy_Button_1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/фото для редактора/копирование.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copy_Button_1.setIcon(icon3)
        self.copy_Button_1.setCheckable(True)
        self.copy_Button_1.setAutoExclusive(True)
        self.copy_Button_1.setObjectName("copy_Button_1")
        self.verticalLayout_11.addWidget(self.copy_Button_1)
        self.paste_Button_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.paste_Button_1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/фото для редактора/вставка.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.paste_Button_1.setIcon(icon4)
        self.paste_Button_1.setCheckable(True)
        self.paste_Button_1.setAutoExclusive(True)
        self.paste_Button_1.setObjectName("paste_Button_1")
        self.verticalLayout_11.addWidget(self.paste_Button_1)
        self.shripht_Button_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.shripht_Button_1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/фото для редактора/шрифтн.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shripht_Button_1.setIcon(icon5)
        self.shripht_Button_1.setCheckable(True)
        self.shripht_Button_1.setAutoExclusive(True)
        self.shripht_Button_1.setObjectName("shripht_Button_1")
        self.verticalLayout_11.addWidget(self.shripht_Button_1)
        self.size_Button_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.size_Button_1.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/фото для редактора/размер.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.size_Button_1.setIcon(icon6)
        self.size_Button_1.setCheckable(True)
        self.size_Button_1.setAutoExclusive(True)
        self.size_Button_1.setObjectName("size_Button_1")
        self.verticalLayout_11.addWidget(self.size_Button_1)
        self.color_Button_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.color_Button_1.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/фото для редактора/цвет.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.color_Button_1.setIcon(icon7)
        self.color_Button_1.setCheckable(True)
        self.color_Button_1.setAutoExclusive(True)
        self.color_Button_1.setObjectName("color_Button_1")
        self.verticalLayout_11.addWidget(self.color_Button_1)
        self.plamp_Button_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.plamp_Button_1.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/фото для редактора/жирный.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plamp_Button_1.setIcon(icon8)
        self.plamp_Button_1.setCheckable(True)
        self.plamp_Button_1.setAutoExclusive(True)
        self.plamp_Button_1.setObjectName("plamp_Button_1")
        self.verticalLayout_11.addWidget(self.plamp_Button_1)
        self.italic_Button_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.italic_Button_1.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/фото для редактора/курсив.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.italic_Button_1.setIcon(icon9)
        self.italic_Button_1.setCheckable(True)
        self.italic_Button_1.setAutoExclusive(True)
        self.italic_Button_1.setObjectName("italic_Button_1")
        self.verticalLayout_11.addWidget(self.italic_Button_1)
        self.underline_Button_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.underline_Button_1.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/фото для редактора/подчёркивание.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.underline_Button_1.setIcon(icon10)
        self.underline_Button_1.setCheckable(True)
        self.underline_Button_1.setAutoExclusive(True)
        self.underline_Button_1.setObjectName("underline_Button_1")
        self.verticalLayout_11.addWidget(self.underline_Button_1)
        self.find_Button_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.find_Button_1.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/фото для редактора/найти.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.find_Button_1.setIcon(icon11)
        self.find_Button_1.setCheckable(True)
        self.find_Button_1.setAutoExclusive(True)
        self.find_Button_1.setObjectName("find_Button_1")
        self.verticalLayout_11.addWidget(self.find_Button_1)
        self.stile_Button_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.stile_Button_1.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/фото для редактора/стили.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stile_Button_1.setIcon(icon12)
        self.stile_Button_1.setIconSize(QtCore.QSize(30, 30))
        self.stile_Button_1.setCheckable(True)
        self.stile_Button_1.setAutoExclusive(True)
        self.stile_Button_1.setObjectName("stile_Button_1")
        self.verticalLayout_11.addWidget(self.stile_Button_1)
        self.new_Button_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.new_Button_1.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/фото для редактора/добавить.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_Button_1.setIcon(icon13)
        self.new_Button_1.setCheckable(True)
        self.new_Button_1.setAutoExclusive(True)
        self.new_Button_1.setObjectName("new_Button_1")
        self.verticalLayout_11.addWidget(self.new_Button_1)
        self.verticalLayout_14.addLayout(self.verticalLayout_11)
        spacerItem2 = QtWidgets.QSpacerItem(20, 312, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem2)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.otstup_Button_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.otstup_Button_1.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/фото для редактора/отступ.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.otstup_Button_1.setIcon(icon14)
        self.otstup_Button_1.setCheckable(True)
        self.otstup_Button_1.setAutoExclusive(True)
        self.otstup_Button_1.setObjectName("otstup_Button_1")
        self.verticalLayout_12.addWidget(self.otstup_Button_1)
        self.interval_Button_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.interval_Button_1.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/фото для редактора/интервал.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.interval_Button_1.setIcon(icon15)
        self.interval_Button_1.setCheckable(True)
        self.interval_Button_1.setAutoExclusive(True)
        self.interval_Button_1.setObjectName("interval_Button_1")
        self.verticalLayout_12.addWidget(self.interval_Button_1)
        self.verticalLayout_14.addLayout(self.verticalLayout_12)
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        self.icon_text_widget = QtWidgets.QWidget(self.widget)
        self.icon_text_widget.setStyleSheet("QWidget{\n"
"    \n"
"    background-color: rgb(255, 170, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"    height: 30px;\n"
"    border:none;\n"
"}")
        self.icon_text_widget.setObjectName("icon_text_widget")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.icon_text_widget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.icon_text_widget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout_13.addLayout(self.horizontalLayout_3)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.file = QtWidgets.QFrame(self.icon_text_widget)
        self.file.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.file.setFrameShadow(QtWidgets.QFrame.Raised)
        self.file.setObjectName("file")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.file)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.file_Button_2 = QtWidgets.QPushButton(self.file)
        self.file_Button_2.setStyleSheet("QPushButton{\n"
"    padding-left:-95px;\n"
"}")
        self.file_Button_2.setIcon(icon1)
        self.file_Button_2.setCheckable(True)
        self.file_Button_2.setObjectName("file_Button_2")
        self.verticalLayout_5.addWidget(self.file_Button_2)
        self.file_frame = QtWidgets.QFrame(self.file)
        self.file_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.file_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.file_frame.setObjectName("file_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.file_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.newfile_Button = QtWidgets.QPushButton(self.file_frame)
        self.newfile_Button.setStyleSheet("QPushButton{\n"
"    padding-left:-65px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:rgba(65,105,225,225);\n"
"}")
        self.newfile_Button.setCheckable(True)
        self.newfile_Button.setObjectName("newfile_Button")
        self.verticalLayout.addWidget(self.newfile_Button)
        self.openfile_Button = QtWidgets.QPushButton(self.file_frame)
        self.openfile_Button.setStyleSheet("QPushButton{\n"
"    padding-left:-65px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:rgba(65,105,225,225);\n"
"}")
        self.openfile_Button.setCheckable(True)
        self.openfile_Button.setObjectName("openfile_Button")
        self.verticalLayout.addWidget(self.openfile_Button)
        self.savepdffile_Button = QtWidgets.QPushButton(self.file_frame)
        self.savepdffile_Button.setStyleSheet("QPushButton{\n"
"    padding-left:-5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:rgba(65,105,225,225);\n"
"}")
        self.savepdffile_Button.setCheckable(True)
        self.savepdffile_Button.setObjectName("savepdffile_Button")
        self.verticalLayout.addWidget(self.savepdffile_Button)
        self.savehtmlfile_Button = QtWidgets.QPushButton(self.file_frame)
        self.savehtmlfile_Button.setStyleSheet("QPushButton:hover{\n"
"    color:rgba(65,105,225,225);\n"
"}")
        self.savehtmlfile_Button.setCheckable(True)
        self.savehtmlfile_Button.setObjectName("savehtmlfile_Button")
        self.verticalLayout.addWidget(self.savehtmlfile_Button)
        self.verticalLayout_5.addWidget(self.file_frame)
        self.verticalLayout_9.addWidget(self.file)
        self.allcheck_Button_2 = QtWidgets.QPushButton(self.icon_text_widget)
        self.allcheck_Button_2.setStyleSheet(" QPushButton{\n"
"    padding-left:-60px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:white;\n"
"    border-radius:3px;\n"
"}")
        self.allcheck_Button_2.setIcon(icon2)
        self.allcheck_Button_2.setCheckable(True)
        self.allcheck_Button_2.setObjectName("allcheck_Button_2")
        self.verticalLayout_9.addWidget(self.allcheck_Button_2)
        self.copy_Button_2 = QtWidgets.QPushButton(self.icon_text_widget)
        self.copy_Button_2.setStyleSheet("QPushButton{\n"
"    padding-left:-65px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:white;\n"
"    border-radius:3px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:white;\n"
"    border-radius:3px;\n"
"}")
        self.copy_Button_2.setIcon(icon3)
        self.copy_Button_2.setCheckable(True)
        self.copy_Button_2.setObjectName("copy_Button_2")
        self.verticalLayout_9.addWidget(self.copy_Button_2)
        self.paste_Button_2 = QtWidgets.QPushButton(self.icon_text_widget)
        self.paste_Button_2.setStyleSheet("QPushButton{\n"
"    padding-left:-85px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:white;\n"
"    border-radius:3px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:white;\n"
"    border-radius:3px;\n"
"}")
        self.paste_Button_2.setIcon(icon4)
        self.paste_Button_2.setCheckable(True)
        self.paste_Button_2.setObjectName("paste_Button_2")
        self.verticalLayout_9.addWidget(self.paste_Button_2)
        self.shripht_Button_2 = QtWidgets.QPushButton(self.icon_text_widget)
        self.shripht_Button_2.setStyleSheet("QPushButton{\n"
"    padding-left:-85px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:white;\n"
"    border-radius:3px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:white;\n"
"    border-radius:3px;\n"
"}")
        self.shripht_Button_2.setIcon(icon5)
        self.shripht_Button_2.setCheckable(True)
        self.shripht_Button_2.setObjectName("shripht_Button_2")
        self.verticalLayout_9.addWidget(self.shripht_Button_2)
        self.size_Button_2 = QtWidgets.QPushButton(self.icon_text_widget)
        self.size_Button_2.setStyleSheet("QPushButton{\n"
"    padding-left:-85px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:white;\n"
"    border-radius:3px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:white;\n"
"    border-radius:3px;\n"
"}")
        self.size_Button_2.setIcon(icon6)
        self.size_Button_2.setCheckable(True)
        self.size_Button_2.setObjectName("size_Button_2")
        self.verticalLayout_9.addWidget(self.size_Button_2)
        self.color_Button_2 = QtWidgets.QPushButton(self.icon_text_widget)
        self.color_Button_2.setStyleSheet("QPushButton{\n"
"    padding-left:-95px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:white;\n"
"    border-radius:3px;\n"
"}")
        self.color_Button_2.setIcon(icon7)
        self.color_Button_2.setCheckable(True)
        self.color_Button_2.setObjectName("color_Button_2")
        self.verticalLayout_9.addWidget(self.color_Button_2)
        self.plamp_Button_2 = QtWidgets.QPushButton(self.icon_text_widget)
        self.plamp_Button_2.setStyleSheet("QPushButton{\n"
"    padding-left:-85px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:white;\n"
"    border-radius:3px;\n"
"}")
        self.plamp_Button_2.setIcon(icon8)
        self.plamp_Button_2.setCheckable(True)
        self.plamp_Button_2.setObjectName("plamp_Button_2")
        self.verticalLayout_9.addWidget(self.plamp_Button_2)
        self.italic_Button_2 = QtWidgets.QPushButton(self.icon_text_widget)
        self.italic_Button_2.setStyleSheet("QPushButton{\n"
"    padding-left:-95px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:white;\n"
"    border-radius:3px;\n"
"}")
        self.italic_Button_2.setIcon(icon9)
        self.italic_Button_2.setCheckable(True)
        self.italic_Button_2.setObjectName("italic_Button_2")
        self.verticalLayout_9.addWidget(self.italic_Button_2)
        self.underline_Button_2 = QtWidgets.QPushButton(self.icon_text_widget)
        self.underline_Button_2.setStyleSheet("QPushButton{\n"
"    padding-left:-55px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:white;\n"
"    border-radius:3px;\n"
"}")
        self.underline_Button_2.setIcon(icon10)
        self.underline_Button_2.setCheckable(True)
        self.underline_Button_2.setObjectName("underline_Button_2")
        self.verticalLayout_9.addWidget(self.underline_Button_2)
        self.find = QtWidgets.QFrame(self.icon_text_widget)
        self.find.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.find.setFrameShadow(QtWidgets.QFrame.Raised)
        self.find.setObjectName("find")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.find)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.find_Button_2 = QtWidgets.QPushButton(self.find)
        self.find_Button_2.setStyleSheet("QPushButton{\n"
"    padding-left:-50px;\n"
"}")
        self.find_Button_2.setIcon(icon11)
        self.find_Button_2.setCheckable(True)
        self.find_Button_2.setObjectName("find_Button_2")
        self.verticalLayout_6.addWidget(self.find_Button_2)
        self.find_frame = QtWidgets.QFrame(self.find)
        self.find_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.find_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.find_frame.setObjectName("find_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.find_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.findtext_Button = QtWidgets.QPushButton(self.find_frame)
        self.findtext_Button.setStyleSheet("QPushButton{\n"
"    padding-left:-75px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:rgba(65,105,225,225);\n"
"}")
        self.findtext_Button.setCheckable(True)
        self.findtext_Button.setObjectName("findtext_Button")
        self.verticalLayout_2.addWidget(self.findtext_Button)
        self.replacedtext_Button = QtWidgets.QPushButton(self.find_frame)
        self.replacedtext_Button.setStyleSheet("QPushButton{\n"
"    padding-left:-55px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:rgba(65,105,225,225);\n"
"}")
        self.replacedtext_Button.setCheckable(True)
        self.replacedtext_Button.setObjectName("replacedtext_Button")
        self.verticalLayout_2.addWidget(self.replacedtext_Button)
        self.verticalLayout_6.addWidget(self.find_frame)
        self.verticalLayout_9.addWidget(self.find)
        self.stile = QtWidgets.QFrame(self.icon_text_widget)
        self.stile.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stile.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stile.setObjectName("stile")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.stile)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.stile_Button_2 = QtWidgets.QPushButton(self.stile)
        self.stile_Button_2.setIcon(icon12)
        self.stile_Button_2.setIconSize(QtCore.QSize(30, 30))
        self.stile_Button_2.setCheckable(True)
        self.stile_Button_2.setObjectName("stile_Button_2")
        self.verticalLayout_7.addWidget(self.stile_Button_2)
        self.stile_frame = QtWidgets.QFrame(self.stile)
        self.stile_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stile_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stile_frame.setObjectName("stile_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.stile_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stile_Button = QtWidgets.QPushButton(self.stile_frame)
        self.stile_Button.setStyleSheet("QPushButton{\n"
"    padding-left:-80px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:rgba(65,105,225,225);\n"
"}")
        self.stile_Button.setCheckable(True)
        self.stile_Button.setObjectName("stile_Button")
        self.verticalLayout_3.addWidget(self.stile_Button)
        self.yourstile_Button = QtWidgets.QPushButton(self.stile_frame)
        self.yourstile_Button.setStyleSheet("QPushButton{\n"
"    padding-left:-30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:rgba(65,105,225,225);\n"
"}")
        self.yourstile_Button.setCheckable(True)
        self.yourstile_Button.setObjectName("yourstile_Button")
        self.verticalLayout_3.addWidget(self.yourstile_Button)
        self.verticalLayout_7.addWidget(self.stile_frame)
        self.verticalLayout_9.addWidget(self.stile)
        self.new_2 = QtWidgets.QFrame(self.icon_text_widget)
        self.new_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.new_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.new_2.setObjectName("new_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.new_2)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.new_Button_2 = QtWidgets.QPushButton(self.new_2)
        self.new_Button_2.setStyleSheet("QPushButton{\n"
"    padding-left:-60px;\n"
"}")
        self.new_Button_2.setIcon(icon13)
        self.new_Button_2.setCheckable(True)
        self.new_Button_2.setObjectName("new_Button_2")
        self.verticalLayout_8.addWidget(self.new_Button_2)
        self.new_frame = QtWidgets.QFrame(self.new_2)
        self.new_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.new_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.new_frame.setObjectName("new_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.new_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.link_Button = QtWidgets.QPushButton(self.new_frame)
        self.link_Button.setStyleSheet("QPushButton{\n"
"    padding-left:-65px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:rgba(65,105,225,225);\n"
"}")
        self.link_Button.setCheckable(True)
        self.link_Button.setObjectName("link_Button")
        self.verticalLayout_4.addWidget(self.link_Button)
        self.image_Button = QtWidgets.QPushButton(self.new_frame)
        self.image_Button.setStyleSheet("QPushButton{\n"
"    padding-left:-30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:rgba(65,105,225,225);\n"
"}")
        self.image_Button.setCheckable(True)
        self.image_Button.setObjectName("image_Button")
        self.verticalLayout_4.addWidget(self.image_Button)
        self.verticalLayout_8.addWidget(self.new_frame)
        self.verticalLayout_9.addWidget(self.new_2)
        self.verticalLayout_13.addLayout(self.verticalLayout_9)
        spacerItem3 = QtWidgets.QSpacerItem(20, 63, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem3)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.otstup_Button_2 = QtWidgets.QPushButton(self.icon_text_widget)
        self.otstup_Button_2.setStyleSheet("QPushButton{\n"
"    padding-left:-90px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:white;\n"
"    border-radius:3px;\n"
"}")
        self.otstup_Button_2.setIcon(icon14)
        self.otstup_Button_2.setCheckable(True)
        self.otstup_Button_2.setObjectName("otstup_Button_2")
        self.verticalLayout_10.addWidget(self.otstup_Button_2)
        self.interval_Button_2 = QtWidgets.QPushButton(self.icon_text_widget)
        self.interval_Button_2.setStyleSheet("QPushButton{\n"
"    padding-left:-80px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:white;\n"
"    border-radius:3px;\n"
"}")
        self.interval_Button_2.setIcon(icon15)
        self.interval_Button_2.setCheckable(True)
        self.interval_Button_2.setObjectName("interval_Button_2")
        self.verticalLayout_10.addWidget(self.interval_Button_2)
        self.verticalLayout_13.addLayout(self.verticalLayout_10)
        self.gridLayout.addWidget(self.icon_text_widget, 0, 1, 1, 1)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.widget1 = QtWidgets.QWidget(self.widget)
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setStyleSheet("QPushButton:checked{\n"
"    background-color: rgb(255, 170, 255);\n"
"    border-radius:3px;\n"
"}")
        self.pushButton.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/фото для редактора/меню.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon16)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        spacerItem4 = QtWidgets.QSpacerItem(724, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_16.addWidget(self.widget1)
        self.main_screen_widget = QtWidgets.QWidget(self.widget)
        self.main_screen_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.main_screen_widget.setObjectName("main_screen_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_screen_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.main_screen_widget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        spacerItem5 = QtWidgets.QSpacerItem(20, 818, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem5)
        self.label = QtWidgets.QLabel(self.main_screen_widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_15.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout_15)
        self.verticalLayout_16.addWidget(self.main_screen_widget)
        self.gridLayout.addLayout(self.verticalLayout_16, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.file_Button_2.toggled['bool'].connect(self.file_frame.hide) # type: ignore
        self.find_Button_2.toggled['bool'].connect(self.find_frame.setHidden) # type: ignore
        self.new_Button_2.toggled['bool'].connect(self.new_frame.setHidden) # type: ignore
        self.stile_Button_2.toggled['bool'].connect(self.stile_frame.setHidden) # type: ignore
        self.file_Button_2.toggled['bool'].connect(self.file_frame.setHidden) # type: ignore
        self.file_Button_2.toggled['bool'].connect(self.file_Button_1.setChecked) # type: ignore
        self.allcheck_Button_2.toggled['bool'].connect(self.allcheck_Button_1.setChecked) # type: ignore
        self.copy_Button_2.toggled['bool'].connect(self.copy_Button_1.setChecked) # type: ignore
        self.paste_Button_2.toggled['bool'].connect(self.paste_Button_1.setChecked) # type: ignore
        self.shripht_Button_2.toggled['bool'].connect(self.shripht_Button_1.setChecked) # type: ignore
        self.size_Button_2.toggled['bool'].connect(self.size_Button_1.setChecked) # type: ignore
        self.color_Button_2.toggled['bool'].connect(self.color_Button_1.setChecked) # type: ignore
        self.plamp_Button_2.toggled['bool'].connect(self.plamp_Button_1.setChecked) # type: ignore
        self.italic_Button_2.toggled['bool'].connect(self.italic_Button_1.setChecked) # type: ignore
        self.underline_Button_2.toggled['bool'].connect(self.underline_Button_1.setChecked) # type: ignore
        self.find_Button_2.toggled['bool'].connect(self.find_Button_1.setChecked) # type: ignore
        self.stile_Button_2.toggled['bool'].connect(self.stile_Button_1.setChecked) # type: ignore
        self.new_Button_2.toggled['bool'].connect(self.new_Button_1.setChecked) # type: ignore
        self.otstup_Button_2.toggled['bool'].connect(self.otstup_Button_1.setChecked) # type: ignore
        self.interval_Button_2.toggled['bool'].connect(self.interval_Button_1.setChecked) # type: ignore
        self.pushButton.toggled['bool'].connect(self.icon_text_widget.setHidden) # type: ignore
        self.pushButton.toggled['bool'].connect(self.icon_only_widget.setVisible) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Текстовый"))
        self.label_2.setText(_translate("MainWindow", "редактор"))
        self.file_Button_2.setText(_translate("MainWindow", "Файл ..."))
        self.newfile_Button.setText(_translate("MainWindow", "Создать"))
        self.openfile_Button.setText(_translate("MainWindow", "Открыть"))
        self.savepdffile_Button.setText(_translate("MainWindow", "Сохранить как .pdf"))
        self.savehtmlfile_Button.setText(_translate("MainWindow", "Сохранить как .html"))
        self.allcheck_Button_2.setText(_translate("MainWindow", "Выделить всё"))
        self.copy_Button_2.setText(_translate("MainWindow", "Копировать"))
        self.paste_Button_2.setText(_translate("MainWindow", "Вставить"))
        self.shripht_Button_2.setText(_translate("MainWindow", "Шрифт"))
        self.size_Button_2.setText(_translate("MainWindow", "Размер"))
        self.color_Button_2.setText(_translate("MainWindow", "Цвет"))
        self.plamp_Button_2.setText(_translate("MainWindow", "Жирный"))
        self.italic_Button_2.setText(_translate("MainWindow", "Курсив"))
        self.underline_Button_2.setText(_translate("MainWindow", "Подчёркнутый"))
        self.find_Button_2.setText(_translate("MainWindow", "Найти текст ..."))
        self.findtext_Button.setText(_translate("MainWindow", "Найти"))
        self.replacedtext_Button.setText(_translate("MainWindow", "Заменить"))
        self.stile_Button_2.setText(_translate("MainWindow", "Стиль форматирования ..."))
        self.stile_Button.setText(_translate("MainWindow", "Стили"))
        self.yourstile_Button.setText(_translate("MainWindow", "Добавить свой"))
        self.new_Button_2.setText(_translate("MainWindow", "Добавить ..."))
        self.link_Button.setText(_translate("MainWindow", "Ссылка"))
        self.image_Button.setText(_translate("MainWindow", "Изображение"))
        self.otstup_Button_2.setText(_translate("MainWindow", "Отступы"))
        self.interval_Button_2.setText(_translate("MainWindow", "Интервалы"))
        self.label.setText(_translate("MainWindow", "1"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
