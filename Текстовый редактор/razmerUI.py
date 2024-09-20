from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Razmer(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(268, 159)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(50, 40, 181, 91))
        self.widget.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"border-radius:30px;")
        self.widget.setObjectName("widget")
        self.spinBox = QtWidgets.QSpinBox(self.widget)
        self.spinBox.setGeometry(QtCore.QRect(30, 30, 51, 31))
        self.spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(100, 30, 61, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:3px;\n"
"}\n"
"QPushButton:pressed{\n"
"    color:rgba(65,105,225,225);\n"
"    border-radius:3px\n"
"}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "OK"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Razmer()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())