from typing import List

def read_lines(file_path: str) -> List[str]:
    """
    Reads all lines from a specified file path.
    Raises TypeError if path is not a string.
    Raises FileNotFoundError if the target file does not exist.
    """
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string.")
    
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readlines()