# https://py.checkio.org/en/mission/most-wanted-letter/

import re


def checkio(text):
    res = {}
    max = 0
    bukva = ''
    text = text.lower()
    data = re.findall(r'[a-z]', text)
    data.sort()
    for i in data:
        if i not in res.keys():
            res[i] = data.count(i)
    for key, value in res.items():
        if value > max:
            bukva = key
            max = value
    print(bukva)
    return bukva
