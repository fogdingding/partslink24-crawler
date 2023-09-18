import json
from config import config
from tool import tool
from tqdm import tqdm
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver import Chrome



class Crawler():
    async def get_brands_urls(self, url: str, driver: Chrome) -> dict:
        brands_url = {}
        await tool.loadings(time=3, msg='等待網頁加載中...')
        driver.get(url)
        await tool.loadings(time=3, msg='等待網頁加載中...獲取品牌中...')
        soup = BeautifulSoup(driver.page_source,'html.parser')
        brands_a_href = soup.select('div.b-logo > a.brand-logo')
        for a in brands_a_href:
            brands_url[a['title']] = a['href']

        return brands_url

    async def get_model_urls(self, url: str, specific_url:str, driver: Chrome) -> dict:
        data = {}
        driver.get(url)
        await tool.loadings(time=5, msg='獲取車型中...')
        for request in driver.requests:
            if request.response and specific_url in request.url:
                try:
                    response_body_str = request.response.body
                    data = json.loads(response_body_str)
                except json.JSONDecodeError:
                    raise Exception('get_model_urls error')
        return data

    async def get_urls(self, urls: str, specific_url: str,driver: Chrome) -> dict:
        data = []
        data_append = data.append
        for url in tqdm(urls):
            driver.get(url)
        for request in driver.requests:
            if request.response and specific_url in request.url:
                try:
                    response_body_str = request.response.body
                    data_append(json.loads(response_body_str))
                except json.JSONDecodeError:
                    raise Exception('get_urls json load error')
        return data
        
        
crawler = Crawler()