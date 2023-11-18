import sys
import pyautogui
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PySide6.QtCore import QTimer, Qt

class DesktopEdgeHideWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口的基本属性
        self.setWindowTitle("Edge Hide Window")
        self.setGeometry(0, 0, 200, 200)  # 设置窗口大小
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 创建一个按钮，用于显示/隐藏窗口
        self.show_hide_button = QPushButton("Show/Hide")
        self.show_hide_button.clicked.connect(self.toggle_visibility)

        # 创建布局并添加按钮
        layout = QVBoxLayout()
        layout.addWidget(self.show_hide_button)
        self.setLayout(layout)

        # 创建一个定时器来检测鼠标位置
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_mouse_position)
        self.timer.start(100)  # 定时器每100毫秒检测一次鼠标位置

    def toggle_visibility(self):
        if self.isHidden():
            self.show()
        else:
            self.hide()

    def check_mouse_position(self):
        mouse_x, mouse_y = pyautogui.position()
        screen_width, screen_height = pyautogui.size()

        # 设置一个阈值，当鼠标接近屏幕边缘时触发显示/隐藏窗口
        threshold = 10

        if mouse_x <= threshold or mouse_x >= (screen_width - threshold) or \
           mouse_y <= threshold or mouse_y >= (screen_height - threshold):
            if self.isHidden():
                self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DesktopEdgeHideWindow()
    window.show()
    sys.exit(app.exec_())
