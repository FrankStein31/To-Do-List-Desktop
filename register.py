from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(500, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Register)
        self.verticalLayout.setObjectName("verticalLayout")
        self.registerLabel = QtWidgets.QLabel(Register)
        self.registerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.registerLabel.setObjectName("registerLabel")
        self.verticalLayout.addWidget(self.registerLabel)
        self.fullNameLineEdit = QtWidgets.QLineEdit(Register)
        self.fullNameLineEdit.setObjectName("fullNameLineEdit")
        self.verticalLayout.addWidget(self.fullNameLineEdit)
        self.emailLineEdit = QtWidgets.QLineEdit(Register)
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.verticalLayout.addWidget(self.emailLineEdit)
        self.passwordLineEdit = QtWidgets.QLineEdit(Register)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.verticalLayout.addWidget(self.passwordLineEdit)
        self.confirmPasswordLineEdit = QtWidgets.QLineEdit(Register)
        self.confirmPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPasswordLineEdit.setObjectName("confirmPasswordLineEdit")
        self.verticalLayout.addWidget(self.confirmPasswordLineEdit)
        self.roleComboBox = QtWidgets.QComboBox(Register)
        self.roleComboBox.setObjectName("roleComboBox")
        self.roleComboBox.addItem("")
        self.roleComboBox.addItem("")
        self.verticalLayout.addWidget(self.roleComboBox)
        self.agreeCheckBox = QtWidgets.QCheckBox(Register)
        self.agreeCheckBox.setObjectName("agreeCheckBox")
        self.verticalLayout.addWidget(self.agreeCheckBox)
        self.registerButton = QtWidgets.QPushButton(Register)
        self.registerButton.setObjectName("registerButton")
        self.verticalLayout.addWidget(self.registerButton)
        self.backToLoginButton = QtWidgets.QPushButton(Register)
        self.backToLoginButton.setObjectName("backToLoginButton")
        self.verticalLayout.addWidget(self.backToLoginButton)

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Register"))
        self.registerLabel.setStyleSheet(_translate("Register", "\n"
"       QLabel {\n"
"           font-size: 18pt;\n"
"           font-weight: bold;\n"
"           color: #333;\n"
"           margin: 10px 0;\n"
"       }\n"
"      "))
        self.registerLabel.setText(_translate("Register", "Create a New Account"))
        self.fullNameLineEdit.setStyleSheet(_translate("Register", "\n"
"       QLineEdit {\n"
"           padding: 10px;\n"
"           border: 1px solid #aaa;\n"
"           border-radius: 5px;\n"
"           margin-bottom: 10px;\n"
"       }\n"
"      "))
        self.fullNameLineEdit.setPlaceholderText(_translate("Register", "Full Name"))
        self.emailLineEdit.setStyleSheet(_translate("Register", "\n"
"       QLineEdit {\n"
"           padding: 10px;\n"
"           border: 1px solid #aaa;\n"
"           border-radius: 5px;\n"
"           margin-bottom: 10px;\n"
"       }\n"
"      "))
        self.emailLineEdit.setPlaceholderText(_translate("Register", "Email"))
        self.passwordLineEdit.setStyleSheet(_translate("Register", "\n"
"       QLineEdit {\n"
"           padding: 10px;\n"
"           border: 1px solid #aaa;\n"
"           border-radius: 5px;\n"
"           margin-bottom: 10px;\n"
"       }\n"
"      "))
        self.passwordLineEdit.setPlaceholderText(_translate("Register", "Password"))
        self.confirmPasswordLineEdit.setStyleSheet(_translate("Register", "\n"
"       QLineEdit {\n"
"           padding: 10px;\n"
"           border: 1px solid #aaa;\n"
"           border-radius: 5px;\n"
"           margin-bottom: 10px;\n"
"       }\n"
"      "))
        self.confirmPasswordLineEdit.setPlaceholderText(_translate("Register", "Confirm Password"))
        self.roleComboBox.setStyleSheet(_translate("Register", "\n"
"       QComboBox {\n"
"           padding: 8px;\n"
"           border: 1px solid #aaa;\n"
"           border-radius: 5px;\n"
"           margin-bottom: 10px;\n"
"       }\n"
"      "))
        self.roleComboBox.setCurrentText(_translate("Register", "Admin"))
        self.roleComboBox.setItemText(0, _translate("Register", "Admin"))
        self.roleComboBox.setItemText(1, _translate("Register", "Personal"))
        self.agreeCheckBox.setStyleSheet(_translate("Register", "\n"
"       QCheckBox {\n"
"           margin: 10px 0;\n"
"       }\n"
"      "))
        self.agreeCheckBox.setText(_translate("Register", "I agree to the Terms and Conditions"))
        self.registerButton.setStyleSheet(_translate("Register", "\n"
"       QPushButton {\n"
"           background-color: #28a745;\n"
"           color: white;\n"
"           padding: 10px;\n"
"           border-radius: 5px;\n"
"           margin-bottom: 10px;\n"
"       }\n"
"       QPushButton:hover {\n"
"           background-color: #218838;\n"
"       }\n"
"      "))
        self.registerButton.setText(_translate("Register", "Register"))
        self.backToLoginButton.setStyleSheet(_translate("Register", "\n"
"       QPushButton {\n"
"           background-color: #6c757d;\n"
"           color: white;\n"
"           padding: 10px;\n"
"           border-radius: 5px;\n"
"       }\n"
"       QPushButton:hover {\n"
"           background-color: #5a6268;\n"
"       }\n"
"      "))
        self.backToLoginButton.setText(_translate("Register", "Back to Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QWidget()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())
