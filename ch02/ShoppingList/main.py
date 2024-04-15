#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Ch02. 'Shopping List' example from the "Effortless GUI Development with PyQt6" book.
   
   Access the repository with all examples at:
   https://github.com/PacktPublishing/Effortless-GUI-Development-with-PyQt6
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QRadioButton, QComboBox


class ShoppingListApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # NOTE: Here we'll use few helper integer variables for better positioning of
        #       our visual components. Later we'll utilize layouts for this purpose.
        # Step, distance between items measured by Y axis
        self.y_step = 30
        # Minimal Y position (also called "top margin")
        self.y_position = 20
        # First row X position (also called "left margin")
        self.first_row_x_position = 20
        # Second row X position
        self.second_row_x_position = 150

        # Checkboxes for items to buy
        self.item_apple = QCheckBox("Apples", self)
        self.item_apple.move(self.first_row_x_position, self.y_position)
        self.item_bread = QCheckBox("Bread", self)
        self.item_bread.move(self.first_row_x_position, self.y_position + 1 * self.y_step)
        self.item_milk = QCheckBox("Milk", self)
        self.item_milk.move(self.first_row_x_position, self.y_position + 2 * self.y_step)

        # Radio buttons for alternative items (to buy only one of a list)
        self.rb_cake = QRadioButton("Cake", self)
        self.rb_cake.move(self.second_row_x_position, self.y_position)
        self.rb_icecream = QRadioButton("Ice cream", self)
        self.rb_icecream.move(self.second_row_x_position, self.y_position + 1 * self.y_step)
        self.rb_donuts = QRadioButton("Pack of donuts", self)
        self.rb_donuts.move(self.second_row_x_position, self.y_position + 2 * self.y_step)

        # NOTE: No radio buttons is checked by default; to check it do next:
        # self.rb_cake.setChecked(True)

        # Label for ComboBox
        self.store_label = QLabel("Buy at: ", self)
        self.store_label.move(self.first_row_x_position, self.y_position + 3 * self.y_step)

        # ComboBox for choosing alternative item (select only one of a category)
        self.store_combo = QComboBox(self)
        self.store_combo.move(self.store_label.x() + self.store_label.width(), self.y_position + 3 * self.y_step)
        self.store_combo.addItems(["Local store", "Supermarket", "23/7", "Order delivery"])
        self.store_combo.resize(160, 20)

        # Set the window title and size
        self.setWindowTitle("Shopping List App")
        self.setGeometry(300, 300, 280, 180)  # x, y, width, height


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShoppingListApp()
    window.show()
    sys.exit(app.exec())
