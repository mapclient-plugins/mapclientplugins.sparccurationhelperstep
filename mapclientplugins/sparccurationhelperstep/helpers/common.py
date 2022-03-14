import os
import re


def relative_to_dataset_dir(path):
    """
    Return the path that is relative to the root directory of a dataset by
    some heuristic.

    We are determining the root directory by searching for the first `files(/|\\)`
    entry, and saying that that is the dataset root directory.

    If `files` is not found we look for `derivative` or `primary` instead.
    If found, we use the parent directory of the directory found as the
    dataset root directory.

    If nothing is found we return None.

    :param path: Path to work with, str.
    :return: Relative path from dataset root directory.
    """
    m = re.match(r'(^.*files[\\/])', path)
    if m is not None:
        return os.path.relpath(path, m.group(1))

    sds_directories_regexp = [r'(^.*derivative[\\/])', r'(^.*primary[\\/])']
    for sds_directory_regexp in sds_directories_regexp:
        m = re.match(sds_directory_regexp, path)
        if m is not None:
            dataset_dir = os.path.dirname(os.path.dirname(m.group(1)))
            return os.path.relpath(path, dataset_dir)

    return None
