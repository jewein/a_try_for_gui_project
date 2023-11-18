from selenium import webdriver

# 创建一个Chrome WebDriver实例
chrome_options = webdriver.ChromeOptions()
# chrome_options.headless = True

driver_path = r'C:\Users\Public\Web\chromedriver-win64\chromedriver-win64\chromedriver.exe'
# 设置Referer请求头
chrome_options.add_argument("--user-agent=Your_User_Agent_String")
chrome_options.add_argument("--referer=https://www.referrerpage.com")  # 设置Referer的值

# 启动无头浏览器
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

# 打开一个网页
driver.get("https://www.example.com")

# 在这里进行其他操作

# 关闭浏览器
driver.quit()
