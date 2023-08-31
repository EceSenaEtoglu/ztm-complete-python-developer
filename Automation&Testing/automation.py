from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_browser = webdriver.Chrome()
chrome_browser.maximize_window()

chrome_browser.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")

# get HTML elements
entry1 = chrome_browser.find_element(By.CSS_SELECTOR,"#value1")
entry2 = chrome_browser.find_element(By.CSS_SELECTOR,"#value2")
button = chrome_browser.find_element(By.CSS_SELECTOR,"#gettotal > button")
output = chrome_browser.find_element(By.CSS_SELECTOR,"#displayvalue")

# clear entries
entry1.clear()
entry2.clear()

# init data
num1,num2 = 3,5
result = num1 + num2

# send data and click
entry1.send_keys(num1)
entry2.send_keys(num2)
button.click()

# test
assert output.text == str(result)


while True:
    pass
