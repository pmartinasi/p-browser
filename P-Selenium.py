import tkinter as tk
from tkinter import Entry, Button, Frame
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

# Ruta manual de GeckoDriver
GECKODRIVER_PATH = "geckodriver.exe"

# Configurar opciones de Firefox
options = Options()
options.headless = False  # Ejecutar en modo visible

# Configurar el servicio con GeckoDriver manual
service = Service(GECKODRIVER_PATH)
driver = webdriver.Firefox(service=service, options=options)

def open_url():
    url = url_entry.get()
    if not url.startswith("http"):
        url = "https://" + url
    driver.get(url)

def go_back():
    driver.back()

def go_forward():
    driver.forward()

def refresh_page():
    driver.refresh()

def on_closing():
    print("Closing browser...")
    driver.quit()
    root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("P-BROWSER")

# Crear un frame para la barra de URL
url_frame = Frame(root)
url_frame.pack(fill="x", padx=5, pady=5)

# Campo de entrada de URL
url_entry = Entry(url_frame, width=50)
url_entry.pack(side="left", expand=True, fill="x")

# Botón para ir a la URL
go_button = Button(url_frame, text="Go", command=open_url)
go_button.pack(side="left")

# Crear un frame para los botones de navegación
nav_frame = Frame(root)
nav_frame.pack(fill="x", padx=5, pady=5)

back_button = Button(nav_frame, text="Back", command=go_back)
back_button.pack(side="left")

forward_button = Button(nav_frame, text="Forward", command=go_forward)
forward_button.pack(side="left")

refresh_button = Button(nav_frame, text="Refresh", command=refresh_page)
refresh_button.pack(side="left")

# Vincular el evento de cierre de la ventana
root.protocol("WM_DELETE_WINDOW", on_closing)

# Ejecutar el bucle de eventos de Tkinter
root.mainloop()