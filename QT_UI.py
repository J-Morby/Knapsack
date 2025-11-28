import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QLabel, QVBoxLayout, QPushButton, QWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QPushButton, QHBoxLayout
)
class Spreadsheet(QWidget):
    def __init__(self):
        super().__init__()

        self.table = QTableWidget(0, 3)  # 0 rows, 3 columns
        self.table.setHorizontalHeaderLabels(["Name", "Value", "Size"])

        # Buttons
        add_btn = QPushButton("Add Item")
        remove_btn = QPushButton("Remove Selected Item")
        add_test_btn = QPushButton("Add Test Data")
        start_button = QPushButton("Start")

        add_btn.clicked.connect(self.add_row)
        remove_btn.clicked.connect(self.remove_row)
        add_test_btn.clicked.connect(self.add_test_rows)
        start_button.clicked.connect(self.start)

        # Layout
        widget_button_layout = QHBoxLayout()
        widget_button_layout.addWidget(add_btn)
        widget_button_layout.addWidget(remove_btn)
        widget_button_layout.addWidget(add_test_btn)

        start_button_layout = QHBoxLayout()
        start_button_layout.addWidget(start_button)


        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(widget_button_layout)
        layout.addLayout(start_button_layout)

        self.setLayout(layout)
        self.setWindowTitle("Spreadsheet Example")

    def start(self):
        pass

    def add_row(self):
        row = self.table.rowCount()
        self.table.insertRow(row)

        #set empty default items
        for col in range(self.table.columnCount()):
            self.table.setItem(row, col, QTableWidgetItem(["Name", "Value", "Size"]))

    def add_test_rows(self):
        row = self.table.rowCount()
        #self.table.insertRow(row)

        preset_values = [["Hat"   , 2, 2],
                         ["Phone" , 5, 3],
                         ["Keys"  , 8, 1],
                         ["Laptop", 8, 8]]

        for row_data in preset_values:
            row = self.table.rowCount()
            self.table.insertRow(row)
            for col, value in enumerate(row_data):
                self.table.setItem(row, col, QTableWidgetItem(str(value)))

        

    def remove_row(self):
        selected = self.table.currentRow()
        if selected >= 0:
            self.table.removeRow(selected)

    def get_data(self):
        data = []
        for row in range(self.table.rowCount()):
            row_data = []
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                row_data.append(item.text() if item else "")
            data.append(row_data)
        return data


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Spreadsheet()
    window.show()
    print("test")
    sys.exit(app.exec_())