from selenium.webdriver.common.by import By

class AccessibilityPage:
    def __init__(self, driver):
        self.driver = driver
        # הגדרת Locators (מזהי אלמנטים) לפי דרישות הנגישות [4, 5]
        self.product_images = (By.CSS_SELECTOR, "img") # לזיהוי כל התמונות ובדיקת Alt Text [10, 11]
        self.search_input = (By.ID, "wc-block-search__input-1") # שדה החיפוש לבדיקת תיוג [10]
        self.main_nav_menu = (By.TAG_NAME, "nav") # תפריט הניווט לבדיקת HTML סמנטי [11]
        self.accessibility_toolbar = (By.CSS_SELECTOR, ".pojo-a11y-toolbar-toggle") # סרגל הנגישות (אם קיים) [12]

    # פונקציות לביצוע פעולות ושליפת נתונים [4, 13]

    def get_all_product_images(self):
        """מחזירה את כל התמונות בדף לצורך בדיקת מאפיין alt [8, 10]"""
        return self.driver.find_elements(*self.product_images)

    def get_search_field_attributes(self):
        """מחזירה את שדה החיפוש לבדיקת aria-label או placeholder [10, 11]"""
        return self.driver.find_element(*self.search_input)

    def get_navigation_menu_element(self):
        """שולפת את רכיב התפריט הראשי לבדיקת נגישות מקלדת [10, 11]"""
        return self.driver.find_element(*self.main_nav_menu)