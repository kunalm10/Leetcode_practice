"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.



Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1).
For nums[3]=2 there exist one smaller number than it (1).
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]
Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]


Constraints:

2 <= nums.length <= 500
0 <= nums[i] <= 100
"""

#Method 1
# def smallerNumbersThanCurrent(nums):
#     output = []
#     for i in range(len(nums)):
#         num_small = 0
#         for j in range(len(nums)):
#             if nums[j] < nums[i] and j!=i:
#                 num_small += 1
#         output.append(num_small)
#     return output

#Method 2
def smallerNumbersThanCurrent(nums):
    sorted_nums = sorted(nums)

    print(sorted_nums)
    num_dic = {}

    index = 0
    for number in sorted_nums:

        if number in num_dic:
            num_dic[number] = num_dic[number]
        else:
            num_dic[number] = index

        index += 1

    output = []
    for num in nums:
        output.append(num_dic[num])

    print(num_dic)
    return output

if __name__ == '__main__':
    nums = [8, 1, 2, 2, 3]
    print(smallerNumbersThanCurrent(nums))