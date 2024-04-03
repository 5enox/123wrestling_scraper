from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to the webpage
driver.get("https://www.google.com")

# Enable network logging
driver.execute_cdp_cmd("Network.enable", {})

# Retrieve network activity
network_activity = driver.execute_cdp_cmd(
    "Network.getAllInterceptedRequests", {})

# Print URLs of intercepted requests
for request in network_activity['requests']:
    print(request['request']['url'])

# Close the WebDriver
driver.quit()
