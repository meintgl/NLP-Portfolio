from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pickle
import time

# Live updates the TFT champions, and puts them into a dictionary

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
DRIVER_PATH = "./chromedriver.exe"
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://www.metatft.com/units")
time.sleep(2)
xpath = "/html/body/div/div/div[2]/div[1]/div/div[2]/div/div[3]/figure/table/tbody/tr"
champdict = {}
for x in range(1, 61):
    line = driver.find_element(By.XPATH, xpath + "[" + str(x) + "]").text
    linearr = line.split('\n')
    print(linearr)
    champdict[linearr[0]] = linearr[1:]
print(champdict)
print(len(champdict))
driver.quit()
pickle.dump(champdict, open('champs.p', 'wb'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
