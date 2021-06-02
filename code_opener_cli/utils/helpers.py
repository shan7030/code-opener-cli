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
    # TODO: Add a proper data structure to create a list of editors
    # It should include short name, display name and command to open
    editor_list = ['VSCode','Sublime Text']


    @classmethod
    def list_projects(cls,incomplete: str):
        """
        Provides autocomplete for list of projects
        """
        current_config = JsonDataOperations.read()
        project_name_list = []
        for project_item in current_config['projects']:
            if project_item['project_name'].startswith(incomplete):
                project_name_list.append(project_item['project_name'])
        return project_name_list

    @classmethod
    def list_of_editors(cls,incomplete:str):
        """
        Provides autocomplete for list of editors
        """
        editors_matched = []
        for editor in cls.editor_list:
            if editor.startswith(incomplete):
                editors_matched.append(editor)
        return editor