import pandas as pd
from fuzzywuzzy import fuzz


def search_and_rank(data_frame, keyword):
    # 创建一个空的Series来存储相关性得分
    scores = pd.Series(0, index=data_frame.index)

    # 进行模糊查询并计算相关性
    for index, row in data_frame.iterrows():
        name = row['名称']
        aliases = row['别名'].split(',')
        # 计算名称和别名与关键词的相关性得分
        name_score = fuzz.ratio(keyword, name)
        alias_scores = [fuzz.ratio(keyword, alias.strip()) for alias in aliases]
        max_alias_score = max(alias_scores) if alias_scores else 0
        total_score = max(name_score, max_alias_score)
        scores[index] = total_score

    # 根据相关性得分进行排序
    sorted_df = data_frame.assign(Score=scores).sort_values(by='Score', ascending=False)

    return sorted_df








