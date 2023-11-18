import base64
import json
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

driver_path = r'C:\Users\Public\Web\chromedriver-win64\chromedriver-win64\chromedriver.exe'
# 代理链接示例
vmess_links = [
    "vmess://ew0KICAidiI6ICIyIiwNCiAgInBzIjogInYyY3Jvc3MuY29tIiwNCiAgImFkZCI6ICJzaW5nYXBvcmUuY29tIiwNCiAgInBvcnQiOiAiODA4MCIsDQogICJpZCI6ICJkM2Y4M3M3MTJmMzI0MjI9IiwNCiAgImFpZCI6ICIwIiwNCiAgInNjeSI6ICJhdXRob3V0IiwNCiAgIm5ldCI6ICJ3cyIsDQogICJ0eXBlIjogIm5vbmUiLA0KICAIaG9zdCI6ICJzNzVtdWxsLmNvbSIsDQogICJwYXRoIjogIi9hcGkvdjMvZG93bmxvYWQuZ2V0RmlsZSIsDQogICJ0bHMiOiAiIiwNCiAgInNuaSI6ICIiLA0KICAiYWxwbiI6ICIiLA0KICAiZnAiOiAiIg0KfQ==",
    # 添加更多VMess链接
]

# 遍历VMess链接并配置Selenium使用代理
for vmess_link in vmess_links:
    # 解析VMess链接
    vmess_data = vmess_link.replace("vmess://", "")
    decoded_data = base64.urlsafe_b64decode(vmess_data + '==').decode('utf-8')
    vmess_info = json.loads(decoded_data)

    # 配置Selenium使用代理
    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = f"http://{vmess_info['add']}:{vmess_info['port']}"
    proxy.ssl_proxy = f"http://{vmess_info['add']}:{vmess_info['port']}"
    capabilities = webdriver.DesiredCapabilities.CHROME
    proxy.add_to_capabilities(capabilities)

    # 创建Selenium WebDriver实例
    driver = webdriver.Chrome(desired_capabilities=capabilities, executable_path=driver_path)

    # 使用代理进行爬取
    driver.get("https://www.example.com")
    # 在这里进行其他操作

    # 关闭浏览器
    driver.quit()




