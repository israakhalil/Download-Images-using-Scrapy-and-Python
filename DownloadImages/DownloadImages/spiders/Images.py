import scrapy

class ImagesSpider(scrapy.Spider):
    name = "DownloadImages"
    start_urls = ["https://en.wikipedia.org/wiki/Eiffel_Tower"]
    
    def parse(self, response):
        row_image_urls=response.css(".image img::attr(src)").getall()
        clean_image_urls=[]
        for img_url in row_image_urls:
            clean_image_urls.append(response.urljoin(img_url))
        
        yield { 
            'image_urls' : clean_image_urls
        }