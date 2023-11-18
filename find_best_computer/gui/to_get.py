import sys

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile

# # 创建应用程序对象
# app = QApplication(sys.argv)
#
# # 创建主窗口
# main_window = QMainWindow()
#
# # 使用QUiLoader加载UI文件
# loader = QUiLoader()
# ui_file = QFile("untitled.ui")
# ui_file.open(QFile.ReadOnly | QFile.Text)
# widget = loader.load(ui_file, main_window)
# ui_file.close()
#
# # 设置主窗口的中心部件
# main_window.setCentralWidget(widget)
#
# # 显示主窗口
# main_window.show()
#
# # 运行应用程序事件循环
# sys.exit(app.exec())

from untitled import Ui_MainWindow

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox.hide()
        self.ui.comboBox.addItem('item1')
        self.ui.comboBox.addItem('item2')
        self.ui.comboBox.addItem('item3')
        self.ui.comboBox.addItem('item4')
        self.ui.lineEdit.textChanged.connect(self.onSearchTextChanged)
        # self.ui.lineEdit.textChanged.connect(self.ui.comboBox.show)

    def onSearchTextChanged(self):
        self.ui.comboBox.show()
        self.ui.comboBox.showPopup()




        # self.ui.pushButton.clicked.connect(self.on_pushButton_clicked)

    def on_pushButton_clicked(self):
        print('按钮被点击')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())




