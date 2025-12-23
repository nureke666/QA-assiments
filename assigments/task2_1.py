import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

url = 'https://www.youtube.com/?themeRefresh=1'
text_for_search = 'marlow highlight'

try:
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(5)

    # input_text
    text_box = driver.find_element(by=By.XPATH, value='//*[@id="center"]/yt-searchbox/div[1]/form/input')
    text_box.send_keys(text_for_search)
    time.sleep(2)

    # search button
    search_button = driver.find_element(by=By.XPATH, value='//*[@id="center"]/yt-searchbox/button')
    search_button.click()
    time.sleep(5)

    # first element after search
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value='ytd-video-renderer.ytd-item-section-renderer:nth-child(1) > div:nth-child(1)')
    submit_button.click()
    time.sleep(60)

except Exception as e:
    print(e)

finally:
    driver.quit()


