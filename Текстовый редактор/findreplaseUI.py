from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Text(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(716, 555)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 30, 661, 511))
        self.widget.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"border-radius:30px;")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(60, 20, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 81, 321, 31))
        self.lineEdit.setStyleSheet("background-color: white;\n"
"border-radius:3px;")
        self.lineEdit.setObjectName("lineEdit")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(70, 150, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_2.setGeometry(QtCore.QRect(70, 180, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_3.setGeometry(QtCore.QRect(70, 210, 351, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(220, 250, 181, 28))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:3px;\n"
"}\n"
"QPushButton:pressed{\n"
"    color:rgba(65,105,225,225);\n"
"    border-radius:3px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 290, 321, 31))
        self.lineEdit_2.setStyleSheet("background-color: white;\n"
"border-radius:3px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 350, 141, 31))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:3px;\n"
"}\n"
"QPushButton:pressed{\n"
"    color:rgba(65,105,225,225);\n"
"    border-radius:3px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 350, 151, 31))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:3px;\n"
"}\n"
"QPushButton:pressed{\n"
"    color:rgba(65,105,225,225);\n"
"    border-radius:3px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(460, 350, 141, 31))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:3px;\n"
"}\n"
"QPushButton:pressed{\n"
"    color:rgba(65,105,225,225);\n"
"    border-radius:3px;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(270, 430, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Введите текст или регулярное выражение для поиска"))
        self.checkBox.setText(_translate("Form", "Чувствительность к регистру"))
        self.checkBox_2.setText(_translate("Form", "Полное слово"))
        self.checkBox_3.setText(_translate("Form", "Использовать регулярные выражения"))
        self.pushButton.setText(_translate("Form", "Найти"))
        self.pushButton_2.setText(_translate("Form", "Заменить"))
        self.pushButton_3.setText(_translate("Form", "Убрать выделение"))
        self.pushButton_4.setText(_translate("Form", "Закрыть"))
        self.label_2.setText(_translate("Form", "Найдено: 0"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Text()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
