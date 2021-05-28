"""

Given an array, rotate the array to the right by k steps, where k is non-negative.



Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

"""


# def rotate(nums, k):
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#     for i in range(1, k+1):
#         popped_num = nums.pop()
#         # print(popped_num)
#         nums = [popped_num] + nums
#         # print(nums)
#     return nums


def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    if k == 0:
        pass
    elif len(nums) == 1:
        pass
    elif len(nums) == k:
        pass
    elif k == 1:
        popped_nums = nums[-1]
        shifting_nums = nums[:-1]
        nums[0] = popped_nums
        nums[1:] = shifting_nums
    else:
        k = k % len(nums)
        popped_nums = nums[len(nums) - k:]
        shifting_nums = nums[:-(k)]
        nums[:k] = popped_nums
        nums[k:] = shifting_nums





if __name__ == '__main__':
    # nums = [1, 2, 3, 4, 5, 6, 7]
    # k = 3
    # rotate(nums, k)
    # print(nums)

    # nums = [-1, -100, 3, 99]
    # k = 2
    # rotate(nums, k)
    # print(nums)

    nums = [1]
    k = 1
    rotate(nums, k)
    print(nums)
