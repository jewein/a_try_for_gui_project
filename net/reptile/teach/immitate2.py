from selenium import webdriver
driver_path = r'C:\Users\Public\Web\chromedriver-win64\chromedriver-win64\chromedriver.exe'

url = "https://www.example.com"
referer_url = "https://www.referrerpage.com"  # 设置来源页面的URL

# 创建一个Chrome WebDriver实例
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=chrome_options, executable_path=driver_path)

# 使用execute_script方法设置Referer
driver.execute_script(f"window.location = '{url}';")
driver.execute_script(f"document.referrer = '{referer_url}';")

# 打开目标页面
driver.get(url)

# 在这里进行其他操作

# 关闭浏览器
driver.quit()
