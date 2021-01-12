from time import sleep
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import os


from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "AC2c05e75ba2288e4b393406c691272573"
# Your Auth Token from twilio.com/console
auth_token  = "98377bc356e160c7041ad878d11d0649"

client = Client(account_sid, auth_token)


#Inputs
def opener():
    global driver
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    except:
        
        driver = webdriver.Firefox(executable_path=GeckoDriveManager().install())



    #Form Opening
    driver.get('https://vacstrac.hctx.net')
    print("Form opened")
    sleep(2)

def message():
        message = client.messages.create(
                to="+19362328113",
                from_="+14158256082",
                body= str("Pop up gone! GET YOUR VACCINE!")
                )

        print(message.sid)


def search():
    sleep(3)
    try:
    #identify element
        l = driver.find_element_by_css_selector("#mat-dialog-0 > popup-dialog")
        print("Element exist -")
        #NoSuchElementException thrown if not present
    except NoSuchElementException:
        print("Element does not exist")
        message()
        driver.close()
    driver.quit()



while 1:
    sleep(1800)
    opener()
    search()