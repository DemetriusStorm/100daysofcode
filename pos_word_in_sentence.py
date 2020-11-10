"""

"""


def solution(sentence, word):
    return [i for i in range(len(sentence)) if [el.startswith(word) for el in sentence.split(' ')]]


print(solution("find a word in some sentence", "in"))
print(solution("test test test protest", "test"))
