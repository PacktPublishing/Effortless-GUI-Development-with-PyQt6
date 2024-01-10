#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   ChXX. 'EXAMPLE' example from the "Effortless GUI Development with PyQt6" book 
   by N.Gerasymchuk published by Packt.
   
   Access the repository with all examples at:
   https://github.com/PacktPublishing/Effortless-GUI-Development-with-PyQt6
"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Example')
        self.setGeometry(300, 300, 320, 150)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    e = Example()
    e.show()
    sys.exit(app.exec())
