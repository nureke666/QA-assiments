import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://tickets.kz/')
    time.sleep(5)

    assert "Tickets.kz" in driver.title
    print("Title Checkpoint passed!")

    text_box_to = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="app-main-search-form"]/div/div[2]/form/section/div[1]/div/div[1]/div[2]/label/input'))
    )
    text_box_to.send_keys('Шымкент')
    time.sleep(2)

    # city again
    driver.find_element(by=By.XPATH,
                        value='//*[@id="app-main-search-form"]/div/div[2]/form/section/div[1]/div/div[1]/div[2]/div/div/div/button').click()
    time.sleep(2)

    # data
    driver.find_element(by=By.XPATH,
                        value='//*[@id="app-main-search-form"]/div/div[2]/form/section/div[1]/div/div[2]/div/div[1]/button').click()
    time.sleep(2)

    # exact data in modal
    driver.find_element(by=By.XPATH,
                        value='//*[@id="app-main-search-form"]/div/div[2]/form/section/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[5]/button[3]').click()
    time.sleep(2)

    driver.find_element(by=By.XPATH, value='//*[@id="app-main-search-form"]/div/div[2]/form/section/div[2]/label').click()

    # button search
    driver.find_element(by=By.XPATH, value='//*[@id="app-main-search-form"]/div/div[2]/form/aside/button').click()
    time.sleep(1)
    driver.refresh()
    time.sleep(10)

    # book button
    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".avia-flexible-tickets-results-submit button"))
    )
    driver.execute_script("arguments[0].click();", button)
    time.sleep(15)

    # passenger data
    data = {
        'Kolbai': '//*[@id="app-avia"]/div/div[2]/section/div[4]/div/div[1]/div[3]/div/div/input',
        'Nurdaulet': '//*[@id="app-avia"]/div/div[2]/section/div[4]/div/div[1]/div[4]/div/div/input'
    }

    for name, xpath in data.items():
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        input_field.send_keys(name)

    time.sleep(5)

except Exception as e:
    print(e)

finally:
    driver.quit()