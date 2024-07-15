import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QMessageBox

class TicketBooking(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Aplikasi Pemesanan Tiket')
        self.setGeometry(100, 100, 300, 200)

        # Label jenis tiket
        self.ticket_type_label = QLabel('Pilih jenis tiket:', self)
        self.ticket_type_combo = QComboBox(self)
        self.ticket_type_combo.addItems(['Reguler', 'VIP', 'Gold'])

        # Label jumlah tiket
        self.ticket_quantity_label = QLabel('Masukkan jumlah tiket:', self)
        self.ticket_quantity_input = QLineEdit(self)

        # Tombol hitung
        self.calculate_button = QPushButton('Hitung Total Harga', self)
        self.calculate_button.clicked.connect(self.calculate_total)

        # Label hasil
        self.result_label = QLabel('', self)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.ticket_type_label)
        layout.addWidget(self.ticket_type_combo)
        layout.addWidget(self.ticket_quantity_label)
        layout.addWidget(self.ticket_quantity_input)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_total(self):
        ticket_type = self.ticket_type_combo.currentText()
        try:
            quantity = int(self.ticket_quantity_input.text())
            if quantity < 1:
                raise ValueError("Jumlah tiket harus lebih dari 0.")
            if ticket_type == 'Reguler':
                price = 50000
            elif ticket_type == 'VIP':
                price = 100000
            elif ticket_type == 'Gold':
                price = 150000

            total_price = price * quantity
            self.result_label.setText(f'Total harga: Rp{total_price:,}')
        except ValueError as e:
            QMessageBox.critical(self, "Error", str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TicketBooking()
    window.show()
    sys.exit(app.exec_())
