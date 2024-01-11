#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Ch02. "BookFeedback-layouts" example from the "Effortless GUI Development with PyQt6" book.
   
   Access the repository with all examples at:
   https://github.com/PacktPublishing/Effortless-GUI-Development-with-PyQt6
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QSlider, QProgressBar, QSpinBox, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

class BookFeedbackPageLayouts(QMainWindow):
    def __init__(self):
        super().__init__()

        self.progress_label = QLabel("**Questionnaire Progress**", self)
        self.progress_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progress_label.setTextFormat(Qt.TextFormat.MarkdownText)

        self.questionnaire_progress = QProgressBar(self)
        self.questionnaire_progress.setMinimum(1)
        self.questionnaire_progress.setMaximum(100)
        self.questionnaire_progress.setValue(20) 

        self.question_label = QLabel("How do you like this book? Rating (0 to 10):", self)
        self.question_label.setWordWrap(True)

        self.book_rating_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.book_rating_slider.setMinimum(0)
        self.book_rating_slider.setMaximum(10)

        self.chapters_label = QLabel("Chapter you like the most:", self)

        self.chapters_spinbox = QSpinBox(self)
        self.chapters_spinbox.setSpecialValueText("Scroll to choose")
        self.chapters_spinbox.setPrefix("Ch. ")
        self.chapters_spinbox.setMinimum(0)
        self.chapters_spinbox.setMaximum(11)  # Assuming the book has 11 chapters

        self.submit_button = QPushButton("Submit Feedback", self)


        # New code goes here:
        central_widget = QWidget(self)  # Central widget to hold the layout
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)  # Main layout for the central widget

        # Add all widgets into the layout one by one
        layout.addWidget(self.progress_label)
        layout.addWidget(self.questionnaire_progress)
        layout.addWidget(self.question_label)
        layout.addWidget(self.book_rating_slider)
        layout.addWidget(self.chapters_label)
        layout.addWidget(self.chapters_spinbox)
        layout.addWidget(self.submit_button)

        self.setWindowTitle("PyQt6 Cookbook Feedback Questionnaire with Layouts")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BookFeedbackPageLayouts()
    window.show()
    sys.exit(app.exec())
