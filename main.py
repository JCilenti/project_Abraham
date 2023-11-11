import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')

def get_my_location():
    my_loc_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    my_loc_driver.get("https://www.n2yo.com/?s=33591")
    my_loc_lat = WebDriverWait(my_loc_driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tablelocation"]/tbody/tr[3]/td[2]/b')))
    my_loc_long = WebDriverWait(my_loc_driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tablelocation"]/tbody/tr[4]/td[2]/b')))
    print("- My Location Latitude: ", my_loc_lat.text)
    print("- My Location Longitude: ",my_loc_long.text)
    my_loc_driver.close()

def track_iss():
    iss_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    iss_driver.get("https://www.n2yo.com/?s=25544")
    iss_lat = WebDriverWait(iss_driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="satlat"]')))
    iss_long = WebDriverWait(iss_driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="satlng"]')))
    print("- ISS Latitude: ", iss_lat.text)
    print("- ISS Longitude: ",iss_long.text)
    iss_driver.close()

def track_noaa19():
    noaa19_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    noaa19_driver.get("https://www.n2yo.com/?s=33591")
    noaa19_lat = WebDriverWait(noaa19_driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="satlat"]')))
    noaa19_long = WebDriverWait(noaa19_driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="satlng"]')))
    print("- NOAA19 Latitude: ", noaa19_lat.text)
    print("- NOAA19 Longitude: ",noaa19_long.text)
    noaa19_driver.close()

if __name__ == "__main__":
    print("Current Available Satellites \n - ISS \n - NOAA19")
    print("-" * 50)

    print("[RETRIEVING CURRENT LOCATION DATA...] \n")
    time.sleep(5)
    os.system('clear')
    print("-" * 50)
    get_my_location()
    print(time.process_time())
    print("-" * 50)
    tracked_sat = input("Enter Satellite to Track: ")
    os.system('clear')
    if tracked_sat == "iss":
        print("[GETTING LOCATION DATA FOR THE ISS...]")
        time.sleep(5)
        os.system('clear')
        print("-" * 50)
        track_iss()
        print(time.process_time())
        print("-" * 50)
    elif tracked_sat == "noaa19":
        print("[GETTING LOCATION DATA FOR NOAA19...]")
        time.sleep(5)
        os.system('clear')
        print("-" * 50)
        track_noaa19()
        print(time.process_time())
        print("-" * 50)
    else:
        print("ERROR...Satellite Not Found!")


