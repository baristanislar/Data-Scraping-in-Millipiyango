# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 15:47:21 2021

@author: baristanislar
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

#chromedriver.exe nin yerini belirliyoruz.
service = Service('D:\\Driver\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

#chrome u başlangıcta göstermez
#driver.set_window_position(-10000,0)

#girilecek siteyi buraya yazınız.
driver.get("https://www.millipiyangoonline.com/cekilis-sonuclari#sayisaloto")

#ayların seçimini sağlar (ocak=1)
aylar = Select(driver.find_element(By.ID, "draw-month"))
aylar.select_by_value("3")

#yılların seçimini sağlar
yillar = Select(driver.find_element(By.ID, "draw-year"))
yillar.select_by_value("2021")

#filtrele butonunu çalıştırır 
driver.find_element(By.XPATH, "//*[@id='draws']/div[2]/div[5]")
filtrele = driver.find_element(By.XPATH, "//*[@id='draws']/div[2]/div[5]/button")
filtrele.click()                         

try:
    #sayfadaki tüm çekiliş sayılarını çeker bu işlemleri sayfa açılınca 10 saniye sonra yapar.
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "tabs-container"))
    )
    
    main2 = main.find_element(By.CLASS_NAME, "tab-content")
    
    main3 = main2.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div")
    
    main4 = main3.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div/div[2]")
    
    main5 = main4.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div/div[2]/div")
    
    main6 = main5.find_element(By.CLASS_NAME, "list")
    
    main7 = main6.find_elements(By.CLASS_NAME, "row")
    
    #bulduğu tüm sayıları yazar.
    for row in main7:
        sayılar = row.find_element(By.CLASS_NAME, "numbers")
        print(sayılar.text)
            
finally:
    driver.quit()
