#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Ch01. 'Test Project' example from the "Effortless GUI Development with PyQt6" book 
   by N.Gerasymchuk published by Packt.
   
   Access the repository with all examples at:
   https://github.com/PacktPublishing/Effortless-GUI-Development-with-PyQt6
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Hello Chapter 1!")
window.show()

app.exec()
