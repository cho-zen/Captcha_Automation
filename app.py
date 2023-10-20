import pytesseract
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import cv2
from PIL import Image

# Add your URL here
url = "https://playrep.pro/Login.mvc"

# Creating a webdriver instance
driver = webdriver.Chrome()

# Opening URL page
driver.get(url)

# Sleep time
time.sleep(2)

# Took the web page screenshot
driver.save_screenshot("ss.png")

# Save the screenshot in the director
# Load Image
img = cv2.cvtColor(cv2.imread('ss.png'),cv2.COLOR_BGR2RGB)

# plt.figure(figsize=(10,12))
# plt.imshow(img[450:490,460:600])
# Crop the image
img = img[450:490,460:600]

# Read text from image using OCR method via. pytesseract
img_text = pytesseract.image_to_string(img)
captcha = ''.join(img_text.split())

# Get Captcha text box ID
capt = driver.find_element(By.ID,"txtCaptcha")

# Enter Captcha Code
capt.send_keys(captcha)
