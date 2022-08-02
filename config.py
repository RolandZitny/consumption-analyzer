import os
from typing import Callable


DEFAULT_CONFIG = {
    'LOG_LEVEL': 'INFO',
    'A1_SCHEDULE_TIME': 3,  # Time in minutes
    'INFLUXDB_URL': 'http://localhost:4050',
    'INFLUXDB_TOKEN': 'yiNB2H_Nj26G1cBDx0AZfA2rcf9nBkUmoV8nPZEcIhnxC6tYThrWTAhOhO4OaJ7BaaCl3-NBzvViNWWubw_mMg==',
    'INFLUXDB_ORG': 'org',
    'INFLUXDB_BUCKET': 'slmp',
    'DB_TYPE': 'influxdb'
}


def get_config(name: str, default=None, wrapper: Callable = None):
    if not wrapper:
        wrapper = lambda x: x  # NOQA
    return wrapper(os.getenv(name, DEFAULT_CONFIG.get(name, default)))
