"""

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.

"""


# def isAlienSorted(words, order):
#     sortedFlag = True
#     newAlphabetOrderDict = {c: i for i, c in enumerate(order)}
#     for i in range(len(words)-1):
#         index = 0
#         while words[i][index] and words[i+1][index]:
#             if newAlphabetOrderDict[words[i][index]] < newAlphabetOrderDict[words[i+1][index]]:
#                 print(newAlphabetOrderDict[words[i][index]], newAlphabetOrderDict[words[i+1][index]])
#                 break
#             elif newAlphabetOrderDict[words[i][index]] > newAlphabetOrderDict[words[i+1][index]]:
#                 return False
#             else:
#                 index += 1
#     return sortedFlag

def isAlienSorted(words, order):
    ind = {c: i for i, c in enumerate(order)}
    for a, b in zip(words, words[1:]):
        if len(a) > len(b) and a[:len(b)] == b:
            return False
        for s1, s2 in zip(a, b):
            if ind[s1] < ind[s2]:
                break
            elif ind[s1] > ind[s2]:
                return False
    return True

if __name__ == '__main__':
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    print(isAlienSorted(words, order))

    words = ["word", "world", "row"]
    order = "worldabcefghijkmnpqstuvxyz"
    print(isAlienSorted(words, order))

    words = ["apple", "app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    print(isAlienSorted(words, order))