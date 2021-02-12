import os
from code_opener_cli.utils.config import DefaultConfiguration
from enum import Enum

class CodeOpenerDirectoryPath(Enum):
    COPEN_ROOT_PATH = os.path.dirname(__file__)

    # Resources Path
    RESOURCE_PATH = os.path.join(COPEN_ROOT_PATH,'resources')
    CONFIG_FILE_PATH = os.path.join(RESOURCE_PATH, DefaultConfiguration.CONFIGURATION_FILE_NAME.value)