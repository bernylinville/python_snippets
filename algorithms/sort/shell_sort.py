# coding:utf-8

import random

def shell_sort(nums):
    indexs = len(nums)
    gap = indexs // 2
    while gap:
        for i in range(gap, indexs):
            while i - gap >= 0 and nums[i - gap] > nums[i]:
                nums[i - gap], nums[i] = nums[i], nums[i - gap]
                i -= gap

        gap //= 2
    return nums

nums = random.sample(list(range(20)), 5)
print(nums)
print(shell_sort(nums))
