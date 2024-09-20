from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_link(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(543, 269)
        # Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 30, 481, 201))
        self.widget.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"border-radius:30px;")
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 31, 221, 31))
        self.lineEdit.setStyleSheet("background-color: white;\n"
"border-radius:3px;")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 20, 221, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(190, 150, 93, 28))
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
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 90, 211, 31))
        self.lineEdit_2.setStyleSheet("background-color: white;\n"
"border-radius:3px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 131, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(50, 90, 131, 21))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Введите текст, на котором должна"))
        self.pushButton.setText(_translate("Form", "OK"))
        self.label_2.setText(_translate("Form", "появиться ссылка"))
        self.label_3.setText(_translate("Form", "Введите ссылку"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_link()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())