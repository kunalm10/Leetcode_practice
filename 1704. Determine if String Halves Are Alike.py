"""

You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.



Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
Example 3:

Input: s = "MerryChristmas"
Output: false
Example 4:

Input: s = "AbCdEfGh"
Output: true


Constraints:

2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters.

"""


def halvesAreAlike(s):
    half = len(s) // 2

    vowels_in_s1 = 0
    vowels_in_s2 = 0
    for letter in s[0:half].lower():
        if letter in {'a', 'e', 'i', 'o', 'u'}:
            vowels_in_s1 += 1
    for letter in s[half:].lower():
        if letter in {'a', 'e', 'i', 'o', 'u'}:
            vowels_in_s2 += 1
    if vowels_in_s1 == vowels_in_s2:
        return True
    else:
        return False


if __name__ == '__main__':
    s = "book"
    print(halvesAreAlike(s))

    s = "textbook"
    print(halvesAreAlike(s))

    s = "MerryChristmas"
    print(halvesAreAlike(s))

    s = "AbCdEfGh"
    print(halvesAreAlike(s))
