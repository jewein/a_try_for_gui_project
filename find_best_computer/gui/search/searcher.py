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

    def search(self,keyword, top=0):
        # 创建一个空的Series来存储相关性得分
        scores = pd.Series(0, index=self.dataframe.index)

        # 将关键词转换为小写以进行不区分大小写的匹配
        keyword = keyword.lower()

        for index, row in self.dataframe.iterrows():
            name = row['cpuname']
            aliases = row['Other names:'].split(',')

            # 使用fuzzywuzzy的partial_ratio来计算部分匹配得分
            name_score = fuzz.partial_ratio(keyword, name)
            alias_scores = [fuzz.partial_ratio(keyword, alias) for alias in aliases]

            # 如果关键词完全匹配名称或别名，增加额外的权重
            if keyword == name:
                name_score += 10  # 增加10分
            for i in range(len(alias_scores)):
                if keyword == aliases[i]:
                    alias_scores[i] += 10  # 增加10分

            max_alias_score = max(alias_scores) if alias_scores else 0
            total_score = max(name_score, max_alias_score)
            scores[index] = total_score

        # 根据相关性得分进行排序
        sorted_dataframe = self.dataframe.assign(Score=scores).sort_values(by='Score', ascending=False)

        # return sorted_dataframe

        if top:
            return sorted_dataframe.head(top)
        else:
            return sorted_dataframe

    def set_dataframe(self, dataframe):
        self.dataframe = dataframe


if __name__ == '__main__':

    # df = pd.DataFrame(data)

    cpu_data = pd.read_csv('../data/cpu_data.csv')

    # keyword = '橙色1111'

    keyword = 'i76600u'
    searcher = Searcher(cpu_data)
    result = searcher.search(keyword)[['cpuname', 'Other names:', 'Score']].values.tolist()

    for i in result:
        print(i)
