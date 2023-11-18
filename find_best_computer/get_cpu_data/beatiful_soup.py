import requests
from bs4 import BeautifulSoup
import openpyxl

# 创建一个Excel文件并写入表头信息
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "CPU Data"
ws.append(["Processor", "Description", "Class", "Socket", "Clockspeed", "Turbo Speed", "Cores", "Threads", "Typical TDP", "L1 Cache", "L2 Cache", "Other Names", "First Seen on Charts", "CPUmark/$Price", "Overall Rank", "Last Price Change"])

# 为了演示目的，假设有多个页面URL存储在一个列表中
urls = [# 定义要爬取的页面URL
 f'https://www.cpubenchmark.net/cpu.php?id=1'
]

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    #================================

    # 假设您已经使用Beautiful Soup解析了HTML并将其存储在soup对象中

    # 找到包含类别信息的p标签
    all_p = soup.find("div", class_="left-desc-cpu").find_all("p")

    for class_p in all_p:
        print(class_p.text.strip())

        #name设为p的strong里的内容
        # name=class_p.strong.text
        #删除掉class_p中的strong标签(包含全部内容)
        # class_p.strong.decompose()
        # class_text = ''.join(class_p.stripped_strings)

        # 排除掉<strong>Class:</strong>标签
        # class_value = class_text.replace("Class:", "").strip()

        # print(name, class_p.text.strip())


    #==================================


    # 提取页面中的数据
#     processor = soup.find("span", class_="cpuname").text # 找到span标签，class属性值为cpuname的元素
#     # description = soup.find("div", class_="desc-foot").p.text.strip() # 找到div标签，class属性值为desc-foot的元素，再找到p标签，提取文本内容
#     class_info = soup.find("div", class_="left-desc-cpu").find_all("p")[0].text # 找到div标签，class属性值为left-desc-cpu的元素，再找到所有的p标签，提取第一个p标签的文本内容
#     socket = soup.find("div", class_="left-desc-cpu").find_all("p")[1].text
#     clockspeed = soup.find("div", class_="left-desc-cpu").find_all("p")[2].text
#     turbo_speed = soup.find("div", class_="left-desc-cpu").find_all("p")[3].text
#     cores_threads = soup.find("div", class_="left-desc-cpu").find_all("p")[4].text
#     typical_tdp = soup.find("div", class_="left-desc-cpu").find_all("p")[5].text
#     l1_cache = soup.find("div", class_="desc-foot").find("strong", text="Cache Size").find_next("p").text
#     other_names = soup.find("div", class_="desc-foot").find("strong", text="Other names").find_next("p").text
#     first_seen = soup.find("div", class_="desc-foot").find("strong", text="CPU First Seen on Charts").find_next("p").text
#     cpumark_price = soup.find("div", class_="desc-foot").find("strong", text="CPUmark/$Price").find_next("p").text
#     overall_rank = soup.find("div", class_="desc-foot").find("strong", text="Overall Rank").find_next("p").text
#     last_price_change = soup.find("div", class_="desc-foot").find("strong", text="Last Price Change").find_next("p").text
#
#     # 将数据添加到Excel文件
#     ws.append([processor,  class_info, socket, clockspeed, turbo_speed, cores_threads, typical_tdp, l1_cache, None, None, other_names, first_seen, cpumark_price, overall_rank, last_price_change])
#
# # 保存Excel文件
# wb.save("cpu_data.xlsx")
