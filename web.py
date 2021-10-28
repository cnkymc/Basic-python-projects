from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/?hl=tr')
nickname= driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
nickname.send_keys('Your İnstagram Nickname')

password= driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys('Your İnstagram password')

loginButton=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
loginButton.click()