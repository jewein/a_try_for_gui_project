import threading
from concurrent.futures import ThreadPoolExecutor

import pandas as pd
import requests
from bs4 import BeautifulSoup

# 创建一个空的字典作为模板  ##################################################################
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

#########################################

global_lock = threading.Lock()

df_existing = None
# 打开现有的Excel文件
try:
    df_existing = pd.read_excel('cpu_data.csv')
except FileNotFoundError:
    df_existing = pd.DataFrame(columns=data_dict_template.keys())


def transform_to_float(number_string):
    import re
    # 从number_string中删除逗号
    number_string = number_string.replace(',', '')
    # 使用正则表达式删除'MOps/Sec'或类似的字符串
    number_string = re.sub(r'[A-Za-z/]+', '', number_string)
    # 将字符串转换为浮点数
    return float(number_string)


def get_cpu_data(number=None):
    err_list = []
    # 修改这里的URL为你需要爬取的页面URL
    url = "https://www.cpubenchmark.net/cpu.php?id=" + str(number)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    try:
        # 找到数据表格
        desc_body = soup.find("div", class_="desc-body")
        # 创建一个副本字典
        data_dict = data_dict_template.copy()
        data_dict['No.'] = number
    except Exception as e:
        print(e)
        print('没找到第一个desc_body')
        err_list.append('没找到第一个desc_body')

    try:
        # 设置处理器型号（cpuname）
        data_dict["cpuname"] = desc_body.find("span", class_="cpuname").get_text()
    except Exception as e:
        print(e)
        print('没找到处理器型号（cpuname）')
        err_list.append('没找到处理器型号（cpuname）')

    try:
        # 查找所有的p标签
        paragraphs = desc_body.find_all("p")
    except Exception as e:
        print(e)
        print('没找到p标签')
        err_list.append('没找到p标签')

    try:
        # 写入数据
        for p in paragraphs:
            strongs = p.find_all("strong")
            # print(p.get_text())
            if strongs:
                for strong in strongs:
                    title = strong.get_text().strip()
                    value = strong.next_sibling.strip()
                    if value == '':  # 如果没有值，尝试从子节点找值
                        print('如果没有值，尝试从子节点找em值')
                        value = strong.find_next('em').get_text()
                        if value is None:
                            print('最终还是没找到')
                    # print(title, '的列赋值为', value)
                    data_dict[title] = value
    except Exception as e:
        print(e)
        err_list.append('没找到strong标签')

    try:
        # 找到数据表格
        right_desc = soup.find("div", class_="right-desc")
        span = right_desc.find("span",
                               style="font-family: Arial, Helvetica, sans-serif;font-size: 44px;	font-weight: bold; color: #F48A18;")
        rating = span.get_text()
    except Exception as e:
        print(e)
        err_list.append('没找到span标签')

    try:
        if rating.isdigit():
            print('找到了 passmark cpu rating')
            data_dict['PassMark CPU Rating:'] = rating
    except Exception as e:
        print(e)
        print('没找到 passmark cpu rating')
        err_list.append('没找到 passmark cpu rating')

    try:
        strong = right_desc.find("strong")
        if strong.get_text().strip() == 'Single Thread Rating:':
            print('找到了 single thread rating')
            value = strong.next_sibling.strip()
            data_dict['Single Thread Rating:'] = value
        else:
            print('没找到 single thread rating')
    except Exception as e:
        print(e)
        err_list.append('找 single thread rating 时发生异常')

    try:
        # 查找所有的p标签
        paragraphs = right_desc.find_all("p")
        # 写入数据
        for p in paragraphs:
            strongs = p.find_all("strong")
            # print(p.get_text())
            if strongs:
                for strong in strongs:
                    title = strong.get_text().strip()
                    value = strong.next_sibling.strip()
                    # print(title, '的列赋值为', value)
                    data_dict[title] = value
        table = soup.find('table', class_='table', id='test-suite-results')
        for tr in table.find_all('tr'):
            data_dict[tr.th.text.strip()] = tr.td.text.strip()
        number_string = data_dict['Floating Point Math']
    except Exception as e:
        print(e)
        err_list.append('没找到第二个table标签')

    # 将number_string转换为数目，注意这里的逗号以及以及删除‘MOps/Sec’类似的字符串
    data_dict['FLOPS'] = transform_to_float(number_string)
    number_string = data_dict['Single Thread']
    data_dict['single_thread'] = transform_to_float(number_string)
    number_string = data_dict['Extended Instructions']
    data_dict['multi_thread'] = transform_to_float(number_string)
    # print('=====================')
    # 变成pandas的DataFrame

    with global_lock:
        # 在锁内部操作全局变量
        # 这里可以安全地访问和修改全局变量
        global df_existing

        if 'No.' in data_dict and not df_existing[df_existing['No.'] == data_dict['No.']].empty:  # 如果已经存在这个No.的数据，更新这一行
            df_existing.loc[
                df_existing['No.'] == data_dict['No.'], data_dict.keys()] = data_dict.values()  # 这里的data.values()是一个列表
        else:
            # 追加新数据到现有DataFrame
            df_existing = pd.concat([df_existing, pd.DataFrame([data_dict])], ignore_index=True)
        pass
    # print('=' * 20)
    print('已经完成了第', number, '个页面的爬取')
    if err_list:
        print('但是出现了错误', err_list)
    else:
        print('一切正常')


if __name__ == '__main__':
    excutor = ThreadPoolExecutor(max_workers=5000)
    err_number_list = []
    for i in range(1, 6001):
        try:
            excutor.submit(get_cpu_data, i)
            print(f'第{i}个线程已经建立')
        except Exception as e:
            print(e)
            print('出现了问题')
            err_number_list.append(i)

    excutor.shutdown(wait=True)

    try:
        # 处理空值
        # df_existing.fillna("N/A", inplace=True)

        # 保存更新后的数据到Excel文件
        with pd.ExcelWriter('cpu_data.xlsx', mode='w', engine='openpyxl') as writer:
            df_existing.to_excel(writer, index=False, header=True)
    except Exception as e:
        print(e)
        print('出现了问题')

    print(df_existing)
    # 保存到csv
    df_existing.to_csv('cpu_data.csv', index=False, header=True)

    print('出现了问题的页面有', err_number_list)
