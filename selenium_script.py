from selenium import webdriver
import urllib
import io
import os
import hashlib
import requests
import time
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementNotVisibleException
)
from selenium.webdriver.support.ui import WebDriverWait



PATH = "C:\Program Files (x86)\chromedriver.exe"
IMAGES_PATH = "D:\projectmachinelearning\Skripsi\images"
driver = webdriver.Chrome(PATH)
inedible_img = ""



for x in range(15):

	driver.get("https://www.mushroom.world/mushrooms/poisonous?page=%d" % x)
	
	if x == 0:
		time.sleep(0.5)
		cookie = driver.find_element_by_xpath("//*[@id='cc_container']/button")
		cookie.click()
		time.sleep(5)
		gotit = driver.find_element_by_xpath("/html/body/div[4]/div/input[1]")
		gotit.click()
		
	page_image = driver.find_elements_by_tag_name('img')

	if page_image == []:		
		break

	try:
		while True:		
			images = driver.find_elements_by_tag_name('img')
			time.sleep(60)		
			for image in images:
				try:					
					singleimage = image.get_attribute('src')					
					print(f"downloading {singleimage}")
					imagecontent = requests.get(singleimage).content
					file_path = os.path.join(IMAGES_PATH, hashlib.sha1(imagecontent).hexdigest()[:10] + '.jpg')
					with open(file_path, 'wb') as f:
						f.write(imagecontent)
					print(f"Download {singleimage} completed")	
				except Exception as e:
					print(f"could not load image {singleimage}, {e}")
					driver.close()		
					raise e
			break

	except ElementNotVisibleException:
		driver.close()

print(f"operation complete")			
driver.close()	
	
			
			
	

	





	



