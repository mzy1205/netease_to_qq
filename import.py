from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
import time
import json
# from cookie_json import cookies
import common

cookie_dir = r'/home/itzj00100/.config/google-chrome'    # 对应你的chrome的用户数据存放路径
# cookie_dir = r'C:\Users\mzy\AppData\Local\Google\Chrome\User Data'    # 对应你的chrome的用户数据存放路径  

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('profile-directory=Default')
chrome_options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"')
# chrome_options.add_argument("user-data-dir="+os.path.abspath(cookie_dir))

chromedriver_path = r'/usr/local/bin/chromedriver'
# chromedriver_path = r'D:\programs\netease_to_qq\chromedrivers\chromedriver.exe'
chromedriver_path = os.path.abspath(chromedriver_path)
driver=webdriver.Chrome(executable_path = chromedriver_path, chrome_options=chrome_options)
driver.maximize_window()
driver.get("https://y.qq.com/")

# driver.delete_all_cookies()
# for k in cookies:
#     print(k + ' -- ' + str(cookies[k]))
#     driver.add_cookie({'name':k,'value':cookies[k]})
# f = open("tmp.html", "w")
# f.write(driver.page_source)
# print(driver.page_source)
time.sleep(10)
ele = driver.find_element_by_css_selector(".top_nav__item:nth-child(2)")        #点击我的音乐
ele.click()

time.sleep(1)
ele = driver.find_element_by_css_selector(".mod_tab__item:nth-child(3)")        #点击我创建的歌单
ele.click()

play_lists = common.load_play_lists('bak.json')
lost = {}
for k in play_lists:        #创建歌单
    print(play_lists[k]['playlist_name'])
    time.sleep(0.5)
    ele = driver.find_element_by_css_selector(".js_create_new")
    ele.click()  # 点击新建歌单

    time.sleep(0.2)
    ele = driver.find_element_by_css_selector("#new_playlist")
    ele.send_keys(play_lists[k]['playlist_name'])

    ele = driver.find_element_by_css_selector(".popup__ft button:nth-child(2)")
    ele.click()

    ele = driver.find_element_by_css_selector(".search_input__input")
    lost[k] = {"playlist_name": play_lists[k]['playlist_name'], "link": play_lists[k]['link'], "songs": {}}
    for song_k in play_lists[k]["songs"]:
        ele.send_keys(play_lists[k]["songs"][song_k]["song_name"] + ' ' + play_lists[k]["songs"][song_k]["album"])  #根据歌曲名称和专辑名称查找，基本能匹配
        ele.send_keys(Keys.ENTER)
        time.sleep(0.2)

        #获取第一条查询结果的name、singer、album_name
        try:
            ele = driver.find_element_by_css_selector(".songlist__songname_txt:nth-child(1)")
            songname = ele.text

            ele = driver.find_element_by_css_selector(".songlist__artist:nth-child(1)")
            artist = ele.text

            ele = driver.find_element_by_css_selector(".songlist__album:nth-child(1)")
            album = ele.text

            if ((songname == play_lists[k]["songs"][song_k]["song_name"]) and (artist == play_lists[k]["songs"][song_k]["singer"]) and (album == play_lists[k]["songs"][song_k]["album"])):
                pass
            else:           #找到歌曲，但是没有完全匹配记录该条歌曲信息
                lost[k]['songs'][song_k] = {
                    "song_name": play_lists[k]["songs"][song_k]["song_name"],
                    "singer"   : play_lists[k]["songs"][song_k]["singer"],
                    "album"    : play_lists[k]["songs"][song_k]["album"]}

        except NoSuchElementException as ex:  # 找不到(根据歌曲名称和专辑未找到结果)记录下该条歌曲信息，等写文件
            lost[k]['songs'][song_k] = {
                "song_name": play_lists[k]["songs"][song_k]["song_name"], 
                "singer"   : play_lists[k]["songs"][song_k]["singer"], 
                "album"    : play_lists[k]["songs"][song_k]["album"]}
        # else:
        #     return
        # finally:
        #     return
