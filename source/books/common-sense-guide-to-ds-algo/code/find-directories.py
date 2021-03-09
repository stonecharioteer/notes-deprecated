"""Recursive algorithm to find all directories within a given directory"""


def get_directories(path=None):
    """Returns a list of directories and subdirectories"""
    import os
    if path is None:
        path = os.getcwd()
    contents = os.listdir(path)
    directories = []
    for item in contents:
        abs_path = os.path.join(path, item)
        if os.path.isdir(abs_path):
            directories.append(abs_path)
            directories.extend(get_directories(abs_path))
    return directories
