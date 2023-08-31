from selenium import webdriver
from selenium.webdriver.common.by import By

# dont include path in version selenium4+
# (see selenium task manager)
chrome_browser = webdriver.Chrome()

chrome_browser.maximize_window()
chrome_browser.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")

assert "Selenium Easy Demo" in chrome_browser.title

button = chrome_browser.find_element(By.CLASS_NAME, "btn-primary")

txt = button.get_attribute("innerHTML")  # returns the text in HTML
assert txt in chrome_browser.page_source

user_message_field = chrome_browser.find_element(By.ID, "user-message")  #button2 = chrome_browser.find_element(By.CSS_SELECTOR,"#user-message > btn-primary")

user_message_field.clear() # clean text

user_message_field.send_keys("Writing through selenium....") # enter input

button.click()

output_message = chrome_browser.find_element(By.ID,"display")
assert "Writing through selenium...." == output_message.text


# selenium closes as soon as script is over
# code to run the script
while True:
    pass
