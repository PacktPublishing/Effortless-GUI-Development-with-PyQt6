#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Ch03. 'Updated Shopping List' example from the "Effortless GUI Development with PyQt6" book.
   
   Access the repository with all examples at:
   https://github.com/PacktPublishing/Effortless-GUI-Development-with-PyQt6
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QRadioButton, QComboBox, QWidget
from PyQt6.QtWidgets import QGridLayout
from PyQt6.QtCore import Qt, pyqtSignal


class CustomCheckBox(QCheckBox):
    # Define a signal that will be fired when an item becomes checked, the argument is text
    item_checked = pyqtSignal(str)

    def __init__(self, label, parent=None):
        super().__init__(label, parent)
        self.stateChanged.connect(self.emit_checked_state)

    def emit_checked_state(self, state):
        # if (Qt.CheckState(state) == Qt.CheckState.Checked):
        if (Qt.CheckState(state) == Qt.CheckState.Checked):
            self.setStyleSheet("QCheckBox { text-decoration: line-through; }")
            # Emit with item label and checked state
            self.item_checked.emit(self.text())
        else:
            self.setStyleSheet("")


class ShoppingListApp(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget(self)  # Central widget to hold the layout
        self.setCentralWidget(central_widget)

        # Apply QGridLayout
        layout = QGridLayout(central_widget)  # Main layout for the central widget

        # Create and add checkboxes
        items = ["Apples", "Bread", "Milk"]
        for index, item in enumerate(items):
            current = CustomCheckBox(item, self)
            current.item_checked.connect(self.handle_item_checked)
            layout.addWidget(current, index, 0)

        items = ["Cake", "Ice cream", "Pack of donuts"]
        for index, item in enumerate(items):
            current = QRadioButton(item, self)
            layout.addWidget(current, index, 1)

        # Label for ComboBox
        self.store_label = QLabel("Buy at: ", self)
        layout.addWidget(self.store_label, 3, 0)

        # ComboBox for choosing alternative item (select only one of a category)
        self.store_combo = QComboBox(self)
        self.store_combo.addItems(["Local store", "Supermarket", "23/7", "Order delivery"])
        layout.addWidget(self.store_combo, 3, 1)

        # Set the window title and size
        self.setWindowTitle("Shopping List App")
        self.setGeometry(300, 300, 280, 180)  # x, y, width, height

    def handle_item_checked(self, item):
        print(f'"{item}" bought!')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShoppingListApp()
    window.show()
    sys.exit(app.exec())
