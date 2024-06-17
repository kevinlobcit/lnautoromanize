from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

import cutlet

import os

#setup translate
katsu = cutlet.Cutlet()

#how to translate use -> tlline = translator.translate(line, dest="en", src="ko")
url = "https://www.lyrical-nonsense.com/lyrics/endorfin/suisai-no-canary/"


#-----------------------------------
#setting up Selenium
dir_path = os.getcwd()
#add option to show the chrome window
options = Options()
options.add_experimental_option("detach", True)

#keep cookies #only works on windows
options.add_argument(f'user-data-dir={dir_path}/selenium')

#start the driver
#windows
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(0) #wait infinitely

#go to the site with the lyrics
driver.get(url)
#-----------------------------------

titleele = driver.find_element(By.CLASS_NAME, "titletext")
title = titleele.get_attribute("innerText").split()[0]

#get the p tags 
ptags = driver.find_elements("xpath", "//div[contains(@id, 'PriLyr')]/p")

fullroma = ""

for p in ptags:
    rawjptext = p.get_attribute("innerText")
    lines = rawjptext.split("\n")
    for line in lines:
        romantext = katsu.romaji(line)
        fullroma += romantext + "\n"
    fullroma += "\n"

driver.close()
 
print(fullroma)
    
filename = title+".txt"
completepath = os.path.join(dir_path+"\\songs\\", filename)
with open(completepath, "w") as f:
    f.write(fullroma)
