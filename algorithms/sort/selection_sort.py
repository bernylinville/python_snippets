# coding:utf-8

import random


def selection_sort(nums):
    indexs = len(nums)
    for i in range(indexs):
        for j in range(i, indexs):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums


nums = random.sample(list(range(20)), 5)
print(nums)
print(selection_sort(nums))
