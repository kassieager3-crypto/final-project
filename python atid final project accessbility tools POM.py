from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ("accessibility tools POM.PY") 
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://atid.store/store")
accessibility_page =(" AccessibilityPage")(driver) 
print("************* Running Accessibility Tests with Assertions *****************")
def test_image_alt_text():
    print("Testing TC_Access_01: Product Image Alt Attributes...")
    images = accessibility_page.get_all_product_images()
    
    for img in images:
        alt_value = img.get_attribute("alt")
        # Assert that the alt attribute exists and is not empty [6, 7]
        assert alt_value is not None and alt_value != "", f"Assertion Failed: Image {img.get_attribute('src')} is missing alt text!"
    
    print("TC_Access_01 - Passed: All images have descriptive alt text.")
def test_search_labels():
    print("\nTesting TC_Access_03: Search Input Accessibility Labels...")
    search_field = accessibility_page.get_search_field_element()
    
    aria_label = search_field.get_attribute("aria-label")
    placeholder = search_field.get_attribute("placeholder")
    assert aria_label or placeholder, "Assertion Failed: Search field lacks descriptive attributes (aria-label/placeholder)!"
    print(f"TC_Access_03 - Passed: Search field label found ({aria_label or placeholder}).")
def test_keyboard_navigation()
    print("\nTesting TC_Access_02: Keyboard Tab Navigation...")
    body = driver.find_element(webdriver.common.by.By.TAG_NAME, "body")
    body.send_keys(Keys.TAB)
    time.sleep(1)
    
    active_element = driver.switch_to.active_element
    tag_name = active_element.tag_name
    assert tag_name in ["a", "button", "input"], f"Assertion Failed: Focus is on non-interactable element: {tag_name}"
    print("TC_Access_02 - Passed: Keyboard focus successfully moved to an active link.")
try:
    test_image_alt_text()
    test_search_labels()
    test_keyboard_navigation()
    print("\n************* All Accessibility Tests Passed Successfully! ***************")
finally:
    driver.quit()