'''
Retrun the config in dict
'''

import configparser
import os.path

import logging

config_file = os.path.dirname(
    os.path.realpath(__file__)) + os.sep + 'config.ini'


def read_config_general(configFile=config_file):
    try:
        logging.info('Read config file: ' + configFile)
        configRead = configparser.ConfigParser()
        configRead.read(configFile)

        config = {}
        for sectionName in configRead.sections():
            config[sectionName] = {}
            options = [i.upper() for i in configRead.options(sectionName)]
            for j in options:
                config[sectionName][j] = configRead[sectionName][j]

    except Exception as e:
        logging.error("Error read config file, check config.ini")
        # print(e)
        raise
    return config

if __name__ == '__main__':
    config = read_config_general('screen_config.ini')
    print(config)
