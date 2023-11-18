import requests
from bs4 import BeautifulSoup

# 创建一个空的字典作为模板
data_dict_template = {
    "cpuname": None,
    "Description:": None,
    "Socket:": None,
    "Clockspeed:": None,
    "Turbo Speed:": None,
    "Cores:": None,
    "Threads:": None,
    "Typical TDP:": None,
    "Cache Size:": None,
    "Other names:": None,
    "CPU First Seen on Charts:": None,
    "CPUmark/$Price:": None,
    "Overall Rank:": None,
    "Last Price Change:": None,

    "PassMark CPU Rating:": None,
    "Single Thread Rating:": None,

}

# 修改这里的URL为你需要爬取的页面URL
url = "https://www.cpubenchmark.net/cpu.php?id=1"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# 找到数据表格
desc_body = soup.find("div", class_="desc-body")

# 创建一个副本字典
data_dict = data_dict_template.copy()

# 设置处理器型号（cpuname）
data_dict["cpuname"] = desc_body.find("span", class_="cpuname").get_text()

# 查找所有的p标签
paragraphs = desc_body.find_all("p")

# for p in paragraphs:
#     strongs = p.find_all("strong")
#     # print(p.get_text())
#     if strongs:
#         for strong in strongs:
#             title = strong.get_text().strip()
#             value = strong.next_sibling.strip()
#             if value == '': # 如果没有值，尝试从子节点找值
#                 print('如果没有值，尝试从子节点找em值')
#                 value = strong.find_next('em').get_text()
#                 if value is None:
#                     print('最终还是没找到')
#             print(title, '的列赋值为', value)
#             data_dict[title] = value


table = soup.find('table', class_='table', id='test-suite-results')
for row in table.find_all('tr'):
    for cell in row.find_all('th'):
        print(cell.text)

# for p in paragraphs:
#     strongs = p.find("strong")
#     # print(p.get_text())
#     if strongs:
#         for strong in strongs:
#
#             title = strong.get_text()
#             value = strong.next_element
#             if value == '': # 如果没有值，尝试从子节点找值
#                 print('如果没有值，尝试从子节点找em值')
#                 value = strong.next_element
#                 if value is None:
#                     print('最终还是没找到')
#                 else:
#                     value = value.text
#             print(title, '的列赋值为', value)
#             data_dict[title] = value
#             # data_dict[strong.text] = strong.next_element.strip()

# print(data_dict)

# 创建DataFrame
# df = pd.DataFrame(data_dict, index=[0])
#
# 将数据保存到Excel文件
# df.to_excel("output.xlsx", index=False)
