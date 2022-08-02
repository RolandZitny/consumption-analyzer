"""
The main program takes care of the planning and management of individual analysis processes.
Each such process consisted of a database input, output and type of analysis method.
The input and output database object can be the same.
"""
import time
import schedule
from config import get_config
from consumption_analyzer.libs.setup_logging import logger
from consumption_analyzer.agent import Agent
from consumption_analyzer.storage_handler import StorageHandler
from consumption_analyzer.analysis_handler import AnalysisHandler

from consumption_analyzer.db_clients.influxdb import InfluxDB
from consumption_analyzer.methods.test import TestAnalysis


def main():
    """
    Main program. Every Agent needs to be initialized with databases and analysis method.
    Those Agents are then scheduler for specific running.
    """
    logger.info("Main program started:")
    # InfluxDB database handler and test method handler
    influxdb = StorageHandler(db_client=InfluxDB())
    test_method = AnalysisHandler(method=TestAnalysis())

    # Agent for first analysis
    agent = Agent(database_in=influxdb, process=test_method, database_out=influxdb)

    # Schedule agent process
    schedule.every(get_config('A1_SCHEDULE_TIME')).seconds.do(agent.process_window)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
