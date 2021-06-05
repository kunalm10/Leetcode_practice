"""

Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1


Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.

"""
import collections

def firstUniqChar(s):

    count = collections.Counter(s)

    for index, char in enumerate(s):
        if count[char] == 1:
            return index

    return -1

if __name__ == '__main__':
    s = "leetcode"
    print(firstUniqChar(s))
    s = "loveleetcode"
    print(firstUniqChar(s))
    s = "aabb"
    print(firstUniqChar(s))
