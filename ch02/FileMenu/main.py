#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Ch02. "FileMenu" example from the "Effortless GUI Development with PyQt6" book.
   
   Access the repository with all examples at:
   https://github.com/PacktPublishing/Effortless-GUI-Development-with-PyQt6
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStatusBar, QToolBar
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt

class FileMenuApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create "New Project" action with status tip and tooltip
        new_action = QAction(QIcon("images/add.png"), "&New Project...", self)
        new_action.setStatusTip("Opens Wizard to create a new project...")
        new_action.setToolTip("New Project")

        # Create "Lock File" action that is checkable
        lock_action = QAction(QIcon("images/lock.png"), "&Lock File", self)
        lock_action.setStatusTip("Makes current file read-only")
        lock_action.setCheckable(True)

        # Create "Save All" action that is disabled
        save_all_action = QAction(QIcon("images/save.png"), "&Save All", self)
        save_all_action.setStatusTip("Saves all files from the project")
        save_all_action.setEnabled(False)

        # Create "Quit" action
        exit_action = QAction(QIcon("images/quit.png"), "&Quit this beautiful app", self)
        exit_action.setStatusTip("Closes the application")

        # Get a menu bar that is the part of QMainWindow
        menu = self.menuBar()

        # Create menu item "File"
        file_menu = menu.addMenu("File")
        # Populate menu "File" with items
        file_menu.addAction(new_action)
        file_menu.addSeparator()
        # Add a submenu "Open Recent"
        recent_menu = file_menu.addMenu(QIcon("images/clock.png"), "Open Recent")
        file_menu.addSeparator()
        file_menu.addAction(lock_action)
        file_menu.addAction(exit_action)
        file_menu.addAction(save_all_action)
        file_menu.addSeparator()

        # Use the same icon for few menu times, load it once
        file_icon = QIcon("images/file.png")
        # Create and add action to "Open Recent" submenu
        recent_menu.addAction(QAction(file_icon, "LoginScreen", self))
        recent_menu.addAction(QAction(file_icon, "ShoppingList", self))
        recent_menu.addAction(QAction(file_icon, "BookFeedback", self))

        # Create a "Helper Toolbar" and add to it to QMainWindow
        toolbar = QToolBar("Helper Toolbar")
        self.addToolBar(toolbar)
        # Add some of existing actions to toolbar
        toolbar.addActions([new_action, lock_action, save_all_action])
        toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)

        self.setWindowTitle("File Menu App")
        self.setStatusBar(QStatusBar(self))
        self.setGeometry(200, 300, 300, 500)

        # Show "Ready!" message in status bar for 3 sec
        self.statusBar().showMessage("Ready!", 3000)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fileMenuApp = FileMenuApp()
    fileMenuApp.show()
    sys.exit(app.exec())
