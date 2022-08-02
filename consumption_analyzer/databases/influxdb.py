from config import get_config
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import ASYNCHRONOUS   # TODO we will se / SYNCHRONOUS
from consumption_analyzer.libs.setup_logging import logger


class InfluxDB:
    def __init__(self, url=get_config('INFLUXDB_URL'),
                 token=get_config('INFLUXDB_TOKEN'),
                 org=get_config('INFLUXDB_ORG')):
        """
        Initialize database.
        :param url:
        :param token:
        :param org:
        :param db_type:
        """
        self.__name__ = 'InfluxDB'
        self._influxdb_client = InfluxDBClient(url=url, token=token, org=org)
        self._query_api = self._influxdb_client.query_api()
        self._write_api = self._influxdb_client.write_api(write_options=ASYNCHRONOUS)
        self._data_frame = None
        logger.info("Influxdb")

    def query_window(self):
        """
        Query to database and return pandas dataframe.
        :return: pandas dataframe
        """
        # TODO parametrize query + config
        influx_query = '''
                           from(bucket:"slmp") 
                               |> range(start: -10s) 
                               |> filter(fn: (r) => r._measurement == "energy-consumption")
                               |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value") 
                               |> keep(columns: ["_time","M32","M33","M34","M35","M36","M37"])
                       '''

        query_parameters = {}

        self._data_frame = self._query_api.query_data_frame(query=influx_query, params=query_parameters)
        return self._data_frame

    def upload_results(self, result):
        """
        Upload results into server.
        :param result: result from analysis
        """
        # TODO create record of points from list of results
        self._write_api.write(bucket=get_config('INFLUXDB_BUCKET'), record=result)


