from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddTaskDialog(object):
    def setupUi(self, AddTaskDialog):
        AddTaskDialog.setObjectName("AddTaskDialog")
        AddTaskDialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(AddTaskDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleInput = QtWidgets.QLineEdit(AddTaskDialog)
        self.titleInput.setObjectName("titleInput")
        self.verticalLayout.addWidget(self.titleInput)
        self.descriptionInput = QtWidgets.QLineEdit(AddTaskDialog)
        self.descriptionInput.setObjectName("descriptionInput")
        self.verticalLayout.addWidget(self.descriptionInput)
        
        # Add type input ComboBox
        self.typeInput = QtWidgets.QComboBox(AddTaskDialog)
        self.typeInput.setObjectName("typeInput")
        self.typeInput.addItem("Personal")
        self.typeInput.addItem("Team")
        self.verticalLayout.addWidget(self.typeInput)
        
        self.statusInput = QtWidgets.QComboBox(AddTaskDialog)
        self.statusInput.setObjectName("statusInput")
        self.statusInput.addItem("")
        self.statusInput.addItem("")
        self.statusInput.addItem("")
        self.verticalLayout.addWidget(self.statusInput)

        self.deadlineInput = QtWidgets.QDateEdit(AddTaskDialog)
        self.deadlineInput.setObjectName("deadlineInput")
        self.deadlineInput.setCalendarPopup(True)
        self.verticalLayout.addWidget(self.deadlineInput)

        self.priorityInput = QtWidgets.QComboBox(AddTaskDialog)
        self.priorityInput.setObjectName("priorityInput")
        self.priorityInput.addItem("")
        self.priorityInput.addItem("")
        self.priorityInput.addItem("")
        self.verticalLayout.addWidget(self.priorityInput)

        self.addButton = QtWidgets.QPushButton(AddTaskDialog)
        self.addButton.setObjectName("addButton")
        self.verticalLayout.addWidget(self.addButton)

        self.retranslateUi(AddTaskDialog)
        QtCore.QMetaObject.connectSlotsByName(AddTaskDialog)

    def retranslateUi(self, AddTaskDialog):
        _translate = QtCore.QCoreApplication.translate
        AddTaskDialog.setWindowTitle(_translate("AddTaskDialog", "Add Task"))
        self.titleInput.setPlaceholderText(_translate("AddTaskDialog", "Title"))
        self.descriptionInput.setPlaceholderText(_translate("AddTaskDialog", "Description"))
        
        # Add translation for type input
        self.typeInput.setItemText(0, _translate("AddTaskDialog", "Personal"))
        self.typeInput.setItemText(1, _translate("AddTaskDialog", "Team"))
        
        self.statusInput.setItemText(0, _translate("AddTaskDialog", "Pending"))
        self.statusInput.setItemText(1, _translate("AddTaskDialog", "In Progress"))
        self.statusInput.setItemText(2, _translate("AddTaskDialog", "Completed"))

        self.deadlineInput.setDisplayFormat("yyyy-MM-dd")
        self.deadlineInput.setDate(QtCore.QDate.currentDate())

        self.priorityInput.setItemText(0, _translate("AddTaskDialog", "Low"))
        self.priorityInput.setItemText(1, _translate("AddTaskDialog", "Medium"))
        self.priorityInput.setItemText(2, _translate("AddTaskDialog", "High"))
        self.addButton.setText(_translate("AddTaskDialog", "Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddTaskDialog = QtWidgets.QDialog()
    ui = Ui_AddTaskDialog()
    ui.setupUi(AddTaskDialog)
    AddTaskDialog.show()
    sys.exit(app.exec_())
