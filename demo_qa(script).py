import utilities
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from faker import Faker

fake = Faker()

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")

driver.maximize_window()
wait = WebDriverWait(driver,3)
action = ActionChains(driver)

wait.until(EC.element_to_be_clickable((By.ID,"firstName"))).send_keys(fake.name())
driver.find_element(By.ID,"lastName").send_keys(fake.name())
driver.find_element(By.ID,"userEmail").send_keys(fake.email())
driver.find_element(By.ID,"userNumber").send_keys(fake.phone_number())
driver.find_element(By.ID,"currentAddress").send_keys(fake.address())
male = driver.find_element(By.XPATH,"//input[@value = 'Male']")
driver.execute_script("arguments[0].click();", male)

subject = driver.find_element(By.ID,"subjectsContainer")
action.send_keys_to_element(subject,"Maths").pause(1).send_keys(Keys.TAB).perform()

state = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[10]/div[2]/div/div/div[1]")
action.send_keys_to_element(state, "NCR").pause(1).send_keys(Keys.TAB).perform()

city = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[10]/div[3]")
action.send_keys_to_element(city, "delhi").pause(1).send_keys(Keys.TAB).perform()
driver.execute_script("arguments[0].click();", city)

driver.find_element(By.ID,"submit").click()