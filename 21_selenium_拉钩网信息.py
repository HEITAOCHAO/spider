# https://npm.taobao.org/mirrors/chromedriver/  谷歌驱动下载地址
# pip install selenium
# 如果报错，看一下是否是utf-8编码，如果不是改成UTF-8跑下
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 创建浏览器
web = Chrome()
# 打开浏览器
web.get("https://www.lagou.com")

title = web.title

# 找到某个元素，点击它   （选择成都）
# web.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[7]/a') 被弃用，使用下面的方法
el = web.find_element(By.XPATH, '//*[@id="changeCityBox"]/ul/li[7]/a')
# 点击事件
el.click()

# 可能数据是通过ajax拿到的,拿到渲染需要时间,睡一秒钟稳一稳,不然后面报错
time.sleep(1)

# 找到输入框
input = web.find_element(By.XPATH, '//*[@id="search_input"]')
# 输入文字,并回车
input.send_keys("java开发", Keys.ENTER)

time.sleep(1)

# 找到数据存放位置，进行数据获取
divs = web.find_elements(By.XPATH, '//*[@id="jobList"]/div[1]/div')
for i in range(len(divs)):
    div = divs[i]
    # 工作
    job = div.find_element(By.TAG_NAME, "a").text
    # 工作年限
    year = div.find_element(By.XPATH, './div/div/div[2]').text
    # 工资
    salary = div.find_element(By.XPATH, './div/div/div[2]/span').text
    # 公司
    company = div.find_element(By.XPATH, './div/div[2]/div/a').text

    print(job, year, salary, company)

    # 进入详细页面，拿去详细数据
    time.sleep(3)
    child_xpath = f'//*[@id="jobList"]/div[1]/div[{i+1}]/div[1]/div[1]/div[1]/a'
    print(f"child_xpath:{child_xpath}")
    web.find_element(By.XPATH, child_xpath).click()
    # 进行窗口切换，切换到最后一个,提取数据
    web.switch_to.window(web.window_handles[-1])
    content = web.find_element(By.XPATH, '//*[@id="job_detail"]/dd[2]/div').text
    print(content)
    time.sleep(1)
    web.close()

    # 在把浏览器窗口切换回来
    web.switch_to.window(web.window_handles[0])


# 关闭浏览器
web.close()
