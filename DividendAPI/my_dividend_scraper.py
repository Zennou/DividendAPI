from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import json
import timeit


def get_dividendJSON(symbol):
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options)
    driver.get("https://seekingalpha.com/symbol/" +
               symbol+"/dividends/scorecard")
    sleep(1)
    price = driver.find_element(
        By.XPATH, '//*[@id="content"]/div[2]/div/div[1]/div/div[2]/span[1]').text.replace('$', "")
    dividend = driver.find_element(
        By.XPATH, '//*[@id="content"]/div[2]/div/div[3]/div/div/section[3]/div/div[2]/div/div[1]/div[2]').text.replace('$', "")
    frequency = driver.find_element(
        By.XPATH, '//*[@id="content"]/div[2]/div/div[3]/div/div/section[3]/div/div[2]/div/div[6]/div[2]').text
    driver.quit()
    return json.dumps({'Price': float(price), 'Dividend Amount': float(dividend), 'Dividend Frequency': frequency})


"""
start = timeit.default_timer()
print(get_dividendJSON("PSEC"))
stop = timeit.default_timer()
print(stop-start)
"""
