from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import json
# from config import cookies

# _name = input("请输入用户昵称：")
_name = "毛阳光很阳光"


# cookie_dir = r'/home/itzj00100/.config/google-chrome'    # 对应你的chrome的用户数据存放路径
cookie_dir = r'C:\Users\mzy\AppData\Local\Google\Chrome\User Data'    # 对应你的chrome的用户数据存放路径  

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('profile-directory=Default')
# chrome_options.add_argument("user-data-dir="+os.path.abspath(cookie_dir))  
# print(os.path.abspath(cookie_dir))
chromedriver_path = r'/usr/local/bin/chromedriver'
chromedriver_path = os.path.abspath(chromedriver_path)
driver=webdriver.Chrome(executable_path = chromedriver_path, chrome_options=chrome_options)
driver.maximize_window()
driver.get("https://music.163.com/")

# driver.delete_all_cookies()
# for k in cookies:
#     print(k + ' -- ' + str(cookies[k]))
#     driver.add_cookie({'name':k,'value':cookies[k]})

# driver.get("https://www.baidu.com/")

# 首页搜索框填充昵称
ele = driver.find_element_by_name("srch")
ele.send_keys(_name)
ele.send_keys(Keys.ENTER)

# 切换到iframe，找到用户那一栏
driver.switch_to.frame("g_iframe")
ele = driver.find_element_by_css_selector(".m-tabs-srch>li:last-child")
ele.click()

time.sleep(0.1)

# 找到查到的用户
ele = driver.find_element_by_css_selector(".h-flag>.first.w7>.u-cover.u-cover-3")
ele.click()

# 进入到用户信息页面结束

time.sleep(0.5)

ele = driver.find_elements_by_css_selector("#cBox p a")
my_songs = {}
num = 1

tmp = {}
for v in ele:
    playlist_name = v.get_attribute('title')
    link = v.get_attribute('href')
    tmp[str(num)] = {"playlist_name":playlist_name, "link":link}
    num += 1
num = 1
for v in tmp.keys():
    playlist_name = tmp[v]["playlist_name"]
    link = tmp[v]["link"]
    my_songs[str(num)] = {"playlist_name":playlist_name, "link":link, "songs":{}}
    driver.get(link)
    time.sleep(3)
    driver.switch_to.frame("g_iframe")

    rows = driver.find_elements_by_css_selector(".m-table tbody>tr")
    
    song_num = 1
    for row in rows:
        song_name = row.find_element_by_css_selector("td:nth-of-type(2) b")
        song_name = song_name.get_attribute('title')
        print(song_name)

        singer = row.find_element_by_css_selector("td:nth-of-type(4) div")
        singer = singer.get_attribute('title')

        album = row.find_element_by_css_selector("td:nth-of-type(5) a")
        album = album.get_attribute("title")

        my_songs[str(num)]["songs"][str(song_num)] = {}
        my_songs[str(num)]["songs"][str(song_num)]["song_name"] = song_name
        my_songs[str(num)]["songs"][str(song_num)]["singer"] = singer
        my_songs[str(num)]["songs"][str(song_num)]["album"] = album

        song_num += 1

    num += 1
    time.sleep(0.1)

f = open("play_list.txt", "w")
f.write(json.dumps(my_songs))