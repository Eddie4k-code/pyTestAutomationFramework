"""
Used for to log

"""

import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename='.\\Logs\\automation.log', mode='a')
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger.setLevel(logging.INFO)
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)

        return logger