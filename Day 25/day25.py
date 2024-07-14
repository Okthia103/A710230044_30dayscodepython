import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox
from PyQt5.QtCore import Qt

class TemperatureConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Konversi Suhu')
        self.setGeometry(100, 100, 300, 200)

        # Label input
        self.input_label = QLabel('Masukkan suhu:', self)
        self.input_temp = QLineEdit(self)

        # Tombol radio untuk jenis konversi
        self.radio_c_to_f = QRadioButton('Celsius ke Fahrenheit', self)
        self.radio_f_to_c = QRadioButton('Fahrenheit ke Celsius', self)
        self.radio_c_to_f.setChecked(True)  # Default pilihan

        # Tombol konversi
        self.convert_button = QPushButton('Konversi', self)
        self.convert_button.clicked.connect(self.convert_temperature)

        # Label output
        self.output_label = QLabel('Hasil konversi:', self)
        self.result_label = QLabel(self)

        # Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.input_label)
        main_layout.addWidget(self.input_temp)

        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.radio_c_to_f)
        radio_layout.addWidget(self.radio_f_to_c)
        main_layout.addLayout(radio_layout)

        main_layout.addWidget(self.convert_button)
        main_layout.addWidget(self.output_label)
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)

    def convert_temperature(self):
        try:
            temperature = float(self.input_temp.text())
            if self.radio_c_to_f.isChecked():
                converted_temp = temperature * 9/5 + 32
                self.result_label.setText(f'Hasil konversi: {converted_temp:.2f} Fahrenheit')
            elif self.radio_f_to_c.isChecked():
                converted_temp = (temperature - 32) * 5/9
                self.result_label.setText(f'Hasil konversi: {converted_temp:.2f} Celsius')
        except ValueError:
            QMessageBox.critical(self, "Error", "Masukkan angka yang valid untuk suhu.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = TemperatureConverter()
    converter.show()
    sys.exit(app.exec_())
