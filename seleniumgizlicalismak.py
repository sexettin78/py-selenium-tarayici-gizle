from selenium import webdriver
import time

from selenium.webdriver.firefox import options

#BU KODLARI YAZMAN GEREKİYOR 
ayarlar = webdriver.ChromeOptions()
ayarlar.headless = True

driver_path = "C:\\Users\\PC\\Downloads\\chromedriver.exe"
#AYRICA options=ayarlar ŞEKLİNDE YAZI EKLEMEN LAZIM.
browser = webdriver.Chrome(options=ayarlar,executable_path=driver_path)

browser.get("http://ipchat.rf.gd/")
time.sleep(7)
yazi = browser.find_element_by_xpath("/html/body/form/input")
yazi.send_keys("SELENYUM TEST")
time.sleep(2)
browser.find_element_by_xpath("/html/body/form/button").click()




