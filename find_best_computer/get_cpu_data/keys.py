# 创建一个空的字典作为模板
import pandas as pd

data_dict_template = {
    "No.": None,
    "cpuname": None,
    "Description:": None,
    "Socket:": None,
    "Clockspeed:": None,
    "Turbo Speed:": None,
    "Cores:": None,
    "Threads:": None,
    "Typical TDP:": None,
    "Cache Size:": None,
    "Memory Support:": None,
    "Other names:": None,
    "CPU First Seen on Charts:": None,
    "CPUmark/$Price:": None,
    "Overall Rank:": None,
    "Last Price Change:": None,

    "PassMark CPU Rating:": None,
    "Single Thread Rating:": None,


    "Integer Math": None,
    "Floating Point Math": None,
    "Find Prime Numbers": None,
    "Random String Sorting": None,
    "Data Encryption": None,
    "Data Compression": None,
    "Physics": None,
    "Extended Instructions": None,
    "Single Thread": None,

    "single_thread": None,
    "multi_thread": None,
    "FLOPS": None

}
#上述的字典把它变成把它的 键名提取到一个列表。
list_of_keys = list(data_dict_template.keys())
print(list_of_keys)

#再把list_of_keys保存为excel表头
df = pd.DataFrame(columns=list_of_keys)
df.to_excel('cpu_data.xlsx', index=False)



