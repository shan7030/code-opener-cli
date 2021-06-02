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
        

class AutoComplete:
    """
    This class is used for providing autocomplete suggestions
    based on the tab press by the user
    """
    
    @classmethod
    def list_projects(incomplete: str):
        """
        Provides autocomplete for list of projects
        """
        current_config = JsonDataOperations.read()
        project_name_list = []
        for project_item in current_config['projects']:
            if project_item['project_name'].startswith(incomplete):
                project_name_list.append(project_item['project_name'])
        return project_name_list