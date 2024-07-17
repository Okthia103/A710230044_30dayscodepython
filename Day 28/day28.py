import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kalkulator")

        layout = QVBoxLayout()

        self.labelinput2 = QLabel("Masukkan Angka 1")
        layout.addWidget(self.labelinput2)
        self.first_number = QLineEdit()
        layout.addWidget(self.first_number)

        self.labelinput3 = QLabel("Masukkan Angka 2")
        layout.addWidget(self.labelinput3)
        self.second_number = QLineEdit()
        layout.addWidget(self.second_number)

        self.add_button = QPushButton("Tambah")
        self.add_button.clicked.connect(self.add_numbers)
        layout.addWidget(self.add_button)

        self.subtract_button = QPushButton("Kurang")
        self.subtract_button.clicked.connect(self.subtract_numbers)
        layout.addWidget(self.subtract_button)

        self.multiply_button = QPushButton("Kali")
        self.multiply_button.clicked.connect(self.multiply_numbers)
        layout.addWidget(self.multiply_button)

        self.divide_button = QPushButton("Bagi")
        self.divide_button.clicked.connect(self.divide_numbers)
        layout.addWidget(self.divide_button)

        self.modulus_button = QPushButton("Modulus")
        self.modulus_button.clicked.connect(self.modulus_numbers)
        layout.addWidget(self.modulus_button)

        self.power_button = QPushButton("Pangkat")
        self.power_button.clicked.connect(self.power_numbers)
        layout.addWidget(self.power_button)

        self.result_label = QLabel("Hasil Perhitungan")
        layout.addWidget(self.result_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_numbers(self):
        result = float(self.first_number.text()) + float(self.second_number.text())
        self.result_label.setText(str(result))

    def subtract_numbers(self):
        result = float(self.first_number.text()) - float(self.second_number.text())
        self.result_label.setText(str(result))

    def multiply_numbers(self):
        result = float(self.first_number.text()) * float(self.second_number.text())
        self.result_label.setText(str(result))

    def divide_numbers(self):
        result = float(self.first_number.text()) / float(self.second_number.text())
        self.result_label.setText(str(result))

    def modulus_numbers(self):
        result = float(self.first_number.text()) % float(self.second_number.text())
        self.result_label.setText(str(result))

    def power_numbers(self):
        result = float(self.first_number.text()) ** float(self.second_number.text())
        self.result_label.setText(str(result))

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
