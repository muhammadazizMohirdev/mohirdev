from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


# service = Service(executable_path='C:\\Users\\admin\\Downloads\\chromedriver-win64\\chromedriver.exe')
# options = webdriver.ChromeOptions()
# web_driver = webdriver.Chrome(service=service, options=options)
# web_driver.maximize_window()
# web_driver.get("https://qase.io/")
# web_driver.implicitly_wait(10)

"""Sign up testing"""
# email = "some15552312email@gmail.com"
# element = web_driver.find_element(By.XPATH, "//li[@id='menu-item-4923']/a")
# assert "A single workspace for" in element.text, "Page did not open"
# web_driver.find_element(By.XPATH, "//p/following-sibling::div/a[text()='START FOR FREE']").click()
# web_driver.find_element(By.XPATH, "//input[@id='inputEmail']").send_keys(email)
# web_driver.find_element(By.XPATH, "//input[@id='inputPassword']").send_keys("123456ABCabc*")
# web_driver.find_element(By.XPATH, "//input[@id='inputPasswordConfirm']").send_keys("123456ABCabc*")
# web_driver.find_element(By.XPATH, "//label/input[@type='checkbox']/following-sibling::span").click()
# web_driver.find_element(By.XPATH, "//*[text()='Create your Qase account >']").click()
# congatulation_label = web_driver.find_element(By.XPATH, "//div/h1")
# email_container = web_driver.find_element(By.XPATH, "//div/span")
# assert "Congratulations!" in congatulation_label.text, "Sign up failed!!!"
# assert email in email_container.text, "Email does not appear!!!"
# web_driver.close()