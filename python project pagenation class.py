from selenium.webdriver.common.by import By

class AccessibilityPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_images = (By.CSS_SELECTOR, "img") 
        self.search_input = (By.ID, "wc-block-search__input-1")  
        self.main_nav_menu = (By.TAG_NAME, "nav") 
        self.accessibility_toolbar = (By.CSS_SELECTOR, ".pojo-a11y-toolbar-toggle")
    def get_all_product_images(self):
        """מחזירה את כל התמונות בדף לצורך בדיקת מאפיין alt [8, 10]"""
        return self.driver.find_elements(*self.product_images)

    def get_search_field_attributes(self):
        """מחזירה את שדה החיפוש לבדיקת aria-label או placeholder [10, 11]"""
        return self.driver.find_element(*self.search_input)

    def get_navigation_menu_element(self):
        return self.driver.find_element(*self.main_nav_menu)
