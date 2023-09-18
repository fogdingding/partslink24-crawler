class Config():
    def get_specific_urls(self) -> dict:
        return {
            'PARTSLINK24_HOME_URL':'https://www.partslink24.com',
            'CARWLER_MODEL_SPECIFIC_URL': 'p5bmw/extern/vehicle/models',
            'CARWLER_MODELTYPE_SPECIFIC_URL': 'p5bmw/extern/vehicle/modeltypes',
            'CARWLER_RES1_SPECIFIC_URL': '/p5bmw/extern/vehicle/restrictions1',
            'CARWLER_RES2_SPECIFIC_URL': '/p5bmw/extern/vehicle/restrictions2',
            'CARWLER_RES3_SPECIFIC_URL': '/p5bmw/extern/vehicle/restrictions3',
            'CARWLER_MAINGROUPSTABLE_SPECIFIC_URL': '/p5bmw/extern/groups/main-mdl',
            'CARWLER_SUBGROUPSTABLE_SPECIFIC_URL': '/p5bmw/extern/groups/func-mdl',
        }

config = Config()