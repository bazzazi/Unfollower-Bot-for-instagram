# Import libraries
from selenium import webdriver
import time

# Instialize driver and path to chrome driver location
driver = webdriver.Chrome("chromedriver")

# Get insta site
driver.get("https://www.instagram.com/")

time.sleep(5)


# Import info.py (which includes your username and password)
import info
username = info.USERNAME

password = info.PASSWORD

# Entering username and password to fields
driver.find_element_by_xpath("""//*[@id="loginForm"]/div/div[1]/div/label/input""").send_keys(username)
driver.find_element_by_xpath("""//*[@id="loginForm"]/div/div[2]/div/label/input""").send_keys(password)

# Press Login Button
driver.find_element_by_xpath("""//*[@id="loginForm"]/div/div[3]/button/div""").click()

time.sleep(15)


# Get your insta account
driver.get("https://www.instagram.com/your account name")

# Click on following link
driver.find_element_by_partial_link_text("following").click()

time.sleep(5)


# Unfollow 20 people
for i in range(0,20):
    # Click on Following Button
    driver.find_element_by_xpath(f"//button[text()='Following']").click()
    # Click on Unfollow Button
    driver.find_element_by_xpath("//button[text()='Unfollow']").click()

    time.sleep(3)



