"""
File util.py contains all custom exceptions for most of situations.
"""


class Error(Exception):
    """Base Error class"""
    pass


class WrongIpAddress(Error):
    """Wrong format of target IP address"""
    pass
