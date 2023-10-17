import pytesseract
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import cv2
from PIL import Image

# Add your URL here
url = "https://www.google.com"

# Creating a webdriver instance
driver = webdriver.Chrome()

# Opening URL page
driver.get(url)

# Sleep time
time.sleep(2)
