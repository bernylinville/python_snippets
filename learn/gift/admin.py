# coding:utf-8

"""
    1. admin 验证（只有admin的用户才能用这个类）
    2. 任何函数都应该动态的更新 get user
    3. 奖品的添加
    4. 奖品的删除
    5. 奖品数量的更新（同步 base 调整）
"""

import os

from base import Base
from common.error import NoneUserError, UserActiveError, RoleError


class Admin(Base):
    def __init__(self, username, user_json, gift_json):
        self.username = username
        super().__init__(user_json, gift_json)
        self.get_user()

    def get_user(self):
        users = self._Base__read_users()
        current_user = users.get(self.username)
        if current_user == None:
            raise NoneUserError('none user %s' % self.username)
        if current_user.get('active') == False:
            raise UserActiveError('the user %s is not active' % self.username)
        if current_user.get('role') != 'admin':
            raise RoleError('permission by admin')
        self.user = current_user
        self.role = self.user.get('role')
        self.name = self.user.get('username')
        self.active = self.user.get('active')

    def add_user(self, username, role):
        self.__check('no permission')
        self._Base__write_user(username=username, role=role)

    def update_user_active(self, username):
        self.__check('no permission')
        self._Base__change_active(username)

    def update_user_role(self, username, role):
        self.__check('no permission')
        self._Base__change_role(username, role)

    def add_gift(self, first_level, second_level, gift_name, gift_count):
        self.__check('no permission')
        self._Base__write_gift(first_level, second_level,
                               gift_name, gift_count)

    def delete_gift(self, first_level, second_level, gift_name):
        self.__check('no permission')
        self._Base__delete_gift(first_level, second_level, gift_name)

    def update_gift(self, first_level, second_level, gift_name, gift_count):
        self.__check('no permission')
        self._Base__gift_update(
            first_level, second_level, gift_name, gift_count, is_admin=True)

    def __check(self, message):
        self.get_user()
        if self.role != 'admin':
            raise Exception(message)


# if __name__ == '__main__':
    # gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')
    # user_path = os.path.join(os.getcwd(), 'storage', 'user.json')
    # admin = Admin('kchou', user_path, gift_path)
    # admin.get_user()
    # admin.add_user('admin', 'admin')
    # admin.update_user_active('test')
    # admin.update_user_role('kchou', 'admin')
    # admin.add_gift('level1', 'level1', 'ball', 10)
    # admin.delete_gift('level1', 'level1', 'ball')
    # admin.update_gift('level1', 'level1', 'ball', 100)
