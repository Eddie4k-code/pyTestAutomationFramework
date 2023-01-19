import configparser

config = configparser.RawConfigParser()

config.read(".\\Configurations\\config.ini")

class ReadConfig():
    """
    Gets Properties from our config file
    """
    @staticmethod
    def getAppUrl():
        url = config.get("common info", "baseURL")
        return url

    @staticmethod
    def getUsername():
        username = config.get("common info", "username")
        return username

    @staticmethod
    def getPath():
        path = config.get("common info", "path")

