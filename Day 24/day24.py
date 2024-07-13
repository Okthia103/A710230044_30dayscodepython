import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 300, 400)

        # Layout utama
        main_layout = QVBoxLayout()

        # Display
        self.display = QLineEdit(self)
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(35)
        main_layout.addWidget(self.display)

        # Tombol-tombol kalkulator
        buttons_layout = QVBoxLayout()

        # Baris tombol
        rows = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C']
        ]

        for row in rows:
            hbox = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text)
                button.setFixedSize(60, 60)
                button.clicked.connect(self.on_button_clicked)
                hbox.addWidget(button)
            buttons_layout.addLayout(hbox)

        main_layout.addLayout(buttons_layout)
        self.setLayout(main_layout)

    def on_button_clicked(self):
        sender = self.sender()
        button_text = sender.text()

        if button_text == '=':
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception as e:
                QMessageBox.critical(self, "Error", "Invalid input")
        elif button_text == 'C':
            self.display.clear()
        else:
            self.display.setText(self.display.text() + button_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
