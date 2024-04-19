#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Ch03. 'Numeric Input Regular expression' example from the "Effortless GUI Development with PyQt6" book.
   
   Access the repository with all examples at:
   https://github.com/PacktPublishing/Effortless-GUI-Development-with-PyQt6
"""


from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
import sys


class NumericInputApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.line_edit = QLineEdit(self)
        # Regexp transcription:
        #   [0-9] matches any single digit from 0 to 9
        #     *   quantifier that matches zero or more occurrences of the preceding element
        self.regular_exp = QRegularExpression("[0-9]*")
        self.validator = QRegularExpressionValidator(self.regular_exp, self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NumericInputApp()
    window.show()
    sys.exit(app.exec())
