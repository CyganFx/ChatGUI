# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Chat.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(401, 658)
        Form.setStyleSheet("")
        self.background = QtWidgets.QLabel(Form)
        self.background.setGeometry(QtCore.QRect(-14, -8, 481, 811))
        self.background.setStyleSheet("background-color: rgb(0, 85, 127);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.textField = QtWidgets.QTextEdit(Form)
        self.textField.setGeometry(QtCore.QRect(0, 620, 311, 41))
        self.textField.setObjectName("textField")
        self.sendButton = QtWidgets.QPushButton(Form)
        self.sendButton.setGeometry(QtCore.QRect(320, 620, 81, 41))
        self.sendButton.setObjectName("sendButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 10, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(20, 90, 271, 501))
        self.textBrowser.setObjectName("textBrowser")
        self.logsButton = QtWidgets.QPushButton(Form)
        self.logsButton.setGeometry(QtCore.QRect(320, 500, 81, 41))
        self.logsButton.setObjectName("logsButton")
        self.privateModeButton = QtWidgets.QPushButton(Form)
        self.privateModeButton.setGeometry(QtCore.QRect(320, 560, 81, 41))
        self.privateModeButton.setObjectName("privateModeButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "GUI Chat"))
        self.textField.setHtml(_translate("Form",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.sendButton.setText(_translate("Form", "Send"))
        self.label.setText(_translate("Form", "                     Telegram"))
        self.logsButton.setText(_translate("Form", "Logs"))
        self.privateModeButton.setText(_translate("Form", "Private Mode"))
