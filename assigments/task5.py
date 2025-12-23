import unittest
import time
import logging
import os
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import HtmlTestRunner

# logger start
logger = logging.getLogger("MinecraftTest")
logger.setLevel(logging.INFO)

# log format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# handler for log report
file_handler = logging.FileHandler("automation_log.log", mode='w')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# handler for console log
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


class MinecraftWikiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logger.info("RUN TESTS")
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

    def setUp(self):
        logger.info("RUN CHROME BROWSER")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        logger.info("EXIT CHROME BROWSER")
        if self.driver:
            self.driver.quit()

    @classmethod
    def tearDownClass(cls):
       logger.info("FINISH THE TEST")

    def capture_screenshot(self, name):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshots/{name}_{timestamp}.png"
        self.driver.save_screenshot(filename)
        logger.info(f"SCREENSHOT SAVED {filename}")

    # tests
    def test_selenium_features(self):
        driver = self.driver

        try:
            logger.info("Step 1: Go to the Minecraft Wiki website")
            driver.get("https://minecraft.wiki/")

            target_element = driver.find_element(By.NAME, "search")
            actions = ActionChains(driver)
            actions.move_to_element(target_element).perform()
            logger.info("Action Chains: Successfully hovered over the search bar")

            # screenshot of Action Chains
            self.capture_screenshot("Step1_ActionChains")
            time.sleep(2)

            search_box = driver.find_element(By.NAME, "search")
            search_box.send_keys("Steve")
            logger.info("Entered 'Steve' into the search")
            time.sleep(1)

            wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
            suggestions = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cdx-menu")))

            logger.info("Explicit/Fluent Wait: Search suggestions are now available")
            self.capture_screenshot("Step2_ExplicitWait")
            time.sleep(2)

            logger.info("Step 3: Go to the Special:AllPages page for the Select test")
            driver.find_element(by=By.XPATH,
                                value='/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/ul/li[1]/span/b/a').click()
            time.sleep(2)

            dropdown_element = driver.find_element(By.XPATH, "//select[@name='namespace']")

            # JS hack for hiding element
            driver.execute_script("arguments[0].style.display = 'block';", dropdown_element)
            logger.info("JS Executor: Made select visible")
            time.sleep(1)


            select = Select(dropdown_element)
            select.select_by_index(2)
            logger.info("Select Class: Option (index 2) selected successfully")

            self.capture_screenshot("Step3_SelectClass")
            time.sleep(2)

            # test
            self.assertTrue(dropdown_element.is_displayed())
            logger.info("Assert: Element is visible, test passed successfully")

        except Exception as e:
            logger.error(f"The test failed with the error: {e}")
            self.capture_screenshot("TEST_FAILURE")
            raise e


if __name__ == "__main__":
    # generate html for test report
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='test_reports',
        report_name='Minecraft_Test_Report',
        combine_reports=True,
        add_timestamp=True
    ))