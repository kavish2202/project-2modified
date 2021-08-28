from selenium import webdriver
from getpass import getpass

username = input("Enter username: ")
password = getpass("Enter your password: ")

driver = webdriver.Chrome("C:\\Users\\akoda\\Desktop\\Python\\project 102\\chromedriver.exe")
driver.get("https://github.com/login")

username_textbox = driver.find_element_by_id("login_field")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id("password")
password_textbox.send_keys(password)

#login_button = driver.find_element_by_tag_name(xpath)
#login_button.submit()


elem = driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]')
elem.click()
