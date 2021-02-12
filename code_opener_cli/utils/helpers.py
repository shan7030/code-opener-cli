"""
    This file contains the utility classes and methods for the project
"""

import json
from code_opener_cli.path_definitions import CodeOpenerDirectoryPath

class JsonDataOperations: 
    """
    This class is used for operations on settings.json file.
    setting.json file servers as basic configuration for the project
    """
    @classmethod
    def update(cls,config_data):
        """
        Creates the setting.json file
        """
        with open(CodeOpenerDirectoryPath.CONFIG_FILE_PATH.value, 'w') as outfile:
            json.dump(config_data, outfile)

    @classmethod
    def read(cls):
        """ 
        Reads the setting.json file
        """
        f = open(CodeOpenerDirectoryPath.CONFIG_FILE_PATH.value,)
        data = json.load(f)
        f.close()
        return data