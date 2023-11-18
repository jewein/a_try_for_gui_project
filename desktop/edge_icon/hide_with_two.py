import sys
import ctypes
import win32con
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import QTimer, Qt

class DesktopEdgeHideWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口的基本属性
        self.setWindowTitle("Edge Hide Window")
        self.setGeometry(0, 0, 200, 200)  # 设置窗口大小
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 创建一个标签，用于显示微小的图标
        self.icon_label = QLabel("Icon")
        self.icon_label.setAlignment(Qt.AlignCenter)

        # 创建一个布局并添加标签
        layout = QVBoxLayout()
        layout.addWidget(self.icon_label)
        self.setLayout(layout)

        # 创建一个定时器来检测鼠标位置
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_mouse_position)
        self.timer.start(100)  # 定时器每100毫秒检测一次鼠标位置

        # 获取当前窗口句柄
        self.hwnd = ctypes.windll.user32.GetForegroundWindow()
        self.icon_hidden = True

    def check_mouse_position(self):
        rect = ctypes.wintypes.RECT()
        ctypes.windll.user32.GetWindowRect(self.hwnd, ctypes.byref(rect))
        screen_width, screen_height = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
        threshold = 10

        if (rect.left <= threshold and rect.top > threshold and rect.bottom < screen_height - threshold):
            # 鼠标靠左边缘，隐藏窗口
            self.move(rect.left - self.width() + threshold, rect.top - self.height() / 2)
            self.icon_label.show()
            ctypes.windll.user32.ShowWindow(self.hwnd, win32con.SW_HIDE)
            self.icon_hidden = True
        elif (rect.right >= screen_width - threshold and rect.top > threshold and rect.bottom < screen_height - threshold):
            # 鼠标靠右边缘，隐藏窗口
            self.move(rect.right - threshold, rect.top - self.height() / 2)
            self.icon_label.show()
            ctypes.windll.user32.ShowWindow(self.hwnd, win32con.SW_HIDE)
            self.icon_hidden = True
        elif (rect.top <= threshold and rect.left > threshold and rect.right < screen_width - threshold):
            # 鼠标靠上边缘，隐藏窗口
            self.move(rect.left - self.width() / 2, rect.top - self.height() + threshold)
            self.icon_label.show()
            ctypes.windll.user32.ShowWindow(self.hwnd, win32con.SW_HIDE)
            self.icon_hidden = True
        else:
            # 鼠标不在边缘附近，显示微小的图标并显示窗口
            self.icon_label.hide()
            if self.icon_hidden:
                ctypes.windll.user32.ShowWindow(self.hwnd, win32con.SW_SHOW)
                self.icon_hidden = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DesktopEdgeHideWindow()
    window.show()
    sys.exit(app.exec_())
