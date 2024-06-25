import sys
from OpenGL.GL import *
from PyOpenGL_accelerate import gl
import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtCore import Qt


class NoteTakingApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Note Taking App")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.note_title = QLineEdit()
        self.note_title.setPlaceholderText("Enter note title")
        layout.addWidget(self.note_title)

        self.note_core_text = QTextEdit()
        layout.addWidget(self.note_core_text)

        self.note_save = QPushButton("Save note")
        self.note_save.clicked.connect(self.save_note)
        layout.addWidget(self.note_save)

    def save_note(self):
        note_to_save = self.note_core_text.toPlainText()
        note_title = self.note_title.text()

        if note_title == "":
            note_title = "Untitled"

        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Text files (*.txt)")
        file_dialog.setDefaultSuffix("txt")
        file_dialog.setWindowTitle("Save note")
        file_dialog.selectFile(note_title)

        if file_dialog.exec_():
            file_name = file_dialog.selectedFiles()[0]

            with open(file_name, 'w') as note:
                note.write(note_to_save)

            self.note_title.clear()
            self.note_core_text.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = NoteTakingApp()
    window.show()

    sys.exit(app.exec_())
