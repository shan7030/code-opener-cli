"""
    This file contains the utility classes and methods for the project
"""

import json
from code_opener_cli.utils.config import DefaultConfiguration


class JsonDataOperations: 
    """
    This class is used for operations on settings.json file.
    setting.json file servers as basic configuration for the project
    """

    @classmethod
    def create(cls):
        """
        Creates the setting.json file
        """
        with open(DefaultConfiguration.CONFIGURATION_FILE_NAME, 'w') as outfile:
            json.dump(DefaultConfiguration.CONFIGURATION_DATA, outfile)

    @classmethod
    def read(cls):
        """ 
        Reads the setting.json file
        """
        with open(DefaultConfiguration.CONFIGURATION_FILE_NAME) as json_file:
            data = json.load(json_file)
            return data

    @classmethod
    def present(cls):
        """
        Checks whether the setting.json is already present

        Returns: 
            True : When configuration file present
            False: When configuration file not present
        
        """
        pass
