import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
try:
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://minecraft.wiki/')
    time.sleep(5)

    # login button
    driver.find_element(by=By.XPATH, value='//*[@id="pt-login"]/a').click()

    # login and password
    text_box_login = driver.find_element(by=By.XPATH, value='//*[@id="wpName1"]')
    text_box_login.send_keys('helper001')
    text_box_password = driver.find_element(by=By.XPATH, value='//*[@id="wpPassword1"]')
    text_box_password.send_keys('helper001@')

    # log in buton
    driver.find_element(by=By.XPATH, value='//*[@id="wpLoginAttempt"]').click()
    time.sleep(5)

    # search
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value='.cdx-button')
    submit_button.click()
    time.sleep(2)

    # log out
    driver.find_element(by=By.XPATH, value='//*[@id="pt-logout"]/a').click()
    time.sleep(5)

except Exception as e:
    print(e)

finally:
    driver.quit()


