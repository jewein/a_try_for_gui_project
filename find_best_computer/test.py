from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook

driver_path = r'C:\Users\Public\Web\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# 创建Chrome浏览器驱动
driver = webdriver.Chrome(executable_path=driver_path)



# 打开网页
driver.get("https://www.baidu.com")

# 设置显式等待时间为10秒，指定等待的元素为搜索框，并等待搜索框可见
search_box = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "kw"))
)

# 在搜索框输入关键词
search_box.send_keys("Hello, World!")

# 继续执行其他操作，例如点击搜索按钮等
# ...

input()
# 关闭浏览器
driver.quit()