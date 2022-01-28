import time
import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# 事件链路
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

# 选择谷歌浏览器
options = Options()
# 无头，就是不显示浏览器
# options.add_argument("-headless")
# options.add_argument("-disable-gpu")

options.add_argument('--disable-blink-features=AutomationControlled')
# sever = Service(executable_path=r'G:\chromedriver.exe')
web = webdriver.Chrome(options=options)

# 输入网址
web.get("https://kyfw.12306.cn/otn/resources/login.html")

# 账号
web.find_element(by=By.XPATH, value='//*[@id="J-userName"]').send_keys('账号')
# 密码
web.find_element(by=By.XPATH, value='//*[@id="J-password"]').send_keys('密码')
# 点击登录
web.find_element(by=By.XPATH, value='//*[@id="J-login"]').click()

# 拖动滑块,事件提交
time.sleep(3)
span_element = web.find_element(by=By.XPATH, value='//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(span_element, 340, 0).perform()

# 进入页面后肯能弹出提示，确定即可
time.sleep(5)
html = web.page_source
obj = re.compile(r'<div class="dzp-confirm" id="(?P<id>.*?)"', re.S)
# 通过正则获取唯一ID
id = obj.search(html).group("id")
web.find_element(by=By.XPATH, value=f'//*[@id="{id}"]/div[2]/a/i').click()

# 进入首页
web.find_element(by=By.XPATH, value='//*[@id="J-index"]/a').click()

# 选择成都-营山的地址
time.sleep(2)
web.find_element(by=By.XPATH, value='//*[@id="fromStationText"]').click()
web.find_element(by=By.XPATH, value='//*[@id="fromStationText"]').send_keys("成都", Keys.ENTER)
web.find_element(by=By.XPATH, value='//*[@id="toStationText"]').click()
web.find_element(by=By.XPATH, value='//*[@id="toStationText"]').send_keys("营山", Keys.ENTER)
web.find_element(by=By.XPATH, value='//*[@id="search_one"]').click()

# 页面切换
web.switch_to.window(web.window_handles[-1])

# 选择时间 下拉框
select_element = web.find_element(by=By.XPATH, value='//*[@id="cc_start_time"]')
select = Select(select_element)
for i in range(len(select.options)):
    time.sleep(2)
    # 按照索引切换
    select.select_by_index(i)

    table_info = web.find_element(by=By.XPATH, value='//*[@id="t-list"]/table')
    print(table_info.text)
    print("=========================================================================")

# 关闭
web.close()
