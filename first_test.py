from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome
driver.maximize_window()
driver.get("https://atid.store")
title = driver.title
print("******* step 1 *********")
print("")
if title == "ATID Demo Store – ATID College Demo Store for Practicing QA Automation":
  print("step 1 _ Title passed")
  print("")
  print("**************")
  print("step 1 titile Passed")
else:
  print("")
  print("**************")
  print("step 1 titile Failed")
driver.find_element(by=By.XPATH,value="/html/body/div/header/div[1]/div[1]/div/div/div/div[2]/div/div/div/nav/div/ul/li[2]/a").click()

driver.find_element(By.XPATH,"/html/body/div/header/div[1]/div[1]/div/div/div/div[2]/div/div/div/nav/div/ul/li[2]/a").click()
driver.find_element(By.XPATH,"/html/body/div/header/div[1]/div/div/div/")
if driver.current_url == "https://atid.store/product/anchor-bracelet":
 print(driver.current_url,"step url Passed")
else:
 print(driver.current_url, "step url failed")