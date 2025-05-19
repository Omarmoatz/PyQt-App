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
    QGridLayout,
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class MainApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt App")
        # self.setGeometry(1100, 300, 300, 200)
        self.setFixedSize(QSize(600,500))
        self.setStyleSheet("""
            QWidget {
                background-color: white;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 6px;
                background-color: #fff;
            }
            QPushButton {
                background-color: #0078d4;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #005fa3;
            }
        """)

        self.label = QLabel()


        self.username_label = QLabel("Username")
        self.username_input = QLineEdit()
        # self.username_input.resize(5,5)
        
        self.password_label = QLabel("password")
        self.password_input = QLineEdit()

        self.age = QLCDNumber()

        image_label = QLabel()
        image = QPixmap("./logo.jpg")
        image_label.setPixmap(image.scaled(320,620, Qt.AspectRatioMode.KeepAspectRatio))


        self.btn = QPushButton("Login")
        self.btn.clicked.connect(self.on_button_click)

        layout = QGridLayout()

        layout.addWidget(self.username_label, 1,0)
        layout.addWidget(self.username_input, 2,0)

        layout.addWidget(self.password_label, 3,0)
        layout.addWidget(self.password_input, 4,0)

        layout.addWidget(self.btn)

        layout.addWidget(image_label, 1,1)

        self.setLayout(layout)
        

    def on_button_click(self):
        self.label.setText("the button clicked")
        self.btn.setText("clicked")



app = QApplication([])
window = MainApp()
window.show()
sys.exit(app.exec())




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