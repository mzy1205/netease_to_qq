from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import json
from cookie_json import cookies

# cookie_dir = r'/home/itzj00100/.config/google-chrome'    # 对应你的chrome的用户数据存放路径
cookie_dir = r'C:\Users\mzy\AppData\Local\Google\Chrome\User Data'    # 对应你的chrome的用户数据存放路径  

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('profile-directory=Default')
chrome_options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"')
# chrome_options.add_argument("user-data-dir="+os.path.abspath(cookie_dir))

# chromedriver_path = r'/usr/local/bin/chromedriver'
chromedriver_path = r'D:\programs\netease_to_qq\chromedrivers\chromedriver.exe'
chromedriver_path = os.path.abspath(chromedriver_path)
driver=webdriver.Chrome(executable_path = chromedriver_path, chrome_options=chrome_options)
driver.maximize_window()
driver.get("https://y.qq.com/")

driver.delete_all_cookies()
for k in cookies:
    print(k + ' -- ' + str(cookies[k]))
    driver.add_cookie({'name':k,'value':cookies[k]})
    