import requests
from bs4 import BeautifulSoup
import pandas as pd

# 创建一个空的DataFrame来存储数据
data = pd.DataFrame(columns=["CPU Name", "Description", "class_", "Socket", "Clockspeed", "Turbo Speed",
                             "Cores", "Threads", "Typical TDP", "L1 Cache", "L2 Cache", "Other Names",
                             "First Seen on Charts", "CPUmark/$Price", "Overall Rank", "Last Price Change"])

# 定义要爬取的页面URL列表
urls = [
    # 定义要爬取的页面URL
f'https://www.cpubenchmark.net/cpu.php?id=1'
    # 添加其他页面的URL
]

# 遍历页面URL
for url in urls:
    # 发起HTTP请求获取页面内容
    response = requests.get(url)
    if response.status_code == 200:
        # 使用Beautiful Soup解析页面
        soup = BeautifulSoup(response.text, "html.parser")

        # 从页面中提取表格数据
        cpu_name = soup.find("span", class_="cpuname").text
        description = soup.find("div", class_="desc-foot").p.text
        class_info = soup.find("div", class_="left-desc-cpu").find_all("p")[0].text
        socket = soup.find("div", class_="left-desc-cpu").find_all("p")[1].text
        clockspeed = soup.find("div", class_="left-desc-cpu").find_all("p")[2].text
        turbo_speed = soup.find("div", class_="left-desc-cpu").find_all("p")[3].text
        cores_threads = soup.find("div", class_="left-desc-cpu").find_all("p")[4].text
        typical_tdp = soup.find("div", class_="left-desc-cpu").find_all("p")[5].text
        cache_size = soup.find("div", class_="desc-foot").find("p", string="Cache Size:").text
        other_names = soup.find("div", class_="desc-foot").find("p", string="Other names:").em.text
        first_seen = soup.find("div", class_="desc-foot").find("p", class__="alt").text
        cpumark_price = soup.find("div", class_="desc-foot").find("p", string="CPUmark/$Price:").text
        overall_rank = soup.find("div", class_="desc-foot").find("p", class__="alt").find("strong").text
        last_price_change = soup.find("div", class_="desc-foot").find("p", string="Last Price Change:").a.text

        # 添加数据到DataFrame
        data = data.append({
            "CPU Name": cpu_name,
            "Description": description,
            "class_": class_info,
            "Socket": socket,
            "Clockspeed": clockspeed,
            "Turbo Speed": turbo_speed,
            "Cores": cores_threads.split()[1],
            "Threads": cores_threads.split()[3],
            "Typical TDP": typical_tdp.split(":")[1].strip(),
            "L1 Cache": cache_size.split(":")[1].split(",")[0].strip(),
            "L2 Cache": cache_size.split(":")[1].split(",")[1].strip(),
            "Other Names": other_names,
            "First Seen on Charts": first_seen.split(":")[1].strip(),
            "CPUmark/$Price": cpumark_price.split(":")[1].strip(),
            "Overall Rank": overall_rank,
            "Last Price Change": last_price_change
        }, ignore_index=True)

# 保存数据到Excel文件
data.to_excel("cpu_data.xlsx", index=False)
