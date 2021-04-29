"""

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.



Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false


Constraints:

1 <= sentence.length <= 1000
sentence consists of lowercase English letters.

"""

def checkIfPangram(sentence):
    if len(sentence) < 26:
        return False
    letter_set = set()

    for char in sentence:
        letter_set.add(char)

        if len(letter_set) == 26:
            return True
    else:
        return False

if __name__ == '__main__':
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    print(len(sentence))
    print(checkIfPangram(sentence))
    sentence = "leetcode"
    print(checkIfPangram(sentence))
    sentence = "jwtucoucmdfwxxqnxzkaxoglszmfrcvjoiunqqausaxxaaijyqdqgvdnqcaihwilqkpivenpnekioyqujrdrovqrlxovcucjqzjsxmllfgndfprctxvxwlzjtciqxgsxfwhmuzqvlksyuztoetyjugmswfjtawwaqmwyxmvo"
    print(checkIfPangram(sentence))