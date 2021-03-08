# coding:utf-8

"""
    1. admin 类的搭建
    2. 获取用户函数（包含获取身份）
    3. 添加用户（判断当前身份是否是管理员）
    4. 冻结与恢复用户
    5. 修改用户身份
"""

import os

from base import Base
from common.error import NoneUserError, UserActiveError


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
        self.user = current_user
        self.role = self.user.get('role')
        self.name = self.user.get('username')
        self.active = self.user.get('active')

    def add_user(self, username, role):
        if self.role != 'admin':
            raise Exception('no permission')

        self._Base__write_user(username=username, role=role)

    def update_user_active(self, username):
        if self.role != 'admin':
            raise Exception('no permission')
        self._Base__change_active(username)

    def update_user_role(self, username, role):
        if self.role != 'admin':
            raise Exception('no permission')
        self._Base__change_role(username, role)


if __name__ == '__main__':
    gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')
    user_path = os.path.join(os.getcwd(), 'storage', 'user.json')
    admin = Admin('kchou', user_path, gift_path)
    # admin.get_user()
    # admin.add_user('test', 'normal')
    # admin.update_user_active('test')
    admin.update_user_role('test', 'normal')
