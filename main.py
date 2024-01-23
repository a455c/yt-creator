#program that runs included modules in order to scrape videos and memes and 
#montage them into shorts clips and videos to upload to youtube

from modules.scraper import Scraper   
from modules.loader import Loader 

def main():
    scraper = Scraper()
    scraper.get_url("https://twitter.com/memes")
    scraper.scrape_twitter()
    scraper.close_driver()


    loader = Loader()
    loader.load_urls('vid_urls.txt')
    loader.glue_vids(['/home/a455c/Downloads/sBScUQKjAI8xszq2.ts', '/home/a455c/Downloads/dWT6e4sRPOsNnRAj.ts'])
    # loader.write_clips(c, '/home/a455c/proj/yt-creator/output')


if __name__ == "__main__":
    main() 

