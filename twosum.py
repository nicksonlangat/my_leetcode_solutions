# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.

def solution(nums, target):
    values = {}
    for index, num in enumerate(nums):
        remaining = target - num
        if remaining in values:
            print([index, values[remaining]])
        values[num] = index

solution([3,2,4], 6)