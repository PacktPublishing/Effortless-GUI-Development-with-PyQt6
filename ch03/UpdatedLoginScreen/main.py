#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Ch03. 'Updated Login Screen' example from the "Effortless GUI Development with PyQt6" book.
   
   Access the repository with all examples at:
   https://github.com/PacktPublishing/Effortless-GUI-Development-with-PyQt6
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QWidget
from PyQt6.QtWidgets import QGridLayout


class UpdatedLoginScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_UI()

        # Define credentials
        self.credentials = {
            "admin": "admin123",
            "user1": "password1"
        }

    def init_UI(self):
        central_widget = QWidget(self)  # Central widget to hold the layout
        self.setCentralWidget(central_widget)

        # Apply QGridLayout
        layout = QGridLayout(central_widget)  # Main layout for the central widget

        # Set up the username components
        self.user_label = QLabel("Username:", self)
        layout.addWidget(self.user_label, 0, 0)

        self.user_text = QLineEdit(self)
        layout.addWidget(self.user_text, 0, 1)

        # Set up the password components
        self.pass_label = QLabel("Password:", self)
        layout.addWidget(self.pass_label, 1, 0)

        self.pass_text = QLineEdit(self)
        self.pass_text.setEchoMode(QLineEdit.EchoMode.Password)  # Mask password
        # Uncomment to make it behave as Windows 10 login screen
        # self.pass_text.textChanged.connect(self.check_password)
        layout.addWidget(self.pass_text, 1, 1)

        # Set up the login button
        self.login_button = QPushButton("Login", self)
        self.login_button.clicked.connect(self.check_password)

        # 1, 2 as last arguments are for rowSpan and columnSpan
        # to make button occupy 1 row and 2 columns
        layout.addWidget(self.login_button, 2, 0, 1, 2)

        # Window settings
        self.setWindowTitle('Login Screen')
        self.setGeometry(300, 300, 320, 150)  # x, y, width, height

    def check_password(self):
        user_login = self.user_text.text()
        user_pass = self.pass_text.text()
        print('-' * 80)
        print(f'Entered login: {user_login}')
        print(f'Entered password: {user_pass}')

        # Check if there is such user with given user_login
        user_exists = user_login in self.credentials

        if not user_exists:
            print(f'No such user "{user_login}"!')
            return

        print(f'User "{user_login}" exists!')

        pass_for_user = self.credentials.get(user_login, None)
        if user_pass != pass_for_user:
            print('Wrong password!')
            return

        print('Correct password! You are welcome!')

        # Do the actions related to successful logging in.
        # Here as example, we disable the components and change the button text
        self.user_text.setEnabled(False)
        self.pass_text.setEnabled(False)
        self.login_button.setEnabled(False)
        self.login_button.setText('You are logged in!')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_screen = UpdatedLoginScreen()
    login_screen.show()
    sys.exit(app.exec())
