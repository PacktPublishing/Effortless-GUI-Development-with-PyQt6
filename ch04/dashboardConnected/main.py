#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Ch04. 'Dashboard Connected' example from the "Effortless GUI Development with PyQt6" book.
   
   Access the repository with all examples at:
   https://github.com/PacktPublishing/Effortless-GUI-Development-with-PyQt6
"""

import sys
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot, pyqtProperty
from PyQt6.QtWidgets import QApplication
from PyQt6.QtQml import QQmlApplicationEngine


# MediaController is dedicated to control the media playback
class MediaController(QObject):
    songChanged = pyqtSignal(str)
    playStateChanged = pyqtSignal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)

        self._playlist = [
            "Pink Floyd -- Echoes",
            "Paralytics on the Crossroads -- Dive",
            "Amon Tobin -- At the End of the Day",
            "Dreadnought In The Pond -- Like Butterflies",
            "The Doors -- The Soft Parade"
        ]
        self._playlistIndex = 0
        self._isPlaying = False
        self._currentSong = self._playlist[self._playlistIndex]

    @pyqtProperty(bool, notify=playStateChanged)
    def isPlaying(self):
        return self._isPlaying

    @isPlaying.setter
    def isPlaying(self, value):
        if self._isPlaying != value:
            self._isPlaying = value
            self.playStateChanged.emit(value)

    @pyqtSlot()
    def play(self):
        self.isPlaying = True

    @pyqtSlot()
    def pause(self):
        self.isPlaying = False

    @pyqtProperty(str, notify=songChanged)
    def currentSong(self):
        return self._currentSong

    @currentSong.setter
    def currentSong(self, value):
        if self._currentSong != value:
            self._currentSong = value
            self.songChanged.emit(value)

    # Slot/method to play the next song and cycle thru the playlist
    @pyqtSlot()
    def nextSong(self):
        self._playlistIndex = (self._playlistIndex + 1) % len(self._playlist)
        self.currentSong = self._playlist[self._playlistIndex]


# SmartHomeController is dedicated to control the Smart Home features (light, temperature)
class SmartHomeController(QObject):

    lightsOnChanged = pyqtSignal(bool)
    temperatureChanged = pyqtSignal(float)
    temperatureColorChanged = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self._lightsOn = True
        self._temperature = 22
        self._temperatureColor = "#ffffff"
        self.update_color()

    @pyqtProperty(bool, notify=lightsOnChanged)
    def lightsOn(self):
        return self._lightsOn

    @lightsOn.setter
    def lightsOn(self, value):
        if self._lightsOn != value:
            self._lightsOn = value
            self.lightsOnChanged.emit(value)

    @pyqtSlot()
    def toggleLights(self):
        print("py: _lightsOn was: ", self._lightsOn)
        self.lightsOn = not self.lightsOn
        print("py: _lightsOn become: ", self._lightsOn)

    @pyqtProperty(float, notify=temperatureChanged)
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if self._temperature != value:
            self._temperature = value
            self.temperatureChanged.emit(value)
            self.update_color()

    @pyqtProperty(str, notify=temperatureColorChanged)
    def temperatureColor(self):
        return self._temperatureColor

    @temperatureColor.setter
    def temperatureColor(self, value):
        if self._temperatureColor != value:
            self._temperatureColor = value
            self.temperatureColorChanged.emit(value)

    def calculate_color(self, temp):
        # Assuming the temperature range is from 15 to 30 degrees
        # Map the temperature to a color range from blue (0x0000FF) to red (0xFF0000)
        # Decrease blue component in color as temperature increases
        blue = max(0, 255 - ((temp - 15) * 17))
        # Increase red component in color as temperature increases
        red = min(255, (temp - 15) * 17)
        return f"#{int(red):02x}{0:02x}{int(blue):02x}"

    def update_color(self):
        self.temperatureColor = self.calculate_color(self.temperature)
        print("py: Updating color to ", self.temperatureColor)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Create an instance of the MediaController
    media_controller = MediaController(engine)

    # Create an instance of the SmartHomeController
    smart_home_controller = SmartHomeController(engine)

    # Expose the media controller and Smart Home controller to QML
    engine.rootContext().setContextProperty("mediaController", media_controller)
    engine.rootContext().setContextProperty("smartHomeController", smart_home_controller)

    # Load the QML file
    engine.load('main.qml')

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
