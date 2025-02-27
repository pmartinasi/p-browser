from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Set up Firefox to run headlessly
options = Options()
options.headless = True  # Run in headless mode

# Use the GeckoDriverManager to automatically download and set up geckodriver
service = Service(GeckoDriverManager().install())

# Initialize WebDriver with the service object
driver = webdriver.Firefox(service=service, options=options)

# Open a website
driver.get('https://www.mozilla.org')

# Print page title
print(driver.title)

# Close the browser
driver.quit()
