# 爬取 partslink24 網站
使用 python3 + selenium-wire ，可運行於 python 版本>=3.10。
抓取 partslink24 之 BMW 所有車型資料。
針對 `len(url) > 10000` 之資料，建議使用平行化爬取，可透過爬取 n+1 層資料範例做切割。
### BMW_func_dml_1~5.json 為所有車型資料。
https://drive.google.com/file/d/1iG3-F04zU8ApQ3KcYmlloiAWc4CBRuYA/view?usp=sharing

### 環境安裝
`pip3 install -r requirements.txt`

### 執行參數
####  初始資料：爬取 BMW 第一層車型資料後結束
`python3 main.py`
#### 爬取 n+1 層資料
```
python3 main.py [read_filename] [n_next_specific_url] [strat_index_url] [strat_index_url] [end_index_url] [write_filename]
```
e.g
```
python3 main.py BMW_model.json CARWLER_MODELTYPE_SPECIFIC_URL 0 -1 BMW_modeltype.json
```


#### 參數說明
1. `read_filename`： 讀取第n階資料。e.g. `n_data.josn`
2. `n_next_specific_url`：識別 n+1 之 url 關鍵字。e.g. `CARWLER_MODELTYPE_SPECIFIC_URL`
3. `strat_index_url`：爬取 n+1 urls 的陣列起始位子( 0 為起始點)。e.g. `0`
4. `end_index_url`：爬取 n+1 urls 的陣列起始位子( -1 為最後)。e.g. `-1`
5. `write_filename`：寫入第n+1階資料。e.g. `n1_data.josn`

#### n_next_specific_url 內涵資料
```
{
    'PARTSLINK24_HOME_URL':'https://www.partslink24.com',
    'CARWLER_MODEL_SPECIFIC_URL': 'p5bmw/extern/vehicle/models',
    'CARWLER_MODELTYPE_SPECIFIC_URL': 'p5bmw/extern/vehicle/modeltypes',
    'CARWLER_RES1_SPECIFIC_URL': '/p5bmw/extern/vehicle/restrictions1',
    'CARWLER_RES2_SPECIFIC_URL': '/p5bmw/extern/vehicle/restrictions2',
    'CARWLER_RES3_SPECIFIC_URL': '/p5bmw/extern/vehicle/restrictions3',
    'CARWLER_MAINGROUPSTABLE_SPECIFIC_URL': '/p5bmw/extern/groups/main-mdl',
    'CARWLER_SUBGROUPSTABLE_SPECIFIC_URL': '/p5bmw/extern/groups/func-mdl'
}
```