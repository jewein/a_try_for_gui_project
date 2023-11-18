import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QCompleter
from PySide6.QtCore import QStringListModel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.line_edit1 = QLineEdit()
        self.line_edit2 = QLineEdit()
        self.line_edit3 = QLineEdit()

        layout.addWidget(self.line_edit1)
        layout.addWidget(self.line_edit2)
        layout.addWidget(self.line_edit3)

        # 创建自动完成模型
        completer_model = QStringListModel()
        completer = QCompleter(completer_model)

        # 将自动完成设置给输入框
        self.line_edit1.setCompleter(completer)
        self.line_edit2.setCompleter(completer)
        self.line_edit3.setCompleter(completer)

        # 假设这是你的模糊查询结果
        fuzzy_search_results = ["Result1", "Result2", "Result3", "Result4"]

        # 将模糊查询结果添加到自动完成模型
        completer_model.setStringList(fuzzy_search_results)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
