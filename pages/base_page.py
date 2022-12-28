from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://b2c.passport.rt.ru'

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def get_current_link(self):
        return self.driver.current_url

    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Not found {locator}')

    def get_page_source(self):
        """ Returns current page body. """

        source = ''
        try:
            source = self.driver.page_source
        except:
            print('Can not get page source')

        return source

    def screenshot(self, file_name='screenshot.png'):
        self.driver.save_screenshot(file_name)