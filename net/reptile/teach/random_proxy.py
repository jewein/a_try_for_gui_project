import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

# 你的代理服务器列表
proxy_list = [
'vmess://ew0KICAidiI6ICIyIiwNCiAgInBzIjogInYyY3Jvc3MuY29tIiwNCiAgImFkZCI6ICJiLmJhb3ppbmV0LnRvcCIsDQogICJwb3J0IjogIjI1MDAyIiwNCiAgImlkIjogIjUwYjQ3OWU2LTg4OGQtNDJiYi1iMGRkLTBlYTk5MzVmN2E3ZSIsDQogICJhaWQiOiAiMCIsDQogICJzY3kiOiAiYXV0byIsDQogICJuZXQiOiAidGNwIiwNCiAgInR5cGUiOiAibm9uZSIsDQogICJob3N0IjogIiIsDQogICJwYXRoIjogIiIsDQogICJ0bHMiOiAiIiwNCiAgInNuaSI6ICIiLA0KICAiYWxwbiI6ICIiLA0KICAiZnAiOiAiIg0KfQ==',
'vmess://ew0KICAidiI6ICIyIiwNCiAgInBzIjogInYyY3Jvc3MuY29tIiwNCiAgImFkZCI6ICIxMTIuMjkuOTQuMjIiLA0KICAicG9ydCI6ICI1MzMwMCIsDQogICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLA0KICAiYWlkIjogIjY0IiwNCiAgInNjeSI6ICJhdXRvIiwNCiAgIm5ldCI6ICJ0Y3AiLA0KICAidHlwZSI6ICJub25lIiwNCiAgImhvc3QiOiAiIiwNCiAgInBhdGgiOiAiIiwNCiAgInRscyI6ICIiLA0KICAic25pIjogIiIsDQogICJhbHBuIjogIiIsDQogICJmcCI6ICIiDQp9',
]

driver_path = r'C:\Users\Public\Web\chromedriver-win64\chromedriver-win64\chromedriver.exe'
# 随机选择一个代理
# selected_proxy = random.choice(proxy_list)



for proxy in proxy_list:
    # 创建Chrome WebDriver实例
    driver = webdriver.Chrome(executable_path=driver_path)
    # 配置Selenium使用选定的代理
    chrome_options = Options()
    chrome_options.add_argument(f"--proxy-server={proxy}")

    # 访问网站
    driver.get("https://chat.openai.com/")
    sleep(3)
    # 在这里进行其他操作

    # 关闭浏览器
    driver.quit()
