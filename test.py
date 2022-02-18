from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

location = "Devoto"
day = "mié"
day = "vie"
class_name = "Boxeo"
timing = "19:00"
user_mail = "usuario_cansado@megatlon.com"
user_password =  "password"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://megatlon.com/#/login')
#print(driver.page_source)

time.sleep(1)

# Log In
#Login = driver.find_element_by_xpath('//*[@id="menu"]/li[9]/a')
#Login = driver.find_element_by_xpath('/login')
#print(Login.page_source)
#Login.click()

# User Mail
user = driver.find_element_by_name('user')
user.send_keys(user_mail)

# Pass
password = driver.find_element_by_name('password')
print(password)
password.send_keys(user_password)

submit = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/form/div[4]/button')
submit.click()

time.sleep(5)

new_class = driver.find_element_by_xpath('//*[@id="menu"]/li[1]/a')
new_class.click()

time.sleep(5)

# Selecciono la sede a la que quiero ir
wait = WebDriverWait(driver, 15)

driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div/div/div[2]/div').click()
wait.until(EC.visibility_of_element_located(
    (By.XPATH, '//*[contains(text(),"' + location + '")]'))).click()

time.sleep(3)
#print(driver.page_source)

# Selecciono la clase que quiero reservar
#driver.find_element_by_xpath('.//div[contains(@class, "css-18zukxb-control") and contains(@class, "css-1uccc91-singleValue")]').click()
driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[2]/div/div/div[2]/div').click()

wait.until(EC.visibility_of_element_located(
    (By.XPATH, '//*[contains(text(),"' + class_name + '")]'))).click()

time.sleep(3)



# Busco la clase que me interesa asistir
WebDriverWait(driver, 15).until(EC.visibility_of_element_located(
    (By.XPATH,
     '//div[contains(h6[1],"' + day + '") and contains(h5,"' + class_name + '") and contains(h6[2],"' + timing + '")]'))).click()

print(driver.page_source)

# clickeo el checkbox de 'no tengo covid'
#driver.find_element_by_class_name('text-center').find_elements_by_class_name('checkbox').click()

WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.ReactModalPortal > div.'ReactModal__Overlay ReactModal__Overlay--after-open' > div.'ReactModal__Content ReactModal__Content--after-open top-0 bottom-0 w-4/5 m-auto bg-gray-100 outline-none md:w-1/3 rounded-xl' > div.p-4 > div.'flex flex-col flex-grow' > div.text-center > input.checkbox"))).click()

#driver.find_element_by_xpath('//*[contains(type(),"checkbox") and contains(text(),"test-center")]').click()
#wait.until(EC.visibility_of_element_located(
#    (By.XPATH, '//*[contains(text(),"checkbox"]'))).click()

# reservo
wait.until(EC.visibility_of_element_located(
    (By.XPATH, '//button[text()="Reservar"]'))).click()
#
#time.sleep(3)

#driver.close()
