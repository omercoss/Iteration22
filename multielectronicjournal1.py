# Form implementation generated from reading ui file 'multielectronicjournal1.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets, uic

class startSide(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(804, 631)
        self.listWidget = QtWidgets.QListWidget(parent=Form)
        self.listWidget.setGeometry(QtCore.QRect(70, 40, 671, 531))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(250, 220, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(260, 280, 60, 16))
        self.label_2.setObjectName("label_2")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(parent=Form)
        self.dateTimeEdit.setGeometry(QtCore.QRect(130, 450, 194, 24))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(450, 320, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser_3 = QtWidgets.QTextBrowser(parent=Form)
        self.textBrowser_3.setGeometry(QtCore.QRect(170, 100, 501, 51))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(80, 50, 60, 16))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(parent=Form)
        self.textEdit.setGeometry(QtCore.QRect(310, 210, 191, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=Form)
        self.textEdit_2.setGeometry(QtCore.QRect(310, 270, 191, 31))
        self.textEdit_2.setObjectName("textEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.login)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Brugernavn:"))
        self.label_2.setText(_translate("Form", "Kodeord:"))
        self.pushButton.setText(_translate("Form", "Log ind"))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:36pt; font-weight:600;\">Multi-Electronic-Journal</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "Læge"))

    def login(self):
        brugernavn = self.textEdit.toPlainText()
        kodeord = self.textEdit_2.toPlainText()

        if brugernavn == "læge" and kodeord == "kode":
            self.korrekt = gui.multijournal2færdig.PatientProfil
        else:
            self.forkert = gui.forkertlogin.ForkertLogin


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = startSide()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())