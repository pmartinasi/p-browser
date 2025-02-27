from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Set up Firefox to run headlessly
options = Options()
options.headless = True  # Run in headless mode

# Initialize WebDriver with the geckodriver path
driver = webdriver.Firefox(executable_path='/path/to/geckodriver', options=options)

# Open a website
driver.get('https://www.mozilla.org')

# Print page title
print(driver.title)

# Close the browser
driver.quit()
