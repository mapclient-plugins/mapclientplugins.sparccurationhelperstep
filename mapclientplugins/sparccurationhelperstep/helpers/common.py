import os
import re


def relative_to_dataset_dir(path):
    """
    Return the path that is relative to the root directory of a dataset by
    some heuristic.

    We are determining the root directory by searching for the first `files(/|\\)`
    entry, and saying that that is the dataset root directory.

    :param path: Path to work with, str.
    :return: Relative path from dataset root directory.
    """
    return re.sub(r'^.*?files' + os.sep, 'files' + os.sep, path)
