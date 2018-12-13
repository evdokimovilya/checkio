# https://py.checkio.org/en/mission/monkey-typing/


def count_words(text, words):
    count = 0
    for word in words:
        if word in text.lower():
            count += 1
    return count
