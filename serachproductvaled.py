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

driver.find_element(By.XPATH,'//*[@id="menu-item-671"]/a').click()
if driver.current_url == "https://atid.store/product-category/accessories/":
    print(driver.current_url,"step  2 - url Passed")
    print(driver.current_url)
    print("**************************************")
else:
    print(driver.current_url, "step  2 - url Failed")
    print(driver.current_url)
    print("**************************************")


driver.find_element(By.XPATH,'//*[@id="wc-block-search__input-1"]').send_keys("Anchor Bracelet")
driver.find_element(By.XPATH,'//*[@id="block-7"]/div/form/div/button').click()
if driver.current_url == "https://atid.store/product/anchor-bracelet/":
    print(driver.current_url,"step  3 - url Passed")
    print(driver.current_url)
    print("**************************************")
else:    
    print(driver.current_url, "step  3 - url Failed")
    print(driver.current_url)
    print("**************************************")
    productName = driver.find_element(By.XPATH,'//*[@id="product-160"]/div[2]/h1').text
if productName == "Anchor Bracelet":
    print("Step 4 - Product Name Passed")
    print(" ")
    print("**************************************")
else:
    print("Step 4 - Product Name Failed")
    print(" ")
    print("**************************************") 

productPath = driver.find_element(By.XPATH,'//*[@id="product-160"]/div[2]/nav').text
if productPath == "Home / Accessories / Anchor Bracelet":
    print("Step 5 - Product Path Passed")
    print(" ")
    print("**************************************") 
else:
    print("Step 5 - Product Path Failed")
    print(" ")
    print("**************************************")