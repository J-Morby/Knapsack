from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSlider, QApplication, QHBoxLayout
from PyQt5.QtCore import Qt
import sys


class TimeSlider(QWidget):
    def __init__(self, text):
        super().__init__()

        self.name = text

        self.label = QLabel(f"{self.name} Time: 00:00")

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(97 - 1)  # 97 increments -> 24h
        self.slider.setSingleStep(1)
        self.slider.valueChanged.connect(self.update_label)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.slider)
        self.setLayout(layout)

    def update_label(self, value):
        total_minutes = value * 15
        h = total_minutes // 60
        m = total_minutes % 60
        self.label.setText(f"{self.name} Time: {h:02d}:{m:02d}") #print fromat hh:mm e.g 09:15

    def get_minutes(self):
        return self.slider.value() * 15

    def set_value(self, hour):
        minutes = (hour*(4*15)) #convert
        self.slider.setValue(minutes // 15)

    def convert_to_hhmm(minutes:int)->str:
        total_minutes = minutes
        h = total_minutes // 60
        m = total_minutes % 60
        hhmm = (f"{h:02d}:{m:02d}") #print fromat hh:mm e.g 09:15
        return hhmm
    
    def convert_to_minutes(hhmm:str)->int:
        h,m = map(int, hhmm.split(":"))
        minutes = (h*60) + m
        return minutes


class StartEndTimeSelector(QWidget):
    def __init__(self):
        super().__init__()

        self.start_slider = TimeSlider(f"Start")
        #self.start_slider.set_value(9)
        self.end_slider = TimeSlider(f"End")
        #self.end_slider.set_value(17)

        # force end >= start & start <= end
        self.start_slider.slider.valueChanged.connect(self.enforce_constraints)
        self.end_slider.slider.valueChanged.connect(self.enforce_constraints)

        layout = QHBoxLayout()
        layout.addWidget(self.start_slider)
        layout.addWidget(self.end_slider)
        self.setLayout(layout)

    def enforce_constraints(self,a,b):
        start = self.start_slider.slider.value()
        end = self.end_slider.slider.value()

        if end < start:
            self.end_slider.slider.setValue(start)
        if start > end:
            self.start_slider.slider.setValue(end)


    def get_time_range(self):
        return (
            self.start_slider.get_minutes(),
            self.end_slider.get_minutes(),
        )
    
    


class Demo(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # create multiple start-end pairs
        self.pairs = []
        widget = StartEndTimeSelector()
        self.pairs.append(widget)
        layout.addWidget(widget)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Demo()
    win.show()
    sys.exit(app.exec_())
