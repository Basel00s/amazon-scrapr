# 🛒 Amazon Product Scraper

A Python web scraper that automatically searches Amazon for products, extracts names and prices, and saves the results to a CSV file.

## 📋 About

Built to practice web scraping with Selenium and BeautifulSoup. The scraper searches for laptops on Amazon, collects the top 10 product links, visits each page, and exports the data.

## ✨ Features

- 🔍 Searches Amazon automatically using a keyword
- 🔗 Collects up to 10 unique product page links
- 💰 Extracts product name and price from each page
- 📄 Exports results to a CSV file (`amazon_laptops.csv`)
- 🛡️ User-agent spoofing to reduce bot detection
- ⚠️ Handles missing titles/prices gracefully without crashing

## 🛠️ Built With

- Python 3
- Selenium (browser automation)
- ChromeDriver
- CSV module

## 📦 Requirements

```bash
pip install selenium
```

Also make sure you have [ChromeDriver](https://chromedriver.chromium.org/) installed and matching your Chrome version.

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Basel00s/amazon-scrapr.git
   cd amazon-scrapr
   ```

2. Install dependencies:
   ```bash
   pip install selenium
   ```

3. Run the scraper:
   ```bash
   python pythonlib.py
   ```

4. Output will be saved to `amazon_laptops.csv`

## 📄 Sample Output

| Product Name | Price | URL |
|---|---|---|
| Lenovo IdeaPad 3... | $499.00 | https://amazon.com/dp/... |
| HP Pavilion 15... | $429.99 | https://amazon.com/dp/... |

## 📁 Project Structure

```
amazon-scrapr/
├── pythonlib.py     # Main scraper logic
├── networkxx.py     # Network/graph analysis
└── README.md
```

## ⚠️ Disclaimer

This project is for educational purposes only. Always check a website's Terms of Service before scraping.

## 📚 What I Learned

- Browser automation with Selenium
- CSS selectors for web scraping
- Handling dynamic content and bot detection
- Exporting structured data to CSV
- Error handling in real-world scraping scenarios# amazon-scrapr
