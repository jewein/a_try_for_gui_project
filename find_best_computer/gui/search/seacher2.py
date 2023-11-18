import pandas as pd
from fuzzywuzzy import fuzz


def custom_fuzzy_ratio(s1, s2):
    # 忽略大小写
    s1 = s1.lower()
    s2 = s2.lower()

    # 计算模糊匹配分数
    ratio = fuzz.ratio(s1, s2)

    # 如果完全匹配，给予更高的权重
    if s1 == s2:
        ratio += 10  # 增加权重，可以根据需要调整

    # 考虑序列的权重，例如，匹配上的序列长度越长，分数越高
    ratio += min(len(s1), len(s2))  # 可以根据需要进行调整

    return ratio


def search_and_rank(data_frame, keyword):
    scores = pd.Series(0, index=data_frame.index)

    for index, row in data_frame.iterrows():
        name = row['cpuname']
        aliases = row['Other names:'].split(',')
        # name = row['名称']
        # aliases = row['别名'].split(',')
        # max_score = 0

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
    sorted_df = data_frame.assign(Score=scores).sort_values(by='Score', ascending=False)

    return sorted_df

if __name__ == '__main__':
    df = pd.DataFrame(pd.read_csv('../data/cpu_data.csv'))

    keyword = "i7 6600"
    result = search_and_rank(df, keyword)[['cpuname', 'Other names:', 'Score']].values.tolist()
    print(result)
