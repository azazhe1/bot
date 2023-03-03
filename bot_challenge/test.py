from selenium import webdriver
from selenium.webdriver.common.by import By
import base64


def mot_de_pass():
    mdp_='cG9sdXg1MTI='
    mdp=base64.b64decode(mdp_)
    mdp = str(mdp)
    mdp=mdp.split('\'')
    return mdp[1]
 
def connect():
    driver = webdriver.Firefox()
    mdp=mot_de_pass()
    driver.get("https://sigee.ave-asso.fr/login")
    username = driver.find_element(By.XPATH, "//*[@id='loginBox']/div[2]/form/div[1]/input[1]")
    username.send_keys("jean.vinnccent@gmail.com")#mettre son login
    password = driver.find_element(By.XPATH, "//*[@id='loginBox']/div[2]/form/div[1]/input[2]")
    password.send_keys(mdp)#mettre son mdp
    login=driver.find_element(By.XPATH, "//*[@id='loginBox']/div[2]/form/div[2]/button")
    login.click()
    driver.get("https://sigee.ave-asso.fr/listSales?event=96#mark")
    html= driver.page_source
        
    table = driver.find_elements_by_class_name("page")
    entries = table.find_elements_by_tag_name("td")
    for i in range(20):
        header = entries[i].text
        print(header)
    

connect()