from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time,sys,pickle
from selenium.webdriver.common.action_chains import ActionChains
btc = "3MUT2imvKa2V4BZ6cBGAfZFeQ5PS9kopdk"


chrome_options = Options()  
chrome_options.add_argument("--headless --window-size=1920,1080")
chrome_options.binary_location = r"/app/.apt/usr/bin/google-chrome"

driver = webdriver.Chrome(chrome_options=chrome_options)
#driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=chrome_options)

while True:
    print(">> MADE BY KRISH!!")
    print(">> Opening Website")
    driver.get("http://claimfreebtc.win/")
    print(">> Closing Ad")
    try:
        driver.find_element_by_xpath('//*[@id="sticky_bar_logo"]/div[2]/button').click()
    except:
        print(">> Ad Close Failed : Maybe No AD!")
    print(">> Input BTC address : " + btc)
    address = driver.find_element_by_xpath('/html/body/center/table/tbody/tr/td[2]/div/form/input[1]')
    address.send_keys(btc)
    print(">> Solving Captcha")
    source = driver.find_element_by_xpath('//*[@id="captchmeslider"]')
    dest = driver.find_element_by_xpath('//*[@id="captchmerefreshimg"]')
    ActionChains(driver).drag_and_drop(source, dest).perform()
    time.sleep(3)
    print(">> Claiming")

    claim = driver.find_element_by_xpath('/html/body/center/table/tbody/tr/td[2]/div/form/input[2]')
    ActionChains(driver).move_to_element(driver.find_element_by_xpath('/html/body/center/iframe[2]')).perform()
    claim.click()
    print(">> Claimed! Waiting 5 minutes")

    time.sleep(305)
