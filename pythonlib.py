from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

def main():
    print(" Starting the scraper...")
    
    
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get('https://www.amazon.com/')
        time.sleep(3)
        
        search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
        search_box.send_keys("laptops" + Keys.RETURN)
        time.sleep(4)
        
        
        link_elements = driver.find_elements(By.CSS_SELECTOR, 'a.a-link-normal.s-no-outline')
        product_links = []
        
        for element in link_elements:
            href = element.get_attribute('href')
            
            if href and '/dp/' in href:
                clean_link = href.split('?')[0]
                if clean_link not in product_links and len(product_links) < 10:
                    product_links.append(clean_link)
        
        
        with open("amazon_laptops.csv", mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Product Name', 'Price', 'URL'])
            
            for url in product_links:
                driver.get(url)
                time.sleep(3) 
                
                
                try:
                    title = driver.find_element(By.ID, 'productTitle').text.strip()
                except:
                    title = "Title not found"
                    
                
                try:
                    price = driver.find_element(By.CSS_SELECTOR, 'span.a-price span.a-offscreen').get_attribute("textContent").strip()
                except:
                    price = "Price not found"
                
                
                writer.writerow([title, price, url])
                print(f" Scraped: {title[:30]}...")

        print(" Successfully saved 10 laptops to amazon_laptops.csv!")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()