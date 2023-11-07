from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.n2yo.com/?s=25544")

#element = driver.find_element(By.XPATH, '//*[@id="tabsatellite"]')
#element = driver.find_element(By.ID, "div").text

latitude = driver.find_element(By.ID, "satlat").get_attribute
longitude = driver.find_element(By.ID, "satlng").get_attribute
print(latitude, longitude)

driver.close()



