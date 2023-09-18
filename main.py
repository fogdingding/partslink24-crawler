import asyncio
import sys
from tqdm import tqdm
from config import config
from crawler import crawler
from tool import tool
from parse import parse

argv = sys.argv
user_argv = tool.get_args(argv)
specific_urls = config.get_specific_urls()
print(user_argv)
async def main() -> None:
    if user_argv is None:
        print('參數數量異常')
    if user_argv['cnt'] == 1:
        print('建立第一層資料 model')
        driver = await tool.get_webdriver()
        brands_url = await crawler.get_brands_urls(url=specific_urls['PARTSLINK24_HOME_URL'], driver=driver)    
        bmw_URL = f'{specific_urls["PARTSLINK24_HOME_URL"]}{brands_url["BMW"]}'
        bmw_model = await crawler.get_model_urls(url=bmw_URL, specific_url=specific_urls['CARWLER_MODEL_SPECIFIC_URL'], driver=driver)
        parse.json_write(data = bmw_model, filename='BMW_model.json')
        driver.requests.clear()
        driver.quit()
        print('完成車型爬取，請用另一種參數後續爬蟲。')
    if user_argv['cnt'] == 6:
        await tool.loadings(time=0, msg='n層資料加載中')
        n_data = parse.json_read(filename=user_argv['read_filename'])
        n_next_urls = await parse.get_record_urls(data=n_data)
        n_next_urls = n_next_urls[user_argv['strat_index_url']:user_argv['end_index_url']]
        await tool.loadings(time=0, msg='n+1層資料爬取中')
        driver = await tool.get_webdriver()
        n_next_data = await crawler.get_urls(urls=n_next_urls, specific_url=specific_urls[user_argv['n_next_specific_url']], driver=driver)
        parse.json_write(data=n_next_data, filename=user_argv['write_filename'])
        driver.requests.clear()
        driver.quit()


if __name__ == '__main__':
    asyncio.run(main())
