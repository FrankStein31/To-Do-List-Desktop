from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(401, 300)
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 401, 291))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.loginLabel = QtWidgets.QLabel(self.centralwidget)
        self.loginLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loginLabel.setObjectName("loginLabel")
        self.verticalLayout.addWidget(self.loginLabel)
        self.emailLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.verticalLayout.addWidget(self.emailLineEdit)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.verticalLayout.addWidget(self.passwordLineEdit)
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout.addWidget(self.loginButton)
        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setObjectName("registerButton")
        self.verticalLayout.addWidget(self.registerButton)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.loginLabel.setStyleSheet(_translate("Login", "\n"
"        QLabel {\n"
"            font-size: 16pt;\n"
"            font-weight: bold;\n"
"            color: #333;\n"
"        }\n"
"       "))
        self.loginLabel.setText(_translate("Login", "Login to Your Account"))
        self.emailLineEdit.setStyleSheet(_translate("Login", "\n"
"        QLineEdit {\n"
"            padding: 10px;\n"
"            border: 1px solid #aaa;\n"
"            border-radius: 5px;\n"
"        }\n"
"       "))
        self.emailLineEdit.setPlaceholderText(_translate("Login", "Email"))
        self.passwordLineEdit.setStyleSheet(_translate("Login", "\n"
"        QLineEdit {\n"
"            padding: 10px;\n"
"            border: 1px solid #aaa;\n"
"            border-radius: 5px;\n"
"        }\n"
"       "))
        self.passwordLineEdit.setPlaceholderText(_translate("Login", "Password"))
        self.loginButton.setStyleSheet(_translate("Login", "\n"
"        QPushButton {\n"
"            background-color: #0078d7;\n"
"            color: white;\n"
"            padding: 10px;\n"
"            border-radius: 5px;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #005fa3;\n"
"        }\n"
"       "))
        self.loginButton.setText(_translate("Login", "Login"))
        self.registerButton.setStyleSheet(_translate("Login", "\n"
"        QPushButton {\n"
"            background-color: #28a745;\n"
"            color: white;\n"
"            padding: 10px;\n"
"            border-radius: 5px;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #218838;\n"
"        }\n"
"       "))
        self.registerButton.setText(_translate("Login", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
