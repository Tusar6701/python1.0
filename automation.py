# youtube automation to find the best video based on the video with the highest views, on a topic selected by the user
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ECs

print('the beginning')

print('started')
search = input("Enter whatever you want to search youtube for : ")
print("browser is opening...")
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=options)
driver.get('https://youtube.com')
print('browser opened')
searchbox = driver.find_element_by_xpath('//input[@id="search"]')
print('search box found')
searchbox.click()
searchbox.send_keys(search)
print('sent keys "', search, '"')
search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
search_button.click()
print("waiting for page to load...")
driver.implicitly_wait(30)
print("wait complete!!!")
filter1 = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/div/ytd-toggle-button-renderer/a/paper-button')
filter1.click()
viewCount = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/iron-collapse/div/ytd-search-filter-group-renderer[5]/ytd-search-filter-renderer[3]/a/div/yt-formatted-string')
driver.execute_script("arguments[0].click();", viewCount)
print("best video found!!!")
time.sleep(1)
best_vid = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail')
best_vid.click()
print("best video opened")

time.sleep(1)
fS=driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[30]/div[2]/div[3]/button[9]')
fS.click()
print("Full-screen video is playing")
