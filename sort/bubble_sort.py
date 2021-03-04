# coding:utf-8

import random

def bubble_sort(nums):
    indexs = len(nums)
    for i in range(indexs):
        for j in range(1, indexs - i):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]

    return nums

nums = random.sample(list(range(20)), 5)
print(nums)
print(bubble_sort(nums))
