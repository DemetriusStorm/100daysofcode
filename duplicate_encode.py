"""
The goal of this exercise is to convert a string to a new string where each character in the new string is "("
if that character appears only once in the original string, or ")" if that character appears more than once in
the original string. Ignore capitalization when determining if a character is a duplicate.
"""


def duplicate_encode(word):
    mapper = dict()
    for element in word:
        if mapper.get(element, None):
            mapper[element.lower()] += word.count(element)
        else:
            mapper[element.lower()] = word.count(element)

    return ''.join('(' if mapper[element.lower()] == 1 else ')' for element in word)


print(duplicate_encode('JIuIzekPPwuT@SeSaG'))
