import configparser
from utilities import *


def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities\properties.ini')
    return config