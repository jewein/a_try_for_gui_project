import pandas as pd
from fuzzywuzzy import fuzz


class Searcher:
    def __init__(self, dataframe=None, by_names=None):
        self.dataframe = dataframe
        self.by_names = by_names

    def calculate_similarity(self, keyword, row):
        name_similarity = fuzz.ratio(keyword, row['cpuname'])  # 计算名称与关键词的相似度
        aliases = row['Other names:'].split(',')  # 获取别名列表
        alias_similarity = max(fuzz.ratio(keyword, alias) for alias in aliases) if aliases else 0  # 计算别名与关键词的相似度
        return max(name_similarity, alias_similarity)  # 返回名称与别名的最大相似度

    def search(self, keyword, top=0):
        self.dataframe['相似度'] = self.dataframe.apply(lambda row: self.calculate_similarity(keyword, row),
                                                        axis=1)  # 计算相似度
        sorted_dataframe = self.dataframe.sort_values(by='相似度', ascending=False)
        if top:
            return sorted_dataframe.head(top)
        else:
            return sorted_dataframe

    def set_dataframe(self, dataframe):
        self.dataframe = dataframe


if __name__ == '__main__':
    data = {
        '序号': [1, 2, 3],
        '名称': ['苹果', '香蕉', '橙子'],
        '别名': ['苹果,苹果红,红苹果', '香蕉,香蕉黄,黄香蕉', '橙子,橙色水果'],
        '其它数据': ['data1', 'data2', 'data3']
    }

    df = pd.DataFrame(data)

    cpu_data = pd.read_csv('../data/cpu_data.csv')

    # keyword = '橙色1111'

    keyword = 'i7-6600U'
    searcher = Searcher(cpu_data)
    result = searcher.search(keyword)[['cpuname', 'Other names:', '相似度']].values.tolist()

    for i in result:
        print(i)
