# coding:utf-8

import random


def insertion_sort(nums):
    indexs = len(nums)
    for i in range(1, indexs):
        while i > 0 and nums[i - 1] > nums[i]:
            nums[i - 1], nums[i] = nums[i], nums[i - 1]
            i -= 1

    return nums


nums = random.sample(list(range(20)), 5)
print(nums)
print(insertion_sort(nums))
