"""

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

"""
from itertools import zip_longest

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]

    pref = strs[0]
    plen = len(pref)

    for s in strs[1:]:
        while pref != s[:plen]:
            pref = pref[:(plen-1)]
            plen -= 1

            if plen == 0:
                return ""
    return pref



if __name__ == '__main__':
    # strs = ["flower", "flow", "flight"]
    # print(longestCommonPrefix(strs))

    strs = ["dog", "racecar", "car"]
    print(longestCommonPrefix(strs))