import sys

# 1. Import QApplication and all the required widgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QMainWindow
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)




class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt App")
        self.setFixedSize(QSize(600,500))

        layout = QVBoxLayout()

        self.label = QLabel()

        self.username_label = QLabel("<h1>Username</h1>")
        self.username_input = QLineEdit()
        
        self.password_label = QLabel("<h1>password</h1>")
        self.password_input = QLineEdit()

        self.age = QLCDNumber()


        self.btn = QPushButton("Login")
        self.btn.clicked.connect(self.on_button_click)

        widgets = [
            self.label,
            self.username_label,
            self.username_input,
            
            self.password_label,
            self.password_input,
            
            # self.age,
            self.btn,
            # QCheckBox,
            # QComboBox,
            # QDateEdit,
            # QDateTimeEdit,
            # QDial,
            # QDoubleSpinBox,
            # QFontComboBox,
            # QLCDNumber,
            # QLabel,
            # QProgressBar,
            # QPushButton,
            # QRadioButton,
            # QSlider,
            # QSpinBox,
            # QTimeEdit,
        ]

        for w in widgets:
            layout.addWidget(w)

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