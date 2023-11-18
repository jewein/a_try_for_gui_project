import pandas as pd


class A:
    def __init__(self):
        self.program_dataframe=None
        try:
            self.program_dataframe = pd.read_csv('program.csv')
        except FileNotFoundError:
            self.program_dataframe = pd.DataFrame(
                columns=['cpu_No', 'gpu_No', 'single_thread', 'multi_thread', 'FLOPS', 'single_thread/price',
                         'multi_thread/price', 'FLOPS/price', 'price', 'store'])

        # 准备新的数据
        new_data = {'cpu_No': 'new_cpu', 'gpu_No': 'new_gpu', 'single_thread': 100, 'multi_thread': 200, 'FLOPS': 300,
                    'single_thread/price': 0.5, 'multi_thread/price': 0.8, 'FLOPS/price': 1.2, 'price': 150,
                    'store': 'new_store'}

        # 将新数据添加到DataFrame
        self.program_dataframe = pd.concat([self.program_dataframe, pd.DataFrame([new_data])], ignore_index=True)

        # 检查重复记录
        duplicates = self.program_dataframe[
            self.program_dataframe.duplicated(subset=['cpu_No', 'gpu_No'], keep='first')]

        # 如果有重复记录，可以更新它们或输出提醒
        if not duplicates.empty:
            for index, row in duplicates.iterrows():
                # 在这里执行更新操作或输出提醒消息
                print(f"重复记录：CPU {row['cpu_No']}, GPU {row['gpu_No']}")

    def __enter__(self):
        print("进入上下文管理器")

    def __exit__(self, exc_type, exc_value, traceback):
        print("退出上下文管理器")
        # 在这里执行清理操作
        # 保存到csv
        self.program_dataframe.to_csv('program.csv', index=False, header=True)


if __name__ == '__main__':
    with A():
        pass

