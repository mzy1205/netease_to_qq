from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def find_targets(driver, count = 0, page_count = 0):
    page_count = page_count + 1
    # 找出所有链接
    eles = driver.find_elements_by_class_name("text-truncate")
    if eles:
        for s_ele in eles:
            count = count + 1
            f.write(str(page_count) + ' -- ' + str(count) + ' -- ' + s_ele.text + '  ' + s_ele.get_attribute("href") + '\n')
    else:
        print("ssssss")

    has_pages = driver.find_elements_by_class_name("page-link")

    if has_pages:
        try:
            next_disabled = driver.find_element_by_css_selector(".next.disabled")   #确认下一页是否可点
        except NoSuchElementException as ex:        #找不到(下一页可点)
            next_page = driver.find_element_by_css_selector(".next")
            next_page.click()
            find_targets(driver, count, page_count)
            print("in except")
        else:
            return
        finally:
            return
    
    return

driver = webdriver.Chrome()
driver.get("http://www.yiichina.com/")

# 获取输入框
ele = driver.find_element_by_css_selector(".input-group>.form-control")
ele.send_keys("test")

# 点击搜索
ele = driver.find_element_by_class_name("btn-light")
ele.click()

f = open("from_yii.txt", "a")

find_targets(driver)
# driver.close()