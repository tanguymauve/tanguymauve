import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog, QShortcut, QToolBar, QTreeView, QFileSystemModel, QSplitter
from PyQt5.QtCore import Qt, pyqtSlot, QModelIndex, QMimeData
from PyQt5.QtGui import QKeySequence, QDrag, QDragEnterEvent, QDropEvent, QDragMoveEvent


class DraggableTextEdit(QTextEdit):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.drag_start_position = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons()
                & Qt.LeftButton) or self.drag_start_position is None:
            return
        if (event.pos() - self.drag_start_position
            ).manhattanLength() < QApplication.startDragDistance():
            return

        drag = QDrag(self)
        mime_data = QMimeData()
        mime_data.setText(self.toPlainText())
        drag.setMimeData(mime_data)

        pixmap = self.grab()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos() - self.rect().topLeft())

        drop_action = drag.exec_(Qt.CopyAction | Qt.MoveAction)


class FileExplorer(QTreeView):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDropIndicatorShown(True)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dragMoveEvent(self, event: QDragMoveEvent):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasText():
            note_text = event.mimeData().text()
            index = self.indexAt(event.pos())
            file_path = self.model().filePath(index)
            if file_path.endswith(".txt"):
                with open(file_path, 'w') as file:
                    file.write(note_text)
                event.acceptProposedAction()


class NoteTakingApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.init_ui()
        self.create_shortcut()

    def init_ui(self):
        self.setWindowTitle("Note Taking App")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.note_title = QLineEdit()
        self.note_title.setPlaceholderText("Enter note title")
        layout.addWidget(self.note_title)

        self.note_core_text = DraggableTextEdit(
        )  # Use DraggableTextEdit instead of QTextEdit
        self.note_core_text.textChanged.connect(
            self.enable_save_button
        )  # Connect textChanged signal to enable_save_button slot
        layout.addWidget(self.note_core_text)

        self.note_save = QPushButton("Save note")
        self.note_save.clicked.connect(self.save_note)
        self.note_save.setEnabled(False)
        layout.addWidget(self.note_save)

        # Create file explorer
        self.file_model = QFileSystemModel()
        initial_path = os.path.join(
            "C:\\", "Users", "20001404", "OneDrive - ACC", "Documents",
            "Stockage")  # Construct the file path using os.path.join()
        self.file_model.setRootPath(initial_path)
        self.file_view = FileExplorer()  # Use the custom FileExplorer class
        self.file_view.setModel(self.file_model)
        self.file_view.setRootIndex(self.file_model.index(initial_path))
        self.file_view.doubleClicked.connect(self.open_file)

        # Create navigation bar
        self.nav_bar = QToolBar()
        self.nav_bar.addAction("New Note", self.new_note)
        self.nav_bar.addAction("Save Note", self.save_note)

        # Create splitter to divide the window into file explorer and note taking area
        splitter = QSplitter()
        splitter.addWidget(self.file_view)
        splitter.addWidget(central_widget)

        self.setCentralWidget(splitter)
        self.addToolBar(self.nav_bar)

    def create_shortcut(self):
        new_note_shortcut = QShortcut(QKeySequence('Ctrl+N'), self)
        new_note_shortcut.activated.connect(self.new_note)

    @pyqtSlot()
    def new_note(self):
        # Clear the current note and title
        self.note_title.clear()
        self.note_core_text.clear()
        self.note_save.setEnabled(False)

    def save_note(self):
        note_to_save = self.note_core_text.toPlainText()
        note_title = self.note_title.text()

        if note_title == "":
            note_title = "Untitled"

        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Text files (*.txt)")
        file_dialog.setDefaultSuffix("txt")
        file_dialog.setWindowTitle("Save note")
        file_dialog.setDirectory(os.path.expanduser("~"))
        file_dialog.selectFile(note_title)

        if file_dialog.exec_():
            file_name = file_dialog.selectedFiles()[0]

            with open(file_name, 'w') as note:
                note.write(note_to_save)

            self.note_title.clear()
            self.note_core_text.clear()
            self.note_save.setEnabled(False)

    def open_file(self, index: QModelIndex):
        file_path = self.file_model.filePath(index)
        if file_path.endswith(".txt"):
            with open(file_path, 'r') as file:
                content = file.read()
                self.note_core_text.setPlainText(content)
                file_name = os.path.basename(file_path)
                note_title = os.path.splitext(file_name)[0]
                self.note_title.setText(note_title)
                self.note_save.setEnabled(
                    True)  # Enable the save button after opening a file

    def enable_save_button(self):
        self.note_save.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = NoteTakingApp()
    window.show()

    sys.exit(app.exec_())
