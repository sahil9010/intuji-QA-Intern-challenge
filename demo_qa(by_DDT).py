import utilities
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.maximize_window()
wait = WebDriverWait(driver,3)

path = "C:/Users\ACER\Desktop\intern\intern_xml.xlsx"

rows = utilities.get_row_count(path,'Sheet1')
action = ActionChains(driver)

for r in range(2,rows+1):
    try:
        driver.get("https://demoqa.com/automation-practice-form")
        driver.find_element(By.XPATH, "//span[text() = 'Practice Form']").click()
        F_N = utilities.readdata(path,"Sheet1",r,1)
        L_N = utilities.readdata(path,"Sheet1",r,2)
        E_mail = utilities.readdata(path, "Sheet1", r, 3)
        Mob_num = utilities.readdata(path,"Sheet1",r,4)
        address = utilities.readdata(path,"Sheet1",r,5)

        wait.until(EC.element_to_be_clickable((By.ID,"firstName"))).send_keys(F_N)
        driver.find_element(By.ID,"lastName").send_keys(L_N)
        driver.find_element(By.ID,"userEmail").send_keys(E_mail)
        driver.find_element(By.ID,"userNumber").send_keys(Mob_num)
        driver.find_element(By.ID,"currentAddress").send_keys(address)

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



        acrt = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text() = 'Thanks for submitting the form']")))
        if "Thanks for submitting the form" in acrt.text:
            print("test is pass")
            utilities.writedata(path,"Sheet1",r,6,"test passed")

        else:

            print("test failed")
            utilities.writedata(path, "Sheet1", r, 6, "test failed")
    except Exception as e:
        print("t",(e))

        print("test failed ")
        utilities.writedata(path, "Sheet1", r, 6, "test failed")
        continue

    print("test complete")

