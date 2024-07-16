import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QMessageBox

class ContactBook(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Daftar Kontak')
        self.setGeometry(100, 100, 400, 300)

        # Label dan input untuk nama
        self.name_label = QLabel('Nama:', self)
        self.name_input = QLineEdit(self)

        # Label dan input untuk nomor telepon
        self.phone_label = QLabel('Nomor Telepon:', self)
        self.phone_input = QLineEdit(self)

        # Tombol untuk menambahkan kontak
        self.add_button = QPushButton('Tambah Kontak', self)
        self.add_button.clicked.connect(self.add_contact)

        # Daftar kontak
        self.contact_list = QListWidget(self)

        # Layout untuk input
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.name_label)
        input_layout.addWidget(self.name_input)
        input_layout.addWidget(self.phone_label)
        input_layout.addWidget(self.phone_input)
        input_layout.addWidget(self.add_button)

        # Layout utama
        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.contact_list)

        self.setLayout(main_layout)

    def add_contact(self):
        name = self.name_input.text()
        phone = self.phone_input.text()

        if not name or not phone:
            QMessageBox.warning(self, "Peringatan", "Nama dan nomor telepon harus diisi.")
            return

        self.contact_list.addItem(f"{name} - {phone}")
        self.name_input.clear()
        self.phone_input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ContactBook()
    window.show()
    sys.exit(app.exec_())
