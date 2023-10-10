from selenium.webdriver.common.by import By
from POM.Base import Base
from selenium.webdriver.support.ui import Select


class HomePage(Base):
    search_box = (By.ID, 'twotabsearchtextbox')
    search_category = (By.ID, 'searchDropdownBox')
    search_button = (By.ID, 'nav-search-submit-button')

    def search_for(self, value):
        self.send_keys(*self.search_box, value)
        item = self.wait_element(*self.search_category)
        select = Select(item)
        select.select_by_visible_text('All Categories')
        self.click_element(*self.search_button)
