import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QCompleter
from PySide6.QtCore import Qt

class SearchBox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("搜索框示例")
        self.setGeometry(100, 100, 400, 200)

        # 创建搜索框
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("搜索...")

        # 创建自动完成器
        self.completer = QCompleter(["建议1", "建议2", "建议3"])
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)  # 不区分大小写
        self.search_input.setCompleter(self.completer)

        # 创建布局
        layout = QVBoxLayout()
        layout.addWidget(self.search_input)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SearchBox()
    window.show()
    sys.exit(app.exec())
