"""
This file hold the path definitions for the package
"""
import os
from code_opener_cli.utils.config import DefaultConfiguration

class PathDefinitions:
    """
    Class with static Path Defintions for the package
    """
    CODE_OPENER_CLI_PATH = os.getcwd()
    UTILS_PATH = os.path.join(CODE_OPENER_CLI_PATH,'utils')
    CONFIG_FILE = os.path.join(UTILS_PATH, DefaultConfiguration.CONFIGURATION_FILE_NAME)
