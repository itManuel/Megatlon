from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, sys, getopt

from datetime import datetime


# datos por defecto, se sobreescriben con parámetros de ser necesario
location = "Devoto"
day = "lun"
class_name = "MegaCross"
timing = "19:00"
user_mail = "usuariocansado@megatlon.com"
user_password =  "supersecurepassword"

arg = sys.argv[1:]
try:
    opts, args = getopt.getopt(arg,"h:u:p:t:c:d:",["help","user_mail","user_password","timing","class_name","day"])
except getopt.GetoptError:
    print('test.py -u <user> -p <passwd> -t <hora> -c <class name> -d <dia>')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print('test.py -u <user> -p <passwd> -t <hora> -c <class name> -d <dia>')
        sys.exit()
    elif opt in ("-u"):
        user_mail = arg
    elif opt in ("-p"):
        user_password = arg
    elif opt in ("-t"):
        timing = arg
    elif opt in ("-c"):
        class_name = arg
    elif opt in ("-d"):
        day = arg

#print(sys.argv[1:])
print('user=',user_mail)
print('pass=',user_password)
print('timing=',timing)
print('class_name=',class_name)
print('day=',day)

# aquí es según el gusto de c/u:
driver = webdriver.Chrome()
#driver = webdriver.Firefox()

driver.set_window_size (1920, 1080)
driver.get('https://megatlon.com/#/login')

time.sleep(2)

# User Mail
# user = driver.find_element_by_name('user')
user = driver.find_element(By.NAME, 'user')
user.send_keys(user_mail)

# Pass
# password = driver.find_element_by_name('password')
password = driver.find_element(By.NAME, 'password')
password.send_keys(user_password)

submit = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[4]/button')
submit.click()

time.sleep(2)

new_class = driver.find_element(By.XPATH, '//*[@id="menu"]/li[1]/a')
new_class.click()

time.sleep(2)

# Selecciono la sede a la que quiero ir
wait = WebDriverWait(driver, 15)

driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div[1]/div/div/div[2]/div').click()
wait.until(EC.visibility_of_element_located(
    (By.XPATH, '//*[contains(text(),"' + location + '")]'))).click()

time.sleep(2)

# Selecciono la clase que quiero reservar
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div[2]/div/div/div[2]/div').click()

wait.until(EC.visibility_of_element_located(
    (By.XPATH, '//*[contains(text(),"' + class_name + '")]'))).click()


time.sleep(469)
#time.sleep(2)

# Busco la clase que me interesa asistir
WebDriverWait(driver, 15).until(EC.visibility_of_element_located(
    (By.XPATH,
     '//div[contains(h6[1],"' + day + '") and contains(h5,"' + class_name + '") and contains(h6[2],"' + timing + '")]'))).click()

# clickeo el checkbox de 'no tengo covid' (Gracias Diego González por el xpath!!)
driver.find_element(By.XPATH, '/html/body/div[8]/div/div/div/div/div[3]/input').click()

now = datetime.now()

current_time = now.strftime("%Y-%m-%d %H:%M:%S")

# reservo
wait.until(EC.visibility_of_element_located(
    (By.XPATH, '//button[text()="Reservar"]'))).click()

#print(time.now())
print(current_time,': reservado ',class_name,' para el día ',day,' a las ',timing)
time.sleep(5)

driver.close()
