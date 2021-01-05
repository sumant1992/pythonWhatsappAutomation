from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
import csv;

lst = []

with open('WthatsApp.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        lst.append(f'"{row[0]}"')

print(lst)

string = "Hi,Message sent using Python!!!";

for user in lst:
    x_arg = '//span[contains(@title,' + user + ')]'
    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    group_title.click()
    inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
    inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1);

print("sent sucessfully")
driver.close()
