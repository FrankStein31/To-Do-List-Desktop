from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime

class Ui_CrudForm(object):
    def setupUi(self, CrudForm):
        CrudForm.setObjectName("CrudForm")
        CrudForm.resize(400, 350)  # Slightly increased height to accommodate new widget
        self.verticalLayout = QtWidgets.QVBoxLayout(CrudForm)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.formLabel = QtWidgets.QLabel(CrudForm)
        self.formLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.formLabel.setObjectName("formLabel")
        self.verticalLayout.addWidget(self.formLabel)
        
        self.titleLineEdit = QtWidgets.QLineEdit(CrudForm)
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.verticalLayout.addWidget(self.titleLineEdit)
        
        self.descriptionLineEdit = QtWidgets.QLineEdit(CrudForm)
        self.descriptionLineEdit.setObjectName("descriptionLineEdit")
        self.verticalLayout.addWidget(self.descriptionLineEdit)
        
        # New Deadline DateEdit Widget
        self.deadlineDateEdit = QtWidgets.QDateEdit(CrudForm)
        self.deadlineDateEdit.setObjectName("deadlineDateEdit")
        self.deadlineDateEdit.setCalendarPopup(True)  # Enable calendar popup
        self.deadlineDateEdit.setDate(QtCore.QDate.currentDate())  # Set default to current date
        self.deadlineDateEdit.setMinimumDate(QtCore.QDate.currentDate())  # Prevent selecting past dates
        self.verticalLayout.addWidget(self.deadlineDateEdit)
        
        self.typeComboBox = QtWidgets.QComboBox(CrudForm)
        self.typeComboBox.setObjectName("typeComboBox")
        self.typeComboBox.addItem("")
        self.typeComboBox.addItem("")
        self.verticalLayout.addWidget(self.typeComboBox)
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.saveButton = QtWidgets.QPushButton(CrudForm)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        
        self.cancelButton = QtWidgets.QPushButton(CrudForm)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(CrudForm)
        QtCore.QMetaObject.connectSlotsByName(CrudForm)

    def retranslateUi(self, CrudForm):
        _translate = QtCore.QCoreApplication.translate
        CrudForm.setWindowTitle(_translate("CrudForm", "CRUD Form"))
        
        self.formLabel.setStyleSheet(_translate("CrudForm", "\n"
"       QLabel {\n"
"           font-size: 16pt;\n"
"           font-weight: bold;\n"
"           color: #333;\n"
"       }\n"
"      "))
        self.formLabel.setText(_translate("CrudForm", "Create Task"))
        
        self.titleLineEdit.setStyleSheet(_translate("CrudForm", "\n"
"       QLineEdit {\n"
"           padding: 10px;\n"
"           border: 1px solid #aaa;\n"
"           border-radius: 5px;\n"
"       }\n"
"      "))
        self.titleLineEdit.setPlaceholderText(_translate("CrudForm", "Enter title..."))
        
        self.descriptionLineEdit.setStyleSheet(_translate("CrudForm", "\n"
"       QLineEdit {\n"
"           padding: 10px;\n"
"           border: 1px solid #aaa;\n"
"           border-radius: 5px;\n"
"       }\n"
"      "))
        self.descriptionLineEdit.setPlaceholderText(_translate("CrudForm", "Enter description..."))
        
        # Styling for Deadline DateEdit
        self.deadlineDateEdit.setStyleSheet(_translate("CrudForm", "\n"
"       QDateEdit {\n"
"           padding: 10px;\n"
"           border: 1px solid #aaa;\n"
"           border-radius: 5px;\n"
"       }\n"
"      "))
        
        self.typeComboBox.setStyleSheet(_translate("CrudForm", "\n"
"       QComboBox {\n"
"           padding: 10px;\n"
"           border: 1px solid #aaa;\n"
"           border-radius: 5px;\n"
"       }\n"
"      "))
        self.typeComboBox.setCurrentText(_translate("CrudForm", "Team"))
        self.typeComboBox.setItemText(0, _translate("CrudForm", "Team"))
        self.typeComboBox.setItemText(1, _translate("CrudForm", "Personal"))
        
        self.saveButton.setStyleSheet(_translate("CrudForm", "\n"
"         QPushButton {\n"
"             background-color: #0078d7;\n"
"             color: white;\n"
"             padding: 10px;\n"
"             border-radius: 5px;\n"
"         }\n"
"         QPushButton:hover {\n"
"             background-color: #005fa3;\n"
"         }\n"
"        "))
        self.saveButton.setText(_translate("CrudForm", "Save"))
        
        self.cancelButton.setStyleSheet(_translate("CrudForm", "\n"
"         QPushButton {\n"
"             background-color: #dc3545;\n"
"             color: white;\n"
"             padding: 10px;\n"
"             border-radius: 5px;\n"
"         }\n"
"         QPushButton:hover {\n"
"             background-color: #c82333;\n"
"         }\n"
"        "))
        self.cancelButton.setText(_translate("CrudForm", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CrudForm = QtWidgets.QWidget()
    ui = Ui_CrudForm()
    ui.setupUi(CrudForm)
    CrudForm.show()
    sys.exit(app.exec_())