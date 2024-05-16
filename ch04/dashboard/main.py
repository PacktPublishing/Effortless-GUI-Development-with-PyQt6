#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Ch04. 'Dashboard' example from the "Effortless GUI Development with PyQt6" book.
   
   Access the repository with all examples at:
   https://github.com/PacktPublishing/Effortless-GUI-Development-with-PyQt6
"""

import sys
from PyQt6.QtCore import QObject, pyqtSlot
from PyQt6.QtWidgets import QApplication
from PyQt6.QtQml import QQmlApplicationEngine


# Controller is the component that will be exposed to QML.
class Controller(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._lightsOn = True

    @pyqtSlot()
    def turnLightsOn(self):
        self._lightsOn = True
        print("py: self._lightsOn =", self._lightsOn)

    @pyqtSlot()
    def turnLightsOff(self):
        self._lightsOn = False
        print("py: self._lightsOn =", self._lightsOn)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Create an instance of the Controller
    controller = Controller(engine)

    # Expose the controller QML
    engine.rootContext().setContextProperty("controller", controller)

    # Load the main QML file
    engine.load('main.qml')

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
