import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

# 对于URL，需要处理后才能访问
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--allow-running-insecure-content")

# 创建Chrome浏览器实例，并打开URL
driver = webdriver.Chrome(options=options)
url = "http://100.69.72.15:8080/cas/main/alarmMng"


# with open('cookies.pkl', 'rb') as f:
#     cookies = pickle.load(f)
#     for cookie in cookies:
#         driver.add_cookie(cookie)

driver.get(url)



# 等待页面加载完成
time.sleep(3)
#
# 输入用户名和密码
username = driver.find_element('name', "name")
password = driver.find_element('name', "password")
username.send_keys("admin")
password.send_keys("Unicloud@123!")

# 等待页面加载完成


# # 自动识别验证码并输入答案
# captcha = driver.find_element_by_xpath("//input[@name='captcha']")
# captcha_img = driver.find_element_by_xpath("//img[@id='captchaImg']")
# captcha_img.screenshot("captcha.png")
# # 这里需要调用自动识别验证码的函数，将识别结果填入下面的变量中
# captcha_answer = "1234"
# captcha.send_keys(captcha_answer)
#
# 等待页面加载完成


# 点击登录按钮
submit = driver.find_element('id', "loginId")
submit.click()
# element = driver.find_element(By.XPATH, '//*[@id="accordion"]/li[6]')
# element.click()



# #
# # 等待页面加载完成
# time.sleep(5)
#
# 截图并保存
driver.save_screenshot("screenshot.png")
#
# # 退出浏览器
driver.quit()