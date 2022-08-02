"""
The database client handler represents the connection between the application and the database.
It is used for obtaining batches of data and for saving the results of analyzes on a predefined database.
"""
from config import get_config
from consumption_analyzer.libs.setup_logging import logger


class StorageHandler:
    def __init__(self, db_client):
        """
        Initialize database client handler with specific database client.
        :param db_client: database client object
        """
        self.db_client = db_client

    def load_data(self):
        """
        Use clients method to get data batch/window.
        :return: dataframe
        """
        return self.db_client.query_window()

    def save_data(self, results=None):
        """
        Use clients method to save data into database.
        :param results: results of analysis
        :return:
        """
        self.db_client.upload_results(results)
