"""

Given two strings s and t, return true if t is an anagram of s, and false otherwise.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

"""

import collections

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    count_s_char = collections.Counter(s)

    for char in t:
        if char not in count_s_char:
            return False
        else:
            count_s_char[char] -= 1
            if count_s_char[char] == 0:
                del count_s_char[char]
    return True

if __name__ == '__main__':
    s, t = "anagram", "nagaram"
    print(isAnagram(s, t))
    s, t = "rat", "car"
    print(isAnagram(s, t))
