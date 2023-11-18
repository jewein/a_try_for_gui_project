import atexit
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from random import random
from time import sleep

import pandas as pd
import requests
from bs4 import BeautifulSoup

data_dict_template = {
    "No.": None,
    "gpuname": None,
    "GPU Name": None,
    "GPU Variant": None,
    "Release Date": None,
    "Bus Interface": None,
    "Base Clock": None,
    "Boost Clock": None,
    "Memory Clock": None,
    "Memory Size": None,
    "Memory Type": None,
    "Memory Bus": None,
    "Compute Units": None,
    "Pixel Rate": None,
    "Texture Rate": None,
    "FP32 (float)": None,
    "TDP": None,
    "FLOPS": None
}

global_lock = threading.Lock()
data_existing = None

# 打开现有的Excel文件
try:
    data_existing = pd.read_csv('gpu_data.csv')
except FileNotFoundError:
    data_existing = pd.DataFrame(columns=data_dict_template.keys())


def transform_to_float(number_string):
    import re
    # 从number_string中删除逗号
    number_string = number_string.replace(',', '')
    # 使用正则表达式删除'MOps/Sec'或类似的字符串
    number_string = re.sub(r'[A-Za-z/]+', '', number_string)
    # 将字符串转换为浮点数
    return float(number_string)


def get_gpu_data(number=None):
    err_list = []
    # 修改这里的URL为你需要爬取的页面URL
    #生成一个随机字母串
    random_string=''
    for i in range(int(random()*10+1)):
        random_letter = chr(int(random() * 26) + 97)
        random_string += random_letter
    url = "https://www.techpowerup.com/gpu-specs/"+random_string+".c" + str(number)
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    try:
        div = soup.find('div', class_='sectioncontainer')
        data_dict = data_dict_template.copy()
        data_dict['No.'] = number
        data_dict['gpuname'] = soup.find('h1', class_='gpudb-name').text.strip()
        dls = div.find_all('dl')
        for dl in dls:
            dt = dl.find('dt')
            dd = dl.find('dd')
            if dt and dd:
                data_dict[dt.text.strip()] = dd.text.strip()
        print(data_dict)

        data_dict['FLOPS'] = transform_to_float(data_dict['FP32 (float)'])

    except Exception as e:
        print(e)

    try:
        with global_lock:
            global data_existing
            if 'No.' in data_dict and not data_existing[
                data_existing['No.'] == data_dict['No.']].empty:  # 如果已经存在这个No.的数据，更新这一行
                data_existing.loc[data_existing['No.'] == data_dict[
                    'No.'], data_dict.keys()] = data_dict.values()  # 这里的data.values()是一个列表
            else:
                # 追加新数据到现有DataFrame
                data_existing = pd.concat([data_existing, pd.DataFrame([data_dict])], ignore_index=True)
    except Exception as e:
        print(e)
        print('出现了问题')

    print(data_existing)
    print(f'第{number}个线程已经完成')


class Mission:
    def __init__(self):
        # global data_existing
        # excutor = ThreadPoolExecutor(max_workers=3)
        err_number_list = []
        times = 0
        while True:
            #随机数，（14, 4500）的范围
            random_number=int(random()*4486)+14
            #范围是（1, 4486）
            try:
                times += 1
                if random_number in data_existing['No.'].values:
                    print(f'第{random_number}行数据已经存在，跳过')

                else:
                    if times % 7 == 0:
                        print('访问TechPowerUp其它网站')
                        requests.get('https://www.techpowerup.com/contact/')
                        time.sleep(18)
                        if times % 3 == 0:
                            requests.get('https://www.techpowerup.com/forums/threads/share-your-speedometer-2-0-benchmark-here.306013/')
                            time.sleep(35)
                    if times % 17 == 0:
                        requests.get('https://www.techpowerup.com/forums/threads/tpus-nostalgic-hardware-club.108251/')
                        time.sleep(23)


                    get_gpu_data(random_number)
                    #sleep 随机5~20秒，包括小数
                    random_time = random() * 36 + 4
                    print('准备沉睡', random_time, '秒')
                    sleep(random_time)
                    print('sleep', random_time, '秒完成')

            except Exception as e:
                print(e)
                print('出现了问题')
                err_number_list.append(random_number)

            # excutor.shutdown(wait=True)
            self.save()

        print('出现了问题的页面有', err_number_list)

    @classmethod
    def save(self):
        try:
            # 处理空值
            # df_existing.fillna("N/A", inplace=True)
            # 保存更新后的数据到Excel文件
            with pd.ExcelWriter('gpu_data.xlsx', mode='w', engine='openpyxl') as writer:
                data_existing.to_excel(writer, index=False, header=True)
        except Exception as e:
            print(e)
            print('出现了问题')

        print(data_existing)
        # 保存到csv
        data_existing.to_csv('gpu_data.csv', index=False, header=True)
        print('保存完成')



atexit.register(Mission.save)

if __name__ == '__main__':
    try:
        m=Mission()
    except Exception as e:
        m.save()
    finally:
        m.save()




