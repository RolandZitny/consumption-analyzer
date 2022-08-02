"""
Agent collects, process and saves data periodically. This period is set in main program.
The agent must have a database that will be queried for windows of a defined length
and a database in which the results of the analysis will be stored.
It is also necessary to define the analysis method that will be performed on the queried data.
"""
from consumption_analyzer.libs.setup_logging import logger


class Agent:
    def __init__(self, database_in=None, process=None, database_out=None):
        """
        Initialization of Agent.
        :param database_in: input database client handler
        :param process: analysis handler
        :param database_out: output database client handler
        """
        self._database_in = database_in
        self._analysis_method = process
        self._database_out = database_out

        logger.info("Agent created -> DB IN: {}     Method: {}     DB OUT: {}".
                    format(self._database_in.db_client.__name__,
                           self._analysis_method.method.__name__,
                           self._database_out.db_client.__name__))

    def process_window(self):
        """
        This process is scheduled:
            - 1. query data on database_in and get window/batch
            - 2. use some method to obtain statistics or predictions
            - 3. save results into database_out
        """
        # Query on input database
        data_window = self._database_in.load_data()
        # Perform analysis
        analysis_results = self._analysis_method.perform_analysis(data_window)
        # Upload results
        self._database_out.save_data(analysis_results)

        logger.info("Agent process executed -> DB IN: {}     Method: {}     DB OUT: {}".
                    format(self._database_in.db_client.__name__,
                           self._analysis_method.method.__name__,
                           self._database_out.db_client.__name__))
