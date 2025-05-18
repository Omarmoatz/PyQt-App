import sys

# 1. Import QApplication and all the required widgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QMainWindow


def on_button_click():
    msg.setText("<h1>the button clicked</h1>")
    btn.setText("clicked")

# 2. Create an instance of QApplication
app = QApplication([])


# 3. Create your application's GUI
window = QWidget()
window.setWindowTitle("")
window.setGeometry(1200, 200, 400, 300)

layout = QVBoxLayout(window)

msg = QLabel("<h1>Hello, World!</h1>", parent=window)
btn = QPushButton("click here", parent=window)
btn.clicked.connect(on_button_click)

layout.addWidget(msg)
layout.addWidget(btn)

# 4. Show your application's GUI
window.show()

# 5. Run your application's event loop
sys.exit(app.exec())