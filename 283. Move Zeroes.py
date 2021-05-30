"""

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

"""


# def moveZeroes(nums):
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#     i = 0
#     n = len(nums)
#     while n-1>i:
#         if nums[i] == 0:
#             nums[i:n-1] = nums[i+1:n]
#             nums[n-len(nums)-1] = 0
#             n -= 1
#             print(nums)
#         else:
#             i += 1


def moveZeroes(nums):
    zero = 0  # records the position of "0"
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    moveZeroes(nums)
    print(nums)

    # nums = [0]
    # moveZeroes(nums)
    # print(nums)

    nums = [0, 0, 1]
    moveZeroes(nums)
    print(nums)
