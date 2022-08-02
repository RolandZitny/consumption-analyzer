"""
Analysis handler represents the controller for the execution of a specific
analysis method and for obtaining statistical results and their evaluation.
"""
from config import get_config
from consumption_analyzer.libs.setup_logging import logger


class AnalysisHandler:
    def __init__(self, method):
        """
        Initialize AnalysisHandler with specific type od analysis.
        :param method: Specific method from processes directory
        """
        self.method = method

    def perform_analysis(self, data):
        self.method.analyzedata(data)
        return 'OK'