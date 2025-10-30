import logging
import os
from typing import Optional, Any, Dict, List

logger = logging.getLogger(__name__)

def read_file(file_path: str) -> Optional[str]:
    """Read and return the content of a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except (IOError, FileNotFoundError) as e:
        logger.error(f"Error reading file {file_path}: {e}")
        return None

def write_file(file_path: str, content: str) -> bool:
    """Write content to a file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    except IOError as e:
        logger.error(f"Error writing to file {file_path}: {e}")
        return False

def ensure_directory_exists(dir_path: str) -> bool:
    """Ensure a directory exists, creating it if necessary."""
    try:
        os.makedirs(dir_path, exist_ok=True)
        return True
    except OSError as e:
        logger.error(f"Error creating directory {dir_path}: {e}")
        return False

def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dictionaries, with dict2 values taking precedence."""
    return {**dict1, **dict2}

def filter_list(items: List[Any], condition: callable) -> List[Any]:
    """Filter a list based on a condition."""
    return [item for item in items if condition(item)]