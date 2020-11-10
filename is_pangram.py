"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence
"The quick brown fox jumps over the lazy dog" is a pangram,
because it uses the letters A-Z at least once (case is irrelevant).
Given a string, detect whether or not it is a pangram. Return True if it is, False if not.
Ignore numbers and punctuation.
"""
import string


def is_pangram(s):
    counter = 0
    for letter in set(s.lower()):
        if letter in string.ascii_lowercase:
            counter += 1
    return counter == len(string.ascii_lowercase), counter


print(is_pangram('The quick, brown fox jumps over the lazy dog!'))
# print(is_pangram('ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ'))
# print(is_pangram('How quickly daft jumping zebras vex'))
# print(is_pangram('Pack my box with five dozen liquor jugs'))
# print(is_pangram('Cwm fjord bank glyphs vext quiz'))
