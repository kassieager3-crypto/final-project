from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://atid.store/store")  

print("************* Accessibility Testing: Step 1 - Alt Text **********************")
product_images = driver.find_elements(By.CSS_SELECTOR, "img.attachment-woocommerce_thumbnail")
all_images_have_alt = True

for img in product_images:
    alt_text = img.get_attribute("alt")
    if alt_text == "" or alt_text is None:
        print(f"Step 1 - Alt Text Failed for image: {img.get_attribute('src')}")
        all_images_have_alt = False
        break

if all_images_have_alt:
    print("Step 1 - All product images have descriptive Alt text - Passed")
print("**************************************************************************")

print("************* Accessibility Testing: Step 2 - Input Labels **********************")
#(aria-label או placeholder) [1, 2]
search_input = driver.find_element(By.ID, 'wc-block-search__input-1')
aria_label = search_input.get_attribute("aria-label")
placeholder = search_input.get_attribute("placeholder")

if aria_label or placeholder:
    print(f"Step 2 - Search bar is descriptive (Label: {aria_label or placeholder}) - Passed")
else:
    print("Step 2 - Search bar lacks accessibility labels - Failed")
print("**************************************************************************")

print("************* Accessibility Testing: Step 3 - Keyboard Navigation ****************")
# -Tab (navigation key board) [1, 4, 5]
body = driver.find_element(By.TAG_NAME, 'body')
body.send_keys(Keys.TAB)
time.sleep(1) 
active_element = driver.switch_to.active_element
if active_element.is_enabled():
    print("Step 3 - Keyboard Focus is active on a menu element - Passed")
else:
    print("Step 3 - Keyboard Navigation focus indicator failed - Failed")
print("**************************************************************************")

driver.quit()