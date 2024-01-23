#scraper module that parses html in order to search through the page
from seleniumwire import webdriver
from selenium.webdriver import Keys, ActionChains
import time

class Scraper():
    def __init__(self):
        self.driver = None
    

    def get_url(self, url):
        self.driver = webdriver.Firefox()
        self.driver.get(url)

    def scrape_twitter(self):
        time.sleep(5)
        print("starting")

        endtime = time.time() + 5

        while time.time() < endtime:
            ActionChains(self.driver).key_down(Keys.DOWN).perform()
        
        ActionChains(self.driver).key_up(Keys.DOWN).perform()

        vids = ['placeholder']
        img = ['placeholder']
        

        for request in self.driver.requests:
            if request.response:
                if request.host == "video.twimg.com":
                    print("VIDEO -> " + request.url)
                    vids.append(request.url)
                elif request.host == "pbs.twimg.com":
                    print("IMG -> " + request.url)
                    img.append(request.url)    
        
        vids[0] = str(len(vids))
        img[0] = str(len(img))

        self.write_file('vid_urls.txt', vids)
        self.write_file('img_urls.txt', img)

    def write_file(self, f, lst):
        f = open(f, 'wb')
        for i in lst:
            f.write(i.encode('utf-8') + str('\n').encode('utf-8'))
        f.close()

    def close_driver(self):
        self.driver.close()