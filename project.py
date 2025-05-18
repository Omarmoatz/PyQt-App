import sys

# 1. Import QApplication and all the required widgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QMainWindow





class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt App")

        layout = QVBoxLayout()

        self.label = QLabel("<h1>Hello, World!</h1>")
        self.btn = QPushButton("click here")

        self.btn.clicked.connect(self.on_button_click)

        layout.addWidget(self.label)
        layout.addWidget(self.btn)

        window = QWidget()
        window.setLayout(layout)
        
        self.setCentralWidget(window)


    def on_button_click(self):
        self.label.setText("<h1>the button clicked</h1>")
        self.btn.setText("clicked")




# 2. Create an instance of QApplication

app = QApplication([])
window = MainApp()
window.show()


# 5. Run your application's event loop
sys.exit(app.exec())