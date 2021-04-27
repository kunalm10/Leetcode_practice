'''
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
'''


def numIdenticalPairs(nums):
    good_pairs = int()
    for i in range(len(nums)-1):
        for j in nums[i+1:]:
            if nums[i] == j:
                # print(nums[i],j)
                good_pairs += 1
    return good_pairs

if __name__ == '__main__':
    nums = [1, 2, 3, 1, 1, 3]
    # print(numIdenticalPairs(nums))
    print(numIdenticalPairs(nums = [1,1,1,1]))
    print(numIdenticalPairs(nums = [1,2,3]))
