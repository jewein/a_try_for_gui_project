from selenium import webdriver

# 1. 创建一个Cookie池，这里只是示例，你可以添加更多的Cookie值
cookie_pool = [
    {"name": "cookie_name1", "value": "cookie_value1", "domain": "www.example.com", },
    {"name": "cookie_name2", "value": "cookie_value2", "domain": "www.example.com", },
    # 添加更多的Cookie
]

driver_path = r'C:\Users\Public\Web\chromedriver-win64\chromedriver-win64\chromedriver.exe'
# 创建一个Chrome WebDriver实例
driver = webdriver.Chrome(executable_path=driver_path)

# 随机选择一个Cookie
import random

selected_cookie = random.choice(cookie_pool)


driver.get("https://www.example.com")

# 2. 设置选定的Cookie
driver.add_cookie(selected_cookie)

# 3. 使用设置的Cookie访问网站
driver.get("https://www.example.com")

# 在这里进行其他操作
input('Press ENTER to exit')
# 关闭浏览器
driver.quit()
