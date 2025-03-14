import tkinter as tk
from tkinter import Entry, Button, Label, Frame
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

def open_url():
    url = url_entry.get()
    if not url.startswith("http"):
        url = "https://" + url
    driver.get(url)

def go_back():
    if driver.current_url:
        driver.back()

def go_forward():
    if driver.current_url:
        driver.forward()

def refresh_page():
    driver.refresh()

def on_closing():
    print("Closing browser...")
    driver.quit()
    root.destroy()

# Create the main Tkinter window
root = tk.Tk()
root.title("P-BROWSER")

# Create a frame for the URL bar
url_frame = Frame(root)
url_frame.pack(fill="x", padx=5, pady=5)

# URL entry field
url_entry = Entry(url_frame, width=50)
url_entry.pack(side="left", expand=True, fill="x")

# Go button
go_button = Button(url_frame, text="Go", command=open_url)
go_button.pack(side="left")

# Navigation buttons
nav_frame = Frame(root)
nav_frame.pack(fill="x", padx=5, pady=5)

back_button = Button(nav_frame, text="Back", command=go_back)
back_button.pack(side="left")

forward_button = Button(nav_frame, text="Forward", command=go_forward)
forward_button.pack(side="left")

refresh_button = Button(nav_frame, text="Refresh", command=refresh_page)
refresh_button.pack(side="left")

# Bind the window close event
root.protocol("WM_DELETE_WINDOW", on_closing)

# Run the Tkinter event loop
root.mainloop()
