from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Font(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 194)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 20, 371, 161))
        self.widget.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"border-radius:30px;\n"
"")
        self.widget.setObjectName("widget")
        self.fontComboBox = QtWidgets.QFontComboBox(self.widget)
        self.fontComboBox.setGeometry(QtCore.QRect(70, 40, 226, 22))
        self.fontComboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fontComboBox.setObjectName("fontComboBox")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(140, 90, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:3px;\n"
"}\n"
"QPushButton:pressed{\n"
"    color:rgba(65,105,225,225);\n"
"    border-radius:3px;\n"
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
    ui = Ui_Font()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())