#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Ch02. 'Login Screen' example from the "Effortless GUI Development with PyQt6" book.
   
   Access the repository with all examples at:
   https://github.com/PacktPublishing/Effortless-GUI-Development-with-PyQt6
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit


class LoginScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the username components
        self.user_label = QLabel("Username:", self)
        self.user_label.move(20, 20)  # Move label to x=20, y=20
        self.user_text = QLineEdit(self)
        self.user_text.move(100, 20)  # Move text field to x=100, y=20
        self.user_text.resize(200, 20)  # Resize the width of text field

        # Set up the password components
        self.pass_label = QLabel("Password:", self)
        self.pass_label.move(20, 60)  # Move label to x=20, y=60
        self.pass_text = QLineEdit(self)
        self.pass_text.move(100, 60)  # Move text field to x=100, y=60
        self.pass_text.resize(200, 20)  # Resize the width of text field
        self.pass_text.setEchoMode(QLineEdit.EchoMode.Password)  # Mask password

        # Set up the login button
        self.login_button = QPushButton("Login", self)
        self.login_button.move(100, 100)  # Position the button

        # Window settings
        self.setWindowTitle('Login Screen')
        self.setGeometry(300, 300, 320, 150)  # x, y, width, height


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_screen = LoginScreen()
    login_screen.show()
    sys.exit(app.exec())
