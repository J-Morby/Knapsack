import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QVBoxLayout, QPushButton



def on_click():
    print("Button clicked!")


def focus_next(widget):
    widget.setFocus()  # move focus to the next widget

# Step 1: Create QApplication
app = QApplication(sys.argv)

# Step 2: Create a main window
window = QWidget()
window.setWindowTitle("PyQt Hello World")
window.setGeometry(100, 100, 300, 200)  # x, y, width, height

# # Step 3: Add a label
# label = QLabel("Hello, PyQt!", parent=window)
# label.move(100, 80)  # Position label

# StartBtn = QPushButton("Start", window)
# StartBtn.move(100,100)
# StartBtn.clicked.connect(on_click)

TxtName = QLineEdit(window)  
TxtName.setPlaceholderText("Name...")
TxtName.move(10,10)

TxtLength= QLineEdit(window)  
TxtLength.setPlaceholderText("Length...")
TxtLength.move(10,40)

TxtValue = QLineEdit(window)  
TxtValue.setPlaceholderText("Value...")
TxtValue.move(10,70)

# Connect returnPressed to move focus
TxtName.returnPressed.connect(lambda: focus_next(TxtLength))
TxtLength.returnPressed.connect(lambda: focus_next(TxtValue))
TxtValue.returnPressed.connect(lambda: focus_next(TxtName))  # loop back to first


# Step 4: Show the window
window.show()

# Step 5: Run the event loop
sys.exit(app.exec_())