import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QPushButton, QHBoxLayout
)

class Spreadsheet(QWidget):
    def __init__(self):
        super().__init__()

        self.table = QTableWidget(0, 3)  # 0 rows, 3 columns
        self.table.setHorizontalHeaderLabels(["Name", "Value", "Comment"])

        # Buttons
        add_btn = QPushButton("Add Row")
        remove_btn = QPushButton("Remove Selected Row")

        add_btn.clicked.connect(self.add_row)
        remove_btn.clicked.connect(self.remove_row)

        # Layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(add_btn)
        button_layout.addWidget(remove_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.setWindowTitle("Spreadsheet Example")

    def add_row(self):
        row = self.table.rowCount()
        self.table.insertRow(row)

        # Optional: set empty default items
        for col in range(self.table.columnCount()):
            self.table.setItem(row, col, QTableWidgetItem(""))

    def remove_row(self):
        selected = self.table.currentRow()
        if selected >= 0:
            self.table.removeRow(selected)

    def get_data(self):
        """Return the spreadsheet data as a list of rows."""
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
    sys.exit(app.exec_())
