# https://py.checkio.org/en/mission/long-repeat/


def long_repeat(line):
    res = 0
    max_length = 0
    if line:
        max_length = 1
        res = 1
    for i in range(len(line)):
        if i < len(line) - 1:
            if line[i] == line[i + 1]:
                res += 1
            else:
                if res > max_length:
                    max_length = res
                res = 1
        else:
            if res > max_length:
                max_length = res
                res = 1

    return max_length
