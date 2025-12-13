import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QLabel, QVBoxLayout, QPushButton, QWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QPushButton, QHBoxLayout,QSlider)

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
        self.start_time_txt = QLineEdit()
        self.start_time_txt.setText("9")
        self.end_time_txt = QLineEdit()
        self.end_time_txt.setText("17")

        # Lable----------------------
        start_time_lbl = QLabel("Start Time")
        end_time_lbl = QLabel("End Time")

        # Slider--------------------
        start_time_layout = QHBoxLayout()
        start_slider = QSlider(Qt.Orientation.Horizontal)
        start_slider.setMinimum(0000)
        start_slider.setMaximum(2400)
        start_slider.setValue(900)
        end_time_layout = QHBoxLayout()
        end_slider = QSlider(Qt.Orientation.Horizontal)
        end_slider.setMinimum(0000)
        end_slider.setMaximum(2400)
        end_slider.setValue(1700)

        # Layouts--------------------
        widget_button_layout = QHBoxLayout()
        widget_button_layout.addWidget(add_btn)
        widget_button_layout.addWidget(remove_btn)
        widget_button_layout.addWidget(add_test_btn)

        times_layout = QHBoxLayout()
        times_layout.addWidget(start_time_lbl)
        times_layout.addWidget(self.start_time_txt)
        times_layout.addWidget(end_time_lbl)
        times_layout.addWidget(self.end_time_txt)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(widget_button_layout)
        layout.addLayout(times_layout)
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

        preset_tasks = [["Unload Washer"   , 2, 2],
                         ["Walk Dog" , 5, 3],
                         ["Pay Mum"  , 8, 1],
                         ["Fix Car", 15, 8]]

        for row_data in preset_tasks:
            row = self.table.rowCount()
            self.table.insertRow(row)
            for col, importance in enumerate(row_data):
                self.table.setItem(row, col, QTableWidgetItem(str(importance)))

        

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