import asyncio
import time
import json

PARTSLINK24_HOME_URL = 'https://www.partslink24.com'

class Parse():
    def json_write(self, data, filename: str = 'output.json') -> None:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii='False', indent=4)
    
    def json_read(self, filename: str) -> None:
        data = None
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    
    async def get_record_urls(self, data: dict) -> dict:
        moduletype_urls = []
        moduletype_urls_append = moduletype_urls.append
        for record in data['data']['records']:
            if 'link' in record.keys():
                moduletype_urls_append(f"{PARTSLINK24_HOME_URL}{record['link']['path']}")
        return moduletype_urls
    
    async def get_n_set_record_urls(self, data: list) -> dict:
        moduletype_urls = []
        moduletype_urls_append = moduletype_urls.append
        for i in data:
            for record in i['data']['records']:
                if 'link' in record.keys():
                    moduletype_urls_append(f"{PARTSLINK24_HOME_URL}{record['link']['path']}")
        return moduletype_urls
        

parse = Parse()