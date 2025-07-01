import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options



chromedriver_autoinstaller.install()

def abrir_site():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1200,1000)
    driver.get("http://books.toscrape.com/")
    return driver