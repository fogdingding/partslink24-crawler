import json
import asyncio
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class Tool():
    def get_args(self, argv):
        if len(argv) == 1:
            return {
                'cnt': 1
            }
        if len(argv) == 6:
            return {
                'cnt': 6,
                'read_filename': str(argv[1]),
                'n_next_specific_url': str(argv[2]),
                'strat_index_url': int(argv[3]),
                'end_index_url': int(argv[4]),
                'write_filename': str(argv[5])
            }
        return None
        
    def json_write(self, data, filename: str = 'output.json') -> None:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii='False', indent=4)
    
    def json_read(self, filename: str) -> None:
        data = None
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    
    async def loadings(self,time: int, msg:str = '等待網頁加載中'):
        print(msg)
        await asyncio.sleep(time)
    
    async def get_webdriver(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options,
            seleniumwire_options={
                'disable_encoding': True
            }
        )
        return driver

tool = Tool()