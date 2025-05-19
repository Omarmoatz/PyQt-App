import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QFrame
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QSize


class MainAppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main App")
        # self.setGeometry(150, 150, 400, 200)
        self.setFixedSize(QSize(650,500))

        label = QLabel("Welcome to the main application!", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Panel")
        # self.setGeometry(100, 100, 600, 300)
        self.setFixedSize(QSize(650,500))
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setup_ui()

    def setup_ui(self):
        # Main Layout
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Left Side (Indigo background)
        left_frame = QFrame()
        left_frame.setStyleSheet("background-color: white;")
        left_frame.setFixedWidth(250)
        left_layout = QVBoxLayout(left_frame)

        # Right Side (White background with centered form)
        right_frame = QFrame()
        right_frame.setStyleSheet("background-color: indigo;")
        right_outer_layout = QVBoxLayout(right_frame)
        right_outer_layout.setContentsMargins(0, 0, 0, 0)
        right_outer_layout.setSpacing(0)

        # Close button (Top-right)
        close_btn = QPushButton("✕")
        close_btn.setFixedSize(30, 30)
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                font-size: 16px;
                color: #444;
            }
            QPushButton:hover {
                color: red;
            }
        """)
        close_btn.clicked.connect(self.close)

        close_layout = QHBoxLayout()
        close_layout.addStretch()
        close_layout.addWidget(close_btn)
        close_layout.setContentsMargins(0, 0, 10, 0)

        # Inner form layout
        form_layout = QVBoxLayout()
        form_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout.setContentsMargins(40, 20, 40, 20)
        form_layout.setSpacing(15)

        self.logo_label = QLabel()
        pixmap = QPixmap("logo.jpg")
        self.logo_label.setPixmap(pixmap.scaled(250, 250, Qt.AspectRatioMode.KeepAspectRatio))
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.login_label = QLabel("<h1> Login </h1>")

        self.username_label = QLabel("User Name:")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.handle_login)

        form_style = """
            QLabel {
                font-size: 14px;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 6px;
                background-color: #f9f9f9;
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
        """
        right_frame.setStyleSheet(right_frame.styleSheet() + form_style)

        form_layout.addWidget(self.login_label)
        form_layout.addWidget(self.username_label)
        form_layout.addWidget(self.username_input)
        form_layout.addWidget(self.password_label)
        form_layout.addWidget(self.password_input)
        form_layout.addWidget(self.login_button)

        right_outer_layout.addLayout(close_layout)
        right_outer_layout.addLayout(form_layout)

        left_layout.addWidget(self.logo_label)

        main_layout.addWidget(left_frame)
        main_layout.addWidget(right_frame)
        self.setLayout(main_layout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "admin" and password == "admin":
            self.main_app = MainAppWindow()
            self.close()
            self.main_app.show()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")


def main():
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
