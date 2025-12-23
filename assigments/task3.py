import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import HtmlTestRunner


class MinecraftWikiTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_selenium_features(self):
        driver = self.driver

        driver.get("https://minecraft.wiki/")

        target_element = driver.find_element(By.NAME, "search")
        actions = ActionChains(driver)
        actions.move_to_element(target_element).perform()

        search_box = driver.find_element(By.NAME, "search")
        search_box.send_keys("Steve")

        wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
        suggestions = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cdx-menu")))

        # selector: AllPages
        driver.find_element(by=By.XPATH,
                            value='/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/ul/li[1]/span/b/a').click()


        dropdown_element = driver.find_element(By.XPATH, "//select[@name='namespace']")
        driver.execute_script("arguments[0].style.display = 'block';", dropdown_element)

        select = Select(dropdown_element)
        select.select_by_index(2)

        print("Select Class: Option selected successfully!")


        # Проверка
        self.assertTrue(dropdown_element.is_displayed())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_reports'))