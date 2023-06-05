words = ('level', 'refer', 'probably', 'noon', 'local')


def palindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[-1-i]:
            return
    return word


filter_result = list(filter(palindrome, words))
print(filter_result)
