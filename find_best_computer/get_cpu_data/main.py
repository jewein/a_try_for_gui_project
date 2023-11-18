# 爬虫程序，从https://www.cpubenchmark.net/ 爬取数据


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

# 全程注释用中文。

###############################################
# 设置Chrome驱动程序的路径（根据实际情况修改）
chrome_driver_path  = r'C:\Users\Public\Web\chromedriver-win64\chromedriver-win64\chromedriver.exe'
# 创建Chrome驱动程序服务
# 创建Chrome浏览器驱动
driver = webdriver.Chrome(executable_path=chrome_driver_path) # 创建Chrome浏览器驱动，指定驱动程序的路径

# 设置隐式等待时间为5秒
driver.implicitly_wait(5) # 设置隐式等待时间为5秒
wait = WebDriverWait(driver, 5) # 设置显式等待时间为5秒
url_head = "https://www.cpubenchmark.net/cpu.php?id=" # 设置url_head
url_tail_number=2794 # 设置url_tail_number

##############################################

def get_cpu_data(url_tail_number): # 定义get_cpu_data函数
url = url_head + str(url_tail_number) # 设置url
    driver.get(url) # 打开网页
    # 等待搜索框元素可见
    search_box = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".sch-searchyuanxiaoku input[name='sch_wd']"))
    )
    # search_box.send_keys("Your search query")
    search_box.send_keys("长江大学") # 在搜索框输入关键词
    # 等待下拉框的出现
    dropdown_menu = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#sch-searchyuanxiaoku-result")))
    # 找到并点击第一个选项
    first_option = dropdown_menu.find_element(By.CSS_SELECTOR, "li.item:first-child a")
    first_option.click()
    # 等待新页面加载完成
    wait.until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])  # 切换到新打开的页面
    # 定位到"专业分数线"链接
    link_element = driver.find_element(By.XPATH,'//li/a[contains(text(), "专业分数线")]')
    # 使用ActionChains模拟点击并在新页面中打开链接
    actions = ActionChains(driver)
    actions.move_to_element(link_element).click().






