import sys
import mysql.connector
import hashlib
from PyQt5 import QtWidgets, QtCore
from login import Ui_Login
from register import Ui_Register
from dashboard import Ui_Dashboard
from add_task import Ui_AddTaskDialog
from crud import Ui_CrudForm
from delete_confirm import Ui_DeleteConfirmDialog

class DatabaseManager:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='notion'
            )
            self.cursor = self.connection.cursor(dictionary=True)
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL Platform: {e}")
            sys.exit(1)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, full_name, email, password, role):
        try:
            self.cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            if self.cursor.fetchone():
                return False, "Email already registered"

            hashed_password = self.hash_password(password)
            
            query = "INSERT INTO users (full_name, email, password, role) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (full_name, email, hashed_password, role))
            self.connection.commit()
            
            return True, "Registration successful"
        except mysql.connector.Error as e:
            return False, f"Registration failed: {str(e)}"

    def login_user(self, email, password):
        try:
            hashed_password = self.hash_password(password)
            
            query = "SELECT * FROM users WHERE email = %s AND password = %s"
            self.cursor.execute(query, (email, hashed_password))
            user = self.cursor.fetchone()
            
            return (True, user) if user else (False, None)
        except mysql.connector.Error as e:
            print(f"Login error: {e}")
            return False, None

    def get_tasks(self, user_id, task_filter=None, user_role=None):
        try:
            if user_role == 'Admin':
                base_query = "SELECT * FROM tasks WHERE user_id = %s"
                params = [user_id]
            else:
                base_query = "SELECT * FROM tasks WHERE user_id = %s"
                params = [user_id]
                base_query += " AND approval_status = 'Approved'"

            if task_filter == 'Personal':
                base_query += " AND type = 'Personal'"
            elif task_filter == 'Team':
                base_query += " AND type = 'Team'"
            elif task_filter == 'Deadline Today':
                base_query += " AND DATE(deadline) = CURRENT_DATE"
            elif task_filter == 'In Progress':
                base_query += " AND status = 'In Progress'"
            elif task_filter == 'Complete':
                base_query += " AND status = 'Completed'"
            elif task_filter == 'Incomplete':
                base_query += " AND status != 'Completed'"

            if user_role == 'Admin':
                base_query += " OR (type = 'Team' AND approval_status = 'Approved')"

            self.cursor.execute(base_query, params)
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Error fetching tasks: {e}")
            return []
        
    def get_pending_tasks(self):
        try:
            query = "SELECT * FROM tasks WHERE approval_status = 'Pending'"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Error fetching pending tasks: {e}")
            return []

    def update_task_approval(self, task_id, approval_status):
        try:
            query = "UPDATE tasks SET approval_status = %s WHERE id = %s"
            self.cursor.execute(query, (approval_status, task_id))
            self.connection.commit()
            return True, "Task approval status updated"
        except mysql.connector.Error as e:
            return False, f"Failed to update task approval: {str(e)}"
    
    def create_task(self, user_id, title, description, status, priority, task_type, deadline, user_role):
        try:
            if user_role == 'Admin':
                approval_status = 'Approved'
            elif task_type == 'Team':
                approval_status = 'Pending'
            else:
                approval_status = 'Approved'
            
            query = """
            INSERT INTO tasks 
            (user_id, title, description, status, priority, type, deadline, approval_status) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (user_id, title, description, status, priority, task_type, deadline, approval_status))
            self.connection.commit()
            
            if approval_status == 'Pending':
                return True, "Tugas Tim berhasil ditambahkan dan menunggu persetujuan admin"
            
            return True, "Tugas berhasil ditambah"
        except mysql.connector.Error as e:
            return False, f"Failed to create task: {str(e)}"

    def update_task(self, task_id, user_id, title, description, status, priority, task_type, deadline, user_role):
        try:
            # approval_status = 'Approved' if user_role == 'Admin' else 'Pending'
            query = """
            UPDATE tasks 
            SET title = %s, description = %s, status = %s, 
                priority = %s, type = %s, deadline = %s
            WHERE id = %s AND user_id = %s
            """
            self.cursor.execute(query, (
                title, description, status, priority, task_type, 
                deadline, task_id, user_id
            ))
            self.connection.commit()
            
            # if approval_status == 'Pending':
            #     return True, "Task updated and awaiting admin approval"
            
            return True, "Tugas berhasil diedit"
        except mysql.connector.Error as e:
            return False, f"Failed to update task: {str(e)}"

    def delete_task(self, task_id, user_id):
        try:
            query = "DELETE FROM tasks WHERE id = %s AND user_id = %s"
            self.cursor.execute(query, (task_id, user_id))
            self.connection.commit()
            return True, "Tugas berhasil dihapus"
        except mysql.connector.Error as e:
            return False, f"Failed to delete task: {str(e)}"

    def __del__(self):
        if hasattr(self, 'connection'):
            self.connection.close()

    def search_tasks(self, user_id, search_term):
        try:
            query = """
            SELECT * FROM tasks 
            WHERE user_id = %s AND 
            (title LIKE %s OR description LIKE %s)
            """
            search_pattern = f"%{search_term}%"
            self.cursor.execute(query, (user_id, search_pattern, search_pattern))
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Error searching tasks: {e}")
            return []

    def get_task_history(self, task_id):
        try:
            query = "SELECT * FROM tasks WHERE id = %s"
            self.cursor.execute(query, (task_id,))
            return self.cursor.fetchone()
        except mysql.connector.Error as e:
            print(f"Error fetching task detail: {e}")
            return None

# ===============================================================================================
# ===============================================================================================
# ===============================================================================================

class DeleteConfirmDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DeleteConfirmDialog()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        
        # Tambahkan koneksi untuk tombol Yes dan No
        self.ui.yesButton.clicked.connect(self.accept)
        self.ui.noButton.clicked.connect(self.reject)

# ===============================================================================================
# ===============================================================================================
# ===============================================================================================

class RegisterWindow(QtWidgets.QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.ui = Ui_Register()
        self.ui.setupUi(self)
        self.db_manager = db_manager
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)

        self.ui.registerButton.clicked.connect(self.register)
        self.ui.backToLoginButton.clicked.connect(self.back_to_login)

    def register(self):
        full_name = self.ui.fullNameLineEdit.text()
        email = self.ui.emailLineEdit.text()
        password = self.ui.passwordLineEdit.text()
        confirm_password = self.ui.confirmPasswordLineEdit.text()
        role = self.ui.roleComboBox.currentText()

        if not full_name or not email or not password:
            QtWidgets.QMessageBox.warning(self, "Registration Error", "Isi semua kolom")
            return

        if password != confirm_password:
            QtWidgets.QMessageBox.warning(self, "Registration Error", "Password berbeda dari yang sebelumnya")
            return

        if not self.ui.agreeCheckBox.isChecked():
            QtWidgets.QMessageBox.warning(self, "Registration Error", "Silahkan setujui aturan kami!")
            return

        success, message = self.db_manager.register_user(full_name, email, password, role)
        
        if success:
            QtWidgets.QMessageBox.information(self, "Success", message)
            self.open_login()
        else:
            QtWidgets.QMessageBox.warning(self, "Registration Error", message)

    def back_to_login(self):
        self.open_login()

    def open_login(self):
        self.login_window = LoginWindow(self.db_manager)
        self.login_window.show()
        self.close()

# ===============================================================================================
# ===============================================================================================
# ===============================================================================================

class LoginWindow(QtWidgets.QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.db_manager = db_manager
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)

        self.ui.loginButton.clicked.connect(self.login)
        self.ui.registerButton.clicked.connect(self.open_register)

    def login(self):
        email = self.ui.emailLineEdit.text()
        password = self.ui.passwordLineEdit.text()

        if not email or not password:
            QtWidgets.QMessageBox.warning(self, "Login Error", "Isi keduanya email dan password")
            return

        success, user = self.db_manager.login_user(email, password)
        
        if success and user:
            self.dashboard = Dashboard(self.db_manager, user['id'], user['full_name'], user['role'])
            self.dashboard.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Login Error", "Email atau password salah")

    def open_register(self):
        self.register_window = RegisterWindow(self.db_manager)
        self.register_window.show()
        self.close()

# ===============================================================================================
# ===============================================================================================
# ===============================================================================================

class AddTaskDialog(QtWidgets.QDialog):
    def __init__(self, db_manager, user_id, user_role, parent=None):
        super().__init__(parent)
        self.ui = Ui_AddTaskDialog()
        self.ui.setupUi(self)
        self.db_manager = db_manager
        self.user_id = user_id
        self.user_role = user_role
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)

        self.ui.addButton.clicked.connect(self.add_task)

    def add_task(self):
        title = self.ui.titleInput.text()
        description = self.ui.descriptionInput.text()
        status = self.ui.statusInput.currentText()
        priority = self.ui.priorityInput.currentText()
        task_type = self.ui.typeInput.currentText()
        deadline = self.ui.deadlineInput.date().toString("yyyy-MM-dd")

        if not title:
            QtWidgets.QMessageBox.warning(self, "Error", "Berikan Judul")
            return

        success, message = self.db_manager.create_task(
            self.user_id, title, description, status, priority, task_type, deadline, self.user_role
        )

        if success:
            QtWidgets.QMessageBox.information(self, "Success", message)
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", message)

# ===============================================================================================
# ===============================================================================================
# ===============================================================================================

class CrudForm(QtWidgets.QDialog):
    def __init__(self, db_manager, user_id, user_role, task=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_CrudForm()
        self.ui.setupUi(self)
        self.db_manager = db_manager
        self.user_id = user_id
        self.task = task
        self.user_role = user_role
        
        from PyQt5.QtCore import QDate
        
        self.status_combo = QtWidgets.QComboBox(self)
        self.status_combo.addItems(['Pending', 'In Progress', 'Completed'])
        
        self.priority_combo = QtWidgets.QComboBox(self)
        self.priority_combo.addItems(['Low', 'Medium', 'High'])
        
        self.ui.verticalLayout.insertWidget(3, QtWidgets.QLabel("Status:"))
        self.ui.verticalLayout.insertWidget(4, self.status_combo)
        
        self.ui.verticalLayout.insertWidget(5, QtWidgets.QLabel("Priority:"))
        self.ui.verticalLayout.insertWidget(6, self.priority_combo)
        
        self.ui.deadlineDateEdit.setCalendarPopup(True)
        self.ui.deadlineDateEdit.setDate(QDate.currentDate())
        
        self.setWindowTitle("Edit Task" if task else "Create Task")
        
        if task:
            self.ui.formLabel.setText("Edit Task")
            self.ui.titleLineEdit.setText(str(task.get('title', '')))
            self.ui.descriptionLineEdit.setText(str(task.get('description', '')))
            
            self.ui.typeComboBox.setCurrentText(str(task.get('type', 'Personal')))
            self.status_combo.setCurrentText(str(task.get('status', 'Pending')))
            self.priority_combo.setCurrentText(str(task.get('priority', 'Medium')))

            if task.get('deadline'):
                deadline_date = QDate.fromString(str(task.get('deadline')), "yyyy-MM-dd")
                self.ui.deadlineDateEdit.setDate(deadline_date)
        
        self.ui.saveButton.clicked.connect(self.save_task)
        self.ui.cancelButton.clicked.connect(self.close)

    def save_task(self):
        title = self.ui.titleLineEdit.text().strip()
        description = self.ui.descriptionLineEdit.text().strip()
        task_type = self.ui.typeComboBox.currentText()
        status = self.status_combo.currentText()
        deadline = self.ui.deadlineDateEdit.date().toString("yyyy-MM-dd")
        priority = self.priority_combo.currentText()

        if not title:
            QtWidgets.QMessageBox.warning(self, "Error", "Berikan judul")
            return

        try:
            if self.task: 
                success, message = self.db_manager.update_task(
                    self.task.get('id'), 
                    self.user_id, 
                    title, 
                    description, 
                    status,  
                    priority,  
                    task_type,
                    deadline,
                    self.user_role
                )
            else:  # Create new task
                success, message = self.db_manager.create_task(
                    self.user_id, title, description, 
                    status, priority, task_type, deadline,
                    self.user_role
                )

            if success:
                QtWidgets.QMessageBox.information(self, "Success", message)
                self.accept()  
            else:
                QtWidgets.QMessageBox.warning(self, "Error", message)
        
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            print(error_message)
            QtWidgets.QMessageBox.critical(self, "Critical Error", error_message)
            import traceback
            traceback.print_exc()

# ===============================================================================================
# ===============================================================================================
# ===============================================================================================

class Dashboard(QtWidgets.QWidget):
    def __init__(self, db_manager, user_id, user_name, user_role):
        super().__init__()
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self)
        self.db_manager = db_manager
        self.user_id = user_id
        self.user_name = user_name
        self.user_role = user_role

        self.setup_dashboard()
        self.connect_buttons()

    def setup_dashboard(self):
        tasks = self.db_manager.get_tasks(self.user_id, user_role=self.user_role)

        if self.user_role == 'Admin':
            pending_tasks = self.db_manager.get_pending_tasks()
            self.setup_pending_tasks_tab(pending_tasks)
        
        self.ui.todoTable.setRowCount(len(tasks))
        self.ui.todoTable.setColumnCount(7) 
        self.ui.todoTable.setHorizontalHeaderLabels(
            ["Title", "Description", "Status", "Type", "Priority", "Deadline", "Approval status"]
        )

        self.ui.searchBar.textChanged.connect(self.search_tasks)

        self.ui.todoTable.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.todoTable.customContextMenuRequested.connect(self.show_task_context_menu)

        total_tasks = len(tasks)
        completed_tasks = sum(1 for task in tasks if task['status'] == 'Completed')
        remaining_tasks = total_tasks - completed_tasks
        progress_percentage = int((completed_tasks / total_tasks) * 100) if total_tasks > 0 else 0

        self.ui.totalTasks.setText(f"Total Tasks: {total_tasks}")
        self.ui.completedTasks.setText(f"Completed: {completed_tasks}")
        self.ui.remainingTasks.setText(f"Remaining: {remaining_tasks}")
        self.ui.progressBar.setValue(progress_percentage)

        for row, task in enumerate(tasks):
            self.ui.todoTable.setItem(row, 0, QtWidgets.QTableWidgetItem(task.get('title', '')))
            self.ui.todoTable.setItem(row, 1, QtWidgets.QTableWidgetItem(task.get('description', '')))
            self.ui.todoTable.setItem(row, 2, QtWidgets.QTableWidgetItem(task.get('status', '')))
            self.ui.todoTable.setItem(row, 3, QtWidgets.QTableWidgetItem(task.get('type', '')))
            self.ui.todoTable.setItem(row, 4, QtWidgets.QTableWidgetItem(task.get('priority', '')))
            self.ui.todoTable.setItem(row, 5, QtWidgets.QTableWidgetItem(task.get('deadline', 'N/A')))
            self.ui.todoTable.setItem(row, 6, QtWidgets.QTableWidgetItem(task.get('approval_status', 'N/A')))

        self.ui.todoTable.resizeColumnsToContents()

    def setup_pending_tasks_tab(self, pending_tasks):
        # Create a new tab for pending tasks
        pending_table = QtWidgets.QTableWidget()
        pending_table.setColumnCount(7)
        pending_table.setHorizontalHeaderLabels(
            ["User", "Title", "Description", "Status", "Type", "Priority", "Actions"]
        )
        pending_table.setRowCount(len(pending_tasks))

        for row, task in enumerate(pending_tasks):
            # Add task details
            pending_table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(task['user_id'])))
            pending_table.setItem(row, 1, QtWidgets.QTableWidgetItem(task['title']))
            pending_table.setItem(row, 2, QtWidgets.QTableWidgetItem(task['description']))
            pending_table.setItem(row, 3, QtWidgets.QTableWidgetItem(task['status']))
            pending_table.setItem(row, 4, QtWidgets.QTableWidgetItem(task['type']))
            pending_table.setItem(row, 5, QtWidgets.QTableWidgetItem(task['priority']))

            # Add approve/reject buttons
            approve_button = QtWidgets.QPushButton("Approve")
            reject_button = QtWidgets.QPushButton("Reject")
            
            approve_button.clicked.connect(lambda checked, t=task: self.approve_task(t))
            reject_button.clicked.connect(lambda checked, t=task: self.reject_task(t))

            button_widget = QtWidgets.QWidget()
            button_layout = QtWidgets.QHBoxLayout()
            button_layout.addWidget(approve_button)
            button_layout.addWidget(reject_button)
            button_widget.setLayout(button_layout)

            pending_table.setCellWidget(row, 6, button_widget)

        self.ui.tabWidget.addTab(pending_table, "Pending Tasks")

    def approve_task(self, task):
        success, message = self.db_manager.update_task_approval(task['id'], 'Approved')
        if success:
            QtWidgets.QMessageBox.information(self, "Success", "Task approved")
            self.setup_dashboard()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", message)

    def reject_task(self, task):
        success, message = self.db_manager.update_task_approval(task['id'], 'Rejected')
        if success:
            QtWidgets.QMessageBox.information(self, "Success", "Task rejected")
            self.setup_dashboard()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", message)

    def show_task_context_menu(self, pos):
        context_menu = QtWidgets.QMenu(self)
        view_history_action = context_menu.addAction("View Detail")
        
        action = context_menu.exec_(self.ui.todoTable.mapToGlobal(pos))
        
        if action == view_history_action:
            self.view_task_history()
            
    def connect_buttons(self):
        self.ui.addButton.clicked.connect(self.open_add_task)
        self.ui.editButton.clicked.connect(self.edit_task)
        self.ui.deleteButton.clicked.connect(self.delete_task)
        self.ui.filterComboBox.currentTextChanged.connect(self.filter_tasks)
        self.ui.refreshButton.clicked.connect(self.setup_dashboard)
        self.ui.backButton.clicked.connect(self.handle_back_button)
        self.ui.searchBar.textChanged.connect(self.search_tasks)

        history_button = QtWidgets.QPushButton("View Detail")
        self.ui.buttonLayout.addWidget(history_button)
        history_button.clicked.connect(self.view_task_history)

    def open_add_task(self):
        add_task_dialog = AddTaskDialog(self.db_manager, self.user_id, self.user_role)
        add_task_dialog.exec_()
        self.setup_dashboard()

    def edit_task(self):
        try:
            selected_row = self.ui.todoTable.currentRow()
            if selected_row == -1:
                QtWidgets.QMessageBox.warning(self, "Error", "Pilih yang mau di edit")
                return

            tasks = self.db_manager.get_tasks(self.user_id, user_role=self.user_role)
            task = tasks[selected_row]

            crud_form = CrudForm(
                self.db_manager, 
                self.user_id, 
                self.user_role, 
                task=task  
            )
            crud_form.exec_()
            
            self.setup_dashboard()
        
        except Exception as e:
            print(f"Error in edit_task: {e}")
            import traceback
            traceback.print_exc()
            QtWidgets.QMessageBox.critical(self, "Critical Error", str(e))

    def delete_task(self):
        selected_row = self.ui.todoTable.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self, "Error", "Pilih yang mau di hapus")
            return

        delete_confirm = DeleteConfirmDialog(self)
        result = delete_confirm.exec_()

        if result == QtWidgets.QDialog.Accepted:
            tasks = self.db_manager.get_tasks(self.user_id)
            task = tasks[selected_row]
            
            success, message = self.db_manager.delete_task(task['id'], self.user_id)
            
            if success:
                QtWidgets.QMessageBox.information(self, "Success", message)
                self.setup_dashboard()
            else:
                QtWidgets.QMessageBox.warning(self, "Error", message)

    def filter_tasks(self, task_filter):
        # Get tasks based on the filter
        tasks = self.db_manager.get_tasks(self.user_id, task_filter)
        
        self.ui.todoTable.setRowCount(len(tasks))
        
        for row, task in enumerate(tasks):
            self.ui.todoTable.setItem(row, 0, QtWidgets.QTableWidgetItem(task['title']))
            self.ui.todoTable.setItem(row, 1, QtWidgets.QTableWidgetItem(task['description']))
            self.ui.todoTable.setItem(row, 2, QtWidgets.QTableWidgetItem(task['status']))
            self.ui.todoTable.setItem(row, 3, QtWidgets.QTableWidgetItem(task['type']))
            self.ui.todoTable.setItem(row, 4, QtWidgets.QTableWidgetItem(task['priority']))
            self.ui.todoTable.setItem(row, 5, QtWidgets.QTableWidgetItem(task['deadline']))
            self.ui.todoTable.setItem(row, 6, QtWidgets.QTableWidgetItem(task['approval_status']))
        
        total_tasks = len(tasks)
        completed_tasks = sum(1 for task in tasks if task['status'] == 'Completed')
        remaining_tasks = total_tasks - completed_tasks
        progress_percentage = int((completed_tasks / total_tasks) * 100) if total_tasks > 0 else 0
        
        self.ui.totalTasks.setText(f"Total Tasks: {total_tasks}")
        self.ui.completedTasks.setText(f"Completed: {completed_tasks}")
        self.ui.remainingTasks.setText(f"Remaining: {remaining_tasks}")
        self.ui.progressBar.setValue(progress_percentage)

    def handle_back_button(self):
        reply = QtWidgets.QMessageBox.question(
            self, 'Konfirmasi', 'Apakah Anda yakin ingin kembali ke halaman login?',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )

        if reply == QtWidgets.QMessageBox.Yes:            
            self.login_window = LoginWindow(self.db_manager)
            
            self.login_window.show()
            
            self.close()

    def search_tasks(self):
        search_term = self.ui.searchBar.text().strip()
        if search_term:
            tasks = self.db_manager.search_tasks(self.user_id, search_term)
        else:
            tasks = self.db_manager.get_tasks(self.user_id)
        
        self.ui.todoTable.setRowCount(len(tasks))
        
        for row, task in enumerate(tasks):
            self.ui.todoTable.setItem(row, 0, QtWidgets.QTableWidgetItem(task['title']))
            self.ui.todoTable.setItem(row, 1, QtWidgets.QTableWidgetItem(task['description']))
            self.ui.todoTable.setItem(row, 2, QtWidgets.QTableWidgetItem(task['status']))
            self.ui.todoTable.setItem(row, 3, QtWidgets.QTableWidgetItem(task['type']))
            self.ui.todoTable.setItem(row, 4, QtWidgets.QTableWidgetItem(task['priority']))
            self.ui.todoTable.setItem(row, 5, QtWidgets.QTableWidgetItem(task['deadline']))
            self.ui.todoTable.setItem(row, 6, QtWidgets.QTableWidgetItem(task['approval_status']))

    def view_task_history(self):
        selected_row = self.ui.todoTable.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self, "Error", "Pilih yang mau di view detail")
            return

        tasks = self.db_manager.get_tasks(self.user_id)
        task = tasks[selected_row]

        history_dialog = QtWidgets.QDialog(self)
        history_dialog.setWindowTitle(f"Task Detail: {task['title']}")
        layout = QtWidgets.QVBoxLayout()

        details = [
            f"Title: {task['title']}",
            f"Description: {task['description']}",
            f"Status: {task['status']}",
            f"Type: {task['type']}",
            f"Priority: {task['priority']}",
            f"Dibuat pada: {task.get('created_at', 'N/A')}",
            f"Deadline: {task['deadline']}",
        ]

        for detail in details:
            label = QtWidgets.QLabel(detail)
            layout.addWidget(label)

        history_dialog.setLayout(layout)
        history_dialog.exec_()

# ===============================================================================================
# ===============================================================================================
# ===============================================================================================

def main():
    app = QtWidgets.QApplication(sys.argv)
    db_manager = DatabaseManager()
    login_window = LoginWindow(db_manager)
    login_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()