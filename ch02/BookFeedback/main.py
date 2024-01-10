#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Ch02. 'Book Feedback' example from the "Effortless GUI Development with PyQt6" book.
   
   Access the repository with all examples at:
   https://github.com/PacktPublishing/Effortless-GUI-Development-with-PyQt6
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QSlider, QProgressBar, QSpinBox, QPushButton
from PyQt6.QtCore import Qt, QPoint

class BookFeedbackPage(QMainWindow):

    y_step = 30
    y_position = 20
    x_position = 20

    # Helper method for easier positioning of components
    def position(self, num):
        return QPoint(self.x_position, self.y_position + num * self.y_step)

    def __init__(self):
        super().__init__()

        # label and Progress bar to show the completion of the questionnaire
        self.progress_label = QLabel("**Questionnaire Progress**",  self)
        self.progress_label.move(self.position(0))
        self.progress_label.resize(200, 20)
        self.progress_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progress_label.setTextFormat(Qt.TextFormat.MarkdownText)

        self.questionnaire_progress = QProgressBar(self)
        self.questionnaire_progress.move(self.position(1))
        self.questionnaire_progress.resize(160, 20)
        self.questionnaire_progress.setMinimum(1)
        self.questionnaire_progress.setMaximum(100)
        self.questionnaire_progress.setValue(20)  # Assuming 20% of the questionnaire is completed

        # Label for the question
        self.question_label = QLabel("How do you like this book? Rating (0 to 10):", self)
        self.question_label.move(self.position(2))
        self.question_label.resize(200, 40)
        self.question_label.setWordWrap(True)

        self.book_rating_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.book_rating_slider.move(self.position(4))
        self.book_rating_slider.resize(160, 20)
        self.book_rating_slider.setMinimum(0)
        self.book_rating_slider.setMaximum(10)

        # Spin box for additional feedback
        self.chapters_label = QLabel("Chapter you like the most:", self)
        self.chapters_label.move(self.position(5))
        self.chapters_label.resize(200, 20)

        self.chapters_spinbox = QSpinBox(self)
        self.chapters_spinbox.move(self.position(6))
        self.chapters_spinbox.resize(140, 20)
        self.chapters_spinbox.setSpecialValueText("Scroll to choose")
        self.chapters_spinbox.setPrefix("Ch. ")
        self.chapters_spinbox.setMinimum(0)
        self.chapters_spinbox.setMaximum(11)  # Assuming the book has 11 chapters

        # Submit button for the feedback
        self.submit_button = QPushButton("Submit Feedback", self)
        self.submit_button.move(self.position(7))
        self.submit_button.resize(140, 30)

        # Set the window title and size
        self.setWindowTitle("PyQt6 Cookbook Feedback Questionnaire")
        self.setGeometry(300, 300, 220, 270)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BookFeedbackPage()
    window.show()
    sys.exit(app.exec())
