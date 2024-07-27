import os
import csv
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

COOKIES_FILE = 'localStorageData.txt'
FILE_NAME = 'wsoo_mvmt.txt' #target file to be downloaded


URL = 'https://web.telegram.org/a/'

driver = webdriver.Firefox()

def save_local_storage(driver, storage_file):
    with open('local_storage.txt', 'w',encoding="utf-8") as file:
        file.write(storage_file)

def load_local_storage(driver, storage_file):
    with open( storage_file, 'r',encoding="utf-8") as file:
        local_storage = file.read()
        driver.execute_script(f"""
        console.log('Miracle...')
        var items = JSON.parse(arguments[0]);
        for (var key in items) {{
            window.localStorage.setItem(key, items[key]);
        }}
    """, local_storage)

driver.get(URL)
time.sleep(15)

local_storage = driver.execute_script("return JSON.stringify(window.localStorage);")

if os.path.exists(COOKIES_FILE):
    load_local_storage(driver, COOKIES_FILE)
    driver.refresh()
else:
    save_local_storage(driver, local_storage)

print(' Click the target chat')
time.sleep(10)
# Click the target chat


with open(FILE_NAME,'r') as file:
    message_area = driver.find_element(By.ID,'editable-message-text')
    # message_area.send_keys(link)
    for link in file:
        print(link)
        # child_count = driver.execute_script("return document.querySelectorAll('#MiddleColumn .message-date-group')[1].childElementCount ")

        message_area.click()
        message_area.send_keys(link)
        message_area.send_keys(Keys.RETURN)
        # print('childcount = ', child_count)
        time.sleep(15)

        # while True:
        #     cur = driver.execute_script("return document.querySelectorAll('#MiddleColumn .message-date-group')[1].childElementCount ")
        #     print(child_count, 'pause' , cur )
        #     if cur > child_count:
        #         break
        #     else:
        #         time.sleep(13)

driver.quit()
"""

#LeftColumn  .Transition .chat-list .ListItem-button

# Top pinned item
#LeftColumn  .Transition .chat-list .ListItem:nth-child(2)  .ListItem-button

#MiddleColumn

message_count = driver.findElement(By.cssSelector('.message-date-group')).childElementCount

message_area = driver.findElement(By.cssSelector('#MiddleColumn #editable-message-text'))
message_area.send_keys(link)
message_area.send_keys(Keys.ENTER)

while driver.findElement(By.cssSelector('.message-date-group')).childElementCount <= message_count:
        time.sleep(2)
"""