from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bt
import time

url = 'https://www.amazon.com/'
options = Options()
# 🛡️ TRICK 1: Add a User-Agent so we don't look like an empty Selenium bot
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# 🛡️ TRICK 2: Disable the "Chrome is being controlled by automated software" banner
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)
   
driver.get(url)
time.sleep(5) 
#try:
search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
search_box.send_keys('laptops' + Keys.RETURN) 
time.sleep(5)
laptops = driver.find_elements(By.CSS_SELECTOR, 'div[data-component-type="s-search-result"] h2 a')
links = laptops[0].get_attribute("href")
print(links)
# except:
#     print('try again')

driver.quit()