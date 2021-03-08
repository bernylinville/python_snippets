# coding:utf-8

"""
    1. user 类的初始化
    2. get_user（时间的转变）
    3. 查看奖品列表
"""

import os

from base import Base
from common.error import NoneUserError, RoleError, UserActiveError
from common.utils import timestamp_to_str


class User(Base):
    def __init__(self, username, user_json, gift_json):
        self.username = username
        super().__init__(user_json, gift_json)
        self.get_user()

    def get_user(self):
        users = self._Base__read_users()

        if self.username not in users:
            raise NoneUserError('none user %s' % self.username)

        current_user = users.get(self.username)

        if current_user.get('active') == False:
            raise UserActiveError('the user %s is not active' % self.username)

        if current_user.get('role') != 'normal':
            raise RoleError('permission by normal')

        self.role = current_user.get('role')
        self.name = current_user.get('username')
        self.gifts = current_user.get('gifts')
        self.create_time = timestamp_to_str(current_user.get('create_time'))

    def get_gifts(self):
        gifts = self._Base__read_gifts()
        gift_lists = []

        for level_one, level_one_pool in gifts.items():
            for level_two, level_two_pool in level_one_pool.items():
                for gift_name, gift_info in level_two_pool.items():
                    gift_lists.append(gift_info.get('name'))

        return gift_lists


if __name__ == '__main__':
    gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')
    user_path = os.path.join(os.getcwd(), 'storage', 'user.json')
    user = User('test', user_path, gift_path)
    # print(user.name, user.create_time, user.gifts, user.role)
    result = user.get_gifts()
    print(result)
