import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import QTimer, Qt, QRect, QPoint

class DesktopEdgeHideWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口的基本属性
        self.setWindowTitle("Edge Hide Window")
        self.setGeometry(0, 0, 200, 200)  # 设置窗口大小
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 创建一个标签，用于显示微小的图标
        self.icon_label = QLabel("Icon", self)
        self.icon_label.setGeometry(QRect(0, 0, 20, 20))
        self.icon_label.setAlignment(Qt.AlignCenter)

        # 创建一个定时器来检测鼠标位置
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_mouse_position)
        self.timer.start(100)  # 定时器每100毫秒检测一次鼠标位置

        # 初始化窗口的拖动变量
        self.dragging = False
        self.offset = None

    def check_mouse_position(self):
        mouse_x, mouse_y = self.mapFromGlobal(QPoint(QApplication.desktop().cursor().pos()))
        screen_width, screen_height = QApplication.desktop().width(), QApplication.desktop().height()
        window_width, window_height = self.width(), self.height()
        threshold = 10

        if (mouse_x <= threshold and mouse_y > threshold and
            mouse_y < screen_height - threshold):
            # 鼠标靠左边缘，隐藏窗口
            self.move(QPoint(-window_width + threshold, mouse_y - window_height / 2))
            self.icon_label.show()
            self.show()
        elif (mouse_x >= screen_width - threshold and mouse_y > threshold and
              mouse_y < screen_height - threshold):
            # 鼠标靠右边缘，隐藏窗口
            self.move(QPoint(screen_width - threshold, mouse_y - window_height / 2))
            self.icon_label.show()
            self.show()
        elif (mouse_y <= threshold and mouse_x > threshold and
              mouse_x < screen_width - threshold):
            # 鼠标靠上边缘，隐藏窗口
            self.move(QPoint(mouse_x - window_width / 2, -window_height + threshold))
            self.icon_label.show()
            self.show()
        else:
            # 鼠标不在边缘附近，显示微小的图标并隐藏窗口
            self.icon_label.hide()
            self.hide()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False
            self.offset = None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DesktopEdgeHideWindow()
    window.show()
    sys.exit(app.exec_())
