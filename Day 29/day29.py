import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox

class NotepadApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Notepad App")
        self.setGeometry(100, 100, 600, 400)

        self.text_edit = QTextEdit(self)
        self.save_button = QPushButton("Save", self)
        self.save_button.clicked.connect(self.save_note)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.save_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def save_note(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Note", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            try:
                with open(file_name, 'w') as file:
                    note = self.text_edit.toPlainText()
                    file.write(note)
                QMessageBox.information(self, "Success", "Note saved successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not save note: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotepadApp()
    window.show()
    sys.exit(app.exec_())
