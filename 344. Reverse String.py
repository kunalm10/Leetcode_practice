"""

Write a function that reverses a string. The input string is given as an array of characters s.



Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.

"""


def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    n = len(s)
    for i in range(n//2):
        print(i)
        s[i], s[n-1-i] = s[n-1-i], s[i]
        print(s)

if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    reverseString(s)
    print(s)