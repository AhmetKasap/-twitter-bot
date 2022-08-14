from ast import While
from re import U
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
url = "https://twitter.com/i/flow/login"
driver.get(url)
driver.maximize_window()
time.sleep(4)

user_name =""
user_password=""
search_user_name = ""


def login_f(user_name, user_password) :
    name = driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
    name.send_keys(user_name)
    time.sleep(1)


    clickMe = driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")
    clickMe.click()
    time.sleep(1)

    password = driver.find_element(By.NAME, "password")
    password.send_keys(user_password)
    time.sleep(2)

    login = driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span")
    login.click()

    time.sleep(5)


def search_user () :
    search_hashtag = driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")
    search_hashtag.send_keys(search_user_name)
    time.sleep(1)
    search_hashtag.send_keys(Keys.ENTER)
    time.sleep(5)

    persons = driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[3]/a")
    persons.click()
    time.sleep(5)

    user = driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div/div")
    time.sleep(1)
    user.click()
    time.sleep(10)


def likeTwit () :
    while True:
        like = driver.find_element(By.XPATH, "//div[@data-testid='like']")
        time.sleep(1)

        like.click()
        time.sleep(1)

        
login_f(user_name,user_password)
search_user()
likeTwit()