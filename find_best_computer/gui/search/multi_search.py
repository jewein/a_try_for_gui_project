import pandas as pd
import concurrent.futures

# 示例数据框
data = {
    '序号': [1, 2, 3, 4, 5, 6],
    '名称': ['苹果', '香蕉', '橙子', '梨', '草莓', '柚子'],
    '别名': ['苹果,苹果红,红苹果', '香蕉,香蕉黄,黄香蕉', '橙子,橙色水果', '梨,黄梨', '草莓,红草莓', '柚子,黄柚子'],
    '其它数据': ['data1', 'data2', 'data3', 'data4', 'data5', 'data6']
}

df = pd.DataFrame(data)

# 查询函数
def search(keyword, row):
    return row['名称'].lower().find(keyword.lower()) >= 0 or any(alias.lower().find(keyword.lower()) >= 0 for alias in row['别名'].split(','))

# 并行查询
def parallel_search(keyword, df):
    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(search, keyword, row): row for index, row in df.iterrows()}
        for future in concurrent.futures.as_completed(futures):
            if future.result():
                results.append(futures[future])
    return pd.DataFrame(results)

keyword = '橙'
result = parallel_search(keyword, df)
print(result)
