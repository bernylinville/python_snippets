# coding:utf-8

class NotPathError(Exception):
    def __init__(self, message):
        self.message = message


class FormatError(Exception):
    def __init__(self, message):
        self.message = message


class NotFileError(Exception):
    def __init__(self, message):
        self.message = message


class UserExistsError(Exception):
    def __init__(self, message):
        self.message = message


class RoleError(Exception):
    def __init__(self, message):
        self.message = message


class LevelError(Exception):
    def __init__(self, message):
        self.message = message


class NegativeNumError(Exception):
    def __init__(self, message):
        self.message = message


class NoneUserError(Exception):
    def __init__(self, message):
        self.message = message


class UserActiveError(Exception):
    def __init__(self, message):
        self.message = message
