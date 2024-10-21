from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

class SourceCode:
    def __init__(self, url):
        options = Options()
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.url = url
        self.soup = self.fetchHtml()

    def fetchHtml(self):
        self.driver.get(self.url)
        time.sleep(5) # impliment driverwait
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        self.driver.quit()
        return soup
    

if __name__ == '__main__':
    url = f'https://leetcode.com/u/khaleeque56/'
    html = SourceCode(url)
    # print(html.soup) # For testing