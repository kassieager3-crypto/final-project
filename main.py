c = -4
a = 5
d= "group"
if a > c > 0 and  c == d:
   print("ok")
   print("GOOD")
   print("SAME") 
else:
   print("NOT")
   print("NOPE")
   print("DIFFERENT")  
    # type: ignore
citizen = input ("are you a iserali citizen? (YES/NO): "). lower()
if citizen == "YES" or citizen == "Y" or citizen == "y":
   age = int (input("please inter your age ")) 
   if age >= 65:
      print ("you are eligible for the discount.")
   else:
      print ("you are not eligible for the discount")
else:
   print("only israli citizens are eligible for the discount")

    # type: ignore

    
city = input ("please enter your city:")
if city == "tel-aviv":
    input ("please enter the total hours worked this month:")
    basic_salary = 25 * 9
    if 9<= " hours worked" <=12:
         bonus = 1000
         print("total salary , including bonus:")
    else: 
      print("total salary with out bonus:")

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://atid.store&quot;)
title = driver.title
if title == "ATID Demo Store – ATID College Demo Store for Practicing QA Automation":
print("step titile Passed")
else:
print("step titile Failed")

# driver.find_element(by=By.XPATH,value="/html/body/div/header/div[1]/div[1]/div/div/div/div[2]/div/div/div/nav/div/ul/li[2]/a").click()
driver.find_element(By.XPATH,"/html/body/div/header/div[1]/div[1]/div/div/div/div[2]/div/div/div/nav/div/ul/li[2]/a").click()
# driver.find_element(By.XPATH,'//*[@id="menu-item-828"]/a')
if driver.current_url == 'https://atid.store/store/&#39;:
print(driver.current_url,"step url Passed")
else:
print(driver.current_url, "step url Failed")
   

      
      
    

   
 










 