import requests
from bs4 import BeautifulSoup
from PIL import Image
import io
import urllib
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import requests
from concurrent.futures import ThreadPoolExecutor


# 设置Chrome驱动程序的路径（根据实际情况修改）
driver_path = r'C:\Users\Public\Web\chromedriver-win64\chromedriver-win64\chromedriver.exe'
# 创建Chrome浏览器驱动
driver = webdriver.Chrome(executable_path=driver_path)
url = f'https://www.cpubenchmark.net/cpu.php?id='


for i in range(1,6000):
    driver.get(url+str(i))

    # 获取页面内容
    html_content = driver.page_source

    # 使用BeautifulSoup解析页面内容
    soup = BeautifulSoup(html_content, 'html.parser')
    



# 只下载并保存jpeg或jpg图像
count = 0
def download_image(image_url):
    global count
    # 发送HTTP请求获取图像内容
    response = requests.get(image_url)
    # 检查请求是否成功
    if response.status_code == 200:
        # 提取图像文件名
        # 使用Pillow库检测图像格式并保存为正确的格式
        d=count
        count+=1
        image_data = io.BytesIO(response.content)
        image = Image.open(image_data)
        image_format = image.format.lower()  # 获取图像格式
        if image_format not in ['jpeg', 'jpg']:
            print('not jpeg or jpg!')
        else:
            filename = f'Pic/{search_term}/{search_term}_ecosia_{d + 1000}.{image_format}'
            image.save(filename)
            print(f'Saved {filename}')
            filename = f'Pic/else/{search_term}/{search_term}_ecosia_{d + 1000}.{image_format}'
            image.save(filename)
            print(f'Saved {filename}')

    else:
        print(f'Failed to download image_{count + 1}')


# 创建线程池
executor = ThreadPoolExecutor()
n=0
for i, link in enumerate(image_links):
    if count >= 1000 or n>=1050:  # 控制下载的图片数量
        break
    try:
        image_url = urllib.parse.urljoin(url, link)
        executor.submit(download_image, image_url)
        n+=1
        print(f'第{n}个线程已经建立')
    except Exception as e:
        print(e)
        print(f'Failed to download {image_url}')



# 等待所有任务完成
executor.shutdown()

# 关闭浏览器驱动
driver.quit()





'''
0-94  
url = f'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=detail&fr=&hs=0&xthttps=000000&sf=1&fmq=1685855380651_R&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word={search_term}'

101-200




'''





'''About Dog
1-1000 from baidu




'''