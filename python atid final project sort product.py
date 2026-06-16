from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://atid.store")
print("Successfully navigated to: " + driver.current_url)

print("************* Step 1: TC_Filter_01 - Verify 'Men' Category **********************")
driver.find_element(By.LINK_TEXT, "Store").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Men").click()
time.sleep(2)
page_header = driver.find_element(By.TAG_NAME, "h1").text
if "Men" in page_header:
    print("Step 1 - Filter 'Men' Passed: Header is '" + page_header + "'")
else:
    print("Step 1 - Filter 'Men' Failed: Header is '" + page_header + "'")
print("*******************************************************************************")

print("************* Step 2: TC_Filter_02 - Verify 'Women' Category ********************")
driver.find_element(By.LINK_TEXT, "Women").click()
time.sleep(2)
page_header = driver.find_element(By.TAG_NAME, "h1").text
if "Women" in page_header:
    print("Step 2 - Filter 'Women' Passed: Header is '" + page_header + "'")
else:
    print("Step 2 - Filter 'Women' Failed: Header is '" + page_header + "'")
print("*******************************************************************************")

print("************* Step 3: TC_Filter_03 - Verify 'Accessories' Category ***************")
driver.find_element(By.LINK_TEXT, "Accessories").click()
time.sleep(2)
page_header = driver.find_element(By.TAG_NAME, "h1").text
if "Accessories" in page_header:
    print("Step 3 - Filter 'Accessories' Passed: Header is '" + page_header + "'")
else:
    print("Step 3 - Filter 'Accessories' Failed: Header is '" + page_header + "'")
print("*******************************************************************************") 
driver.quit