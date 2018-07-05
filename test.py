from selenium import webdriver
import os
import time
# from config import cookies
# from pyvirtualdisplay import Display

# from xvfbwrapper import Xvfb

# vdisplay = Xvfb()
# vdisplay.start()

# display = Display(visible=0, size=(800, 800))
# display.start()

cookie_dir= r'C:\Users\mzy\AppData\Local\Google\Chrome\User Data'    # 对应你的chrome的用户数据存放路径  
chrome_options=webdriver.ChromeOptions()
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-setuid-sandbox")

# chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("user-data-dir="+os.path.abspath(cookie_dir))  

driver=webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window()
driver.get("https://www.baidu.com/")

# driver.delete_all_cookies()
# for k in cookies:
#     print(k + ' -- ' + str(cookies[k]))
#     driver.add_cookie({'name':k,'value':cookies[k]})

# driver.get("https://www.baidu.com/")