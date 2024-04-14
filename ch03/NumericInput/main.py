#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Ch03. 'Numeric Input' example from the "Effortless GUI Development with PyQt6" book.
   
   Access the repository with all examples at:
   https://github.com/PacktPublishing/Effortless-GUI-Development-with-PyQt6
"""

from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
import sys

class KeyPressFilter(QtCore.QObject):
  def eventFilter(self, watched, event):
    if event.type() == QtCore.QEvent.Type.KeyPress:
      if event.key() >= QtCore.Qt.Key.Key_0 and event.key() <= QtCore.Qt.Key.Key_9:
        return False
      print(f"'{event.text()}' (key '{event.key()}') is not numeric. Skipping.")
      return True
    return super().eventFilter(watched, event)

class KeyPressFilter(QtCore.QObject):
  def eventFilter(self, watched, event):
    if event.type() == QtCore.QEvent.Type.KeyPress:
      # Check if the key pressed is a digit
      if event.key() >= QtCore.Qt.Key.Key_0 and event.key() <= QtCore.Qt.Key.Key_9:
        # If it's a digit, let the event be processed as usual
        return False
      # If it's not a digit, ignore the key press event
      print(f"'{event.text()}' (key '{event.key()}') is not numeric. Skipping.")
      return True
    # For all other events, process as usual
    return super().eventFilter(watched, event)

class NumericInputApp(QMainWindow):
  def __init__(self):
    super().__init__()
    # Create QLineEdit
    self.line_edit = QLineEdit(self)
    self.line_edit.installEventFilter(KeyPressFilter(self.line_edit))
    self.setCentralWidget(self.line_edit)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NumericInputApp()
    window.show()
    sys.exit(app.exec())
