# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

def solution(nums):
    nums2 = set()
    for i in nums:
        if i in nums:
            return True
        nums2.add(i)
    return False

solution([1,2,5,7,2,1])