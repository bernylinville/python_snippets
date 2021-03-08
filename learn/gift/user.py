# coding:utf-8

"""
    1. 抽奖函数 随机判断第一层（level1） 1：50% 2:30% 3: 15% 4：5%
    2. 抽奖函数 随机判断第二层（level2） 1: 80% 2: 15% 3：5%
    3. 抽奖函数 获取到对应层级的真实奖品，并随机一个奖品，查看奖品 count 是否为 0
               不为 0 中奖，提示用户，并奖品数量减 1，并为用户更新
               奖品到 user 表中的 gifts 中，
               数量为 0，则未中奖
"""

import os
import random

from base import Base
from common.error import NoneUserError, RoleError, UserActiveError, CountError
from common.utils import timestamp_to_str


class User(Base):
    def __init__(self, username, user_json, gift_json):
        self.username = username
        self.gift_random = list(range(1, 101))
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

        self.user = current_user
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

    def choice_gift(self):
        # level1 get
        first_level = None
        second_level = None
        level_one_count = random.choice(self.gift_random)
        if 1 <= level_one_count <= 50:
            first_level = 'level1'
        elif 50 < level_one_count <= 80:
            first_level = 'level2'
        elif 80 < level_one_count <= 95:
            first_level = 'level3'
        elif 95 < level_one_count <= 100:
            first_level = 'level4'
        else:
            raise CountError('level_one_count in 0~100')

        gifts = self._Base__read_gifts()
        level_one = gifts.get(first_level)

        level_two_count = random.choice(self.gift_random)
        if 1 <= level_two_count <= 80:
            second_level = 'level1'
        elif 80 < level_two_count <= 95:
            second_level = 'level2'
        elif 95 < level_two_count <= 100:
            second_level = 'level4'
        else:
            raise CountError('level_two_count in 0~100')

        level_two = level_one.get(second_level)
        if not level_two:
            print('哦可惜 您没有中奖')
            return

        gift_names = []
        for k, _ in level_two.items():
            gift_names.append(k)

        gift_name = random.choice(gift_names)
        gift_info = level_two.get(gift_name)
        if gift_info.get('count') == 0:
            print('哦可惜 您没有中奖')
            return
        gift_count = gift_info['count'] - 1
        self._Base__gift_update(
            first_level, second_level, gift_name, gift_count)

        self.user['gifts'].append(gift_name)
        self.update()
        print('恭喜您获得 %s 奖品' % gift_name)

    def update(self):
        users = self._Base__read_users()
        users[self.username] = self.user

        self._Base__save(users, self.user_json)


if __name__ == '__main__':
    gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')
    user_path = os.path.join(os.getcwd(), 'storage', 'user.json')
    user = User('test', user_path, gift_path)
    # print(user.name, user.create_time, user.gifts, user.role)
    # result = user.get_gifts()
    # print(result)
    user.choice_gift()
