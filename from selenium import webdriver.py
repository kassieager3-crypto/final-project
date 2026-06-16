from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://atid.store")
title = driver.title
print(driver.current_url)
print("************* Step 1 **********************")
print(" ")
if title == "ATID Demo Store – ATID College Demo Store for Practicing QA Automation":
    print("Step 1 -  Title Passed")
    print(" ")
    print("**************************************")
else:
    print("Step 1 -  Title Failed")
    print(" ")
    print("**************************************")

driver.find_element(By.ID,'menu-item-829').click()
if driver.current_url == "https://atid.store/contact-us/":
    print(driver.current_url,"step  2 - url Passed")
    print(driver.current_url)
    print("**************************************")
else:
    print(driver.current_url, "step  2 - url Failed")
    print(driver.current_url)
    print("**************************************")

driver.find_element(By.ID,'wpforms-15-field_0').send_keys("Israel Mangisto")
driver.find_element(By.ID,'wpforms-15-field_5').send_keys("Test Contact Us Form")
driver.find_element(By.ID,'wpforms-15-field_4').send_keys("test@test.com")
driver.find_element(By.ID,'wpforms-15-field_2').send_keys("Contact Us Test valid")
driver.find_element(By.ID,'wpforms-submit-15').click()
textMessage = driver.find_element(By.XPATH,'//*[@id="wpforms-confirmation-15"]/p').text
if textMessage == "Thanks for contacting us! We will be in touch with you shortly.":
    print("Step 3 - Contact Us Form Sent  -  Passed")
    print(" ")
    print("**************************************")
else:
    print("Step 3 - Contact Us Form Sent  -  Failed")
    print(" ")
    print("**************************************") 