from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import requests

# Set up Selenium WebDriver
service = Service('chromedriver')
options = Options()
options.headless = True  # To run Chrome in headless mode
driver = webdriver.Chrome(service=service, options=options,)

# Open Google
driver.get("https://www.google.com")

# Get all network requests
logs = driver.get_log('performance')
requests_list = []

for entry in logs:
    try:
        request = entry['message']['params']['request']
        url = request['url']
        requests_list.append(url)
    except KeyError:
        pass

# Print all URLs
for url in requests_list:
    print(url)

# Quit the driver
driver.quit()
