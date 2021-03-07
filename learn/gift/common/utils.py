# coding:utf-8
import os
import time

from .error import NotFileError, NotPathError, FormatError


def check_file(path):
    if not os.path.exists(path):
        raise NotPathError('don\'t found %s' % path)
    if not path.endswith('.json'):
        raise FormatError('need json format')
    if not os.path.isfile(path):
        raise NotFileError('this is not a file')


def timestamp_to_str(timestamp):
    time_obj = time.localtime(timestamp)
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time_obj)
    return time_str
