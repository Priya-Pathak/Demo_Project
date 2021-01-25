# from selenium import webdriver
# import time
# import pandas as pandas





# from selenium import webdriver

# browser = webdriver.Firefox()
# browser.get('www.google.com')


# for i in range(1): 
#     matched_elements = browser.get("https://www.google.com/search?q=BTS") 


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox()
# driver.get("http://www.google.com/")

# #open tab
# driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
# # You can use (Keys.CONTROL + 't') on other OSs

# # Load a page 
# driver.get('http://stackoverflow.com/')
# # Make the tests...

# # close the tab
# # (Keys.CONTROL + 'w') on other OSs.
# driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 


# driver.close()

#Importing packages
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

# options = Options()
# ua = UserAgent()
# userAgent = ua.random
# print(UserAgent)
# options.add_argument('--disable-infobars')
# options.add_argument(f'user-agent={userAgent}')

# driver = webdriver.Chrome(chrome_options=options,executable_path=r'/usr/local/bin/chromedriver')

chrome_driver_path = "/usr/local/bin/chromedriver"
options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('--kiosk')
options.add_argument('--window-position=0,0')
options.add_argument('--disable-infobars')
options.add_argument('--window-size=1920,1080')
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=options)
# driver.get('https://forums.edmunds.com/discussion/2864/general/x/entry-level-luxury-performance-sedans/')

# driver.get('http://stackoverflow.com/')

#driver.get('https://www.google.com/search?q=bts&tbm=isch&ved=2ahUKEwjeyO2CoK_uAhW8Q30KHW11AvMQ2-cCegQIABAA&oq=bts&gs_lcp=CgNpbWcQAzIFCAAQsQMyBQgAELEDMgUIABCxAzICCAAyBQgAELEDMgUIABCxAzIFCAAQsQMyBQgAELEDMgUIABCxAzIFCAAQsQNQpgNYlQ1gsg9oAHAAeACAAb4DiAG-A5IBAzQtMZgBAKABAaoBC2d3cy13aXotaW1nsAEAwAEB&sclient=img&ei=7p0KYN6ZKryH9QPt6omYDw&bih=637&biw=1294')


# driver.get("http://google.com")
#driver.maximize_window()
#time.sleep(5)
# inputElement = driver.find_element_by_name("q")
# inputElement.send_keys("Amazon")
# inputElement.submit()
#time.sleep(5)
# elem = driver.find_element_by_partial_link_text("Amazon")
# print("element found")
# elem.click()
# elem1 = driver.find_element_by_name("field-keywords")
# elem1.send_keys("Realme 6")
# elem1.submit()
# elem1 = driver.find_element_by_partial_link_text("Realme 6")
# elem1.click()
#time.sleep(20)

driver.get("http://google.com")
inputElement = driver.find_element_by_name("q")
inputElement.send_keys("Flipkart")
inputElement.submit()
#time.sleep(5)
elem = driver.find_element_by_partial_link_text("Flipkart")
elem.click()
print("element found")

elem1 = driver.find_element_by_name("q")
elem1.send_keys("Realme6")
elem1.submit()

# elem1.click()
#driver.close()