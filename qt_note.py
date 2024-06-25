import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog, QShortcut, QToolBar, QTreeView, QFileSystemModel, QSplitter, QHBoxLayout
from PyQt5.QtCore import Qt, pyqtSlot, QModelIndex, QMimeData
from PyQt5.QtGui import QKeySequence, QDrag, QDragEnterEvent, QDropEvent, QDragMoveEvent, QIcon
import markdown


class MarkdownEditor(QTextEdit):

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

        note_icon = QIcon("icon/music-note.jpg")
        drag.setPixmap(note_icon.pixmap(32, 32))
        drag.setHotSpot(event.pos() - self.rect().topLeft())

        drop_action = drag.exec_(Qt.CopyAction | Qt.MoveAction)


class MarkdownPreview(QTextEdit):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)

    def update_preview(self, markdown_text):
        html = markdown.markdown(markdown_text)
        self.setHtml(html)


class FileExplorer(QTreeView):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDropIndicatorShown(True)

        self.file_model = QFileSystemModel(
        )  # Create an instance of QFileSystemModel
        self.setModel(
            self.file_model)  # Set the model for the FileExplorer instance

        self.setColumnWidth(0, 150)

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
            if self.model().isDir(index):
                file_path = self.model().filePath(index)
            else:
                file_path = os.path.dirname(self.model().filePath(index))
            note_title = self.window().note_title.text()
            if not note_title:
                note_title = "Nommez votre note!"
            file_path = os.path.join(file_path, note_title + ".txt")
            with open(file_path, 'w') as file:
                file.write(note_text)
            self.window().note_title.setText(note_title)
            self.window().note_save.setEnabled(True)
            event.acceptProposedAction()

    def adjust_column_width(self, topLeft, bottomRight, roles):
        if topLeft.column(
        ) == 0:  # Check if the changed column is the "Name" column (index 0)
            self.resizeColumnToContents(0)


class NoteTakingApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.saved_file_path = None
        self.init_ui()
        self.create_shortcut()

    def init_ui(self):
        self.setWindowTitle("Note Taking App with Live Markdown Preview")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        self.note_title = QLineEdit()
        self.note_title.setPlaceholderText("Enter note title")
        main_layout.addWidget(self.note_title)

        editor_preview_layout = QHBoxLayout()

        self.markdown_editor = MarkdownEditor()
        self.markdown_editor.textChanged.connect(self.update_preview)
        editor_preview_layout.addWidget(self.markdown_editor)

        self.markdown_preview = MarkdownPreview()
        editor_preview_layout.addWidget(self.markdown_preview)

        main_layout.addLayout(editor_preview_layout)

        self.note_save = QPushButton("Save note")
        self.note_save.clicked.connect(self.save_note)
        self.note_save.setEnabled(False)
        main_layout.addWidget(self.note_save)

        # Create file explorer
        self.file_model = QFileSystemModel()
        initial_path = os.path.join("C:\\", "Users", "20001404",
                                    "OneDrive - ACC", "Documents", "Stockage")
        self.file_model.setRootPath(initial_path)
        self.file_view = FileExplorer()
        self.file_view.setModel(self.file_model)
        self.file_view.setRootIndex(self.file_model.index(initial_path))
        self.file_view.doubleClicked.connect(self.open_file)

        self.nav_bar = QToolBar()
        new_note_action = self.nav_bar.addAction("New Note")
        new_note_action.triggered.connect(self.new_note)
        new_note_action.setToolTip("New Note (Ctrl + N)")

        save_note_action = self.nav_bar.addAction("Save Note")
        save_note_action.triggered.connect(self.save_note)
        save_note_action.setToolTip("Save Note (Ctrl + S)")

        # Create splitter to divide the window into file explorer and note taking area
        splitter = QSplitter()
        splitter.addWidget(self.file_view)
        splitter.addWidget(central_widget)

        self.setCentralWidget(splitter)
        self.addToolBar(self.nav_bar)

    def create_shortcut(self):
        new_note_shortcut = QShortcut(QKeySequence('Ctrl+N'), self)
        new_note_shortcut.activated.connect(self.new_note)

        save_note_shortcut = QShortcut(QKeySequence('Ctrl+S'), self)
        save_note_shortcut.activated.connect(self.save_note)

    @pyqtSlot()
    def new_note(self):
        self.note_title.clear()
        self.markdown_editor.clear()
        self.markdown_preview.clear()
        self.note_save.setEnabled(False)

    def save_note(self):
        note_to_save = self.markdown_editor.toPlainText()
        note_title = self.note_title.text()

        if note_title == "":
            note_title = "Untitled"

        if self.saved_file_path is None:
            file_dialog = QFileDialog(self)
            file_dialog.setNameFilter("Markdown files (*.md)")
            file_dialog.setDefaultSuffix("md")
            file_dialog.setWindowTitle("Save note")
            file_dialog.setDirectory(os.path.expanduser("~"))
            file_dialog.selectFile(note_title)

            if file_dialog.exec_():
                self.saved_file_path = file_dialog.selectedFiles()[0]

        if self.saved_file_path:
            with open(self.saved_file_path, 'w') as note:
                note.write(note_to_save)

            self.note_save.setEnabled(False)

    def open_file(self, index: QModelIndex):
        file_path = self.file_model.filePath(index)
        if file_path.endswith(".md"):
            with open(file_path, 'r') as file:
                content = file.read()
                self.markdown_editor.setPlainText(content)
                file_name = os.path.basename(file_path)
                note_title = os.path.splitext(file_name)[0]
                self.note_title.setText(note_title)
                self.note_save.setEnabled(True)

    def update_preview(self):
        markdown_text = self.markdown_editor.toPlainText()
        self.markdown_preview.update_preview(markdown_text)
        self.note_save.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = NoteTakingApp()
    window.show()

    sys.exit(app.exec_())
