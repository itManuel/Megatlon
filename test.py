from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

location = "Devoto"
day = "mar"
class_name = "MegaCross"
timing = "19:00"
user_mail = "usuario_cansado@megatlon.com"
user_password =  "password"

# aquí es según el gusto de c/u:
driver = webdriver.Chrome()
#driver = webdriver.Firefox()

driver.maximize_window()
driver.get('https://megatlon.com/#/login')

time.sleep(2)

# User Mail
user = driver.find_element_by_name('user')
user.send_keys(user_mail)

# Pass
password = driver.find_element_by_name('password')
password.send_keys(user_password)

submit = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/form/div[4]/button')
submit.click()

time.sleep(2)

new_class = driver.find_element_by_xpath('//*[@id="menu"]/li[1]/a')
new_class.click()

time.sleep(2)

# Selecciono la sede a la que quiero ir
wait = WebDriverWait(driver, 15)

driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div/div/div[2]/div').click()
wait.until(EC.visibility_of_element_located(
    (By.XPATH, '//*[contains(text(),"' + location + '")]'))).click()

time.sleep(2)

# Selecciono la clase que quiero reservar
driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[2]/div/div/div[2]/div').click()

wait.until(EC.visibility_of_element_located(
    (By.XPATH, '//*[contains(text(),"' + class_name + '")]'))).click()

time.sleep(2)

# Busco la clase que me interesa asistir
WebDriverWait(driver, 15).until(EC.visibility_of_element_located(
    (By.XPATH,
     '//div[contains(h6[1],"' + day + '") and contains(h5,"' + class_name + '") and contains(h6[2],"' + timing + '")]'))).click()

# clickeo el checkbox de 'no tengo covid' (Gracias Diego González por el xpath!!)
driver.find_element_by_xpath('/html/body/div[8]/div/div/div/div/div[3]/input').click()

# reservo
wait.until(EC.visibility_of_element_located(
    (By.XPATH, '//button[text()="Reservar"]'))).click()

time.sleep(2)

#cierro
driver.close()
