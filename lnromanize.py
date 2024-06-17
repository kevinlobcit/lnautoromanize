from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

from googletrans import Translator

import os

#setup translate
translator = Translator()

#how to translate use -> tlline = translator.translate(line, dest="en", src="ko")

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
driver.get("https://www.lyrical-nonsense.com/lyrics/endorfin/suisai-no-canary/")
#-----------------------------------

#get the p tags 
ptags = driver.find_elements("xpath", "//div[contains(@id, 'PriLyr')]/p")


for p in ptags:
    rawjptext = p.get_attribute("innerText"))
    romantext = translator.romanizeText("jp", "rawjptext")
    print(rawjptext)
    print()
    