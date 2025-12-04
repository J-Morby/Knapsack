import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QLabel, QVBoxLayout, QPushButton, QWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QPushButton, QHBoxLayout)

from Knapsack import Fill_Knapsack, Generate_Schedule
from Config import Task,tasks



class Spreadsheet(QWidget):
    def __init__(self):
        super().__init__()

        self.table = QTableWidget(0, 3)  # 0 rows, 3 columns
        self.table.setHorizontalHeaderLabels(["Name", "Importance", "Length"])

        # Buttons--------------------
        add_btn = QPushButton("Add Task")
        remove_btn = QPushButton("Remove Selected Task")
        add_test_btn = QPushButton("Add Test Data")
        start_button = QPushButton("Start")

        add_btn.clicked.connect(self.add_row)
        remove_btn.clicked.connect(self.remove_row)
        add_test_btn.clicked.connect(self.add_test_rows)
        start_button.clicked.connect(self.start)

        # TextBox--------------------
        self.knapsack_size_txt = QLineEdit()
        self.knapsack_size_txt.setText("10")

        # Lable----------------------
        knapsack_size_lbl = QLabel("Knappsack Size")

        # Layouts--------------------
        widget_button_layout = QHBoxLayout()
        widget_button_layout.addWidget(add_btn)
        widget_button_layout.addWidget(remove_btn)
        widget_button_layout.addWidget(add_test_btn)

        knapsack_size_layout = QHBoxLayout()
        knapsack_size_layout.addWidget(knapsack_size_lbl)
        knapsack_size_layout.addWidget(self.knapsack_size_txt)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(widget_button_layout)
        layout.addLayout(knapsack_size_layout)
        layout.addWidget(start_button)

        self.setLayout(layout)
        self.setWindowTitle("Spreadsheet Example")

    def start(self):
        # read knapsack size from textbox
        try:
            knapsack_size = int(self.knapsack_size_txt.text())
        except ValueError:
            print("Invalid knapsack size")
            return
        
        # get rows from UI
        self.get_data()

        Generate_Schedule()
        

    def add_row(self):
        row = self.table.rowCount()
        self.table.insertRow(row)

        #set empty default items
        for col in range(self.table.columnCount()):
            self.table.setItem(row, col, QTableWidgetItem(["Name", "Importance", "Length"]))

    def add_test_rows(self):
        row = self.table.rowCount()
        #self.table.insertRow(row)

        preset_values = [["Unload Washer"   , 2, 2],
                         ["Walk Dog" , 5, 3],
                         ["Pay Mum"  , 8, 1],
                         ["Fix Car", 8, 8]]

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
        tasks.clear()   # wipe old data

        for row in range(self.table.rowCount()):
            name_task  = self.table.item(row, 0)
            importance_task = self.table.item(row, 1)
            length_task  = self.table.item(row, 2)

            # skip empty rows
            if not name_task or not importance_task or not length_task:  
                continue

            name = name_task.text()
            importance = int(importance_task.text())
            lenth = int(length_task.text())

            tasks.append(Task(name, importance, lenth))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Spreadsheet()
    window.show()   
    print("test")
    sys.exit(app.exec_())