import tkinter as tk
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Set up Firefox options
options = Options()
options.headless = False  # Run in visible mode to allow user interaction

# Set up the WebDriver
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)

# Open a website
driver.get('https://www.mozilla.org')

# Create a simple Tkinter window to handle close events
root = tk.Tk()
root.title("WebDriver Controller")

def on_closing():
    """Handles the window close event."""
    print("Closing browser...")
    driver.quit()
    root.destroy()

# Bind the window close event
root.protocol("WM_DELETE_WINDOW", on_closing)

# Run the Tkinter event loop
root.mainloop()
