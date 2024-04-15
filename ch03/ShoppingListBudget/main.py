#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Ch03. 'Shopping List Budget' example from the "Effortless GUI Development with PyQt6" book.
   
   Access the repository with all examples at:
   https://github.com/PacktPublishing/Effortless-GUI-Development-with-PyQt6
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QRadioButton, QComboBox, QWidget
from PyQt6.QtWidgets import QGridLayout, QStatusBar, QMessageBox
from PyQt6.QtCore import Qt, pyqtSignal

total_budget = 10  # Starting budget
current_spent = 0  # Amount already spent


class RemainingBudgetLabel(QLabel):
    default_style = "QLabel { font: bold }"
    highlighted_style = "QLabel { background-color: red; font: bold }"
    
    def __init__(self, budget, parent=None):
        super().__init__(parent)
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.setStyleSheet(self.default_style)
        self.setBudgetAmount(budget)

    def setHighlighted(self, needHighlight):
        if needHighlight:
            self.setStyleSheet(self.highlighted_style)
        else:
            self.setStyleSheet(self.default_style)

    def setBudgetAmount(self, newBudgetAmount):
        self.budget = newBudgetAmount
        self.setText(f"${self.budget}")
        self.setHighlighted(self.budget < 0)


class CustomCheckBox(QCheckBox):
    # Define a signal that will be fired when an item becomes checked, the argument is text
    item_checked = pyqtSignal(str, int, bool)

    def __init__(self, label, price, parent=None):
        super().__init__(f"{label} - ${price}", parent)
        self.price = price
        self.itemName = label
        self.stateChanged.connect(self.emit_checked_state)

    def emit_checked_state(self, state):
        checked = Qt.CheckState(state) == Qt.CheckState.Checked
        
        if checked:
            self.setStyleSheet("QCheckBox { text-decoration: line-through; }")
        else:
            self.setStyleSheet("")

        self.item_checked.emit(self.itemName, self.price, checked)


class ShoppingListApp(QMainWindow):
    budget_changed = pyqtSignal(int)    

    def __init__(self):
        super().__init__()

        central_widget = QWidget(self)  # Central widget to hold the layout
        self.setCentralWidget(central_widget)

        self.setStatusBar(QStatusBar(self))
        self.statusBar().showMessage("Ready for shopping!", 3000)

        # Apply QGridLayout
        layout = QGridLayout(central_widget)  # Main layout for the central widget

        items = [("Apples", 3), ("Bread", 4), ("Milk", 5)]
        for item, price in items:
            checkbox = CustomCheckBox(item, price)
            checkbox.item_checked.connect(self.update_budget)
            layout.addWidget(checkbox)

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

        self.label = QLabel("<b>Remaining budget:</b>", self)
        layout.addWidget(self.label, 4, 0)        

        self.budget_label = RemainingBudgetLabel(total_budget, self)
        layout.addWidget(self.budget_label, 4, 1)

        self.budget_changed.connect(self.update_budget_labels)

        # Set the window title and size
        self.setWindowTitle("Shopping List App")
        self.setGeometry(300, 300, 280, 180)  # x, y, width, height

    def update_budget(self, item, price, checked):
        global current_spent, total_budget
        last_budget = total_budget - current_spent
        if checked:
            current_spent += price
        else:
            current_spent -= price

        remaining_budget = total_budget - current_spent

        self.budget_changed.emit(remaining_budget)
        
        if remaining_budget < 0:
            msg = f"Sorry, you can't buy {item} for ${price}, bacause you have ${last_budget}."
            print(msg)
            QMessageBox.critical(self, "No more money left", msg)

    def update_budget_labels(self, budget):
        self.statusBar().showMessage(f"Remaining Budget: ${budget}", 0)
        self.budget_label.setBudgetAmount(budget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShoppingListApp()
    window.show()
    sys.exit(app.exec())
