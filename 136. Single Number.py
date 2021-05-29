"""

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1


Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

"""


# Method 1
# def singleNumber(nums):
#     for i in range(len(nums)//2 + 1):
#         check_duplicate = nums[0]
#         nums.remove(check_duplicate)
#         try:
#             nums.remove(check_duplicate)
#         except Exception as e:
#             return check_duplicate

# Method 2
def singleNumber(nums):
    a = 0
    for i in nums:
        a ^= i
    return a


if __name__ == '__main__':
    nums = [2, 2, 1]
    print(singleNumber(nums))
    nums = [4, 1, 2, 1, 2]
    print(singleNumber(nums))
    nums = [1]
    print(singleNumber(nums))
