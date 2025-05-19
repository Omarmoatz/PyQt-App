import sys
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QMessageBox


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("PyQt App")
        self.setGeometry(1100,300, 600, 400)
        
        self.count = 0
        self.label = QLabel(str(self.count), self)
        self.label.move(100, 150)

        button = QPushButton("Add", self)
        button.move(100, 200)
        button.clicked.connect(self.on_click)
        
        
        button1 = QPushButton("show message", self)
        button1.resize(120, 30)
        button1.move(300, 200)
        button1.clicked.connect(self.on_click_show_message)




    def on_click(self):
        self.count += 254
        self.label.setText(str(self.count))
        self.label.adjustSize()

    def on_click_show_message(self):
        message = QMessageBox(self)
        message.setWindowTitle("A message Title")
        message.setText("some info message Text")
        message.setIcon(QMessageBox.Icon.Question)
        message.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        message.setDefaultButton(QMessageBox.StandardButton.Ok)
        message.adjustSize()
        message.exec()


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
        
    



