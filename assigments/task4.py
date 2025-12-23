import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        element = self.find_clickable(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.find_clickable(locator)
        element.clear()
        element.send_keys(text)

    def execute_script_click(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)


class TicketsHomePage(BasePage):
    URL = 'https://tickets.kz/'
    INPUT_DESTINATION = (By.XPATH, '//*[@id="app-main-search-form"]/div/div[2]/form/section/div[1]/div/div[1]/div[2]/label/input')
    DROPDOWN_CITY = (By.XPATH, '//*[@id="app-main-search-form"]/div/div[2]/form/section/div[1]/div/div[1]/div[2]/div/div/div/button')
    DATE_FIELD = (By.XPATH, '//*[@id="app-main-search-form"]/div/div[2]/form/section/div[1]/div/div[2]/div/div[1]/button')
    # locators of date time
    SPECIFIC_DATE = (By.XPATH, '//*[@id="app-main-search-form"]/div/div[2]/form/section/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[5]/button[3]')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="app-main-search-form"]/div/div[2]/form/aside/button')
    CHECKBOX_LABEL = (By.XPATH, '//*[@id="app-main-search-form"]/div/div[2]/form/section/div[2]/label')

    def open(self):
        self.driver.get(self.URL)
        assert "Tickets.kz" in self.driver.title
        print("The main page is open.")

    def search_flight(self, city_name):
        self.enter_text(self.INPUT_DESTINATION, city_name)
        time.sleep(1)
        self.click(self.DROPDOWN_CITY)
        self.click(self.DATE_FIELD)
        self.click(self.SPECIFIC_DATE)
        self.click(self.CHECKBOX_LABEL)
        self.click(self.SEARCH_BUTTON)
        print("The search has started.")

class SearchResultsPage(BasePage):
    BOOK_BUTTON = (By.CSS_SELECTOR, ".avia-flexible-tickets-results-submit button")

    def wait_and_refresh(self):
        print("Waiting for results to load (10 sec)...")
        time.sleep(10)
        print("Reloading page...")
        self.driver.refresh()
        time.sleep(20)

    def select_first_ticket(self):
        print("We are looking for the 'Book' button...")
        self.execute_script_click(self.BOOK_BUTTON)
        print("The 'Book' button has been clicked.")

class PassengerInfoPage(BasePage):
    # Локаторы полей ввода
    INPUT_NAME_1 = (By.XPATH, '//*[@id="app-avia"]/div/div[2]/section/div[4]/div/div[1]/div[3]/div/div/input')
    INPUT_NAME_2 = (By.XPATH, '//*[@id="app-avia"]/div/div[2]/section/div[4]/div/div[1]/div[4]/div/div/input')

    def fill_passengers(self, name1, name2):
        print("Filling in passenger details...")
        time.sleep(20)
        self.enter_text(self.INPUT_NAME_1, name1)
        self.enter_text(self.INPUT_NAME_2, name2)
        print("The data has been entered.")


def test_booking_process():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        home_page = TicketsHomePage(driver)
        results_page = SearchResultsPage(driver)
        passenger_page = PassengerInfoPage(driver)

        home_page.open()
        home_page.search_flight("Шымкент")

        results_page.wait_and_refresh()
        results_page.select_first_ticket()

        passenger_page.fill_passengers("Kolbai", "Nurdaulet")

        print("Test passed successfully!")
        time.sleep(5)

    except Exception as e:
        print(f"Error during test: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_booking_process()