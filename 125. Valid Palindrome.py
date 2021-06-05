"""

Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.


Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

"""

def isPalindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i].isalnum():
            if s[j].isalnum():
                if s[i].lower() != s[j].lower():
                    return False
                else:
                    i += 1
                    j -= 1
            else:
                j -= 1
        else:
            i += 1
    return True


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))
    s = "race a car"
    print(isPalindrome(s))
    s = "a123456carrac   a"
    print(isPalindrome(s))
    s = "0P"
    print(isPalindrome(s))