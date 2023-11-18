import sys
from datetime import datetime
import shutil

import pandas as pd
from PySide6.QtCore import QTimer
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow

# 指定列的数据类型字典
data_types = {
    'cpu_No': int,
    'gpu_No': int,
    'single_thread': float,
    'multi_thread': float,
    'FLOPS': float,
    'single_thread/price': float,
    'multi_thread/price': float,
    'FLOPS/price': float,
    'price': float,
    'store': str,
    'cpuname': str,
}


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cpu_No = 0
        self.gpu_No = 0
        self.single_thread = 0
        self.multi_thread = 0
        self.FLOPS = 0
        self.single_thread_price = 0
        self.multi_thread_price = 0
        self.FLOPS_price = 0
        self.price = 0
        self.store = '"unknown"'
        self.full_data = {}
        self.existing_record = None
        self.program_dataframe = None
        self.cpu_index = 0
        self.cpuname = ''

        print('初始化1')
        try:
            print('初始化2')
            self.program_dataframe = pd.read_csv('program.csv', dtype=data_types, encoding='utf-8')  # 读取csv文件
            self.program_dataframe = self.program_dataframe.astype(data_types)  # 指定列的数据类型
            self.program_dataframe['store'] = self.program_dataframe['store'].astype(str)

            print(self.program_dataframe.dtypes)  # 打印数据类型
        # except FileNotFoundError:
        except Exception as e:  # 如果文件不存在，创建一个空的DataFrame
            print(e)
            self.program_dataframe = pd.DataFrame(
                columns=('cpu_No', 'gpu_No', 'single_thread', 'multi_thread', 'FLOPS', 'single_thread/price',
                         'multi_thread/price', 'FLOPS/price', 'price', 'store', 'cpuname'))

        self.cpu_list = []
        self.ui = QUiLoader().load('untitled.ui')  # 加载ui文件
        self.ui.comboBox1.hide()
        self.ui.comboBox2.hide()

        # 创建定时器
        self.cpu_timer = QTimer()
        self.cpu_timer.setSingleShot(True)  # 设置为单次触发
        self.cpu_timer.timeout.connect(self.onCpuTextChanged)  # 绑定信号与槽函数

        # self.gpu_timer = QTimer()
        # self.gpu_timer.setSingleShot(True)
        # self.gpu_timer.timeout.connect(self.onGpuTextChanged)

        self.price_timer = QTimer()  # 创建定时器
        self.price_timer.setSingleShot(True)  # 设置为单次触发
        self.price_timer.timeout.connect(self.onPriceChanged)  # 绑定信号与槽函数

        self.cpu_data = pd.read_csv('data/cpu_data.csv')  # 读取csv文件
        # print(self.cpu_data)
        from search.searcher import Searcher  # 导入Searcher类
        self.searcher = Searcher(self.cpu_data)  # 创建Searcher对象

        self.ui.lineEdit1.textChanged.connect(self.onCpuTextChangedTimer)
        self.ui.comboBox1.activated.connect(self.onComboBox1Activated)
        self.ui.lineEdit.textChanged.connect(self.onPriceChangedTimer)
        self.ui.pushButton.clicked.connect(self.on_pushButton_clicked)

    def onComboBox1Activated(self):
        self.update()

    def onCpuTextChangedTimer(self):
        self.cpu_timer.start(1000)

    def onCpuTextChanged(self):
        if self.ui.lineEdit1.text() == '':
            self.ui.comboBox1.hide()
        else:
            self.ui.comboBox1.clear()
            print(self.ui.lineEdit1.text())
            # data=self.searcher.search(self.ui.lineEdit1.text())['cpuname','Other names:']
            data = self.searcher.search(self.ui.lineEdit1.text(), top=10)
            # sys.stdout.flush()
            self.cpu_list = data[['No.', 'cpuname', 'Other names:', 'Score']].values.tolist()
            # print(data_list)
            # 加入到下拉框中
            for i in self.cpu_list:
                self.ui.comboBox1.addItem(i[1] + '(' + i[2] + ')')

            self.ui.comboBox1.show()
            self.ui.comboBox1.showPopup()

        # self.ui.pushButton.clicked.connect(self.on_pushButton_clicked)

    def onGpuTextChangedTimer(self):
        pass

    def onPriceChangedTimer(self):
        self.price_timer.start(1000)

    def onGpuTextChanged(self):
        pass

    def onPriceChanged(self):
        self.update()

    def save(self):
        self.full_data = {'cpu_No': self.cpu_No,
                          'gpu_No': self.gpu_No,
                          'single_thread': self.single_thread,
                          'multi_thread': self.multi_thread,
                          'FLOPS': self.FLOPS,
                          'single_thread/price': self.single_thread_price,
                          'multi_thread/price': self.multi_thread_price,
                          'FLOPS/price': self.FLOPS_price,
                          'price': self.price,
                          'store': str(self.store),
                          'cpuname': str(self.cpuname),
                          }

        # 检查新数据是否已存在于DataFrame中
        # print('self.cpu_No, self.gpu_No:', self.cpu_No, self.gpu_No)
        # print(self.program_dataframe['cpu_No'])
        # print(self.program_dataframe['gpu_No'])
        # print(self.program_dataframe)
        print(self.program_dataframe.dtypes)
        self.existing_record = self.program_dataframe[
            (self.program_dataframe['cpu_No'] == int(self.cpu_No)) &
            (self.program_dataframe['gpu_No'] == int(self.gpu_No))
            ]

        print('self.existing_record:', self.existing_record)
        # 如果新数据不是重复的，将其添加到DataFrame中
        if self.existing_record.empty:  #
            new_data = pd.DataFrame([self.full_data])
            # print(new_data)
            self.program_dataframe = pd.concat([self.program_dataframe, new_data], ignore_index=True)
        else:
            for index, row in self.existing_record.iterrows():
                # 在这里执行更新操作或输出提醒消息
                print(f"重复记录：CPU {row['cpu_No']}, GPU {row['gpu_No']}")
                self.program_dataframe.loc[index] = self.full_data
            # self.program_dataframe.loc[self.existing_record.index] = self.full_data
            print("新数据是重复的， 更新了它")
        # 检查新数据是否已存在于DataFrame中

        # 删除重复记录，保留最新的记录
        # self.program_dataframe = self.program_dataframe.drop_duplicates(subset=['cpu_No', 'gpu_No'], keep='last')
        self.program_dataframe.to_csv('program.csv', index=False)
        # 复制program.csv到另外一个位置，并且加上日期时间后缀。
        # copy

        shutil.copyfile('program.csv', 'program' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.csv')

        # 删除重复记录，保留最新的记录
        # self.program_dataframe.drop_duplicates(subset=['cpu_No', 'gpu_No'], keep='last').to_excel('program.csv', index=False)

    def update(self):
        self.cpu_index = self.ui.comboBox1.currentIndex()  # 获取当前选中的索引
        if self.cpu_index >= 0:  # 如果索引大于等于0，说明有选中的项
            self.cpuname = self.cpu_list[self.cpu_index][1]
            self.ui.lineEdit1.setText(self.cpuname)  # 设置文本框的内容
            self.ui.comboBox1.hide()  # 隐藏下拉框
            self.cpu_No = int(self.cpu_list[self.cpu_index][0])  # 获取选中的CPU编号
            data = self.cpu_data[self.cpu_data['No.'] == self.cpu_list[self.cpu_index][0]]  # 获取选中的CPU数据
            # clear
            self.ui.textEdit.clear()
            for key, value in data.items():
                self.ui.textEdit.append(key + ':' + str(value.values))
            self.cpu_timer.stop()
            # 更新下方所有数值
            self.single_thread = data['single_thread'].values[0]
            self.multi_thread = data['multi_thread'].values[0]
            self.FLOPS = data['FLOPS'].values[0]
            self.ui.information11.setText(str(self.single_thread) + 'MOps/Sec')
            self.ui.information21.setText(str(self.multi_thread) + 'Mmat/Sec')
            self.ui.information31.setText(str(self.FLOPS) + 'MFLOPS')
            self.gpu_No = int(self.ui.lineEdit2.text())
        if self.ui.lineEdit.text() == '':
            pass
        else:
            self.price = float(self.ui.lineEdit.text())
            self.single_thread_price = self.single_thread / self.price
            self.ui.information12.setText(str(self.single_thread_price) + 'MOps/￥')
            self.multi_thread_price = self.multi_thread / self.price
            self.ui.information22.setText(str(self.multi_thread_price) + 'Mmats/￥')
            self.FLOPS_price = self.FLOPS / self.price
            self.ui.information32.setText(str(self.FLOPS_price) + 'MFLOPS/￥')

    def on_pushButton_clicked(self):
        self.store = str(self.ui.lineEdit_store.text())
        # self.update()
        self.save()
        print('保存成功')


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    app = QApplication([])
    window = Window()
    window.ui.show()
    sys.exit(app.exec())
