from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service('C:/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.set_window_size(1345, 728)
driver.get("https://elementy.ru/")
driver.find_element(By.ID, "pgbody").click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="pgbody"]/div/div[3]/div[1]/div/div[2]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="pgbody"]/div[2]/div[2]/div[2]/div[3]/div[1]/div[3]/span[2]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="forum_btm_btn"]').click()
time.sleep(2)
driver.find_element(By.ID, "forum_login").send_keys("borisovameggi")
time.sleep(2)
driver.find_element(By.NAME, "PASSWD").send_keys("dd130558")
time.sleep(2)
driver.find_element(By.ID, "rpw_chk").click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="forum_input_block"]/div[2]/div/form/input[4]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="forum_input_textarea"]').send_keys("Очень интересный вопрос)")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="forum_input_block"]/form/div[3]/input').click()
time.sleep(2)
