from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 设置Chrome驱动程序的路径（根据实际情况修改）
driver_path = r'C:\Users\Public\Web\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# 创建一个UserAgent对象
user_agent = UserAgent()
# 创建一个Chrome WebDriver实例
chrome_options = Options()



# 在每次请求之前重新生成随机的User-Agent
# for i in range(5):  # 举例：连续访问5次
#     random_user_agent = user_agent.random
#     chrome_options.add_argument(f"--user-agent={random_user_agent}")

random_user_agent = user_agent.random
chrome_options.add_argument(f"--user-agent={random_user_agent}")

# 创建Chrome浏览器驱动
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

# 打开网页
driver.get("https://www.baidu.com")

# 在这里进行其他操作

# 关闭浏览器
driver.quit()





