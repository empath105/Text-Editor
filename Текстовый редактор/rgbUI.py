from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_rgb(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(50, 60, 281, 211))
        self.widget.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"border-radius:30px;")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 30, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(112, 160, 121, 28))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:3px;\n"
"}\n"
"QPushButton:pressed{\n"
"    color:rgba(65,105,225,225);\n"
"    border-radius:3px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 30, 113, 22))
        self.lineEdit.setStyleSheet("background-color: white;\n"
"border-radius:3px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 70, 113, 22))
        self.lineEdit_2.setStyleSheet("background-color: white;\n"
"border-radius:3px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 110, 113, 22))
        self.lineEdit_3.setStyleSheet("background-color: white;\n"
"border-radius:3px;")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "R:"))
        self.label_2.setText(_translate("Form", "G:"))
        self.label_3.setText(_translate("Form", "B:"))
        self.pushButton.setText(_translate("Form", "Добавить цвет"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_rgb()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
